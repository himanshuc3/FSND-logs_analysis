# Logs_analysis
 - This is the 1st project in my Full Stack Nanodegree program from Udacity which teaches SQL practise by hand.

## Introduction
 - This is the solution for the Logs Analysis project in Udacity Full Stack Nanodegree course. In this, we have to execute complex queries on a large database.
 - The database in question is a newspaper company database where we have 3 tables: ```articles, authors and log.```
 - There are 3 queries to be written to complete the assignment. Therefore ```logs_analysis.py consists``` of linking to ```news``` database which we create.
 - They are:
    1. What are the most popular three articles of all time?
    2. Who are the most popular article authors of all time?
    3. On which days did more than 1% of requests lead to errors?

## Development Environment Setup
 - Download virtualbox and vagrant from their official websites.
 - Run ```vagrant --version``` to verify that the latest version of vagrant has been installed.
 - Download vagrant configuration from ```https://github.com/udacity/fullstack-nanodegree-vm```.
 - Go into vagrant folder from command line.
 - Run ```vagrant up``` to install and  ```vagrant ssh``` to login to remote linux. 
 - Run ```cd /vagrant``` to go into shared folder.
 - Download newsdata.sql from nanodegree webpage. It has all the queries for making the database.
 - Run ```psql -d news -f newsdata.sql``` to make the database.
 - Install dependency by ```pip3 install psycopg2```.
 - Run ```python3 logs_analysis.py``` and get the output.
 - It will present you with answers to the 3 queries given above.