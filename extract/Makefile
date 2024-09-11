VERSION ?= $(shell git describe --always --tags)
DOCKER_TAG ?= latest

export DOCKER_BUILDKIT=1

.DEFAULT_GOAL := help

.PHONY: build_docker
build_docker: ## Build docker image
	docker build --tag=camptocamp/asit-extract:$(VERSION) \
		--build-arg=VERSION=$(VERSION) .
	docker tag camptocamp/asit-extract:$(VERSION) camptocamp/asit-extract:$(DOCKER_TAG)

.PHONY: build_ghcr
build_ghcr: ## Build docker image tagged for GHCR
	docker build --tag=ghcr.io/camptocamp/asit-extract:$(VERSION) \
		--build-arg=VERSION=$(VERSION) .
	docker tag ghcr.io/camptocamp/asit-extract:$(VERSION) ghcr.io/camptocamp/asit-extract:$(DOCKER_TAG)

.PHONY: push_ghcr
push_ghcr: ## Push docker image to GHCR
	docker push ghcr.io/camptocamp/asit-extract:$(VERSION)
	docker push ghcr.io/camptocamp/asit-extract:$(DOCKER_TAG)

.PHONY: help
help: ## Display this help
	@echo "Usage: make <target>"
	@echo
	@echo "Available targets:"
	@grep --extended-regexp --no-filename '^[a-zA-Z_-]+:.*## ' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "	%-20s%s\n", $$1, $$2}'
