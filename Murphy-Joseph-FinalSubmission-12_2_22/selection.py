#!/usr/bin/python
import cgi
import cgitb
import http.client
import logging
import random
logging.basicConfig(filename='Logs.log', level=logging.WARN)
logging.warn("selection.py")
cgitb.enable()


form = cgi.FieldStorage()
layovers = form.getfirst("Number of Indirect Stops", "")
#logging.warn(layovers)

if layovers == "1" :
    #logging.warn("here")
    cgitb.enable()
    print("Content-type: text/html")
    print("")
    print ("""
<html>
 <head>
  <link rel="stylesheet" type="text/css" href="styles.css" />
  <title>
   Joseph Murphy Welcome Page
  </title>
 </head>
 <body>
<h1>
 Welcome to my site, Here you can compare whether it is better for you to book a direct flight or indirect flight due to total cost and time.
</h1>
<form method="post" enctype="multipart/form-data" action="oneLayover.py">
    <fieldset>
                    <legend>Please enter your direct  and indirect flight info below and how much an hour of your time is worth</legend>
                    <ul>
                                    <li><label>Direct Flight Number</label> <input name="DirectFlightNumber"
                                                    type="text" id="DirectFlightNumber"  required/></li>
                                    <br>
                                    <li><label>Direct Time</label> <input name="DirectTime"
                                                    type="number" id="DirectTime"  required/></li>
                                    <br>
                                    <li><label>Direct Cost</label> <input name="DirectCost"
                                                    type="number" id="DirectCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <br>
                    <ul>
                                    <li><label>Layover Flight Number 1</label> <input name="LayoverFlightNumber1"
                                                    type="text" id="LayoverFlightNumber1"  required/></li>
                                    <br>
                                    <li><label>Layover Time 1</label> <input name="LayoverTime1"
                                                    type="number" id="LayoverTime1"  required/></li>
                                    <br>
                                    <li><label>Layover Flight Number 2</label> <input name="LayoverFlightNumber2"
                                                    type="text" id="LayoverFlightNumber2"  required/></li>
                                    <br>
                                    <li><label>Layover Time 2</label> <input name="LayoverTime2"
                                                    type="number" id="LayoverTime2"  required/></li>
                                    <br>
                                    <li><label>Layover Cost</label> <input name="LayoverCost"
                                                    type="number" id="LayoverCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <br>
                    <ul>
                                <li><label>Hour Cost</label> <input name="HourCost"
                                                type="number" id="HourCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <input type = "submit" id="upload" value = "Continue"/>
    </fieldset>
</form>
</body>
</html>""")

if layovers == "2" :
    logging.warn("here")
    cgitb.enable()
    print("Content-type: text/html")
    print("")
    print ("""
<html>
 <head>
  <link rel="stylesheet" type="text/css" href="styles.css" />
  <title>
   Joseph Murphy Welcome Page
  </title>
 </head>
 <body>
<h1>
 Welcome to my site, Here you can compare whether it is better for you to book a direct flight or indirect flight due to total cost and time.
</h1>
<form method="post" enctype="multipart/form-data" action="twoLayover.py">
    <fieldset>
                    <legend>Please enter your direct  and indirect flight info below and how much an hour of your time is worth</legend>
                    <ul>
                                    <li><label>Direct Flight Number</label> <input name="DirectFlightNumber"
                                                    type="text" id="DirectFlightNumber"  required/></li>
                                    <br>
                                    <li><label>Direct Time</label> <input name="DirectTime"
                                                    type="number" id="DirectTime"  required/></li>
                                    <br>
                                    <li><label>Direct Cost</label> <input name="DirectCost"
                                                    type="number" id="DirectCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <br>
                    <ul>
                                    <li><label>Layover Flight Number 1</label> <input name="LayoverFlightNumber1"
                                                    type="text" id="LayoverFlightNumber1"  required/></li>
                                    <br>
                                    <li><label>Layover Time 1</label> <input name="LayoverTime1"
                                                    type="number" id="LayoverTime1"  required/></li>
                                    <br>
                                    <li><label>Layover Flight Number 2</label> <input name="LayoverFlightNumber2"
                                                    type="text" id="LayoverFlightNumber2"  required/></li>
                                    <br>
                                    <li><label>Layover Time 2</label> <input name="LayoverTime2"
                                                    type="number" id="LayoverTime2"  required/></li>
                                    <br>
                                    <li><label>Layover Flight Number 3</label> <input name="LayoverFlightNumber3"
                                                    type="text" id="LayoverFlightNumber3"  required/></li>
                                    <br>
                                    <li><label>Layover Time 3</label> <input name="LayoverTime3"
                                                    type="number" id="LayoverTime3"  required/></li>
                                    <br>
                                    <li><label>Layover Cost</label> <input name="LayoverCost"
                                                    type="number" id="LayoverCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <br>
                    <ul>
                                <li><label>Hour Cost</label> <input name="HourCost"
                                                type="number" id="HourCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <input type = "submit" id="upload" value = "Continue"/>
    </fieldset>
</form>
</body>
</html>""")

