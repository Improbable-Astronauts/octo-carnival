# Octo-Carnival - A Django and TDD Practice Project

## Goals for the current sprint:

- 1 model - a movies table that stores a movie title, poster_url, year, imdbid, length, and movie_rating

- 3 views - a main page, search result page, and movie detail page

    - main page should display:
        - title and header that indicate this is an app to make a movie list
        - an input box with placeholder to prompt users to add a movie title
        - a list that displays either all the movies currently entered for a
        a message that alerts that user that no movies have been added yet.
        - the movies list should be persistent since its contents come from the database.
        - a button that POSTS a search query to OMDB, returning a list of searchterm results, then redirects the user to the search view.
            - future optimization: if only one result is found, the search view can be skipped - send a GET request for that result, and redirect the user to the movie detail page.

    - search result page should display:
        - a title and header that indicate this is the search result page
            - heading should also contain the user's search term
        - a list of information related to each result returned from OMDB
            - for each movie, display the following:
                - image of the movie poster
                - movie title
                - year movie was released
                - a link to the movie detail page for that film
        - clicking a link on this page will send a GET request to OMDB for that specific film, then redirect to the appropriate movie detail page
            - future optimization: check db for movie first - then send request to omdb

    - movie detail page should display:
        - url for movie details should follow this format `detail/<imdb_id>`
        - all details needed to create a new movie object should be displayed on this page: movie poster url, title, year, imdb_id, length, and movie_rating
        - a button that creates a new Movie object with the relevant fields, then redirects the user to the main page, where they will see the newest addition in the list of movies.

- functional and unit tests for all new additions to the app

## Technology used:

- Python 3.6
- Django 2.0
- Selenium 3
- Javascript
- HTML/CSS
- Postgres

## Setting up your development environment for local testing

- Make sure you have installed python 3.6

    `$ python --version`
- clone the repository

    `$ git clone https://github.com/Improbable-Astronauts/octo-carnival.git`
- change to the directory with manage.py in it

    `$ cd path/to/octo-carnival/`
- create a virtual environment for this project - we recommend using venv

    `$ python -m venv myvenv`

    (this should create a directory called myvenv inside the project directory)
- activate your virtual environment

    `$ source myvenv/bin/activate`

    (you should see (myvenv) at the beginning of your command line prompt now)

    - Windows users: your path will most likely be `source myvenv/Scripts/activate`
- add the name of your virtual environment to the .gitignore file

    `$ echo "myvenv/" >> .gitignore`
- add all project dependencies by running

    `$ pip install -r requirements.txt`
- create database tables by running:

    `$ python manage.py migrate`
- start the server by running:

    `$ export OMDB_API_KEY=1A2B3C4D`
- set an environment variable for your OMDB_API_KEY. Find out how to get one at http://www.omdbapi.com

    `$ python manage.py runserver`
- open browser to http://localhost:8000/
- see results for all tests by running

    `$ python manage.py test`
- see results for unit tests only by running

    `$ python manage.py test movies`


## To contribute to the project

- Follow the setup instructions above
- Assign yourself to an open issue
- Make sure your local repo is up-to-date

    `$ git pull origin master`
- From master, create a new feature branch

    `$ git checkout -b fix-issue-9`
- Make changes in feature branch
- Open a pull request from feature branch into master for team review
    - reference the issue you are working on in the text of the PR
    - make sure to update requirements.txt and let the team know if additional dependencies are added

        `$ pip freeze > requirements.txt`
    - if your changes affect how the app runs or project setup instructions, please update README.md with the necessary information.

- After getting at least one approval, merge your branch
- If this pull request resolves your assigned issue, please also mark the issue closed.

