from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

def get_all_rest():
    output = {}
    # print([(e.id, e.name) for e in session.query(Restaurant).all()])
    for rest in session.query(Restaurant).all():
        output[rest.id] = rest.name
    return output

def new_restaurant(name):
    userRestaurant = Restaurant(name=name)
    session.add(userRestaurant)
    session.commit()
    print("Added new restaurant, full list: ", [(e.id, e.name) for e in session.query(Restaurant).all()])

def delete_restaurant(id):
    to_be_deleted = session.query(Restaurant).filter_by(id=id).one()
    session.delete(to_be_deleted)
    session.commit()
    print("Record id = %s was succesfully deleted" % str(id))

def update_name(id, new_name):
    to_be_renamed = session.query(Restaurant).filter_by(id=id).one()
    to_be_renamed.name = new_name
    session.commit()
    print("Record id = %s was succesfully renamed to %s" % (str(id), new_name))