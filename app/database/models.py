import sqlite3


class OktanBD:
    def __init__(self) -> None:
        self.db = sqlite3.connect("sto_oktan.db")
        self.cur = self.db.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS data_table (
                id INTEGER PRIMARY KEY NOT NULL,
                name TEXT,
                username BLOB)""")
        self.db.commit()

    def main(self, name, username):
        self.cur.execute("SELECT username FROM data_table WHERE username = ?", (username,))
        if self.cur.fetchone() is None:
            self.cur.execute("""
            INSERT INTO data_table (
                    name,
                    username)
                    VALUES (?, ?)""", (name, username))
            self.db.commit()
        else:
            print("Существует!")