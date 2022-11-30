#!/usr/bin/python3
import cgi
import cgitb
import logging
logging.basicConfig(filename='Logs.log', level=logging.WARN)
cgitb.enable()

 
  

form = cgi.FieldStorage()

layovers = str(form.getfirst("Layovers", ""))

hourCost = str(form.getfirst("HourCost", ""))

cgitb.enable()


if layovers == "1":

	#goto oneLayover.py and bring with you hourCost variable
    
elif layovers == "2":

	#goto twoLayover.py and bring with you hourCost variable
    
elif layovers == "3":

   	#goto threeLayover.py and bring with you hourCost variable

else:

    #go back to intro page and restart something went wrong.
 

 