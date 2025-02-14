import sqlite3

class VocabDB:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def check_vocab_exist(self, vocab):
        """Check if `vocab` exists in the database. If it does, return the row; otherwise None."""
        query = "SELECT * FROM vocabulary_main WHERE vocab = ? LIMIT 1"
        self.cursor.execute(query, (vocab,))
        return self.cursor.fetchone()

    def get_max_id(self):
        """Get the maximum ID in the 'vocabulary_main' table."""
        query = "SELECT MAX(ID) FROM vocabulary_main"
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        return int(row[0]) if row[0] is not None else 0

    def update_vocab(self, vocab, pos, chinese, familiarity):
        """Update the row that matches `vocab` with new data."""
        update_query = """UPDATE vocabulary_main
                          SET part_of_speech = ?, chinese = ?, familiarity = ?
                          WHERE vocab = ?"""
        self.cursor.execute(update_query, (pos, chinese, familiarity, vocab))
        self.conn.commit()

    def insert_vocab(self, vocab_type, vocab, pos, chinese, familiarity):
        """Insert a new vocab into the database."""
        new_id = self.get_max_id() + 1
        insert_query = """INSERT INTO vocabulary_main
                          (ID, vocab_type, vocab, part_of_speech, chinese, familiarity)
                          VALUES (?, ?, ?, ?, ?, ?)"""
        self.cursor.execute(
            insert_query,
            (new_id, vocab_type, vocab, pos, chinese, familiarity)
        )
        self.conn.commit()
