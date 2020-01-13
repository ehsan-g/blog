# SAY blog


## Introduction 

As project SAY was founded base on believing in an
open-source world. We are developing a blog to contribute to world

     

## Project Title

One Paragraph of project description goes here
Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
Prerequisites

What things you need to install the software and how to install them

Give examples

## Libraries

1. SQLAlchemy-Continuum
2. SQLAlchemy-Utils
3. Flask-RESTful API
4. Flask-WTF
5. Flask-Login
6. Flask-Limiter


1- [SQLAlchemy-Continuum](https://sqlalchemy-continuum.readthedocs.io/en/latest/intro.html#why)

- Does not store updates which don’t change anything
- Supports alembic migrations
- Can revert objects data as well as all object relations at given transaction even if the object was deleted
- Transactions can be queried afterwards using SQLAlchemy query syntax
- Querying for changed records at given transaction
- Querying for versions of entity that modified given property
- Querying for transactions, at which entities of a given class changed
- History models give access to parent objects relations at any given point in time

2- [SQLAlchemy-Utils](https://sqlalchemy-utils.readthedocs.io/en/latest/)

Various utility functions, new data types and helpers for SQLAlchemy
- Listeners
- Data types: {..., ChoiceType, CountryType, JSONType, URLType, UUIDType, ...}
- Range data types
- Aggregated attributes
- Generates decorator
- Generic relationships
- Database helpers: create_database, drop_database
- Foreign key helpers
- ORM helpers
- Utility classes
- Model mixins: Timestamp (created, updated times)
    


3- [Flask-RESTful API](https://flask-restful.readthedocs.io/en/latest/quickstart.html)

example of a simple application: we only have tasks, 
so our only resource will be the tasks in our to do list.

Our tasks resource will use HTTP methods as follows:
    
        
    - GET	http://[hostname]/todo/api/v1.0/tasks	Retrieve list of tasks
    - GET	http://[hostname]/todo/api/v1.0/tasks/[task_id]	Retrieve a task
    - POST	http://[hostname]/todo/api/v1.0/tasks	Create a new task
    - PUT	http://[hostname]/todo/api/v1.0/tasks/[task_id]	Update an existing task
    - DELETE	http://[hostname]/todo/api/v1.0/tasks/[task_id]	Delete a task
 
 We can define a task as having the following fields:

**id**: unique identifier for tasks. Numeric type.

**title**: short task description. String type.

**description**: long task description. Text type.

**done**: task completion state. Boolean type.



4- [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/)

- Integration with WTForms.
- Secure Form with CSRF token.
- Global CSRF protection.
- reCAPTCHA support.
- File upload that works with Flask-Uploads.
- Internationalization using Flask-Babel.


5- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)

It will:
- Store the active user’s ID in the session, and let you log them in and out easily.
- Let you restrict views to logged-in (or logged-out) users.
- Handle the normally-tricky “remember me” functionality.
- Help protect your users’ sessions from being stolen by cookie thieves.
- Possibly integrate with Flask-Principal or other authorization extensions later on.

However, it does not:
- Impose a particular database or other storage method on you. You are entirely in charge of how the user is loaded.
- Restrict you to using usernames and passwords, OpenIDs, or any other method of authenticating.
- Handle permissions beyond “logged in or not.”
- Handle user registration or account recovery.



6- [Flask-Limiter](https://flask-limiter.readthedocs.io/en/stable/)

The above Flask app will have the following rate limiting characteristics:
   
- Rate limiting by remote_address of the request
- A default rate limit of 200 per day, and 50 per hour applied to all routes.
- The slow route having an explicit rate limit decorator will bypass the default rate limit and only allow 1 request per day.
- The ping route will be exempt from any default rate limits.

   

## Running the tests

I have no clue yet.

## And coding style tests

I will be using PEP 8 styling for this project

## Deployment

I have no clue yet.

## Built With

- Python - Flask
- SQLAlchemy
- Postgres
- HTML, Bootstrap, JavaScript


## Versioning

I will be using SQLAlchemy-Continuum for further versioning.

## Author

Ehsan Ghasemi 

## License

This project is licensed under pendara.co

## Acknowledgments

“That's one small step for man, one giant leap for mankind.” 

- [x] Create DataBase
- [ ] Receive the wireframes
- [ ] build backEnd
- [ ] build the front templates
- [ ] Push my commits to Git
- [ ] Open a pull request
- [ ] Finish changes
- [ ] Time to SAY it.

