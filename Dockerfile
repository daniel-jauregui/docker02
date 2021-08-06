FROM python:3.8-slim-buster AS builder

WORKDIR /tmp/app

COPY . .

FROM python:3.8-slim-buster AS Prod

WORKDIR /app

COPY --from=builder /tmp/app /app

RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
