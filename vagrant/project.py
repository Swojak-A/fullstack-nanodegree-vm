from flask import Flask
app = Flask(__name__)

from _CRUD import get_all_rest, get_all_menuitems, new_restaurant, delete_restaurant, update_name

html_output_in = '<html><body>'
html_output_out = '</body></html>'



@app.route('/')
@app.route('/hello')
def main_page():

    restaurants = get_all_rest()
    menu_items = get_all_menuitems()

    # print(menu_items)

    html_output = ''
    html_output += '<h4>%s</h4>' % restaurants[restaurants.keys()[1]]
    for item in menu_items:
        if menu_items[item]["restaurant_id"] == restaurants.keys()[1]:
            html_output += '<p>%s</p>' % menu_items[item]["name"]

    html_output = "".join([html_output_in, html_output, html_output_out])

    return html_output


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port = 5000)