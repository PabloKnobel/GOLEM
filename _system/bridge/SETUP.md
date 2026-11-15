---
type: setup
---

# GOLEM setup

Order matters: **laptop → VPS → other devices**. The VPS seeds the vault from GitHub into Obsidian Sync,
so every device must start from an empty vault. About 45 minutes in total.

## Part A — Obsidian Sync (personal laptop, ~10 min)
- [ ] A1. Subscribe to Obsidian Sync. Check how many devices per vault your plan allows: you need 4 (laptop, VPS, work PC, phone).
- [ ] A2. In Obsidian on the laptop, create a new **empty** local vault named `GOLEM`.
- [ ] A3. Settings → Sync → create a new remote vault named `GOLEM`, with an encryption password you store in your password manager. Connect this laptop vault to it.
- [ ] A4. Leave it empty. The VPS fills it in Part B.

## Part B — VPS (Hostinger, ~25 min, terminal)
- [ ] B1. Log in as your normal (non-root) user. Install `git` and **Node.js 22 or later** (follow nodejs.org for your Linux).
- [ ] B2. `npm install -g obsidian-headless` then check `ob --help` works.
- [ ] B3. Deploy key for GitHub:
  `ssh-keygen -t ed25519 -f ~/.ssh/golem_deploy -N ""` then `cat ~/.ssh/golem_deploy.pub`.
  On github.com → GOLEM → Settings → Deploy keys → Add → paste → **tick "Allow write access"**.
- [ ] B4. Get the scripts and install:
  `git clone -c core.sshCommand="ssh -i ~/.ssh/golem_deploy" git@github.com:PabloKnobel/GOLEM.git /tmp/golem-setup`
  `bash /tmp/golem-setup/_system/bridge/install.sh git@github.com:PabloKnobel/GOLEM.git`
- [ ] B5. Link the vault folder to Obsidian Sync (official commands):
  `cd ~/golem/vault && ob login && ob sync-list-remote`
  `ob sync-setup --vault "GOLEM" --device-name vps`
  `ob sync` (one-time) → on the laptop, check the GOLEM vault now shows `Home.md`, `wiki/`, etc.
- [ ] B6. Start the services: `systemctl --user enable --now golem-sync.service golem-bridge.timer`
- [ ] B7. Check: `systemctl --user status golem-sync.service` and, after 5 minutes, `cat ~/golem/state/bridge.log`.
- [ ] B8. Hardening (if not done): SSH key login only, no password login; automatic security updates.

Do **not** also run the Obsidian desktop app against `~/golem/vault` on the VPS (Obsidian warns that two sync methods on one device cause conflicts).

## Part C — Other devices (~5 min each)
- [ ] C1. Work PC and phone: install Obsidian, create an empty local vault `GOLEM`, connect it to the remote vault `GOLEM` (Settings → Sync).
- [ ] C2. On one device: Settings → Community plugins → install and enable **Dataview** (portals, project hubs and Home use it). In Sync settings, turn on syncing of community plugins and settings so other devices get it.
- [ ] C3. Optional: the **Obsidian Web Clipper** browser extension, saving into `00_inbox/`.
- [ ] C4. If the work PC blocks community plugins, everything still works except the auto-built tables.

## Part D — Claude settings (~2 min)
- [ ] D1. claude.ai → Settings → Capabilities → allowed domains: add `api.crossref.org` and `api.openalex.org` (citation checks at ingest). Without them, papers are marked `metadata_checked: false`.
- [ ] D2. Drive folder **Second Brain Inbox** exists (Claude created it). Save files there from any browser.

## If the bridge raises an alert
You'll see `_system/BRIDGE-ALERT.md` in Obsidian. Mirroring is paused; nothing is lost.
- **Sync not running:** `systemctl --user restart golem-sync.service`, then delete the alert file.
- **Fetch/push failed:** check network and the deploy key (B3), then delete the alert file.
- **Conflict** (the same file edited in Obsidian and by Claude):
  ```
  export GIT_DIR=~/golem/golem.git GIT_WORK_TREE=~/golem/vault; cd ~/golem/vault
  git fetch origin && git rebase origin/main      # lists the conflicted files
  # open each file, keep both texts, remove the <<<<<<< ======= >>>>>>> markers
  git add -A && git rebase --continue && git push origin HEAD:main
  rm _system/BRIDGE-ALERT.md
  ```
  Or paste the conflicted file into a Claude chat and ask for the merge.

## How the pieces fit
Devices ↔ Obsidian Sync ↔ VPS (`ob sync --continuous` + `bridge.sh` every 5 min) ↔ GitHub `GOLEM` ↔ Claude
(chats, nightly ingest, weekly digest). The git folder sits outside the vault (`~/golem/golem.git`),
so no `.git` folder reaches your devices.
