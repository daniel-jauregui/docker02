FROM python:3.8-slim-buster AS bulider

WORKDIR /temp/app

COPY . /temp/app

FROM python:3.8-slim-buster AS Prod

WORKDIR /app

COPY /temp/app/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
