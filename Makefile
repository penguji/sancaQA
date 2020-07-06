.PHONY: Commands for developers

.PHONY: clean
clean: ## Run all lint checks and unittest
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*.html' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -rf reports && mkdir -p reports

.PHONY: isort
isort: ## Run isort for sorting imports
	pipenv run isort $(ARGS) -rc .

.PHONY: flake8
flake8: ## Run flake8 for code checker
	pipenv run flake8 $(ARGS)

.PHONY: black
black: ## Run black for code formater
	pipenv run black .

.PHONY: code_clean
code_clean: isort black flake8  ## Run isort and flake8
	@echo "-- Cleaning Code Completed-- "

.PHONY: test_mobile
test_mobile: ## Run Pytest in directory tests/mobile
	pipenv run pytest tests/mobile --reportportal  --rp-launch microservices

.PHONY: test_api
test_api: ## Run Pytest in directory tests/integrations
	pipenv run pytest tests/api/ --reportportal --rp-launch integrations

.PHONY: help
help: ## Display this help screen
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
