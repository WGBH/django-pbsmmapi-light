========
PBSMMAPI-LIGHT
========

This is a Django app to allow Django-based projects to work with the PBS MediaManager API.
It is not expected to be a COMPLETE interface to the entirety of the PBS MediaManager; however
it should allow access to all of the primary content object types.

The "light" version of the app doesn't copy over the content for each record; only enough to identify it in the local database 
and allow administrative control of which objects are shown on the Django site;  it relies on the API to generate content for each object.

Documentation is in the "docs" directory.

Quick start
-----------

1. Add "pbsmmapi" to your INSTALLED_APPS setting:

        INSTALLED_APPS = [
                ...
                'pbsmmapi-light',
        ]

2. Run  `python manage.py migrate` to create the PBSMM API models.


