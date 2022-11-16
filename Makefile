export:
  @pdm export -f requirements > requirements.txt

build: export
	@docker build .
