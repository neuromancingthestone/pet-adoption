from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  =  False
app.config['SQLALCHEMY_ECHO'] =  True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

app.app_context().push()
connect_db(app)

@app.route('/')
def list_pets():
    """Shows list of all pets in db"""
    pets = Pet.query.all()
    return render_template('list.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Take user to add a pet form and process data"""
    print(request.form)
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

        flash(f"Created new pet - name is {name}")
        return redirect('/')
    else:
        return render_template("add.html", form=form)

@app.route('/<int:id>', methods=["GET", "POST"])
def edit_pet(id):
    """Show pet edit form and handle edit."""
    pet = Pet.query.get_or_404(id)
    form=EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template("details.html", form=form, pet=pet)
    
@app.route('/<int:id>/delete.html')
def delete_pet(id):
    """Delete the pet"""
    pet = Pet.query.get(id)

    db.session.delete(pet)
    db.session.commit()

    return redirect("/")