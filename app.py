"""Flask app for adopt app."""

from flask import Flask, flash, redirect, render_template

from flask_debugtoolbar import DebugToolbarExtension

from models import Pet, db, connect_db

from forms import AddPetForm, EditPetForm

from petfinder_requests import get_random_pet_info, refresh_credentials

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from petfinder_requests import auth_token


connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.route('/')
def root():
    """Shows home page and displays pets that are avilable for adoption"""
    
    pets = Pet.query.filter(Pet.available == True).all()
    unavailable_pets = Pet.query.filter(Pet.available == False).all()
    # list comprehension for 1 query  

    refresh_credentials()
    get_random_pet_info()
    random_pet = get_random_pet_info()
    
    return render_template('home.html', 
                            pets=pets, 
                            unavailable_pets=unavailable_pets, 
                            random_pet=random_pet)

@app.route('/add', methods=['GET','POST'])
def add_pet():
    """Shows form to add a pet; handles adding"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name}!")
        return redirect('/')
    
    else:
        return render_template('add.html', form=form)

@app.route('/pet/<int:pet_id>', methods=['GET','POST'])
def pet_info_and_pet_edit(pet_id):
    """Shows pet info and edit info form"""

    pet = Pet.query.get_or_404(pet_id)

    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available

        db.session.commit()

        flash(f"Edited {pet.name}!")
        return redirect('/')
    
    else:
        return render_template('info.html', pet=pet, form=form)