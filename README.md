# The Log Analysis Application

The ``Log Analysis Appication`` is an internal reporting tool that allows you to find out pertainant details for the newspaper site, specifically the activity of users reading the newspaper articles on the site. 

# Running the App

The Log Analysis App runs using python version 2 and includes two main python files and the main sql file for importing the data into a postgresql database: 

1. log_analysis.py

The log_analysis.py is the main app that should be ran. to run the report. to run this app, you will need to have python 2 installed on your system. With the command having the log_analysis.py file within it's current directory, you can run the application with the following command: 

``python log_analysis.py``

2. queries.py

The queries.py holds the function required for connecting to the database (which you will need to configure), along with 3 specific functions imported into the log_analysis.py file that carry out the three required queries on the newsdata database. 

##connect_db() 

After you have configured the database utilizing the newsdata.sql file, you will need to set up the user and password within the queries.py within the connect_db() function by replacing ENTER_HERE in the code snippet shown below with your chosen username and password.

```
def connect_db():
    myConnection = psycopg2.connect( host='localhost', 
        user='ENTER_HERE', 
        password='ENTER_HERE', 
        dbname='news')
    return myConnection
```

Once you have completed this, you can test the connection by running the application and selection one of the options. if  you receive any FATAL errors when running the configuration, it's a good indication that your database is not set up properly. A few reasons you are receiving a FATAL error could include not connecting to the correct database, not having the correct user and password entered for authenticating access, or the user not having the correct credentials for accessing the news database.

The following list shows the three other functions within the queries.py file and a brief description of what they do:


* _popular_articles()_ - shows the three most popular articles of all time, based on most views. 

* _popular_authors()_ - shows the three most popular authors

* _errors()_ - shows if any of the dates within the database had more than 1% of requests lead to error on that particular day

## Supported Python Versions
`Log Analysis Application` has been tested and working on both Python versions 2 and 3.

## Licensing
`Log Analysis Application` is a public domain work, dedicated using [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Feel free to do whatever you want with it.



