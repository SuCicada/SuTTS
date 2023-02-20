import os
import sqlite3

from sutts.utils.path import db_path


class AudioEntity:
    id: int
    text: str
    speaker: str
    sampling_rate: int
    data: bytes

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class CacheSqlite:
    sqlite_file = os.path.join(db_path, 'tts.sqlite')
    table_name = 'tts'

    def __init__(self):
        # Connect to the database or create it if it doesn't exist
        self.conn = sqlite3.connect(self.sqlite_file, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        # Create a table if it doesn't exist
        self.cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {self.table_name} (
            id INTEGER PRIMARY KEY, 
            text TEXT, 
            speaker TEXT,
            sampling_rate INTEGER,
            data BLOB
            )
        """)

    def get(self, text: str, speaker: str) -> AudioEntity:
        self.cursor.execute(f"""
        SELECT * FROM {self.table_name} WHERE text=? AND speaker=?
        """, (text, speaker))
        res = self.cursor.fetchone()
        # return dict(res) if res else None
        return AudioEntity(**dict(res)) if res else None

    def save_from_obj(self, audio_entity: AudioEntity):
        return self.save(audio_entity.text, audio_entity.speaker, audio_entity.sampling_rate, audio_entity.data)

    def save(self, text: str, speaker: str, sampling_rate: int, data: bytes):
        # Insert data into the table
        self.cursor.execute(f"""INSERT INTO {self.table_name} (text, speaker,sampling_rate,data) VALUES (?,?,?,?)""",
                            (text, speaker, sampling_rate, data))
        print(f"Saved {text} {speaker} {sampling_rate} ")
        # Commit the changes
        self.conn.commit()

    def close(self):
        # Close the connection
        self.conn.close()
