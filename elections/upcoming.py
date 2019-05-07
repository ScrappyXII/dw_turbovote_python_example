# Imports
import functools
import json

from elections.us_states import postal_abbreviations
from elections.querytv import getUpcomingElections
from elections.querytv import validateAddress
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('address_form', __name__, url_prefix='/')

# note: we should consider removing the POST from this route so it only supports GET to simplify
# and to match the actual form submission which submits to the /search route
# note: left as-is for now in case there is some backward compatible requirement here
@bp.route('/', methods=('GET','POST'))
def searchform():
    """Collects an address"""
    if request.method == 'POST':
        redirect(url_for('search'))

    return render_template('address_form.html', states=postal_abbreviations)

# route to handle search results for upcoming elections
@bp.route('/search', methods=('POST',))
def searchresults():
    """Takes in an address and shows upcoming elections for that address."""
    # gather data from the submitted form while protecting against incorrect or missing field names
    try:
        street1Name = str(request.form['street'])
    except:
        street1Name = ''

    try:    
        street2Name = str(request.form['street-2'])
    except: 
        street2Name = ''

    try:
        cityName = str(request.form['city'])
    except:
        cityName = ''

    try:
        stateShortName = str(request.form['state'])
    except:
        stateShortName = ''

    try:    
        zipCode = str(request.form['zip'])
    except:
        zipCode = ''

    # check if we have a valid address from the form 
    if validateAddress(street1Name, street2Name, cityName, stateShortName, zipCode):   
        # get the upcoming elections from TurboVote and provide to the user
        response = getUpcomingElections(street1Name, street2Name, cityName, stateShortName, zipCode) 
        return render_template('election_results.html', street=street1Name, street2=street2Name, city=cityName, state=stateShortName, zipcode=zipCode, elections=response)
    else:
        # go back to the search form since we didn't get complete information
        return render_template('address_form.html', states=postal_abbreviations)      
 
