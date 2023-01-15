# Sample of data engineering using Python: simple data import pipeline (MySQL --> Postgre with no transformation)

This programs copies data from a MySQL database to a Postgre one. You should have both DBs installed in your machine, plus the dependencies listed in the item 1 below.

After cloning the repository, execute the below steps:

1-The below libraries need to be installed in your environment (using pip install [library_name]) before you execute the program 
pandas==1.0.4
mysql-connector-python==8.0.20
psycopg2-binary==2.8.5
loguru==0.5.1

2-Execute the scripts for creating the MySQL (source) and Postgre (target) DBs in each of the database IDE:

MySql (creates and populates tables):
retail_db\create_db.sql

Postgre (only creates the tables, as the python program will populate them by copying the data from the MySQL db):
retail_db\create_db_tables_pg.sql

3-Run the program App.py by executing the comand below from the [data-copier-live] folder:

python app.py 'dev', 'all'
