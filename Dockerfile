FROM python:3.7.4

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV GATEWAY_APP_CONFIG=routes.cfg

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "api_pkg/gateway.py" ]