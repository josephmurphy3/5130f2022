#!/usr/bin/python

#This code was 100% written by me, Joseph Murphy. The only thing that is not mine is the API calls, and header/navbar but those are the default ones used for the API. I did use https://www.w3schools.com/css/css_navbar_horizontal.asp as a base and went from there. Everything else is 100% my own code.

import cgi
import cgitb
import http.client
import logging
import random
import math
logging.basicConfig(filename='Logs.log', level=logging.WARN)
logging.warn("twoLayover.py")
cgitb.enable()

 
  
cgitb.enable()
form = cgi.FieldStorage()
#hourCost = 50
hourCost = int(form.getfirst("HourCost", ""))
logging.warn(type(hourCost))
directFlightNumber = str(form.getfirst("DirectFlightNumber", ""))
logging.warn(type(directFlightNumber))
#directFlightNumber = "AA9419"
directTimeHour = int(form.getfirst("DirectTimeHour", ""))
logging.warn(directTimeHour)
directTimeMinute = int(form.getfirst("DirectTimeMinute", ""))
logging.warn(directTimeMinute)
#layoverTime2 = 14
directTimeMinute = directTimeMinute / 60
directTime = directTimeHour + directTimeMinute
directCost = int(form.getfirst("DirectCost", ""))
logging.warn(type(directCost))
#directCost = 100
layoverFlightNumber1 = str(form.getfirst("LayoverFlightNumber1", ""))
logging.warn(type(layoverFlightNumber1))
#layoverFlightNumber1 = "AA2823"
layoverFlightNumber2 = str(form.getfirst("LayoverFlightNumber2", ""))
logging.warn(type(layoverFlightNumber2))
layoverFlightNumber3 = str(form.getfirst("LayoverFlightNumber3", ""))
logging.warn(type(layoverFlightNumber3))
#layoverFlightNumber2 = "AA3420"
logging.warn(type("here1"))
layoverTimeHour1 = int(form.getfirst("LayoverTimeHour1", ""))
logging.warn(layoverTimeHour1)
layoverTimeMinute1 = int(form.getfirst("LayoverTimeMinute1", ""))
logging.warn(layoverTimeMinute1)
#layoverTime1 = 8
amPM1 = str(form.getfirst("AMPM1", ""))
logging.warn(amPM1)
if amPM1 == "PM":
	layoverTimeHour1 = layoverTimeHour1 + 12
layoverTimeMinute1 = layoverTimeMinute1 / 60
layoverTime1 = layoverTimeHour1 + layoverTimeMinute1
logging.warn("here3")
layoverTimeHour2 = int(form.getfirst("LayoverTimeHour2", ""))
logging.warn(layoverTimeHour2)
layoverTimeMinute2 = int(form.getfirst("LayoverTimeMinute2", ""))
logging.warn(layoverTimeMinute2)
#layoverTime2 = 14
amPM2 = str(form.getfirst("AMPM2", ""))
logging.warn(amPM2)
if amPM2 == "PM":
	layoverTimeHour2 = layoverTimeHour2 + 12
layoverTimeMinute2 = layoverTimeMinute2 / 60
layoverTime2 = layoverTimeHour2 + layoverTimeMinute2
layoverTimeHour3 = int(form.getfirst("LayoverTimeHour3", ""))
logging.warn(layoverTimeHour3)
layoverTimeMinute3 = int(form.getfirst("LayoverTimeMinute3", ""))
logging.warn(layoverTimeMinute3)
#layoverTime2 = 14
amPM3 = str(form.getfirst("AMPM3", ""))
logging.warn(amPM3)
if amPM3 == "PM":
	layoverTimeHour3 = layoverTimeHour3 + 12
layoverTimeMinute3 = layoverTimeMinute3 / 60
layoverTime3 = layoverTimeHour3 + layoverTimeMinute3
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

	minutes = delayTime % 1
	minutes = minutes * 60

	global newDirectDelayTimeHour
	global newDirectDelayTimeMinutes
	global newDirectDelayCost 
	newDirectDelayTimeHour = math.floor(delayTime)
	newDirectDelayTimeMinutes = math.floor(minutes)
	newDirectDelayCost = delayCost
	
	return totalDirectTimeCost

def layoverTimeCost(layoverFlightNumber1, layoverFlightNumber2, layoverFlightNumber3, layoverTime1, layoverTime2, layoverTime3, layoverCost, hourCost):
	global newLayoverDelayTimeHour
	global newLayoverDelayTimeMinutes
	global newLayoverDelayCost 
	newLayoverDelayTimeHour = 0
	newLayoverDelayTimeMinutes = 0
	newLayoverDelayCost = 0
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
	layoverTime2 = layoverTime2 + delayTime2
	if layoverTime2 > layoverTime3 :
		totalLayoverTimeCost = 10000000000000
		return totalLayoverTimeCost
	conn = http.client.HTTPSConnection("aerodatabox.p.rapidapi.com")
	headers = {
    	'X-RapidAPI-Key': "c21cc07c73msh0200b16e9e4a1a7p19a8e0jsnb76c9cc8eaa0",
    	'X-RapidAPI-Host': "aerodatabox.p.rapidapi.com"
    	}
	conn.request("GET", "/flights/" + layoverFlightNumber3 + "/delays", headers=headers)
	res = conn.getresponse()
	data = res.read()
	delayTime3 = data.decode("utf-8")
	delayTime3 = random.uniform(0,4)
	delayCost = delayTime3 * hourCost
	totalTime= layoverTime3 + delayTime3
	totalLayoverTimeCost = delayCost + layoverCost

	minutes = delayTime3 % 1
	minutes = minutes * 60
 
	newLayoverDelayTimeHour = math.floor(delayTime3)
	newLayoverDelayTimeMinutes = math.floor(minutes)
	newLayoverDelayCost = delayCost

	return totalLayoverTimeCost



