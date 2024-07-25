from src.infra.http_server.http_server import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