if layovers == "3" :
    logging.warn("here")
    cgitb.enable()
    print("Content-type: text/html")
    print("")
    print ("""
<html>
 <head>
  <link rel="stylesheet" type="text/css" href="styles.css" />
  <title>
   Joseph Murphy Welcome Page
  </title>
 </head>
 <body>
<h1>
 Welcome to my site, Here you can compare whether it is better for you to book a direct flight or indirect flight due to total cost and time.
</h1>
<form method="post" enctype="multipart/form-data" action="threeLayover.py">
    <fieldset>
                    <legend>Please enter your direct  and indirect flight info below and how much an hour of your time is worth</legend>
                    <ul>
                                    <li><label>Direct Flight Number</label> <input name="DirectFlightNumber"
                                                    type="text" id="DirectFlightNumber"  required/></li>
                                    <br>
                                    <li><label>Direct Time</label> <input name="DirectTime"
                                                    type="number" id="DirectTime"  required/></li>
                                    <br>
                                    <li><label>Direct Cost</label> <input name="DirectCost"
                                                    type="number" id="DirectCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <br>
                    <ul>
                                    <li><label>Layover Flight Number 1</label> <input name="LayoverFlightNumber1"
                                                    type="text" id="LayoverFlightNumber1"  required/></li>
                                    <br>
                                    <li><label>Layover Time 1</label> <input name="LayoverTime1"
                                                    type="number" id="LayoverTime1"  required/></li>
                                    <br>
                                    <li><label>Layover Flight Number 2</label> <input name="LayoverFlightNumber2"
                                                    type="text" id="LayoverFlightNumber2"  required/></li>
                                    <br>
                                    <li><label>Layover Time 2</label> <input name="LayoverTime2"
                                                    type="number" id="LayoverTime2"  required/></li>
                                    <br>
                                    <li><label>Layover Flight Number 3</label> <input name="LayoverFlightNumber3"
                                                    type="text" id="LayoverFlightNumber3"  required/></li>
                                    <br>
                                    <li><label>Layover Time 3</label> <input name="LayoverTime3"
                                                    type="number" id="LayoverTime3"  required/></li>
                                    <br>
                                    <li><label>Layover Flight Number 4</label> <input name="LayoverFlightNumber4"
                                                    type="text" id="LayoverFlightNumber4"  required/></li>
                                    <br>
                                    <li><label>Layover Time 4</label> <input name="LayoverTime4"
                                                    type="number" id="LayoverTime4"  required/></li>
                                    <br>
                                    <li><label>Layover Cost</label> <input name="LayoverCost"
                                                    type="number" id="LayoverCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <br>
                    <ul>
                                <li><label>Hour Cost</label> <input name="HourCost"
                                                type="number" id="HourCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <input type = "submit" id="upload" value = "Continue"/>
    </fieldset>
</form>
</body>
</html>""")