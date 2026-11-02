#!/usr/bin/env bash
# Run locally after installing/authenticating GitHub CLI as YanIanZ.
# This script creates a PUBLIC repo and pushes only with the owner's explicit execution.
set -euo pipefail
cd "$(dirname "$0")/.."

if ! command -v git >/dev/null 2>&1; then
  echo 'ERROR: git is required.' >&2; exit 1
fi
if ! command -v gh >/dev/null 2>&1; then
  echo 'ERROR: GitHub CLI is required. Install with: brew install gh' >&2; exit 1
fi
if ! gh auth status >/dev/null 2>&1; then
  echo 'ERROR: Authenticate first using: gh auth login' >&2; exit 1
fi
login="$(gh api user --jq '.login')"
if [[ "$login" != 'YanIanZ' ]]; then
  echo "ERROR: GitHub CLI is authenticated as $login, expected YanIanZ." >&2
  exit 1
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo 'ERROR: Not a git repository. Extract the git-ready RUKSA package first.' >&2
  exit 1
fi
if [[ -n "$(git status --porcelain)" ]]; then
  echo 'ERROR: Commit or revert uncommitted changes before publishing.' >&2
  exit 1
fi

if gh repo view YanIanZ/RUKSA >/dev/null 2>&1; then
  echo 'Repository already exists; checking origin and pushing main.'
  if git remote get-url origin >/dev/null 2>&1; then
    actual="$(git remote get-url origin)"
    case "$actual" in
      https://github.com/YanIanZ/RUKSA|https://github.com/YanIanZ/RUKSA.git|git@github.com:YanIanZ/RUKSA.git) ;;
      *) echo "ERROR: Existing origin points elsewhere: $actual" >&2; exit 1;;
    esac
  else
    git remote add origin https://github.com/YanIanZ/RUKSA.git
  fi
  git push -u origin main
else
  echo 'Creating public repository YanIanZ/RUKSA and pushing main.'
  gh repo create YanIanZ/RUKSA --public \
    --description 'Proof-carrying autonomous procurement agent on Vultr: work done, proof attached.' \
    --source . --remote origin --push
fi

echo 'Verify repository at https://github.com/YanIanZ/RUKSA'
