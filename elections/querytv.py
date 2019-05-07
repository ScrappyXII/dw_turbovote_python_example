# handles querying backend TurboVote API and parsing results 

import requests
import json

from elections.us_states import postal_abbreviations

# useful known constants
TURBOVOTE_BASEURL = 'https://api.turbovote.org/elections/'
TURBOVOTE_HEADERS = {'Accept': 'application/json'}
TURBOVOTE_UPCOMINGEP = "upcoming"
TURBOVOTE_BASEQS = '?district-divisions='
TURBOVOTE_BASEOCDID = 'ocd-division/country:us'
TURBOVOTE_STATEOCDID = '/state:'
TURBOVOTE_PLACEOCDID = '/place:'

def generateStateOCDID(state):
    """ generate OCD-ID string for state """
    ocdid = TURBOVOTE_BASEOCDID
    ocdid += TURBOVOTE_STATEOCDID
    ocdid += state.lower()

    return ocdid 

def generatePlaceOCDID(city, state):
    """ generate OCD-ID string for city/place """
    ocdid = generateStateOCDID(state)
    ocdid += TURBOVOTE_PLACEOCDID
    ocdid += city.lower().replace(' ','_')

    return ocdid

def generateTurboVoteURL(street, street2, city, state, zipcode):
    """ create full URL including querystring with all the OCIDs to use with TurboVote REST API """
    url = TURBOVOTE_BASEURL
    url += TURBOVOTE_UPCOMINGEP
    url += TURBOVOTE_BASEQS
    url += ','.join([generateStateOCDID(state), generatePlaceOCDID(city, state)])

    return url

def validateAddress(street, street2, city, state, zipcode):
    """ validate that an address has required fields and do any other checks we can to ensure the address is valid"""
    # for now, assuming street, city, state and zip are required and state should be in the state list
    isValidAddress = ((len(street) > 0) and (len(city) > 0) and (len(state) == 2) and (len(zipcode) == 5))
    isValidAddress = isValidAddress and (state.upper() in postal_abbreviations)
 
    # note: in future, can do further validations against address info and can refine the checks here

    return isValidAddress

def getUpcomingElections(street, street2, city, state, zipcode):
    """ Calls the TurboVote upcoming elections API and returns the JSON based results """
    if validateAddress(street, street2, city, state, zipcode):
        try:
            response = requests.get(generateTurboVoteURL(street, street2, city, state, zipcode), params=None, headers=TURBOVOTE_HEADERS)
            upcomingElections = json.loads(response.text)
        except:
            # note: in future, we would want to do some more logging for us and indicative info for user if call to TurboVote failed 
            upcomingElections = []
    else:
        # note: in future, we would want provide some additional info on why the address was not valid
        upcomingElections = []
    
    # use the following to see the pretty-printed JSON for easier visual analysis
    # print(json.dumps(upcomingElections, indent=2, sort_keys=True))

    return upcomingElections





