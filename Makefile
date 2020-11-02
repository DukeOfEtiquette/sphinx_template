# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?= -E
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
DEVBUILDDIR   = build_dev
INTERNALBUILDDIR = $(DEVBUILDDIR)/html
INTERNALDOCTREEDIR = $(DEVBUILDDIR)/doctrees

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# .PHONY: devhtml
devhtml:
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(INTERNALBUILDDIR)" -d "$(INTERNALDOCTREEDIR)" $(SPHINXOPTS) -t Internal
	@echo
	@echo "Build finished. The HTML pages are in $(INTERNALBUILDDIR)."

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
