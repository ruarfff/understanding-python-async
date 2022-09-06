export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1


build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down --remove-orphans

black:
	black -l 86 $$(find * -name '*.py')
