from flask import Flask, request
import sqlite3
import sqlalchemy
import requests

app = Flask(__name__)

# Connect to SQLite database
def connect_db():
    connection = sqlite3.connect("shows.db")
    return connection

# Get show information from API and save to database
@app.route("/shows", methods=["POST"])
def add_show():
    show_name = request.json["show_name"]

    # Call the API and get show information
    response = requests.get(f"http://api.tmdb.org/3/search/movie?api_key=<API_KEY>&query={show_name}")
    show_info = response.json()

    # Extract the show information
    runtime = show_info["runtime"]
    genre = show_info["genre"]
    synopsis = show_info["synopsis"]
    watched_on = show_info["watched_on"]

    # Save show information to database
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO shows (show_name, runtime, genre, synopsis, watched_on)
        VALUES (?, ?, ?, ?, ?)
    """, (show_name, runtime, genre, synopsis, watched_on))
    conn.commit()
    conn.close()

    return {"message": "Show added successfully"}, 201

# Fetch all shows from the database
@app.route("/shows", methods=["GET"])
def get_shows():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM shows
    """)
    shows = cursor.fetchall()
    conn.close()

    return {"shows": shows}, 200

if __name__ == "__main__":
    app.run()