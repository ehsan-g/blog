import csv
from app import app, dbsession
from models import *


def importing():

    user = User(name='Madjeed',lastname='amiri', email='md4@zsdwaeekjfhlsdfk.ochom', password='123456', role='admin')
    dbsession.add(user)

    f = open("static/posts.csv")
    reader = csv.reader(f)
    for aut_fav, catnames, uptittle, tittle, mainp, mainimg, tittle2, secondp, video, galtittle, galtext, galimg1, \
        galimgtxt1, galimg2, galimgtxt2, galimg3, galimgtxt3, galimg4, galimgtxt4, galimg5, galimgtxt5, galimg6,\
        galimgtxt6, tittle3, subtittle, thirdp, hashtags, duration in reader:

        aut_fav = bool(aut_fav)
        hashtags = hashtags.split(';')
        catnames = catnames.split(';')


        user_post = user.add_post(aut_fav=aut_fav, uptittle=uptittle, tittle=tittle, mainp=mainp, mainimg=mainimg,
                                  tittle2=tittle2, secondp=secondp, video=video, galtittle=galtittle, galtext=galtext,
                                  galimg1=galimg1, galimgtxt1=galimgtxt1, galimg2=galimg2, galimgtxt2=galimgtxt2,
                                  galimg3=galimg3, galimgtxt3=galimgtxt3, galimg4=galimg4, galimgtxt4=galimgtxt4,
                                  galimg5=galimg5, galimgtxt5=galimgtxt5, galimg6=galimg6, galimgtxt6=galimgtxt6,
                                  tittle3=tittle3, subtittle=subtittle, thirdp=thirdp, hashtags=hashtags,
                                  duration=duration)
        dbsession.add(user_post)

        for name in catnames:
            cat = user_post.add_cat(name)
            user_post.categories.append(cat)

        dbsession.add(user_post)
        dbsession.commit()
        dbsession.close()


if __name__ == "__main__":
    with app.app_context():
        importing()
