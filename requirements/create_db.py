import sqlalchemy as db
import secrets_file


cursor = db.create_engine(secrets_file.connection_credentials)


def main():
    create_table_todos()
    create_table_notes()
    create_table_profiles()
    print("Finished!")
    input("Press Enter to close this window...")


def create_table_todos():
    sql_statement = "CREATE TABLE TASKS (" \
                    "id MEDIUMINT(9) NOT NULL AUTO_INCREMENT," \
                    "creator_id MEDIUMINT(9) NOT NULL," \
                    "text VARCHAR(64) NOT NULL," \
                    "is_done BOOLEAN NOT NULL," \
                    "creation_date DATETIME NOT NULL," \
                    "color VARCHAR(10) DEFAULT 'Using UnChat'," \
                    "PRIMARY KEY (id)," \
                    "FOREIGN KEY (creator_id) REFERENCES PROFILES(id)" \
                    ")"
    cursor.execute(sql_statement)
    print("Created 'TASKS' table successfully!")


# only a blueprint since history tables are created automatically
def create_table_notes():
    sql_statement = "CREATE TABLE NOTES (" \
                    "id MEDIUMINT(9) NOT NULL AUTO_INCREMENT," \
                    "creator_id MEDIUMINT(9) NOT NULL" \
                    "content VARCHAR(2048) NOT NULL," \
                    "is_visible BOOLEAN NOT NULL," \
                    "is_highlighted BOOLEAN NOT NULL," \
                    "color VARCHAR(10) NOT NULL," \
                    "PRIMARY KEY (id)," \
                    "FOREIGN KEY (creator_id) REFERENCES PROFILES(id)" \
                    ")"
    cursor.execute(sql_statement)
    print("Created 'NOTES' table successfully!")


def create_table_profiles():
    sql_statement = "CREATE TABLE PROFILES (" \
                    "id MEDIUMINT(9) NOT NULL AUTO_INCREMENT," \
                    "name VARCHAR(16) NOT NULL," \
                    "password VARCHAR(256) NOT NULL," \
                    "creation_date DATETIME NOT NULL," \
                    "PRIMARY KEY (id)" \
                    ")"
    cursor.execute(sql_statement)
    print("Created 'PROFILES' table successfully!")


if __name__ == '__main__':
    main()
