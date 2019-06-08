from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///myhotel.db', echo=True)
Base = declarative_base()

class Hotels(Base):
    """"""
    __tablename__ = "hotels"

    pid = Column(Integer, primary_key=True)
    pname = Column(String)
    hsr_layout = Column(String)
    location = Column(String)
    cordinates = Column(String)
    s_room = Column(String)
    p_room = Column(String)

# create tables
Base.metadata.create_all(engine)