FROM --platform=linux/arm64 python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
#
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#
COPY ./app /app/app
COPY ./src /app/src
COPY ./resources /app/resources
# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]