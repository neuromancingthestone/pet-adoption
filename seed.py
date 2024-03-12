"""Seed file to make sample data for pets db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
whiskey = Pet(
    name='Whiskey', 
    species="dog", 
    photo_url="https://cdn-prod.medicalnewstoday.com/content/images/articles/322/322868/golden-retriever-puppy.jpg", 
    age=4, 
    available=True)
bowser = Pet(
    name='Bowser', 
    species="dog", 
    photo_url="https://media.wired.com/photos/65651b7225ccbd8cc7d5403c/master/pass/Science-Life-Extension-Drug-for-Big-Dogs-Is-Getting-Closer-1330545769.jpg",
    age=2, 
    notes="Very good boy", 
    available=True)
spike = Pet(
    name='Spike', 
    species="porcupine", 
    photo_url="https://i.ytimg.com/vi/ZphlCdI2yqA/sddefault.jpg",
    age=100, 
    notes="Very spiky boy", 
    available=False)

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)

# Commit--otherwise, this never gets saved!
db.session.commit()
