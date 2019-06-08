from flask_table import Table, Col, LinkCol

class Results(Table):
    pid = Col('Property ID')
    pname = Col('Property name')
    hsr_layout = Col('HSR layout')
    location = Col('Location')
    cordinates = Col('co-ordinate')
    s_room = Col('Sharing room price(Rs.)')
    p_room = Col('Private room(Rs.)')