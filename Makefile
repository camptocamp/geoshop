.PHONY: run
run:
	docker compose down
	docker compose up

.PHONY: build
build:
	docker compose create --build --pull missing

.PHONY: clean
clean:
	docker compose rm -fsv

test:
	docker compose --env-file ./test.env down
	docker compose --env-file ./test.env --profile testing up --build updatedb test

acceptance: test
	@echo Acceptance tests -- to be done
