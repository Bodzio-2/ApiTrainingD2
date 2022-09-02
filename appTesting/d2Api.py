import sqlite3
from sqlite3 import Error
import json
from venv import create
import requests
from os.path import exists

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

def listEquippedItems(membershipType, membershipId):
    query_params_Components={
        "components": '205'
    }

    query_params_LinkedMembership = {
        "getAllMemberships": 'true'
    }

    getLinkedProfiles = requests.get(f"{BASE_URL}/Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/", headers=headers, params=query_params_LinkedMembership)
    destinyMembershipType = getLinkedProfiles.json()['Response']['profiles'][0]['membershipType']
    destinyMembershipId = getLinkedProfiles.json()['Response']['profiles'][0]['membershipId']

    getProfile = requests.get(f"{BASE_URL}/Destiny2/{destinyMembershipType}/Profile/{destinyMembershipId}/", headers=headers, params=query_params_Components)

    itemsHash = []

    characterId = list(getProfile.json()['Response']['characterEquipment']['data'].keys())[0]
    
    for item in getProfile.json()['Response']['characterEquipment']['data'][f'{characterId}']['items']:
        itemsHash.append(item['itemHash'])
    
    return itemsHash

def displayItemNames(conn, itemIDs):
    TABLE = "DestinyCollectibleDefinition"
    for id in itemIDs:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {TABLE} WHERE json LIKE '%{id}%'")

        rows = cur.fetchall()

        for row in rows:
            jsonRow = json.loads(row[1])
            print(jsonRow['displayProperties']['name'])


def printEquippedItems(mbmrType, mbmrId, database):
    
    if mbmrType == '' or mbmrId == '':
        pass
    
    manifest = create_connection(database)
    equippedList = listEquippedItems(mbmrType, mbmrId)
    downloadItemIcons(equippedList, database)

    imgPaths = []

    TABLE = "DestinyCollectibleDefinition"
    for id in equippedList:
        cur = manifest.cursor()
        cur.execute(f"SELECT * FROM {TABLE} WHERE json LIKE '%{id}%'")

        rows = cur.fetchall()

        for row in rows:
            jsonRow = json.loads(row[1])
            print(jsonRow['displayProperties']['name'])
            if jsonRow['displayProperties']['hasIcon']:
                imgPaths.append(f"appTesting/images/{id}.png")
            else:
                imgPaths.append(f"appTesting/images/unknown.png")
    
    return imgPaths


def downloadItemIcons(itemIds, database):
    manifest = create_connection(database)
    TABLE = "DestinyCollectibleDefinition"

    for id in itemIds:

        if exists(f"appTesting/images/{id}.png"):
            continue

        cur = manifest.cursor()
        cur.execute(f"SELECT * FROM {TABLE} WHERE json LIKE '%{id}%'")

        rows = cur.fetchall()
        for row in rows:
            jsonRow = json.loads(row[1])
            if jsonRow['displayProperties']['hasIcon']:
                link = jsonRow['displayProperties']['icon']
                URL = f"https://www.bungie.net{link}"
                response = requests.get(URL)
                open(f"appTesting/images/{id}.png", "wb").write(response.content)
                print(id)

