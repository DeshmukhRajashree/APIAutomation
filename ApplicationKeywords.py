import json
import requests
import string
import random

#Common inputs
#Endpoint url
url = "https://api.nexmo.com/v0.2/conversations"
#JWT token using https://developer.nexmo.com/jwt by passing

headers = {
'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2Mzk2MzQwMDEsImV4cCI6MTY0MDE1MjQwMSwianRpIjoiRnIycGpqN2N5NnZOIiwiYXBwbGljYXRpb25faWQiOiI2YmVjODBjMy0yMWI3LTQ2NmItYTQ2NS02YzVhYzdlNGYyZDUifQ.H2bMWg2hcNAEtsnoE52Ot8PcfhClWyHTxV83sKI5TWBOrXYRCWCzFU_ZGwr_jfAkF4wngL2bjzr2AXaEa-uwCdibGdHEpvooAp9i5V8DxwhEDr17mF7uzMYdqTRKC4z76pw7Z5ZmGf6hB2_4HoFNf-9tv1T-FWzcMmXDpU_M4csfAxsdC3YVlxLL2_AQccc1ch2eAajc2yPTjT2lebRuDL3PnB57WryamUdoAMVWx21kfEjbDFiCrkw2jN2qteGgVvtTjrkaYFntEUXpP228XJ4Jnds4CkfvzCqKxmGFCe4IWpKa0AdroxZToVmy2KZiMP86yoXCIeiIs7Ru8-gynA'
,'Content-Type': 'application/json'
}

###################################################################
#keywords to get all converstions.
#Get request with bearer token and return http response object
def getConversations() :
 #make GET request by passing header to Conversation API
 response = requests.request("GET", url, headers=headers)
 return response
###################################################################

#keywords to get a converstion by Id .
#Get request with bearer token and with convesation Id and return http response object
def getConversation(conId):
  #make GET request by passing a specific conversation id that needs to be retrieves
  response = requests.request("GET", url + "/" + conId, headers=headers)
  return response
###################################################################

#keywords to delete a converstion by Id .
#DELETE request with bearer token and with convesation Id and return http response object
def deleteconversation(conId):
  #make DELETE request by passing a specific conversation id that needs to be deleted
  response = requests.request("DELETE", url + "/" + conId, headers=headers)
  return response
###################################################################

#keywords to create a converstion
#POST request with bearer token and with request body
# returns http response object
def createconversation():
  ranString = 'test'.join(random.choices(string.ascii_uppercase,k=2))

  requestBody = {
    "name": "Name"+ranString+"",
    "display_name": "DisplayName"+ranString+"",
    "image_url": "https://example.com/image.png",
    "properties": {
      "ttl": 60
    }
  }
  # convert into JSON using dups()
  # the result is a JSON string:
# POST request to create conversation
  response = requests.request("POST", url, headers=headers, data=json.dumps(requestBody))
  return response