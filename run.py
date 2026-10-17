
import sys
import http.server as hs
import functools

def http_run():
    args = sys.argv
    arg1 = args[1]

    port = 8000
    bind = "127.0.0.1"
    directory = arg1

    handler = functools.partial(hs.SimpleHTTPRequestHandler, directory=directory)

    with hs.HTTPServer((bind, port), handler) as httpd:
        print(f"Serving {directory} at http://{bind}:{port}")
        httpd.serve_forever()


if __name__ == "__main__":
    http_run()