# Udacity Log Analysis Project

This is a Udacity class project. The project is a reporting tool that displays SQL queries based on given data.

## REQUIREMENTS

* You'll need [Python](https://www.python.org/) and a working computer to view or edit this project.
* [PostgreSQL](https://www.postgresql.org/) installed.
* A virtual machine to run everything. Why not use [Vagrant](https://www.vagrantup.com/)?

## INSTALLATION

1. [`Clone`](https://github.com/purwin/Udacity_Log_Analysis.git) this project so you have a copy on your computer.
2. Unzip `newsdata.sql.zip`.
3. Start up your virtual machine. Run the following in Terminal if you're using Vagrant:
* `vagrant up`
* `vagrant ssh`
* `cd /vagrant` to access project files
4. Load the SQL database data in `newsdata.sql`. Run the following in Terminal:
* `psql -d news -f newsdata.sql`
5. Run `newsdata.py` in Terminal to display the following queries:
* 1. What are the most popular three articles of all time?
* 2. Who are the most popular article authors of all time?
* 3. On which days did more than 1% of requests lead to errors?
6. Check out those beautiful SQL query results!

## CONTRIBUTE

Feel free to `clone` or `fork` this project!