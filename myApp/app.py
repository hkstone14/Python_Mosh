import json
from pathlib import Path
import sqlite3


data = Path("movies.json").read_text()
movies = json.loads(data)

# Inserting into the Database
with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Movies VALUES(?, ?, ?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()


# Retrieve from Database(SQLiteDB)
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * from Movies"
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
    movies_fetch = cursor.fetchall()
    print(movies_fetch)


