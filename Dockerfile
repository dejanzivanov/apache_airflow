FROM apache/airflow:2.5.3
COPY requirements.txt /requirements.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt

#sudo docker build . --tag extending_airflow:latest