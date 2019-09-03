SHELL:=/bin/bash
BASEDIR=$(CURDIR)
OUTPUTDIR=public
HUGOOUTPUTDIR=public/blog
.PHONY: all
all: clean get_repository build deploy
.PHONY: clean
clean:
	@echo "Removing public directory"
	rm -rf $(BASEDIR)/$(OUTPUTDIR)
.PHONY: get_repository
get_repository:
	@echo "Getting public repository"
	git clone https://github.com/roytang/roytang.github.io.git public
.PHONY: build
build:
	@echo "Generating site"
	hugo version
	hugo --gc --minify
.PHONY: deploy
deploy:
	@echo "Preparing commit"
	@cd $(OUTPUTDIR) \
	 && git config user.email "roytang@gmail.com" \
	 && git config user.name "Roy Tang" \
	 && git add . \
	 && git status \
	 && git commit -a -m "Deploy via Makefile" \
	 && git push -f -q https://$(GITHUB_TOKEN)@github.com/roytang/roytang.github.io.git master
	@echo "Pushed to remote"