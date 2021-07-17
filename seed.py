"""Seed file to make sample data for pets db."""

from models import Pet, db
from app import app

DOG_URL = 'https://ourfunnylittlesite.com/wp-content/uploads/2018/07/1-4-696x696.jpg'
CAT_URL = 'https://www.gannett-cdn.com/-mm-/938db79d26e3ee729e6b7468e9f299d2e4ef16df/c=0-279-2491-1684/local/-/media/USATODAY/test/2013/09/05/1378400626002--NASBrd-08-11-2013-Tennessean-1-B004-2013-08-10-IMG-NAS-FATCAT-03jpg-1-1-P.jpg'
PORCUPINE_URL = 'https://www.eatliver.com/wp-content/uploads/2019/04/bearded-dragon1.jpg'

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
whiskey = Pet(name='Whiskey', species="dog", photo_url=DOG_URL, age='baby', notes='is cute', available=True)
bowser = Pet(name='Bowser', species="cat", photo_url=CAT_URL, age='young', notes='is terrifying', available=False)
spike = Pet(name='Spike', species="porcupine", photo_url=PORCUPINE_URL, age='senior', available=True)

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)

db.session.commit()