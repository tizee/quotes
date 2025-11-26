.PHONY: all fortune style check-json clean mrproper

SCRIPT_DIR=$(PWD)/scripts
all: check-json fortune

fortune: style check-json
	$(SCRIPT_DIR)/install_fortune.sh

# validate all quote json files
check-json:
	@./scripts/validate_json.sh

# sort imports and format
style:
	ruff check --config ruff.toml --fix generate.py
	ruff format --config ruff.toml generate.py

clean:
	rm -r output
