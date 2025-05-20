import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from .pipeline import recommend


class RecommendHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path != '/recommend':
            self.send_error(404)
            return
        params = parse_qs(parsed.query)
        user_id = int(params.get('user_id', ['0'])[0])
        user = {"id": user_id}
        results = recommend(user)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(results, ensure_ascii=False).encode('utf-8'))


def run(host='0.0.0.0', port=8000):
    server = HTTPServer((host, port), RecommendHandler)
    print(f"Serving on {host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    run()
