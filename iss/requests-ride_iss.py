#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    ## Call the webservice
    response = requests.get(MAJORTOM)


    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    data_dict = response.json()


    ## display 

    print('People in Space: ', data_dict['number'])
    people_list = data_dict['people']
    for person in people_list:
        print(person['name'],"is on the ",person['craft'])

if __name__ == "__main__":
    main()

