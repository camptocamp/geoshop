.PHONY: run
run:
	docker compose up

.PHONY: build
build:
	docker compose create --build --pull missing

.PHONY: clean
clean:
	docker compose rm -fsv

test: build
	docker compose up test --build --abort-on-container-exit

acceptance: test
	@echo Acceptance tests -- to be done