cgitb.enable()

totalDirectTimeCost = directTimeCost(directFlightNumber, directTime, directCost, hourCost)
totalLayoverTimeCost = layoverTimeCost(layoverFlightNumber1, layoverFlightNumber2,layoverFlightNumber3, layoverTime1, layoverTime2, layoverTime3, layoverCost, hourCost)

if totalLayoverTimeCost == 10000000000000:
	cgitb.enable()
	print("Content-type: text/html")
	print("""
<html>
<head>
<style>
ul.nav{
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}
li {
  float: left;
}
li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}
li a:hover:not(.active) {
  background-color: #111;
}
.active {
  background-color: #04AA6D;
}
</style>
</head>
<body>
<ul class = "nav">
  <li><a href="index.html"><img src="website.jpg" alt ="website" width ="100" height="100"></a></li>
  <li style="float:right"><a href="index.html"><img src="home.png" alt ="home" width ="100" height="100"></a></li>
</ul>
<br>
<br>
<br>
<h1>
<font size="+5"><center>You should go Direct!</center></font>
</h1>
<br>
<br>
<br>
<h2>
<center> You should go direct because the layover flight will be missed on average due to delay! </center>
</h2>
<center>This to me is priceless, and results in a automatic direct flight chosing</center>
<br>
<center>The Direct Flight will be delayed by an average of %i hours and %i minutes </center>
<br>
<center>This will cost you %.2f dollars in wasted time raising the total of the direct flight to %.2f dollars however this is still better than missing a connecting flight</center>
<br>
<br>
<br>
<center><a href="index.html">Try Another!</a></center>
</body>
</html>"""%(newDirectDelayTimeHour,newDirectDelayTimeMinutes,newDirectDelayCost,totalDirectTimeCost)
)

if (totalDirectTimeCost <= totalLayoverTimeCost) and totalLayoverTimeCost != 10000000000000:

	cgitb.enable()
	print("Content-type: text/html")
	print("""
<html>
<head>
<style>
ul.nav{
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}
li {
  float: left;
}
li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}
li a:hover:not(.active) {
  background-color: #111;
}
.active {
  background-color: #04AA6D;
}
</style>
</head>
<body>
<ul class = "nav">
  <li><a href="index.html"><img src="website.jpg" alt ="website" width ="100" height="100"></a></li>
  <li style="float:right"><a href="index.html"><img src="home.png" alt ="home" width ="100" height="100"></a></li>
</ul>
<br>
<br>
<br>
<h1>
<font size="+5"><center>You should go Direct!</center></font>
</h1>
<br>
<br>
<br>
<h2>
<center> You should go direct because  the total cost of the Direct Flight is $%.2f compared to the Layover Flights cost $%.2f </center>
</h2>
<center>The Direct Flight will be delayed by an average of %i hours and %i minutes compared to %i hours and %i minutes for the final layover flight</center>
<br>
<center>This will cost you %.2f dollars in wasted time raising the total of the direct flight to %.2f dollars</center>
<br>
<br>
<br>
<center><a href="index.html">Try Another!</a></center>
</body>
</html>"""%(totalDirectTimeCost,totalLayoverTimeCost , newDirectDelayTimeHour,newDirectDelayTimeMinutes,newLayoverDelayTimeHour,newLayoverDelayTimeMinutes,newDirectDelayCost,totalDirectTimeCost)
)
	#goto final.py and bring with you directFlightNumber and totalDirectTimeCost variable    
if totalDirectTimeCost > totalLayoverTimeCost:
	cgitb.enable()
	print("Content-type: text/html")
	print("""
<html>
<head>
<style>
ul.nav{
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
}
li {
  float: left;
}
li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}
li a:hover:not(.active) {
  background-color: #111;
}
.active {
  background-color: #04AA6D;
}
</style>
</head>
<body>
<ul class = "nav">
  <li><a href="index.html"><img src="website.jpg" alt ="website" width ="100" height="100"></a></li>
  <li style="float:right"><a href="index.html"><img src="home.png" alt ="home" width ="100" height="100"></a></li>
</ul>
<br>
<br>
<br>
<h1>
<font size="+5"><center>You should go Layover!</center></font>
</h1>
<br>
<br>
<br>
<h2>
<center> You should go layover because  the total cost of the Layover Flights is $%.2f compared to the Direct Flight cost of $%.2f </center>
</h2>
<center>The Layover Flight will be delayed by an average of %i hours and %i minutes compared to %i hours and %i minutes for the direct flight</center>
<br>
<center>This will cost you %.2f dollars in wasted time raising the total of the layover flight to %.2f dollars</center>
<br>
<br>
<br>
<center><a href="index.html">Try Another!</a></center>
</body>
</html>"""%(totalLayoverTimeCost,totalDirectTimeCost, newLayoverDelayTimeHour,newLayoverDelayTimeMinutes,newDirectDelayTimeHour,newDirectDelayTimeMinutes,newLayoverDelayCost,totalLayoverTimeCost)
)