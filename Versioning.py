from sqlalchemy_continuum import version_class, parent_class
from models import *
from app import app, dbsession

# When the models have been configured either by calling configure_mappers() or by accessing some of them
# the first time, the following things become available:

version_class(User)  # User History class
parent_class(version_class(User))  # User class


with app.app_context():
    user = User(name='', email='kk$@Dail', password='12jj345')
    dbsession.add(user)
    dbsession.commit()

    # article has now one version stored in database

    user.name = 'user2'
    dbsession.commit()

    user.name = 'user3'
    dbsession.commit()

    user.versions[1].revert()
    dbsession.commit()