import csv
from app import app, dbsession
from models import *


def importing():

    user = User(name='Madjeed', email='md4@zsdwaeekjfhlsdfk.ochom', password='123456', role='admin')
    dbsession.add(user)

    f = open("static/posts.csv")
    reader = csv.reader(f)
    for aut_fav, catnames, uptitle, title, mainp, mainimg, title2, secondp, video, galtitle, galtext, galimg1, \
        galimgtxt1, galimg2, galimgtxt2, galimg3, galimgtxt3, galimg4, galimgtxt4, galimg5, galimgtxt5, galimg6,\
        galimgtxt6, tittle3, subtitle, thirdp, hashtags, duration in reader:

        aut_fav = bool(aut_fav)
        hashtags = hashtags.split(';')
        catnames = catnames.split(';')

        user_post = user.add_post(aut_fav=aut_fav, uptitle=uptitle, title=title, mainp=mainp, mainimg=mainimg,
                                  title2=title2, secondp=secondp, video=video, galtitle=galtitle, galtext=galtext,
                                  galimg1=galimg1, galimgtxt1=galimgtxt1, galimg2=galimg2, galimgtxt2=galimgtxt2,
                                  galimg3=galimg3, galimgtxt3=galimgtxt3, galimg4=galimg4, galimgtxt4=galimgtxt4,
                                  galimg5=galimg5, galimgtxt5=galimgtxt5, galimg6=galimg6, galimgtxt6=galimgtxt6,
                                  tittle3=tittle3, subtitle=subtitle, thirdp=thirdp, hashtags=hashtags,
                                  duration=duration)
        dbsession.add(user_post)
        print('add cats')
        for name in catnames:
            cat = user_post.add_cat(name)
            user_post.categories.append(cat)
            print(user_post, cat)


        print("lets go")
        print(user_post)
        dbsession.add(user_post)
        dbsession.commit()
        dbsession.close()
        print('done')


if __name__ == "__main__":
    with app.app_context():
        importing()
