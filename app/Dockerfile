# pull official base image
FROM python:3.9

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get -y update
#    && apt-get install postgresql-dev gcc python3-dev musl-dev

RUN apt-get install -y openssl libssl-dev cmake make git pkg-config
ENV LD_LIBRARY_PATH /usr/local/lib

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# run entrypoint.sh
#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
#CMD ['celery --app myapp.tasks worker --loglevel=INFO']