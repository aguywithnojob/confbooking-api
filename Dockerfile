FROM python:3.10.7-alpine

WORKDIR /code

COPY ./requirements.txt  /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code

EXPOSE 8002

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8002"]