# forms.py

from wtforms import Form, StringField, SelectField, validators

class HotelForm(Form):
    pid = StringField('Property ID')
    pname = StringField('Property Name')
    hsr_layout = StringField('HSR Layout')
    location = StringField('Location')
    cordinates = StringField('Cordinates')
    s_room = StringField('Single Room Price')
    p_room = StringField('Private Room Price')
    search = StringField('')