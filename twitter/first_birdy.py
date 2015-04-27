from birdy.twitter import UserClient

access_token = "3161805806-5knas90qzqkaLqO11HY9KwhTWKFskukj45tUocP"
access_token_secret = "m1ILxyRFwCoPHzQ55MOieoUObjXh976vz3hcgUK1a8b2G"
consumer_key = "8sOsbXSPd9ZgAzOrrktEu9nKD"
consumer_secret = "pQbOdiJEjWqVrvUFXggcoGnSD9ZgxtXnBer4Xm4RRAmdFsc1G9"

client = UserClient(consumer_key, consumer_secret, access_token, access_token_secret)

print("Getting Resources...")
resource = client.stream.statuses.filter.get(track='python')
print("Printing Data....")
for data in resource.stream():
   print(data)

print("Ending...")
