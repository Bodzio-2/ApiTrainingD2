from PIL import Image
import requests

URL = "https://www.bungie.net/common/destiny2_content/icons/DestinyDamageTypeDefinition_092d066688b879c807c3b460afdd61e6.png"

response = requests.get(URL)
open("image.png", "wb").write(response.content)

im = Image.open('image.png')

im.show()