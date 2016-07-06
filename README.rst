Flask-EPICS Demo
================

This app was created as part of a seminar on Flask at the Australian Synchrotron.

It demonstrates how to control an EPICS areaDetector IOC through a simple Flask
web interface.


To run the application in Docker
--------------------------------

1. Install `Docker <https://docs.docker.com/>`_.
2. Download this repository.
3. From inside the project folder run::

   docker-compose up -d

The first time you run this it may take a few minutes to download the docker
images it needs. Once this is done you will be able to access the site at
http://localhost:5000/.
