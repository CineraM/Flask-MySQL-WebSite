# Database Design Final Project - Fall 2021  
#### Members: Devin Parmet, Keylin Sanchez, Matias Cinera   
#### For our group project, we designed and implemented a website for “PWR Fit”, a mock gym where members can register for classes and trainers can register to teach classes and view all members registered for the classes they are teaching.
#### The front-end of this project was developed using Flask with Python. The DBMS used was MySQL. Mock data created using Mockaroo.
#### Technology Enviroments: PopSQL(DataBase Manager), IDE's (ATOM & VS Code). Story tracking done using Jira.
## Application Structure
     .
     |--__pycache__/
     |--templates/
     | |--***HTMLfiles***
     |--***application routes and input validation file*** 
     |--***JSON files for class, member, and trainer data*** 
     |--***SQL Command files***
     |--***README file***
## How to run
#### MySQL and Flask with Python needed.
#### Run the following commands for setup:
     pip install mysql-connector
     pip install mysql-connector-python
     pip install mysql-connector-python-rf
     pip install pymysql
     pip install cryptography
     pip install Flask
     pip install Flask-SQLAlchemy
#### Create a database using MySQL
#### Run the following commands in the directory containing the python file:
     FLASK_APP=app.py
     set DEBUG_MODE=1
     flask run
#### The terminal should then output the address where the webapp is running.
## Running examples
### Registering as a trainer:
![image-20211122-080136](https://user-images.githubusercontent.com/66031870/142877954-4cc6344d-ec38-451f-a819-52796ffeaa04.png)
### Displaying all members: 
![image](https://user-images.githubusercontent.com/64340009/138615163-b7cfab9c-7dc7-4e47-8689-505f5b71eb30.png)  
