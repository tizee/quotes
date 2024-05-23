.PHONY: clean, mrproper

SCRIPT_DIR=$(PWD)/scripts
all: fortune

fortune: style
	$(SCRIPT_DIR)/install_fortune.sh

# sort imports and format
style:
	ruff check --config ruff.toml --fix generate.py
	ruff format --config ruff.toml generate.py

clean:
	rm -r output

mrproper: clean
	rm -rf fortune
