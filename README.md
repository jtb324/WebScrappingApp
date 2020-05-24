# WebScrapping Script

## Goal:

The goal of this script is to be able to enter an item from Amazon in (in the form of a url) and get information about it. This script uses the python module BeautifulSoup4 to accomplish this

## Long Term Goals:

- incorporate this into a GUI of some kind. I read about incorporating Python 3 into Electron using zerorpc

## Current Functionality:

- getTitle: gives the title of the object that the user is looking for

- getPrice: gives the price of the item that the user is looking for. This uses the side buyerbox of the Amazon page for the price. More information can be found in the description of the function

- getDescription: **(work in progress)** This is meant to provide a description of the object such as weight, height, width, etc.. Ideally, this might return a table with all the information.

## Current Progress on the Long Term Goal:

~~Set up the electron framework.
~~Created the mainwindow in the main.js
~~began creating the mainWindow.html
