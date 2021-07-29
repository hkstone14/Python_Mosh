import json
from pathlib import Path
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


#email module added with
message = MIMEMultipart()
message["from"] = "Harikrushna Patel"
message["to"] = "abc123@gmail.com"
message["subject"] = "This is my testing module for email"
message.attach(MIMEText("Body"))
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("abc@gmail.com", "abc@12324")
    smtp.send_message(message)
    print("Sent...")


# SQLite3 db insert and get
data = Path("movies.json").read_text()
movies = json.loads(data)

# Inserting into the Database
with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Movies VALUES(?, ?, ?)"
    for movie in movies:
        conn.execute(command, tuple(movie.values()))
    conn.commit()


# Retrieve from Database
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * from Movies"
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
    movies_fetch = cursor.fetchall()
    print(movies_fetch)


