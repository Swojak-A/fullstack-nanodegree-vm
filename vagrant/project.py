from flask import Flask
app = Flask(__name__)

from _CRUD import get_all_rest, get_all_menuitems, new_restaurant, delete_restaurant, update_name

html_output_open = '<html><body>'
html_output_close = '</body></html>'



@app.route('/')
@app.route('/restaurants')
def main_page():

    restaurants = get_all_rest()
    menu_items = get_all_menuitems()

    # print(menu_items)

    html_output = ''
    html_output += '<h4>%s</h4>' % restaurants[restaurants.keys()[1]]


    for item in menu_items:

        if menu_items[item]["restaurant_id"] == restaurants.keys()[1]:
            html_paragraph = '<p>'
            html_paragraph += '%s</br>%s</br>%s' % (menu_items[item]["name"],menu_items[item]["price"],menu_items[item]["description"])
            html_paragraph += "</p>"
            html_output += html_paragraph

    html_output = "".join([html_output_open, html_output, html_output_close])

    return html_output


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port = 5000)