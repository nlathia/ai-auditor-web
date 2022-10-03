VIRTUALENV_NAME=$(shell pwd | rev | cut -d '/' -f 1 | rev)

.PHONY: install uninstall clean localhost

uninstall:
	@./bin/remove_pyenv.sh

install: uninstall
	@./bin/setup_pyenv.sh $(VIRTUALENV_NAME)

clean:
	@./bin/cleanup.sh

localhost:
	@./bin/launch.sh
