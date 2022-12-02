#!/usr/bin/python
import cgi
import cgitb
import http.client
import logging
import random
logging.basicConfig(filename='Logs.log', level=logging.WARN)
logging.warn("oneLayover.py")
cgitb.enable()

 
  
cgitb.enable()
form = cgi.FieldStorage()
#hourCost = 50
hourCost = int(form.getfirst("HourCost", ""))
logging.warn(type(hourCost))
directFlightNumber = str(form.getfirst("DirectFlightNumber", ""))
logging.warn(type(directFlightNumber))
#directFlightNumber = "AA9419"
directTime = int(form.getfirst("DirectTime", ""))
logging.warn(type(directTime))
#directTime = 16
directCost = int(form.getfirst("DirectCost", ""))
logging.warn(type(directCost))
#directCost = 100
layoverFlightNumber1 = str(form.getfirst("LayoverFlightNumber1", ""))
logging.warn(type(layoverFlightNumber1))
#layoverFlightNumber1 = "AA2823"
layoverFlightNumber2 = str(form.getfirst("LayoverFlightNumber2", ""))
logging.warn(type(layoverFlightNumber2))
#layoverFlightNumber2 = "AA3420"
layoverTime1 = int(form.getfirst("LayoverTime1", ""))
logging.warn(type(layoverTime1))
#layoverTime1 = 8
layoverTime2 = int(form.getfirst("LayoverTime2", ""))
logging.warn(type(layoverTime2))
#layoverTime2 = 14
layoverCost = int(form.getfirst("LayoverCost", ""))
logging.warn(type(layoverCost))
#layoverCost = 50

def directTimeCost(directFlightNumber, directTime, directCost, hourCost):

	conn = http.client.HTTPSConnection("aerodatabox.p.rapidapi.com")
	headers = {
    	'X-RapidAPI-Key': "c21cc07c73msh0200b16e9e4a1a7p19a8e0jsnb76c9cc8eaa0",
    	'X-RapidAPI-Host': "aerodatabox.p.rapidapi.com"
    	}
	conn.request("GET", "/flights/" + directFlightNumber + "/delays", headers=headers)
	res = conn.getresponse()
	data = res.read()
	delayTime = data.decode("utf-8")
	delayTime = random.uniform(0,2)
	delayCost = delayTime * hourCost
	totalTime= directTime + delayTime
	totalDirectTimeCost = delayCost + directCost
	
	return totalDirectTimeCost

def layoverTimeCost(layoverFlightNumber1, layoverFlightNumber2, layoverTime1, layoverTime2, layoverCost, hourCost):
	conn = http.client.HTTPSConnection("aerodatabox.p.rapidapi.com")
	headers = {
    	'X-RapidAPI-Key': "c21cc07c73msh0200b16e9e4a1a7p19a8e0jsnb76c9cc8eaa0",
    	'X-RapidAPI-Host': "aerodatabox.p.rapidapi.com"
    	}
	conn.request("GET", "/flights/" + layoverFlightNumber1 + "/delays", headers=headers)
	res = conn.getresponse()
	data = res.read()
	delayTime1 = data.decode("utf-8")
	delayTime1 = random.uniform(0,4)
	layoverTime1 = layoverTime1 + delayTime1
	if layoverTime1 > layoverTime2 :
		totalLayoverTimeCost = 10000000000000
		return totalLayoverTimeCost
	conn = http.client.HTTPSConnection("aerodatabox.p.rapidapi.com")
	headers = {
    	'X-RapidAPI-Key': "c21cc07c73msh0200b16e9e4a1a7p19a8e0jsnb76c9cc8eaa0",
    	'X-RapidAPI-Host': "aerodatabox.p.rapidapi.com"
    	}
	conn.request("GET", "/flights/" + layoverFlightNumber2 + "/delays", headers=headers)
	res = conn.getresponse()
	data = res.read()
	delayTime2 = data.decode("utf-8")
	delayTime2 = random.uniform(0,4)
	delayCost = delayTime2 * hourCost
	totalTime= layoverTime2 + delayTime2
	totalLayoverTimeCost = delayCost + layoverCost

	return totalLayoverTimeCost



cgitb.enable()

totalDirectTimeCost = directTimeCost(directFlightNumber, directTime, directCost, hourCost)
totalLayoverTimeCost = layoverTimeCost(layoverFlightNumber1, layoverFlightNumber2, layoverTime1, layoverTime2, layoverCost, hourCost)

if totalDirectTimeCost <= totalLayoverTimeCost:

	cgitb.enable()
	print("""
<html>
 <head>
  <link rel="stylesheet" type="text/css" href="styles.css" />
  <title>
   Joseph Murphy Welcome Page
  </title>
 </head>
 <body>

<h2>
<font size="+5">You should go direct!</font>
</h2>
<br>
<br>
<br>
<a href="index.html">Try Another!</a>
</body>
</html>""")
	#goto final.py and bring with you directFlightNumber and totalDirectTimeCost variable    
if totalDirectTimeCost > totalLayoverTimeCost:
	cgitb.enable()
	print("""
<html>
 <head>
  <link rel="stylesheet" type="text/css" href="styles.css" />
  <title>
   Joseph Murphy Welcome Page
  </title>
 </head>
 <body>
<h2>
<font size="+5">You should go layover!</font>
</h2>
<br>
<br>
<br>
<a href="index.html">Try Another!</a>
</body>
</html>""")
	#goto final.py and bring with you layoverFlightNumber1 and totalLayoverTimeCost variable

 
