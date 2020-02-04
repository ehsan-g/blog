# SAY blog


## Introduction 

As project SAY was founded base on the philosophy of an
open-source world. We are developing a blog/media to contribute even further.
This project will be designed and developed from scratch to fulfill SAY company needs in every steps.
This is going to be an ongoing projects. Some of the below libraries will be used:
     
## Libraries

1. SQLAlchemy-Continuum
2. Cerberus
3 .SQLAlchemy-Utils
4. Image
5. Flask-RESTful API
6. Flask-WTF
7. Flask-Login
8. Flask-Limiter


1- [SQLAlchemy-Continuum](https://sqlalchemy-continuum.readthedocs.io/en/latest/intro.html#why)

- Does not store updates which don’t change anything
- Supports alembic migrations
- Can revert objects data as well as all object relations at given transaction even if the object was deleted
- Transactions can be queried afterwards using SQLAlchemy query syntax
- Querying for changed records at given transaction
- Querying for versions of entity that modified given property
- Querying for transactions, at which entities of a given class changed
- History models give access to parent objects relations at any given point in time

2- [Cerberus](http://docs.python-cerberus.org/en/stable/usage.html#basic-usage)

- Validating inputs before inserting into database
- User permission


3- [SQLAlchemy-Utils](https://sqlalchemy-utils.readthedocs.io/en/latest/)

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
    

4- [Media](https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/) ( to be upgraded )

- Using Flask image upload and if neccessary the following libriaries will be implemented. 
- Libraries: Python Imaging Library, Flask-AppBuilder, SQLAlchemy-ImageAttach or sqlalchemy-media.
 

5- [Flask-RESTful API](https://flask-restful.readthedocs.io/en/latest/quickstart.html)

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



6- [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/)

- Integration with WTForms.
- Secure Form with CSRF token.
- Global CSRF protection.
- reCAPTCHA support.
- File upload that works with Flask-Uploads.
- Internationalization using Flask-Babel.


7- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)

It will:
- Store the active user’s ID in the sessionion, and let you log them in and out easily.
- Let you restrict views to logged-in (or logged-out) users.
- Handle the normally-tricky “remember me” functionality.
- Help protect your users’ sessionions from being stolen by cookie thieves.
- Possibly integrate with Flask-Principal or other authorization extensions later on.

However, it does not:
- Impose a particular database or other storage method on you. You are entirely in charge of how the user is loaded.
- Restrict you to using usernames and passwords, OpenIDs, or any other method of authenticating.
- Handle permissions beyond “logged in or not.”
- Handle user registration or account recovery.



8- [Flask-Limiter](https://flask-limiter.readthedocs.io/en/stable/)

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

-  [Miguel Grinberg](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask) 's 
post was used for better understanding of Designing a RESTful API with Python and Flask

“One small step for man, one giant leap for mankind.” 

- [x] Create DataBase
- [x] Receive the wireframes
- [x] R&D libraries
- [x] build back-End
- [x] build the front templates
- [x] Push my commits to Git
- [ ] Receive the first release bugs and fix them
- [ ] Open a pull request
- [ ] Adding more features.




