from wsgiref.simple_server import make_server


def hello(env, response):
    response("200 OK", [("Content-type", "text/html")])
    return [b"<h1>Hello Kitty!</h1>"]


if __name__ == "__main__":
    web_server = make_server(host="", port=9527, app=hello)

    print("server on 9527!")
    web_server.serve_forever()
