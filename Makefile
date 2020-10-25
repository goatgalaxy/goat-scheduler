run:
	pipenv run python -m scheduler 

build-image:
	docker build -t scheduler .

tag-image:
	docker tag scheduler localhost:5000/scheduler

push-image:
	docker push localhost:5000/scheduler

run-docker:
	docker run -d scheduler 

deploy:
	@make build-image
	@make tag-image
	@make push-image
	kubectl apply -f deployment.yml --record

