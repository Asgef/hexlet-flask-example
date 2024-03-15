start:
	poetry run flask --app hexlet_flask_example/example --debug run --port 8000

start_handler:
	poetry run flask --app hexlet_flask_example/example_handler --debug run --port 8000

start_form:
	poetry run flask --app hexlet_flask_example/example_form --debug run --port 8000