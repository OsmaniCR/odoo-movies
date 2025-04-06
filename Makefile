run-dev:
	docker compose up -d

run-tests:
	docker compose run --rm web odoo --test-enable -d odoo -u movie_module
