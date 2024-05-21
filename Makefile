.PHONY: clean, mrproper

SCRIPT_DIR=$(PWD)/scripts
all: fortune

fortune:
	$(SCRIPT_DIR)/install_fortune.sh

clean:
	rm -r output

mrproper: clean
	rm -rf fortune
