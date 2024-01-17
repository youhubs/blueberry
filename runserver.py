"""
This is the entry point to the application.
"""
from farm import create_app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True, port=5001)
