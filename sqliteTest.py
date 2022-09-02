import sqlite3
from sqlite3 import Error
import json
from PIL import Image
import requests

BASE_URL = "https://www.bungie.net/Platform"

headers = {
    "x-api-key": 'c0fb3fa2aa5b4e66a63f3c0af2443885'
}

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

def listEquippedItems(destinyMembershipType, destinyMembershipId, characterId):
    query_params_Components = {
        "components": '205'
    }

    getProfile = requests.get(f"{BASE_URL}/Destiny2/{destinyMembershipType}/Profile/{destinyMembershipId}/", headers=headers, params=query_params_Components)

    itemsHash = []

    for item in getProfile.json()['Response']['characterEquipment']['data'][f'{characterId}']['items']:
        itemsHash.append(item['itemHash'])

    return itemsHash

def displayEquippedWeaponNames(conn, weaponIDs):
    TABLE = "DestinyCollectibleDefinition"
    for id in weaponIDs:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {TABLE} WHERE json LIKE '%{id}%'")

        rows = cur.fetchall()

        for row in rows:
            jsonRow = json.loads(row[1])
            print(jsonRow['displayProperties']['name'])      

database = r"world_sql_content_eab836f0f0bd68f7ac09055c2e38fe14.sqlite3"
manifest = create_connection(database)

#displayDamageTypes(manifest)
#displayEquippedWeaponNames(manifest)

equippedListBod = listEquippedItems("2", "4611686018463887794", "2305843009366923962")
#print(equippedList)
print("Bodzio:")
displayEquippedWeaponNames(manifest, equippedListBod)

equippedListDusz = listEquippedItems("3", "4611686018486261830", "2305843009417904195")
print("Duszek:")
displayEquippedWeaponNames(manifest, equippedListDusz)