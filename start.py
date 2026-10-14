import http.server
import webbrowser
from pathlib import Path

PORT = 3000
DIRECTORY = Path(__file__).resolve().parent


class ReusableThreadingServer(http.server.ThreadingHTTPServer):
    allow_reuse_address = True
    daemon_threads = True


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

    def log_message(self, format, *args):
        # Keep console output clean
        print(f"[{self.log_date_time_string()}] {format % args}")


def main():
    url = f"http://localhost:{PORT}"
    print(f"Starting server for {DIRECTORY} at {url}...")

    # Optional: open browser automatically
    try:
        webbrowser.open(url)
    except Exception:
        pass

    with ReusableThreadingServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Server is live at: {url} (http://127.0.0.1:{PORT})")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")


if __name__ == "__main__":
    main()
