import sqlite3


CREATE_HEROES_TABLE = "CREATE TABLE IF NOT EXISTS heroes (id INTEGER PRIMARY KEY, name TEXT, power TEXT, rating INTEGER);"
INSERT_HERO = "INSERT INTO heroes (name, power, rating) VALUES (?,?,?);"
GET_ALL_HEROES = "SELECT * FROM heroes;"
GET_HEROES_BY_NAME = "SELECT * FROM heroes WHERE name = ?;"
GET_BEST_HERO = """
SELECT * FROM heroes
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""


def connect():
    return sqlite3.connect("data.db")


def create_table(connection):
    with connection:
        connection.execute(CREATE_HEROES_TABLE)


def add_hero(connection, name, power, rating):
    with connection:
        connection.execute(INSERT_HERO, (name, power, rating))


def get_all_heroes(connection):
    with connection:
        return connection.execute(GET_ALL_HEROES).fetchall()


def get_heroes_by_name(connection, name):
    with connection:
        return connection.execute(GET_HEROES_BY_NAME, (name,)).fetchall()


def get_best_hero(connection, name):
    with connection:
        return connection.execute(GET_BEST_HERO, (name,)).fetchone()
