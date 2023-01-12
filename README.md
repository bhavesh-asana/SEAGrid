# Small Molecule Ionic Lattices (SMILES) Data Models

![Local Build](https://img.shields.io/badge/local%20build-successful%20-green)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/bhavesh-asana/SEAGrid)

This project is an experimental workspace used for the Scientific and Chemical Engineering.
This is an end to end implementation of [SEAGrid Data Catalog](https://data.seagrid.org/),
embedded with the new features and advanced data visualization techniques.

**DEVELOPMENT GOALS**

1. Create a robust database to reduce the latency.
2. Redesigning the data models.
3. Synchronising the data with a user dashboard on performing experiment successfully.

# Table of Contents
- [Set up the code directory](#set-up-the-code-directory)
- [How to run the project](#how-to-run-the-project)
    - [Server Initialization](#server-initialization)
    - [Middleware (Django Application)](#middleware-django-application)
    - [Client Initialization](#client-initialization)
    - [Database Management](#database-management)
        - [Mongo Compass GUI](#visualize-the-data-with-mongo-compass-gui)
        - [Mongo CLI](#visualize-with-mongo-cli)
- [References](#references)
- [The Team](#the-team)

# Set up the code directory

## Tools and versions

| **Tools/Software** |    **Version**    |
|--------------------|:-----------------:|
| Java               |    version 19     |
| Python             | version <= 3.8.10 |
| Node               |     v14.20.1      |
| npm                |      6.14.17      |


**Suggestion:** If you are using conda, the python version will be installed on creating virtual environment in the next steps. If not please installed the specific version and 

**Working on Mac Environment:** <br/>

1. Open the terminal application and set the path to the home directory,
   use the command `cd ~/` to move to the home directory.
2. Clone the GitHub repository and use the following commands to change
   the working directory.
   ```commandline
    git init
    git clone https://github.com/bhavesh-asana/SEAGrid.git
   ```

# How to run the project?

## Server Initialization

1. Before initializing the server, make sure the MongoDB is installed and the instance
   is running locally.
   ```commandline
   mongo --port 27017
   ```
   This command ensure the Mongo instance is running locally and connected the instance to the port 27017.
2. Open a new terminal window (server_runner) and change the directory to the
   server codebase
   ```commandline
   cd ~/server/
   ```
3. Build the Maven project.
   ```commandline
   mvn clean
   mvn package install compile
   ```
4. Run the Spring Boot application.
   ```commandline
   mvn spring-boot:run
   ```
   On successful running of the server application, it shows a message as
   _"Server running successfully"_ and open connection with mongodb driver.

## RPC Handler (Django Application)

Open a new terminal window and follow the steps to run the middleware application.

1. Change the working directory to SMILES middleware.
   ```commandline
   cd ~/rpcHandler
   ```
2. Create a virtual environment using the following command. <br/>
   Strictly recommended to use Python version <=3.8.3 to build the **grpcio-wheel**.
   ```commandline
   $ conda create -n <EnvironmentName> python=3.8.3
   $ conda activate <EnvironmentName>
   ```
3. Upgrade the PIP version and install the required dependencies using the **requirements.txt** file.
   ```commandline
   pip install -U pip
   pip install -r requirements.txt
   ```
4. Run the Django application.
   ```commandline
   python manage.py runserver
   ```
5. Open http://127.0.0.1:8000/api/molecule/ to check the data transmission from
   the server application. On successful transmission, the data can also be visualized
   in the server terminal.

## Client Initialization

The front-end client application is developed in the JavaScript framework (vue.js).
The vue.js is communicated with the Django application (Middleware)
using REST api calls and the data is exchanged in between the server
and client application.

To run the client application, open a new terminal window and follow the below steps

1. Change the working directory to SMILES Dashboard.
   ```commandline
   cd ~/airavata-sandbox/gsoc2022/smilesdb/data-catalog
   ```
2. Open the new terminal and run the following commands to build the project.
   ```commandline
   yarn install
   yarn run serve
   ```
3. Open
    - http://localhost:8080/ for Login page.
    - http://localhost:8080/home for SEAGrid Homepage.
    - http://localhost:8080/search for the live data catalog.

## Database Management

### Visualize the data with Mongo Compass GUI

The mongo instances are configured in the application.properties file (located
under Server/src/main/resources/). Initialise the mongo compass and connect
to the respective port (27017). On execution of the **ServerApplication**,
the **smiles** database is created and the test data of _calcinfo_ is sent
to the database, which can be viewed under the **calcInfo** collection.

### Visualize with Mongo CLI

To view the data using Mongo shell, open the terminal and follow the commands
mentioned below.

```mongo
 mongo
 show dbs
 use smiles
 show collections
 db.molecule.find().pretty()
```

# The team
- Sudhakar Pamidighatam <br/>
  [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=plastic&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/sudhakar-pamidighantam-0074a77/)
- Bhavesh Asanabada <br/>
  [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=plastic&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/bhavesh-asana/)