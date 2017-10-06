from flask import Flask

from _CRUD import get_all_rest, get_all_menuitems, new_restaurant, delete_restaurant, update_name


app = Flask(__name__)


html_output_open = '<html><body>'
html_output_close = '</body></html>'


@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def main_page(restaurant_id):

    restaurants = get_all_rest()
    menu_items = get_all_menuitems()

    # print(menu_items)

    html_output = ''
    html_output += '<h4>%s</h4>' % restaurants[restaurants.keys()[restaurant_id]]


    for item in menu_items:

        if menu_items[item]["restaurant_id"] == restaurants.keys()[restaurant_id]:
            html_paragraph = '<p>'
            html_paragraph += '%s</br>%s</br>%s' % (menu_items[item]["name"],menu_items[item]["price"],menu_items[item]["description"])
            html_paragraph += "</p>"
            html_output += html_paragraph

    html_output = "".join([html_output_open, html_output, html_output_close])

    return html_output



@app.route('/restaurants/<int:restaurant_id>/menu/new/')
def newMenuItem(restaurant_id):

    return "page to create a new menu item. Task 1 complete!"



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