from flask import Flask, render_template, url_for, request, redirect

from _CRUD import get_all_rest, get_all_menuitems, get_all_menuitems_by_restaurant, new_restaurant, new_menu_item, delete_restaurant, update_restaurant, update_menu_item


app = Flask(__name__)


html_output_open = '<html><body>'
html_output_close = '</body></html>'


# @app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def restaurantMenu(restaurant_id):

    restaurants = get_all_rest()
    menu_items = get_all_menuitems()

    # print(restaurants)
    # print(menu_items)

    return render_template("menu.html", restaurants=restaurants, restaurant_id=restaurant_id, menu_items=menu_items)



@app.route('/restaurants/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        new_menu_item(name=request.form['name'], restaurant_id=restaurant_id, description=request.form['description'], price=request.form['price'])
        return redirect(url_for("restaurantMenu", restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)
    ## need to update template to show restaurant name


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):

    menu_items = get_all_menuitems_by_restaurant(restaurant_id=restaurant_id)

    if request.method == 'POST':
        update_menu_item(id=menu_id, new_name=request.form['new_name'], new_description=request.form['new_description'] , new_price=request.form['new_price'])
        return redirect(url_for("restaurantMenu", restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html', menu_items=menu_items, restaurant_id=restaurant_id, menu_id=menu_id)



@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):

    return "page to delete a menu item. Task 3 complete!"



# ### #####  @_@  ##### ### #

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port = 5000)