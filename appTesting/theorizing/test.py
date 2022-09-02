import sqlite3
from sqlite3 import Error
import json
import requests

BASE_URL = "https://www.bungie.net/Platform"

headers = {
    "x-api-key": 'c0fb3fa2aa5b4e66a63f3c0af2443885'
}

membershipType = ''
membershipId = ''

query_params_LinkedMembership = {
        "getAllMemberships": 'true'
    }

getLinkedProfiles = requests.get(f"{BASE_URL}/Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/", headers=headers, params=query_params_LinkedMembership)

#print(getLinkedProfiles.json())
print(getLinkedProfiles.json()['Response']['profiles'][0]['membershipType'])
print(getLinkedProfiles.json()['Response']['profiles'][0]['membershipId'])

type = getLinkedProfiles.json()['Response']['profiles'][0]['membershipType']
print(type)