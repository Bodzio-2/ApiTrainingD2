import requests
import json

BASE_URL = "https://www.bungie.net/Platform"

headers = {
    "x-api-key": 'c0fb3fa2aa5b4e66a63f3c0af2443885'
}
#BODZIO
#membershipType = "254"
#membershipId = "21023690"
#destinyMembershipId = "4611686018463887794"
#destinyMembershipType = "2"

#DUSZEK
membershipType = "254"
membershipId = "20587488"
destinyMembershipId = "4611686018486261830"
destinyMembershipType = "3"


query_params_LinkedMembership = {
    "getAllMemberships": 'true'
}

getLinkedProfiles = requests.get(f"{BASE_URL}/Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/", headers=headers, params=query_params_LinkedMembership)
print (getLinkedProfiles.json())

with open(f'{membershipId}.json', 'w') as json_file:
    json.dump(getLinkedProfiles.json(), json_file)

query_params_Components = {
    "components": '205'
}


#getProfile = requests.get(f"{BASE_URL}/Destiny2/{destinyMembershipType}/Profile/{destinyMembershipId}/", headers=headers, params=query_params_Components)

#with open(f'{destinyMembershipId}.json', 'w') as json_file:
#    json.dump(getProfile.json(), json_file)

#getManifest = requests.get(f"{BASE_URL}/Destiny2/Manifest/", headers=headers)

#with open('manifest.json', 'w') as json_file:
#    json.dump(getManifest.json(), json_file)

