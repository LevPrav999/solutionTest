from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/hello")
    def hello():
        return jsonify(message="Hello from Flask")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
