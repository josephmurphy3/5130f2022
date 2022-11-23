#!/usr/bin/python3
import cgi
import cgitb
import http.cookies
import configparser
import os
import hashlib
import uuid
import logging
import re
import http.client
logging.basicConfig(filename='Logs.log', level=logging.WARN)
cgitb.enable()


def callAPI(flightNumber):

	conn = http.client.HTTPSConnection("aerodatabox.p.rapidapi.com")

	headers = {
    		'X-RapidAPI-Key': "c21cc07c73msh0200b16e9e4a1a7p19a8e0jsnb76c9cc8eaa0",
    		'X-RapidAPI-Host': "aerodatabox.p.rapidapi.com"
    	}
	request = '/flights/' + flightNumber + '/delays'

	conn.request("GET", request, headers=headers)

	res = conn.getresponse()
	data = res.read()
 



 

form = cgi.FieldStorage()

flightNumber = str(form.getfirst("FlightNumber", "))

cost = str(form.getfirst("Cost", ""))

callAPI(flightNumber)