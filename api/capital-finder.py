from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        # self.dic = dict(query_string_list)  # Store the query dictionary as an instance variable

        # checks if the query string contains the word country
        if "country" in dic:
            country_name = dic["country"]
            url = "https://restcountries.com/v3.1/all?fields=name,country,capital"
            r = requests.get(url + dic["country"])
            data = r.json()
            capital = []
            for country_data in data:
                definition = country_data[0]["capital"][0]
                capital.append(definition)
            message = f"The capital of {country_name} is {str(capital)}"

        else:
            message = "Give me a country or capital please"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
