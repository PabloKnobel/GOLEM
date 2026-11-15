#!/usr/bin/env bash
# GOLEM bridge (runs on the VPS every 5 minutes via golem-bridge.timer).
# Mirrors the Obsidian Sync copy of the vault <-> the private GitHub repo.
#   Obsidian edits  -> committed and pushed to GitHub
#   Claude's commits -> pulled into the vault, then Obsidian Sync spreads them to your devices
# The git directory lives OUTSIDE the vault, so no .git folder is ever synced to your devices.
# On any failure it writes _system/BRIDGE-ALERT.md into the vault (you see it in Obsidian,
# Claude sees it in the weekly digest) and stops until the alert is removed.
set -euo pipefail

VAULT="${GOLEM_VAULT:-$HOME/golem/vault}"
GITDIR="${GOLEM_GITDIR:-$HOME/golem/golem.git}"
STATE="${GOLEM_STATE:-$HOME/golem/state}"
ALERT="$VAULT/_system/BRIDGE-ALERT.md"
export GIT_DIR="$GITDIR" GIT_WORK_TREE="$VAULT"

mkdir -p "$STATE"
log() { echo "$(date -Is) $*" >> "$STATE/bridge.log"; }
fail() {
  log "ERROR: $*"
  cat > "$ALERT" <<EOF
---
type: alert
---
# Bridge alert

**$(date -Is)**: $*

The vault is NOT being mirrored to GitHub until this is fixed.
Fix steps: _system/bridge/SETUP.md, section "If the bridge raises an alert".
Delete this file when fixed.
EOF
  exit 1
}

cd "$VAULT"

# Stop while an alert is open (prevents piling up half-merged states).
if [[ -f "$ALERT" ]]; then log "skipped: open alert"; exit 1; fi

# Obsidian Sync daemon must be running.
if ! systemctl --user is-active --quiet golem-sync.service; then
  fail "Obsidian headless sync (golem-sync.service) is not running."
fi

# 1. Commit edits that arrived from your devices.
git add -A
if ! git diff --cached --quiet; then
  git commit -q -m "sync: Obsidian edits $(date -u +%Y-%m-%dT%H:%MZ)"
  log "committed device edits"
fi

# 2. Bring in Claude's commits.
git fetch -q origin main || fail "git fetch from GitHub failed (network or deploy key)."
if ! git rebase -q origin/main; then
  git rebase --abort || true
  fail "Conflict: the same file was changed in Obsidian and by Claude."
fi

# 3. Publish.
git push -q origin HEAD:main || fail "git push to GitHub failed."
date -Is > "$STATE/last_ok"
log "ok"
