FROM python:3.10

EXPOSE 3000/tcp

COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Variables de ambiente Flask
ENV FLASK_APP=./src/propiedadesDA/api
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=3001

# Ejecución de la aplicación con pipenv y flask
#CMD ["pipenv", "run", "flask", "run"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]