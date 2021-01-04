# FastAPI-Keycloak-Angular

A small sandbox application that demonstrates Keycloak authentication for a
backend written in Python using [FastAPI](https://fastapi.tiangolo.com/) and
a frontend in [Angular](https://angular.io/). This application uses this
project
[https://github.com/mauriciovigolo/keycloak-angular](https://github.com/mauriciovigolo/keycloak-angular)
to handle the Angular part of the Keycloak communication.

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
