#!/usr/bin/env bash
# Validate all JSON quote files; prints offending file paths on error.
set -euo pipefail

status=0

while IFS= read -r file; do
  if ! output=$(python3 -m json.tool "$file" 2>&1 >/dev/null); then
    printf 'Invalid JSON: %s\n' "$file" >&2
    printf '%s\n' "$output" >&2
    status=1
  fi
done < <(fd -e json . quotes)

exit "$status"
