FROM --platform=$BUILDPLATFORM python:3.10
ENV PYTHONNUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

EXPOSE 5000


WORKDIR /jwt
RUN pwd

COPY requirements.txt /jwt

RUN pip install -U pip &&\ 
    pip install -r requirements.txt

COPY . /jwt


COPY entrypoint.sh /jwt
ENTRYPOINT ["sh", "/jwt/entrypoint.sh"]

