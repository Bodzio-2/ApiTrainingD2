import sqlite3
from sqlite3 import Error
import json
from PIL import Image
import requests


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def displayDamageTypes(conn):
    TABLE = "DestinyDamageTypeDefinition"
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {TABLE}")

    rows = cur.fetchall()

    for row in rows:
        #print(row)
        jsonRow = json.loads(row[1])
        print(jsonRow['displayProperties']['name'])
        NAME = jsonRow['displayProperties']['name']

        if jsonRow['displayProperties']['hasIcon']:
            imgLink = jsonRow['displayProperties']['icon']
            URL = f"https://www.bungie.net{imgLink}"

            response = requests.get(URL)
            open(f"{NAME}.png", "wb").write(response.content)


            im = Image.open(f'{NAME}.png')
            im.show()
            
        

database = r"world_sql_content_eab836f0f0bd68f7ac09055c2e38fe14.sqlite3"
manifest = create_connection(database)

displayDamageTypes(manifest)