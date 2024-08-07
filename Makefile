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
	docker compose down
	docker compose --env-file ./test.env up --build test

acceptance: test
	@echo Acceptance tests -- to be done