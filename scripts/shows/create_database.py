import sqlite3

# Connect to the database
conn = sqlite3.connect('shows.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS shows (
        name TEXT PRIMARY KEY,
        runtime INTEGER,
        platforms TEXT,
        genre TEXT,
        synopsis TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        show_name TEXT,
        user_name TEXT,
        rating INTEGER,
        review_text TEXT,
        FOREIGN KEY (show_name) REFERENCES shows (name)
    )
''')

# Insert data into the tables
show = ('Breaking Bad', 62, 'Netflix', 'Drama', 'A high school chemistry teacher diagnosed with inoperable lung cancer turns to manufacturing and selling methamphetamine in order to secure his family\'s future.')
cursor.execute('INSERT INTO shows VALUES (?,?,?,?,?)', show)

review = ('Breaking Bad', 'Jane Doe', 5, 'One of the best shows I have ever watched!')
cursor.execute('INSERT INTO reviews VALUES (?,?,?,?)', review)

# Commit the changes and close the connection
conn.commit()
conn.close()