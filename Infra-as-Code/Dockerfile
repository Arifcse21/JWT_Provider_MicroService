FROM --platform=$BUILDPLATFORM python:3.10
ENV PYTHONNUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

EXPOSE 5000

WORKDIR /jwt
COPY ../requirements.txt /jwt

RUN pip install -r requirements.txt

COPY ../ /jwt


ENTRYPOINT [ "python3" ]

CMD [ "manage.py", "runserver", "0.0.0.0:5000" ]
