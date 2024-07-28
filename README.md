# FastAPI-Keycloak-Angular

(this project is not really being used any more, but check out this
project instead [https://github.com/andreaskring/bootstrap-keycloak-fastapi-postgres](https://github.com/andreaskring/bootstrap-keycloak-fastapi-postgres))

A small sandbox application that demonstrates Keycloak authentication for a
backend written in Python using [FastAPI](https://fastapi.tiangolo.com/) and
a frontend in [Angular](https://angular.io/). This application uses this
project
[https://github.com/mauriciovigolo/keycloak-angular](https://github.com/mauriciovigolo/keycloak-angular)
to handle the Angular part of the Keycloak communication.

## Prerequisites
* Docker and Docker Compose
* ... and Python and [Angular CLI](https://cli.angular.io/) to develop
  stuff further.

## Running the app

Keycloak likes to speak SSL, so this sandbox application uses self-signed
SSL certificates signed for the domain `proxy`. Unfortunately, we have
to use a name different from `localhost` due to the Docker setup, since 
`localhost` within a Docker container refers to the container itself. So
in order to have the different Docker containers communicate properly, we
have to use something other than `localhost`.

To run the stack (Keycloak with a preconfigured realm, FastAPI and Angular),
do the following:
1. Add the hostname `proxy` to your `/etc/hosts` file, i.e. ensure that this
   file has a line similar to e.g.
   ```
   127.0.0.1    localhost proxy
   ```
1. Start the application from the root folder of this project with
   ```
   $ docker-compose up -d --build
   ```
   and give the stack a few moments to fire up. You can follow the logs
   with
   ```
   $ docker-compose -f logs
   ```
1. Open a browser and navigate to `https://proxy/something-cool`. The
   browser will throw some warnings due to the self-signed certificate,
   but you can safely accept these.
   
## Disclaimer

This app is not production ready in its current state (e.g. certificate
verification has been disabled in the Python backend, users with
trivial passwords have been pre-configured, there is no test suite,
allowed origins are set way too broad,...).
