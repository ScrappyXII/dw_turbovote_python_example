# Upcoming Elections Example
Full instructions for installing Flask can be found [here](http://flask.pocoo.org/docs/1.0/installation/).

Install all required dependencies via:

```
pip install -r requirements.txt
```

This will ensure the install the dependencies such as Flask, requests and pytest, as necessary

## Running

```
export FLASK_APP=elections
export FLASK_ENV=development
flask run
```

## Testing

```
pytest
```

## Information about this example

The example is runnable and testable by following the instructions above. Any new requirements/dependencies are captured in the requirements.txt file and thus will be installed by following the instructions above to use pip to install these requirements. 

The following requirements have been met:
* The form submits  (the assumption for this submission is that the street, city, state and zip are required but that street2 is optional. For now, if you attempt to submit without the required fields, it will simply display the form again.)
* State and place OCD-IDs are correctly generated (as per the TurboVote definitions)
* The Democracy Works Elections API is called correctly (using the API URI and querystring format defined by TurboVote)
* Returned elections are displayed to the user (the example obtains the upcoming elections in JSON format and displays the data to the user in a formatted web page)
* The results are formatted for the user (the examole displays the data from the JSON results in a simple but organized fashion, iterating through the various data points in the results)
* The code that generates OCD-IDs can be easily changed (the OCD-ID generation code is organized such that it would be easy to adjust the format/contents)
* The project has documentation (the install, run and test instructions above are the same as in the original readme)
* There are tests for all functionality (functions/functionality have tests added to exercise and validate them)
* Functions/classes/methods are small and clearly scoped
* Names are clear

This example contains some added  measure of error checking and failure case handling, though not production comprehensive, that showcase the foundation for that.
This example also has a few notes in the code to indicate some thoughts for future improvements or potential issues that could be addressed.


