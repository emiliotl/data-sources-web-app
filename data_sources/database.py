import psycopg2


class CursorFromConnection:

    def __init__(self, credentials):
        self.connection = None
        self.cursor = None
        self.credentials = credentials

    def __enter__(self):
        self.connection = psycopg2.connect(**self.credentials)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        self.connection.close()


class Database:

    def __init__(self, credentials):
        self.credentials = credentials
        self.cursor = CursorFromConnection(self.credentials)

    def query_to_insert_data(self, query, *args):
        with self.cursor as cursor:
            cursor.execute(query, *args)

    def query_to_select_data(self, query, *args):
        with self.cursor as cursor:
            cursor.execute(query, *args)
            return [row[0] for row in cursor.fetchall()]

    def get_source_access_object(self):
        return self
