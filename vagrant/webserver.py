from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

from _CRUD import get_all_rest, new_restaurant, delete_restaurant, update_name

output_open = "<html><body>"
output_close = "</body></html>"

def update_temp_data():
    # creating dict of restaurant names
    restaurants = get_all_rest()

    # creating dict of restaurant url
    restaurant_urls = {}
    for id in restaurants.keys():
        restaurant_urls[id] = "restaurant/" + str(id)
    print("TEMP_DATA updated")
    return restaurants, restaurant_urls


class webserverHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        restaurants, restaurant_urls = update_temp_data()

        try:

            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                # restaurants = get_all_rest()

                output = ""
                output += "<h1>Hello! Welcome to Udacity Restaurant Listing!</h1>"
                for e in restaurants.keys():
                    output += """
                    <div>
                        <h3>%s</h3>
                        <a href="%s">Edit</a>
                        <a href="%s">Delete</a>
                    </div>
                    """ % (restaurants[e], "/restaurant/" + str(e) + "/edit", "/restaurant/" + str(e) + "/delete")
                output += '''
                    </br></br></br>
                    <h2>Want to add your restaurant?</h2>
                    <a href="restaurants/new">click here</a>
                    '''

                output = (output_open + output + output_close)

                self.wfile.write(output)
                # print(output)
                return



            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<h1>Hello!</h1>"
                output += """
                    <form method='POST' enctype='multipart/form-data'>
                    <h2>Whats your restaurant name?</h2>
                    <input name="new_resturant" type="text" >
                    <input type="submit" value="Submit"> </form>
                """
                output += """
                <p>To get back to main page click <a href="/restaurants">here</a></p>
                """

                output = (output_open + output + output_close)

                self.wfile.write(output)
                # print(output)
                return



            for e in restaurant_urls.keys():
                if self.path.endswith(restaurant_urls[e] + "/edit"):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output = ""
                    output += "<h1>This is edit page for %s restaurant</h1>" % restaurants[e]
                    output += """
                        <form method='POST' enctype='multipart/form-data'>
                        <h2>If you want to rename restaurant put new name below</h2>
                        <input name="new_name" type="text" >
                        <input type="submit" value="Submit"> </form>
                    """
                    output += """
                    <p>To get back to main page click <a href="/restaurants">here</a></p>
                    """

                    output = (output_open + output + output_close)

                    self.wfile.write(output)
                    # print(output)
                    return



            for e in restaurant_urls.keys():
                if self.path.endswith(restaurant_urls[e] + "/delete"):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output = ""
                    output += "<h1>This is delete confirmation page for %s restaurant</h1>" % restaurants[e]
                    output += """
                        <form method='POST' enctype='multipart/form-data'>
                        <h2>If you really want to delete it from database please retype "delete"?</h2>
                        <input name="delete_confirmation" type="text" >
                        <input type="submit" value="Submit"> </form>
                    """
                    output += """
                    <p>To get back to main page click <a href="/restaurants">here</a></p>
                    """

                    output = (output_open + output + output_close)

                    self.wfile.write(output)
                    # print(output)
                    return




        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):

        restaurants, restaurant_urls = update_temp_data()

        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                new_restaurant_name = fields.get("new_resturant")
                delete_confirmation = fields.get("delete_confirmation")
                new_name = fields.get("new_name")



            if self.path.endswith("/restaurants/new"):

                new_restaurant(new_restaurant_name[0])

                output = ""
                output += "<h2>Thank You, for your input</h2>"
                output += "<p>We added <b>%s</b> to our database</p>" % new_restaurant_name[0]
                output += """
                <p>To get back to main page click <a href="/restaurants">here</a></p>
                """

                output = (output_open + output + output_close)

                self.wfile.write(output)



            for e in restaurant_urls.keys():
                if self.path.endswith(restaurant_urls[e] + "/edit"):
                    # print(new_name[0])
                    update_name(e, new_name[0])

                    output = ""
                    output += "<h2>Thank You, for your input</h2>"
                    output += "<p>We renamed <b>%s</b> to <b>%s</b> for you</p> " % (restaurants[e], new_name[0])
                    output += """
                    <p>To get back to main page click <a href="/restaurants">here</a></p>
                    """

                    output = (output_open + output + output_close)

                    self.wfile.write(output)



            for e in restaurant_urls.keys():
                if self.path.endswith(restaurant_urls[e] + "/delete"):
                    # print(delete_confirmation[0])

                    if delete_confirmation[0].lower() == "delete":
                        delete_restaurant(e)

                        output = ""
                        output += "<h2>We have succesfully deleted the record from our database</br>Thank You for your action</h2>"
                        # output += "<p>We added <b>%s</b> to our database</p>" % new_restaurant_name[0]

                        output += """
                            <p>To get back to main page click <a href="/restaurants">here</a></p>
                            """
                    else:
                        output = ""
                        output += "<h2>We were unable to delete the record</h2>"
                        output += "<p>to try again click <a href='/%s'>here</a></p>" % (restaurant_urls[e] + "/delete")
                        print(restaurant_urls[e])
                        output += """
                            <p>To get back to main page click <a href="/restaurants">here</a></p>
                            """

                    output = (output_open + output + output_close)

                    self.wfile.write(output)



        except:
            pass




def main():
    try:
        port = 8000
        server = HTTPServer(('', port), webserverHandler)
        print("Web server running on port %s" % port)
        server.serve_forever()

    except KeyboardInterrupt:
        print("^C entered, stopping the server...")
        server.socket.close()


if __name__ == "__main__":
    main()