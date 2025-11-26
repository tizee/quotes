# Agent Workflow Notes

## Merging New Quotes JSON
- Save any new quotes drop as temporary JSON files using the same schema as `schema.json` (include `$schema`, `name`, `quotes`).
- Append them into an existing quotes file with the merge helper:
  ```bash
  python scripts/merge_quotes.py quotes/naval-on-wealth.json /path/to/new-quotes.json [/path/to/more.json ...]
  ```
  The first file is updated in place; all subsequent files have their `quotes` arrays appended in order.
- After a successful merge, remove the temporary JSON files you used for input.
- Optional: run `./scripts/validate_json.sh quotes/naval-on-wealth.json` to confirm the merged file still matches the schema.
