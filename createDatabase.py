import sqlite3

connection = sqlite3.connect("bdd.db") # Stocker la connexion à la bdd
cursor = connection.cursor() #On y accédera ensuite à partir du curseur

cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        name TEXT             NOT NULL,
        mdp TEXT              NOT NULL
    );
    """
)

connection.commit() # Save changes
connection.close() # End connection after edit