import psycopg2


class CursorFromConnection:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = psycopg2.connect(
            host="",
            database="",
            user="",
            password=""
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        self.connection.close()


def query_to_insert_data(query, *args):
    with CursorFromConnection() as cursor:
        cursor.execute(query, *args)


def query_to_select_data(query, *args):
    with CursorFromConnection() as cursor:
        cursor.execute(query, *args)
        return [row[0] for row in cursor.fetchall()]
