#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    start_date_value=input("Please enter the start date(YYYY-MM-DD):")
    startdate = "start_date="+start_date_value
    end_date_value=input("Please enter the end date(YYYY-MM-DD):")
    enddate="end_date="+end_date_value
    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds+"&"+enddate)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
#    print(neodata)
    largest={"absolute_magnitude_h":"0.0"}
    smallest={"absolute_magnitude_h":"999999999999999.99"}
    count =0
    for everydate in neodata["near_earth_objects"]:
        for asterdict in neodata["near_earth_objects"][everydate]:
            if float(asterdict["absolute_magnitude_h"])>float(largest["absolute_magnitude_h"]):
                largest=asterdict
            if float(asterdict["absolute_magnitude_h"])<float(smallest["absolute_magnitude_h"]):
                smallest=asterdict
            if asterdict["is_potentially_hazardous_asteroid"]:
             t   count += 1
    print("Largest assteroid in this date range: ",largest["name"])
    print("Smallest assteroid in this date range: ",smallest["name"])
    print("Number of potentially hazardous asteroid: ",count)
        
if __name__ == "__main__":
    main()

