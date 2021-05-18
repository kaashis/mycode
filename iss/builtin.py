import urllib.request
import json

URL="http://api.open-notify.org/astros.json"

webobj=urllib.request.urlopen(URL)
reademup=webobj.read().decode("utf-8")

#print(json.loads(reademup))
reademup = json.loads(reademup)
    # send a post with requests.post()
    # send a put with requests.put()
    # send a delete with requests.delete()
    # send a head with requests.head()
## display
def main():
    print('People in Space: ', reademup['number'])
    people_list = reademup['people']
    for person in people_list:
        print(person['name'],"is on the ",person['craft'])

if __name__ == "__main__":
    main()
