# Connect to the database
conn = sqlite3.connect("shows.db")
cursor = conn.cursor()

# Execute a SELECT statement to retrieve the information
cursor.execute("SELECT * FROM shows")

# Fetch the result
result = cursor.fetchall()

# Loop through the result and print each row
for row in result:
    print(row)

# Close the connection to the database
conn.close()