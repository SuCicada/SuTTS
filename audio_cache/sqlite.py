import sqlite3

import numpy


class CacheSqlite:
    table_name = 'tts'

    def __init__(self):
        # Connect to the database or create it if it doesn't exist
        self.conn = sqlite3.connect('example.db')
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        # Create a table if it doesn't exist
        self.cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY, 
            text TEXT, 
            speaker INTEGER,
            sampling_rate INTEGER,
            data BLOB
            )
        """)

    def get(self, text: str, speaker: int):
        self.cursor.execute(f"""
        SELECT * FROM {self.table_name} WHERE text=? AND speaker=?
        """, (text, speaker))
        res = self.cursor.fetchone()
        return dict(res) if res else None

    def save(self, text: str, speaker: int, sampling_rate: int, data:bytes):
        # Insert data into the table
        self.cursor.execute(f"""INSERT INTO {self.table_name} (text, speaker,sampling_rate,data) VALUES (?,?,?,?)""",
                            (text, speaker, sampling_rate, data))

        # Commit the changes
        self.conn.commit()

    def close(self):
        # Close the connection
        self.conn.close()
