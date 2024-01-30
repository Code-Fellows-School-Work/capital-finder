from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handlerxxx(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "word" in dic:
            url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
            r = requests.get(url + dic["word"])
            data = r.json()
            definitions = []
            for word_data in data:
                definition = word_data["meanings"][0]["definitions"][0]["definition"]
                definitions.append(definition)
            message = str(definitions)

        else:
            message = "Give me a word to define please"

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        name = dic.get("name")

        if name:
            message = f"Aloha {name}"
        else:
            message = "Aloha stranger"

        # message += f"\nGreetings from Python version {platform.python_version()}"
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())