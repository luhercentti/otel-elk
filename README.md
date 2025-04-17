# otel-elk
Opentelemty does not have a default exporter for logstash, then if we want we can use filebeat to save optenelemtry collectors logs to a file, then those logs
will be read by logstash and then send to elastic


# Remove the existing virtual environment
rm -rf lhctestvenv
python3 -m venv lhctestvenv
source lhctestvenv/bin/activate
pip install -r requirements.txt



docker build -t python-logging-app:latest .
minikube image load python-logging-app:latest


Create a persistent mount from your local dir to minikube
minikube mount "/Users/luisangelo.hernandez/Documents/Proyectos personales/OTEL-ELK/generatedlogs:/generatedlogs"


before starting the docker-compose run , en el mismo directorio que el docker-compose:
echo "ENCRYPTION_KEY=$(openssl rand -base64 32 | tr -d '\n' | cut -c1-32)" >> .env
echo "ALERTING_ENCRYPTION_KEY=$(openssl rand -base64 32 | tr -d '\n' | cut -c1-32)" >> .env



 curl -X GET "http://localhost:9200/otel-logs-*/_search?pretty" -u elastic:elastic  


find logstash private ip:
docker inspect 0c25c8888b8f
to find ip of logastash

deactivate

