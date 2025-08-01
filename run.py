#Starts your Flask app
from app import create_app

# This gets the app object from our app folder
app = create_app()

# Run the app only if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)