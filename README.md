# Flask application

## Routes

- / : Hello world
- /goodbye : Goodbye World

## Deployment

- Nginx
```
server {
    listen 80;
    location / {
        include uwsgi_params;
        uwsgi_pass flask:8080;
    }
}
```

- Docker
```
version: "3.7"

services:

  flask:
    build: ./
    container_name: flask
    restart: always
    environment:
      - APP_NAME=MyFlaskApp
    expose:
      - 8080

  nginx:
    build: ./nginx
    container_name: nginx
    restart: always
    ports:
      - "80:80"
```

## How to run ?

Build the application and run with docker-compose
```
docker-compose up
```