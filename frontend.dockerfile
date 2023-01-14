FROM --platform=linux/arm64 python:3.9

WORKDIR /app
#
COPY ./front /app
# 
ENV APP_PORT=8000
EXPOSE $APP_PORT
CMD python -m http.server $APP_PORT