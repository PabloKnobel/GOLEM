#!/usr/bin/env bash
# One-time VPS setup for the GOLEM bridge. Run as your normal (non-root) user:
#   bash install.sh git@github.com:PabloKnobel/GOLEM.git
# Prerequisites (see SETUP.md, Part B): git, Node.js 22+, obsidian-headless, deploy key in ~/.ssh/golem_deploy
set -euo pipefail

REPO="${1:?usage: bash install.sh <git ssh url>}"
BASE="$HOME/golem"
VAULT="$BASE/vault"
GITDIR="$BASE/golem.git"
KEY="$HOME/.ssh/golem_deploy"

[[ -f "$KEY" ]] || { echo "Missing deploy key $KEY (SETUP.md step B3)"; exit 1; }
command -v ob >/dev/null || { echo "Missing 'ob' (npm install -g obsidian-headless)"; exit 1; }

mkdir -p "$BASE/state" "$VAULT"
if [[ ! -d "$GITDIR" ]]; then
  # Bare-style git dir outside the vault; the vault folder is its work tree.
  GIT_SSH_COMMAND="ssh -i $KEY -o IdentitiesOnly=yes" \
    git clone --no-checkout --separate-git-dir="$GITDIR" "$REPO" "$BASE/tmp-clone"
  rm -f "$BASE/tmp-clone/.git" && rmdir "$BASE/tmp-clone"
  export GIT_DIR="$GITDIR" GIT_WORK_TREE="$VAULT"
  git config core.sshCommand "ssh -i $KEY -o IdentitiesOnly=yes"
  git config core.worktree "$VAULT"
  git config user.name "GOLEM bridge"
  git config user.email "golem-bridge@localhost"
  git checkout -f main
  echo "Vault files checked out into $VAULT"
fi

# systemd user units
UNIT_DIR="$HOME/.config/systemd/user"
mkdir -p "$UNIT_DIR"
SRC="$(cd "$(dirname "$0")" && pwd)"
cp "$SRC/golem-sync.service" "$SRC/golem-bridge.service" "$SRC/golem-bridge.timer" "$UNIT_DIR/"
install -m 755 "$SRC/bridge.sh" "$BASE/bridge.sh"

loginctl enable-linger "$USER" || echo "WARN: enable-linger failed; ask root to run: loginctl enable-linger $USER"
systemctl --user daemon-reload
echo
echo "Next (SETUP.md B5-B6):"
echo "  cd $VAULT && ob login && ob sync-list-remote && ob sync-setup --vault \"GOLEM\" --device-name vps"
echo "  ob sync            # one-time sync first; check the result"
echo "  systemctl --user enable --now golem-sync.service golem-bridge.timer"
