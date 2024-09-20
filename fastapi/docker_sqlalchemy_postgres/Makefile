.PHONY: help up down db-up db-down restart logs clean rebuild

help:  ## Exibe a lista de comandos
	@echo "Comandos disponíveis:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

up: ## Sobe todos os containers em modo desanexado
	docker-compose -f docker-compose.yml up -d

down: ## Derruba todos os containers
	docker-compose -f docker-compose.yml down

db-up:  ## Sobe apenas o container do banco de dados
	docker-compose -f docker-compose.yml up -d --build --force-recreate --remove-orphans db

db-down:  ## Derruba apenas o container do banco de dados
	docker-compose -f docker-compose.yml down -v --remove-orphans db

restart: down up  ## Reinicia os containers (derruba e sobe novamente)

logs:  ## Mostra os logs de todos os serviços
	docker-compose -f docker-compose.yml logs -f

clean:  ## Remove arquivos temporários e containers parados
	sudo docker system prune -f -a
	sudo find . -type f -name '*.pyc' -delete
	sudo find . -type d -name '__pycache__' -exec rm -r {} +

rebuild: ## Rebuilda e reinicia os containers Docker
	docker compose -f docker-compose.yml up -d --build --force-recreate --remove-orphans
