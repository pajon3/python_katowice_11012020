import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_pracownicy_table = """
CREATE TABLE IF NOT EXISTS pracownicy (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  imie TEXT NOT NULL,
  nazwisko TEXT NOT NULL,
  rok_ur INTEGER,
  pensja REAL
);
"""
create_posts_table = """
CREATE TABLE IF NOT EXISTS posts(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  title TEXT NOT NULL, 
  description TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  text TEXT NOT NULL, 
  user_id INTEGER NOT NULL, 
  post_id INTEGER NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

create_likes_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_id INTEGER NOT NULL, 
  post_id integer NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""


connection = create_connection("pracownicy.sqlite")
execute_query(connection, create_pracownicy_table)
# execute_query(connection, create_posts_table)
# execute_query(connection, create_comments_table)
# execute_query(connection, create_likes_table)

#
create_pracownicy = """
INSERT INTO
  pracownicy (imie, nazwisko, rok_ur, pensja)
VALUES
  ('James', "Dean", 1972, 60000),
  ('Ala', "Dean", 1974, 70000);
"""
#
execute_query(connection, create_pracownicy)
#
# create_posts = """
# INSERT INTO
#   posts (title, description, user_id)
# VALUES
#   ("Happy", "I am feeling very happy today", 1),
#   ("Hot Weather", "The weather is very hot today", 2),
#   ("Help", "I need some help with my work", 2),
#   ("Great News", "I am getting married", 1),
#   ("Interesting Game", "It was a fantastic game of tennis", 5),
#   ("Party", "Anyone up for a late-night party today?", 3);
# """
#
# # execute_query(connection, create_posts)
#
# create_comments = """
# INSERT INTO
#   comments (text, user_id, post_id)
# VALUES
#   ('Count me in', 1, 6),
#   ('What sort of help?', 5, 3),
#   ('Congrats buddy', 2, 4),
#   ('I was rooting for Nadal though', 4, 5),
#   ('Help with your thesis?', 2, 3),
#   ('Many congratulations', 5, 4);
# """
#
# create_likes = """
# INSERT INTO
#   likes (user_id, post_id)
# VALUES
#   (1, 6),
#   (2, 3),
#   (1, 5),
#   (5, 4),
#   (2, 4),
#   (4, 2),
#   (3, 6);
# """
#
# # execute_query(connection, create_comments)
# # execute_query(connection, create_likes)
#
#
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

select_users = "SELECT * from pracownicy"
pracownicy = execute_read_query(connection, select_users)

print(pracownicy)

#
# for user in users:
#     print(user)
#
# # select_posts = "SELECT * FROM posts"
# # posts = execute_read_query(connection, select_posts)
#
# for post in posts:
#     print(post)
#
# # JOIN
#
#
# select_users_posts = """
# SELECT
#   users.id,
#   users.name,
#   posts.description
# FROM
#   posts
#   INNER JOIN users ON users.id = posts.user_id
# """
#
# users_posts = execute_read_query(connection, select_users_posts)
#
# for users_post in users_posts:
#     print(users_post)