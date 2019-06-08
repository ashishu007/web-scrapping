# main.py

from app import app
from db_setup import init_db, db_session
from forms import HotelForm
from flask import flash, render_template, request, redirect, jsonify
from models import Hotels
from tables import Results

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    search = HotelForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
    print(search_string)

    qry = db_session.query(Hotels)
    results = qry.filter_by(hsr_layout = search_string).all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)

@app.route('/new_hotel', methods=['GET', 'POST'])
def new_hotel():
    """
    Add a new Hotel
    """
    form = HotelForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the hotel
        hotel = Hotels()
        save_changes(hotel, form)
        flash('Hotel added successfully!')
        return redirect('/')

    return render_template('new_hotel.html', form=form)

@app.route('/get_results/<hsr>', methods=['GET', 'POST'])
def get_results(hsr):
    db_out = []
    qry = db_session.query(Hotels)
    results = qry.filter_by(hsr_layout = hsr).all()

    if not results:
        return "No data for " + str(hsr)

    else:
        for i in results:
            diction = {
                "Propoerty ID": i.pid,
                "Property Name": i.pname,
                "HSR Layout": i.hsr_layout,
                "Location": i.location,
                "Cordinates": i.cordinates,
                "Shared Room Price": i.s_room,
                "Private Room Price": i.p_room
            }
            print(diction)
            db_out.append(diction)

        return jsonify(db_out)

def save_changes(hotel, form):
    """
    Save the changes to the database
    """
    hotel.pname = form.pname.data
    hotel.hsr_layout = form.hsr_layout.data
    hotel.location = form.location.data
    hotel.cordinates = form.cordinates.data
    hotel.s_room = form.s_room.data
    hotel.p_room = form.p_room.data

    db_session.add(hotel)
    db_session.commit()

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug = True)