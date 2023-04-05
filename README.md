# Apache Airflow

Basic setup of Apache Airflow, how to use it: 

Have Docker installed

1) Clone this repo:

```bash
git clone https://github.com/dejanzivanov/apache_airflow.git
```

### Initiate Airflow Database:

2) Initialize the database of the airflow using docker
```bash
docker-compose up airflow db init
```

### Start containers

3) Start the containers of the airflow with the docker, and wait few minutes
```bash
docker-compose up airflow init
```

