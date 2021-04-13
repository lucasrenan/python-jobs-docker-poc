# python-jobs-docker-poc

## Usage

```bash
docker-compose build
docker-compose run --rm job1 # Running "job1": Operator1

docker-compose run --rm job2 operator1 # Running "job2": Operator1
docker-compose run --rm job2 operator2 # Running "job2": Operator2
```
