from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


### READ - FETCHING DATA FROM DB ###

def get_all_rest():
    output = {}
    # print([(e.id, e.name) for e in session.query(Restaurant).all()])
    for rest in session.query(Restaurant).all():
        output[rest.id] = rest.name
    return output

def get_all_menuitems():
    output = {}
    # print([(e.id, e.name) for e in session.query(Restaurant).all()])
    for item in session.query(MenuItem).all():
        output[item.id] = {}
        output[item.id]["name"] = item.name
        output[item.id]["price"] = item.price
        output[item.id]["restaurant_id"] = item.restaurant_id
        output[item.id]["description"] = item.description
    return output

### CREATING DATA ###

def new_restaurant(name):
    userRestaurant = Restaurant(name=name)
    session.add(userRestaurant)
    session.commit()
    print("Added new restaurant, full list: ", [(e.id, e.name) for e in session.query(Restaurant).all()])

def new_menu_item(name, restaurant_id, description="", price=""):
    userMenuItem = MenuItem(name=name, restaurant_id=restaurant_id, description=description, price=price, course="")
    session.add(userMenuItem)
    session.commit()
    print("Added new menu_item, full list: ", [(e.id, e.name, e.restaurant_id) for e in session.query(MenuItem).all()])


### DELETING DATA ###

def delete_restaurant(id):
    to_be_deleted = session.query(Restaurant).filter_by(id=id).one()
    session.delete(to_be_deleted)
    session.commit()
    print("Record id = %s was succesfully deleted" % str(id))

def delete_menu_item(id):
    to_be_deleted = session.query(MenuItem).filter_by(id=id).one()
    session.delete(to_be_deleted)
    session.commit()
    print("Record id = %s was succesfully deleted" % str(id))


### UPDATING DATA ###

def update_restaurant(id, new_name):
    to_be_renamed = session.query(Restaurant).filter_by(id=id).one()
    to_be_renamed.name = new_name
    session.commit()
    print("Record id = %s was succesfully renamed to %s" % (str(id), new_name))

def update_menu_item(id, new_name, new_description, new_price):
    to_be_changed = session.query(MenuItem).filter_by(id=id).one()
    to_be_changed.name = new_name
    to_be_changed.description = new_description
    to_be_changed.price = new_price
    session.commit()
    print("Record id = %s was succesfully renamed to %s" % (str(id), new_name))


if __name__ == "__main__":
    # delete_menu_item(50)
    # delete_menu_item(51)
    pass