# Pix Admin API

Administration API for The Pix. 👾

## Pre-requisites

In order to use this software on your workstation, you must meet the following requirements:

- Python v3.8.5+
  > Type in your console `python -v` and check your current version. In the absence of its installation, enter the [following link](https://www.python.org/downloads/).

Note:
  > This project can be run with or without [Docker](https://www.docker.com/)

## Run App without Docker 🐍

1. Clone the repository.
   ```sh
   $ git clone https://github.com/thecodeworkers/pix-admin-api.git
   ```
2. Onto to the downloaded repository folder.
   ```sh
   $ cd pix-admin-api
   ```
3. Create virtual environment.
    ```
    $ python -m venv venv
    ```
4. Install all dependencies.
   ```sh
   $ pip install requirements.txt
   ```
5. Copy the contents of the .env.example to .env
   ```sh
   $ cp .env.example .env
   ```
6. Run the application.
   ```sh
   $ flask run
   ```

## Run App with Docker 🐋

1. Clone the repository.
   ```sh
   $ git clone https://github.com/thecodeworkers/pix-admin-api.git
   ```
2. Onto to the downloaded repository folder.
   ```sh
   $ cd pix-admin-api
   ```
3. Copy the contents of the .env.example to .env
   ```sh
   $ cp .env.example .env
   ```
5. Run containers.
   ```sh
   $ docker compose up
   ```

## Use Application 🚀

For use application, follow the steps below:

1. Run setup.py
    ```sh
    $ python setup.py
    ```
2. When executing this files, three options appear, the first creates the keys for the use of the application, the second executes the migration of the database and the third ends the program.
    ```
    1) Key Generation 
    2) Migrate Database 
    0) Exit 
    ```
3. Generate keys to use the API (the instructions in how to place these keys are in the program).
4. Execute Database migration.
5. Make a request to the /signin endpoint with the following information:
    ```
    email: admin@email.com
    password: 12345678
    ```
6. Use Authorization token in the request header as Authorization Bearer ...
