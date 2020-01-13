from sqlalchemy_continuum import version_class, parent_class
from models import *
from app import app, dbsession

# When the models have been configured either by calling configure_mappers() or by accessing some of them
# the first time, the following things become available:

version_class(User)  # User History class
parent_class(version_class(User)) # User class


with app.app_context():
    user = User(name='user1', email='@email', password='12345')
    dbsession.add(user)
    dbsession.commit()

    # article has now one version stored in database

    user.name = 'user2'
    dbsession.commit()


    user.versions[0].revert()
    dbsession.commit()