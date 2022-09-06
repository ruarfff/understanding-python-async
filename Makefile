export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1


build:
	docker compose build

up:
	docker compose up

down:
	docker compose down --remove-orphans

black:
	black -l 86 $$(find * -name '*.py')

async-example:
	docker compose run --rm app python src/async_example.py

pubsub:
	docker compose run --rm app python src/pubsub_client.py
