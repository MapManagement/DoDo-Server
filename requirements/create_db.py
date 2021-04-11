import sqlalchemy as db
import secrets_file


cursor = db.create_engine(secrets_file.connection_credentials)


def main():
    create_table_todos()
    create_table_notes()
    create_table_profiles()
    create_table_tags()
    create_table_notes_tags()
    print("Finished!")
    input("Press Enter to close this window...")


def create_table_todos():
    sql_statement = "CREATE TABLE tasks (" \
                    "id MEDIUMINT(9) NOT NULL AUTO_INCREMENT," \
                    "creator_id MEDIUMINT(9) NOT NULL," \
                    "text VARCHAR(64) NOT NULL," \
                    "is_done BOOLEAN NOT NULL," \
                    "creation_date DATETIME NOT NULL," \
                    "color VARCHAR(10) DEFAULT '#8e47d1'," \
                    "PRIMARY KEY (id)," \
                    "FOREIGN KEY (creator_id) REFERENCES profiles(id)" \
                    ")"
    cursor.execute(sql_statement)
    print("Created 'tasks' table successfully!")


def create_table_notes():
    sql_statement = "CREATE TABLE notes (" \
                    "id MEDIUMINT(9) NOT NULL AUTO_INCREMENT," \
                    "creator_id MEDIUMINT(9) NOT NULL" \
                    "content VARCHAR(2048) NOT NULL," \
                    "is_visible BOOLEAN NOT NULL," \
                    "is_highlighted BOOLEAN NOT NULL," \
                    "color VARCHAR(10) NOT NULL," \
                    "PRIMARY KEY (id)," \
                    "FOREIGN KEY (creator_id) REFERENCES profiles(id)" \
                    ")"
    cursor.execute(sql_statement)
    print("Created 'notes' table successfully!")


def create_table_profiles():
    sql_statement = "CREATE TABLE profiles (" \
                    "id MEDIUMINT(9) NOT NULL AUTO_INCREMENT," \
                    "name VARCHAR(16) NOT NULL," \
                    "password VARCHAR(256) NOT NULL," \
                    "creation_date DATETIME NOT NULL," \
                    "PRIMARY KEY (id)" \
                    ")"
    cursor.execute(sql_statement)
    print("Created 'profiles' table successfully!")


def create_table_tags():
    sql_statement = "CREATE TABLE tags(" \
                    "id MEDIUMINT(9) NOT NULL AUTO_INCREMENT," \
                    "name VARCHAR(20) NOT NULL," \
                    "PRIMARY KEY (id)" \
                    ")"
    cursor.execute(sql_statement)
    print("Created 'tags' table successfully!")


def create_table_notes_tags():
    sql_statement = "CREATE TABLE tags(" \
                    "note_id MEDIUMINT(9) NOT NULL" \
                    "tag_id MEDIUMINT(9) NOT NULL," \
                    "FOREIGN KEY (note_id) REFERENCES notes(id)," \
                    "FOREIGN KEY (tag_id) REFERENCES tags(id)" \
                    ")"
    cursor.execute(sql_statement)
    print("Created 'notes_tags' table successfully!")


if __name__ == '__main__':
    main()
