from elections.querytv import getUpcomingElections
from elections.querytv import generateStateOCDID
from elections.querytv import generatePlaceOCDID
from elections.querytv import generateTurboVoteURL
from elections.querytv import validateAddress

def test_state_OCDID():
    # confirm properly generated state OCID
    assert generateStateOCDID('NY') == 'ocd-division/country:us/state:ny'
    assert generateStateOCDID('Ny') == 'ocd-division/country:us/state:ny'
    assert generateStateOCDID('nY') == 'ocd-division/country:us/state:ny'
    assert generateStateOCDID('ny') == 'ocd-division/country:us/state:ny'

def test_place_OCDID():
    # confirm properly generated place OCID 
    assert generatePlaceOCDID('Wales','MA') == 'ocd-division/country:us/state:ma/place:wales'
    assert generatePlaceOCDID('waLEs','MA') == 'ocd-division/country:us/state:ma/place:wales'
    assert generatePlaceOCDID('wales','MA') == 'ocd-division/country:us/state:ma/place:wales'   

    # confirm properly generated place OCID with a city that has a space in its name
    assert generatePlaceOCDID('White Plains','NY') == 'ocd-division/country:us/state:ny/place:white_plains'
    assert generatePlaceOCDID('white Plains','NY') == 'ocd-division/country:us/state:ny/place:white_plains'
    assert generatePlaceOCDID('White plains','NY') == 'ocd-division/country:us/state:ny/place:white_plains'

def test_generate_URL():
    # confirm properly generated TurboVote URL 
    assert generateTurboVoteURL('3 Hollow Road','','Wales','MA','01081') == 'https://api.turbovote.org/elections/upcoming?district-divisions=ocd-division/country:us/state:ma,ocd-division/country:us/state:ma/place:wales'

def test_validate_Address():
    # test incorrect state (too long, not in the state list)
    assert validateAddress('20 Jay Street', '', 'Brooklyn', 'MY', '11201') == False
    assert validateAddress('20 Jay Street', '', 'Brooklyn', 'NYY', '11201') == False

    # test missing, non-optional fields
    assert validateAddress('', '', 'Brooklyn', 'NY', '11201') == False
    assert validateAddress('20 Jay Street', '', '', 'NY', '11201') == False
    assert validateAddress('20 Jay Street', '', 'Brooklyn', '', '11201') == False
    assert validateAddress('20 Jay Street', '', 'Brooklyn', 'NY', '') == False

    # test valid address
    assert validateAddress('20 Jay Street', '', 'Brooklyn', 'NY', '11201')
    assert validateAddress('20 Jay Street', '', 'brooklyn', 'ny', '11201')


def test_get_UpcomingElections():
    # test failure situations where address doesn't exist
    assert getUpcomingElections('Street1','Street2','Some Unknown City','MA','12345') == []

    # test a valid address that will return upcoming results
    # note: this test will fail after 6-10-19 so in future, find a test for a success scenario that we can guarantee a consistent result from every time (curently upcoming elections are time based so will change)
    assert getUpcomingElections('17 School Street', '', 'Rockport', 'MA', '01966') != []