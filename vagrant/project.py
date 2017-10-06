from flask import Flask, render_template, url_for, request, redirect

from _CRUD import get_all_rest, get_all_menuitems, new_restaurant, delete_restaurant, update_name, new_menu_item


app = Flask(__name__)


html_output_open = '<html><body>'
html_output_close = '</body></html>'


# @app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def restaurantMenu(restaurant_id):

    restaurants = get_all_rest()
    menu_items = get_all_menuitems()

    # print(menu_items)

    return render_template("menu.html", restaurants=restaurants, restaurant_id=restaurant_id, menu_items=menu_items)



@app.route('/restaurants/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        new_menu_item(name=request.form['name'], restaurant_id=restaurant_id)
        return redirect(url_for("restaurantMenu", restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)



@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):

    return "page to edit a menu item. Task 2 complete!"



@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):

    return "page to delete a menu item. Task 3 complete!"



# ### #####  @_@  ##### ### #

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port = 5000)