FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY images/ /images

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
