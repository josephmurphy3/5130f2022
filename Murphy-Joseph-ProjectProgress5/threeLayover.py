#!/usr/bin/python3
import cgi
import cgitb
import http.client
import logging
logging.basicConfig(filename='Logs.log', level=logging.WARN)
cgitb.enable()

 
  

form = cgi.FieldStorage()

directFlightNumber = str(form.getfirst("DirectFlightNumber", ""))

directTime = form.getfirst("DirectTime", "")

directCost = form.getfirst("DirectCost", "")

layoverFlightNumber1 = str(form.getfirst("LayoverFlightNumber1", ""))

layoverFlightNumber2 = str(form.getfirst("LayoverFlightNumber2", ""))

layoverFlightNumber3 = str(form.getfirst("LayoverFlightNumber3", ""))

layoverFlightNumber4 = str(form.getfirst("LayoverFlightNumber4", ""))

layoverTime1 = form.getfirst("LayoverTime1", "")

layoverTime2 = form.getfirst("LayoverTime2", "")

layoverTime3 = form.getfirst("LayoverTime3", "")

layoverTime4 = form.getfirst("LayoverTime4", "")

layoverCost = form.getfirst("LayoverCost", "")


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
	delayCost = delaytime/60 * hourCost
	totalTime= directTime + delayTime
	totalDirectTimeCost = delayCost + directCost


    return totalDirectTimeCost

def layoverTimeCost(layoverFlightNumber1, layoverFlightNumber2,layoverFlightNumber3,layoverFlightNumber4 , layoverTime1, layoverTime2,layoverTime3,layoverTime4 ,layoverCost, hourCost):

	conn = http.client.HTTPSConnection("aerodatabox.p.rapidapi.com")
	headers = {
    	'X-RapidAPI-Key': "c21cc07c73msh0200b16e9e4a1a7p19a8e0jsnb76c9cc8eaa0",
    	'X-RapidAPI-Host': "aerodatabox.p.rapidapi.com"
    	}
	conn.request("GET", "/flights/" + layoverFlightNumber1 + "/delays", headers=headers)
	res = conn.getresponse()
	data = res.read()
	delayTime1 = data.decode("utf-8")
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
	layoverTime3 = layoverTime3 + delayTime3
	if layoverTime3 > layoverTime4 :
		totalLayoverTimeCost = 10000000000000
		return totalLayoverTimeCost
	conn = http.client.HTTPSConnection("aerodatabox.p.rapidapi.com")
	headers = {
    	'X-RapidAPI-Key': "c21cc07c73msh0200b16e9e4a1a7p19a8e0jsnb76c9cc8eaa0",
    	'X-RapidAPI-Host': "aerodatabox.p.rapidapi.com"
    	}
	conn.request("GET", "/flights/" + layoverFlightNumber4 + "/delays", headers=headers)
	res = conn.getresponse()
	data = res.read()
	delayTime4 = data.decode("utf-8")
	delayCost = delaytime4/60 * hourCost
	totalTime= layoverTime4 + delayTime
	totalLayoverTimeCost = delayCost + directCost


    
    return totalLayoverTimeCost



cgitb.enable()

totalDirectTimeCost = directTimeCost(directFlightNumber, directTime, directCost, hourCost)
totalLayoverTimeCost = layoverTimeCost(layoverFlightNumber1, layoverFlightNumber2,layoverFlightNumber3,layoverFlightNumber4 , layoverTime1, layoverTime2,layoverTime3,layoverTime4 ,layoverCost, hourCost)

if totalDirectTimeCost <= totalDirectTimeCost:

	#goto final.py and bring with you directFlightNumber and totalDirectTimeCost variable    

elif totalDirectTimeCost > totalDirectTimeCost:

	#goto final.py and bring with you layoverFlightNumber1 and totalLayoverTimeCost variable

else:

    #go back to intro page and restart something went wrong.
 
