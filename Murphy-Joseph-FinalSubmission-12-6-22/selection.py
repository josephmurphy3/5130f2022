#!/usr/bin/python

#This code was 100% written by me, Joseph Murphy. Everything I added is my code but for the header/navbar I did use https://www.w3schools.com/css/css_navbar_horizontal.asp as a base and went from there.


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
ul.form1{
  display: inline;
  list-style-type: none;
}
ul.form2{
  display: inline;
  list-style-type: none;
}
ul.form3{
  display: inline;
  list-style-type: none;
}
</style>
</head>
<body>
<ul class = "nav">
  <li><a href="index.html"><img src="website.jpg" alt ="website" width ="100" height="100"></a></li>
  <li style="float:right"><a href="index.html"><img src="home.png" alt ="home" width ="100" height="100"></a></li>
</ul>
<form method="post" enctype="multipart/form-data" action="oneLayover.py">
    <fieldset>
                    <legend>Flight Info</legend>
                    <font size="+3">Enter your Direct Flight Info Below </font>
                    <br>
                    <br>
                    <ul class = "form1">
                                    <li><label>Direct Flight Number</label> <input name="DirectFlightNumber"
                                                    type="text" id="DirectFlightNumber"  required/></li>
                                    <li><label> Time </label>
                                            <select name = "DirectTimeHour" required>
                                                    <option disabled selected value> -- Hour --</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                </select></li>
                                    <li><label>:</label>
                                            <select name = "DirectTimeMinute" required>
                                                    <option disabled selected value> -- Minute --</option>
                                                    <option value = "0"> 00</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                    <option value = "13"> 13</option>
                                                    <option value = "14"> 14</option>
                                                    <option value = "15"> 15</option>
                                                    <option value = "16"> 16</option>
                                                    <option value = "17"> 17</option>
                                                    <option value = "18"> 18</option>
                                                    <option value = "19"> 19</option>
                                                    <option value = "20"> 20</option>
                                                    <option value = "21"> 21</option>
                                                    <option value = "22"> 22</option>
                                                    <option value = "23"> 23</option>
                                                    <option value = "24"> 24</option>
                                                    <option value = "25"> 25</option>
                                                    <option value = "26"> 26</option>
                                                    <option value = "27"> 27</option>
                                                    <option value = "28"> 28</option>
                                                    <option value = "29"> 29</option>
                                                    <option value = "30"> 30</option>
                                                    <option value = "31"> 31</option>
                                                    <option value = "32"> 32</option>
                                                    <option value = "33"> 33</option>
                                                    <option value = "34"> 34</option>
                                                    <option value = "35"> 35</option>
                                                    <option value = "36"> 36</option>
                                                    <option value = "37"> 37</option>
                                                    <option value = "38"> 38</option>
                                                    <option value = "39"> 39</option>
                                                    <option value = "40"> 40</option>
                                                    <option value = "41"> 41</option>
                                                    <option value = "42"> 42</option>
                                                    <option value = "43"> 43</option>
                                                    <option value = "44"> 44</option>
                                                    <option value = "45"> 45</option>
                                                    <option value = "46"> 46</option>
                                                    <option value = "47"> 47</option>
                                                    <option value = "48"> 48</option>
                                                    <option value = "49"> 49</option>
                                                    <option value = "50"> 50</option>
                                                    <option value = "51"> 51</option>
                                                    <option value = "52"> 52</option>
                                                    <option value = "53"> 53</option>
                                                    <option value = "54"> 54</option>
                                                    <option value = "55"> 55</option>
                                                    <option value = "56"> 56</option>
                                                    <option value = "57"> 57</option>
                                                    <option value = "58"> 58</option>
                                                    <option value = "59"> 59</option>
                                                    <option value = "60"> 60</option>
                                                </select></li>
                                    <li><label> AM/PM </label>
                                            <select name = "AMPM" required>
                                                    <option disabled selected value> -- AM/PM --</option>
                                                    <option value = "AM"> AM</option>
                                                    <option value = "PM"> PM</option>
                                                </select></li>
                                    <br>
                                    <br>
                                    <br>
                                    <li><label>Direct Cost</label> <input name="DirectCost"
                                                    type="number" id="DirectCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <br>
                    <font size="+3">Enter your Layover Flights Info Below </font>
                    <br>
                    <br>
                    <ul class = "form2">
                                    <li><label>Layover Flight Number 1</label> <input name="LayoverFlightNumber1"
                                                    type="text" id="LayoverFlightNumber1"  required/></li>
                                    <li><label> Layover Time 1 </label>
                                            <select name = "LayoverTimeHour1" required>
                                                    <option disabled selected value> -- Hour --</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                </select></li>
                                    <li><label>:</label>
                                            <select name = "LayoverTimeMinute1" required>
                                                    <option disabled selected value> -- Minute --</option>
                                                    <option value = "0"> 00</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                    <option value = "13"> 13</option>
                                                    <option value = "14"> 14</option>
                                                    <option value = "15"> 15</option>
                                                    <option value = "16"> 16</option>
                                                    <option value = "17"> 17</option>
                                                    <option value = "18"> 18</option>
                                                    <option value = "19"> 19</option>
                                                    <option value = "20"> 20</option>
                                                    <option value = "21"> 21</option>
                                                    <option value = "22"> 22</option>
                                                    <option value = "23"> 23</option>
                                                    <option value = "24"> 24</option>
                                                    <option value = "25"> 25</option>
                                                    <option value = "26"> 26</option>
                                                    <option value = "27"> 27</option>
                                                    <option value = "28"> 28</option>
                                                    <option value = "29"> 29</option>
                                                    <option value = "30"> 30</option>
                                                    <option value = "31"> 31</option>
                                                    <option value = "32"> 32</option>
                                                    <option value = "33"> 33</option>
                                                    <option value = "34"> 34</option>
                                                    <option value = "35"> 35</option>
                                                    <option value = "36"> 36</option>
                                                    <option value = "37"> 37</option>
                                                    <option value = "38"> 38</option>
                                                    <option value = "39"> 39</option>
                                                    <option value = "40"> 40</option>
                                                    <option value = "41"> 41</option>
                                                    <option value = "42"> 42</option>
                                                    <option value = "43"> 43</option>
                                                    <option value = "44"> 44</option>
                                                    <option value = "45"> 45</option>
                                                    <option value = "46"> 46</option>
                                                    <option value = "47"> 47</option>
                                                    <option value = "48"> 48</option>
                                                    <option value = "49"> 49</option>
                                                    <option value = "50"> 50</option>
                                                    <option value = "51"> 51</option>
                                                    <option value = "52"> 52</option>
                                                    <option value = "53"> 53</option>
                                                    <option value = "54"> 54</option>
                                                    <option value = "55"> 55</option>
                                                    <option value = "56"> 56</option>
                                                    <option value = "57"> 57</option>
                                                    <option value = "58"> 58</option>
                                                    <option value = "59"> 59</option>
                                                    <option value = "60"> 60</option>
                                                </select></li>
                                    <li><label> AM/PM </label>
                                            <select name = "AMPM1" required>
                                                    <option disabled selected value> -- AM/PM --</option>
                                                    <option value = "AM"> AM</option>
                                                    <option value = "PM"> PM</option>
                                                </select></li>
                                    <br>
                                    <br>
                                    <br>
                                    <li><label>Layover Flight Number 2</label> <input name="LayoverFlightNumber2"
                                                    type="text" id="LayoverFlightNumber2"  required/></li>
                                    <li><label> Layover Time 2 </label>
                                            <select name = "LayoverTimeHour2" required>
                                                    <option disabled selected value> -- Hour --</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                </select></li>
                                    <li><label>:</label>
                                            <select name = "LayoverTimeMinute2" required>
                                                    <option disabled selected value> -- Minute --</option>
                                                    <option value = "0"> 00</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                    <option value = "13"> 13</option>
                                                    <option value = "14"> 14</option>
                                                    <option value = "15"> 15</option>
                                                    <option value = "16"> 16</option>
                                                    <option value = "17"> 17</option>
                                                    <option value = "18"> 18</option>
                                                    <option value = "19"> 19</option>
                                                    <option value = "20"> 20</option>
                                                    <option value = "21"> 21</option>
                                                    <option value = "22"> 22</option>
                                                    <option value = "23"> 23</option>
                                                    <option value = "24"> 24</option>
                                                    <option value = "25"> 25</option>
                                                    <option value = "26"> 26</option>
                                                    <option value = "27"> 27</option>
                                                    <option value = "28"> 28</option>
                                                    <option value = "29"> 29</option>
                                                    <option value = "30"> 30</option>
                                                    <option value = "31"> 31</option>
                                                    <option value = "32"> 32</option>
                                                    <option value = "33"> 33</option>
                                                    <option value = "34"> 34</option>
                                                    <option value = "35"> 35</option>
                                                    <option value = "36"> 36</option>
                                                    <option value = "37"> 37</option>
                                                    <option value = "38"> 38</option>
                                                    <option value = "39"> 39</option>
                                                    <option value = "40"> 40</option>
                                                    <option value = "41"> 41</option>
                                                    <option value = "42"> 42</option>
                                                    <option value = "43"> 43</option>
                                                    <option value = "44"> 44</option>
                                                    <option value = "45"> 45</option>
                                                    <option value = "46"> 46</option>
                                                    <option value = "47"> 47</option>
                                                    <option value = "48"> 48</option>
                                                    <option value = "49"> 49</option>
                                                    <option value = "50"> 50</option>
                                                    <option value = "51"> 51</option>
                                                    <option value = "52"> 52</option>
                                                    <option value = "53"> 53</option>
                                                    <option value = "54"> 54</option>
                                                    <option value = "55"> 55</option>
                                                    <option value = "56"> 56</option>
                                                    <option value = "57"> 57</option>
                                                    <option value = "58"> 58</option>
                                                    <option value = "59"> 59</option>
                                                    <option value = "60"> 60</option>
                                                </select></li>
                                    <li><label> AM/PM </label>
                                            <select name = "AMPM2" required>
                                                    <option disabled selected value> -- AM/PM --</option>
                                                    <option value = "AM"> AM</option>
                                                    <option value = "PM"> PM</option>
                                                </select></li>
                                    <br>
                                    <br>
                                    <br>
                                    <li><label>Layover Cost</label> <input name="LayoverCost"
                                                    type="number" id="LayoverCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <br>
                    <font size="+3">Enter How Much an Hour is Worth to You </font>
                    <br>
                    <br>
                    <ul class = "form3">
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
ul.form1{
  display: inline;
  list-style-type: none;
}
ul.form2{
  display: inline;
  list-style-type: none;
}
ul.form3{
  display: inline;
  list-style-type: none;
}
</style>
</head>
<body>
<ul class = "nav">
  <li><a href="index.html"><img src="website.jpg" alt ="website" width ="100" height="100"></a></li>
  <li style="float:right"><a href="index.html"><img src="home.png" alt ="home" width ="100" height="100"></a></li>
</ul>
<form method="post" enctype="multipart/form-data" action="twoLayover.py">
    <fieldset>
                    <legend>Flight Info</legend>
                    <font size="+3">Enter your Direct Flight Info Below </font>
                    <br>
                    <br>
                    <ul class = "form1">
                                    <li><label>Direct Flight Number</label> <input name="DirectFlightNumber"
                                                    type="text" id="DirectFlightNumber"  required/></li>
                                    <li><label> Time </label>
                                            <select name = "DirectTimeHour" required>
                                                    <option disabled selected value> -- Hour --</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                </select></li>
                                    <li><label>:</label>
                                            <select name = "DirectTimeMinute" required>
                                                    <option disabled selected value> -- Minute --</option>
                                                    <option value = "0"> 00</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                    <option value = "13"> 13</option>
                                                    <option value = "14"> 14</option>
                                                    <option value = "15"> 15</option>
                                                    <option value = "16"> 16</option>
                                                    <option value = "17"> 17</option>
                                                    <option value = "18"> 18</option>
                                                    <option value = "19"> 19</option>
                                                    <option value = "20"> 20</option>
                                                    <option value = "21"> 21</option>
                                                    <option value = "22"> 22</option>
                                                    <option value = "23"> 23</option>
                                                    <option value = "24"> 24</option>
                                                    <option value = "25"> 25</option>
                                                    <option value = "26"> 26</option>
                                                    <option value = "27"> 27</option>
                                                    <option value = "28"> 28</option>
                                                    <option value = "29"> 29</option>
                                                    <option value = "30"> 30</option>
                                                    <option value = "31"> 31</option>
                                                    <option value = "32"> 32</option>
                                                    <option value = "33"> 33</option>
                                                    <option value = "34"> 34</option>
                                                    <option value = "35"> 35</option>
                                                    <option value = "36"> 36</option>
                                                    <option value = "37"> 37</option>
                                                    <option value = "38"> 38</option>
                                                    <option value = "39"> 39</option>
                                                    <option value = "40"> 40</option>
                                                    <option value = "41"> 41</option>
                                                    <option value = "42"> 42</option>
                                                    <option value = "43"> 43</option>
                                                    <option value = "44"> 44</option>
                                                    <option value = "45"> 45</option>
                                                    <option value = "46"> 46</option>
                                                    <option value = "47"> 47</option>
                                                    <option value = "48"> 48</option>
                                                    <option value = "49"> 49</option>
                                                    <option value = "50"> 50</option>
                                                    <option value = "51"> 51</option>
                                                    <option value = "52"> 52</option>
                                                    <option value = "53"> 53</option>
                                                    <option value = "54"> 54</option>
                                                    <option value = "55"> 55</option>
                                                    <option value = "56"> 56</option>
                                                    <option value = "57"> 57</option>
                                                    <option value = "58"> 58</option>
                                                    <option value = "59"> 59</option>
                                                    <option value = "60"> 60</option>
                                                </select></li>
                                    <li><label> AM/PM </label>
                                            <select name = "AMPM" required>
                                                    <option disabled selected value> -- AM/PM --</option>
                                                    <option value = "AM"> AM</option>
                                                    <option value = "PM"> PM</option>
                                                </select></li>
                                    <br>
                                    <br>
                                    <br>
                                    <li><label>Direct Cost</label> <input name="DirectCost"
                                                    type="number" id="DirectCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <br>
                    <font size="+3">Enter your Layover Flights Info Below </font>
                    <br>
                    <br>
                    <ul class = "form2">
                                    <li><label>Layover Flight Number 1</label> <input name="LayoverFlightNumber1"
                                                    type="text" id="LayoverFlightNumber1"  required/></li>
                                    <li><label> Layover Time 1 </label>
                                            <select name = "LayoverTimeHour1" required>
                                                    <option disabled selected value> -- Hour --</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                </select></li>
                                    <li><label>:</label>
                                            <select name = "LayoverTimeMinute1" required>
                                                    <option disabled selected value> -- Minute --</option>
                                                    <option value = "0"> 00</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                    <option value = "13"> 13</option>
                                                    <option value = "14"> 14</option>
                                                    <option value = "15"> 15</option>
                                                    <option value = "16"> 16</option>
                                                    <option value = "17"> 17</option>
                                                    <option value = "18"> 18</option>
                                                    <option value = "19"> 19</option>
                                                    <option value = "20"> 20</option>
                                                    <option value = "21"> 21</option>
                                                    <option value = "22"> 22</option>
                                                    <option value = "23"> 23</option>
                                                    <option value = "24"> 24</option>
                                                    <option value = "25"> 25</option>
                                                    <option value = "26"> 26</option>
                                                    <option value = "27"> 27</option>
                                                    <option value = "28"> 28</option>
                                                    <option value = "29"> 29</option>
                                                    <option value = "30"> 30</option>
                                                    <option value = "31"> 31</option>
                                                    <option value = "32"> 32</option>
                                                    <option value = "33"> 33</option>
                                                    <option value = "34"> 34</option>
                                                    <option value = "35"> 35</option>
                                                    <option value = "36"> 36</option>
                                                    <option value = "37"> 37</option>
                                                    <option value = "38"> 38</option>
                                                    <option value = "39"> 39</option>
                                                    <option value = "40"> 40</option>
                                                    <option value = "41"> 41</option>
                                                    <option value = "42"> 42</option>
                                                    <option value = "43"> 43</option>
                                                    <option value = "44"> 44</option>
                                                    <option value = "45"> 45</option>
                                                    <option value = "46"> 46</option>
                                                    <option value = "47"> 47</option>
                                                    <option value = "48"> 48</option>
                                                    <option value = "49"> 49</option>
                                                    <option value = "50"> 50</option>
                                                    <option value = "51"> 51</option>
                                                    <option value = "52"> 52</option>
                                                    <option value = "53"> 53</option>
                                                    <option value = "54"> 54</option>
                                                    <option value = "55"> 55</option>
                                                    <option value = "56"> 56</option>
                                                    <option value = "57"> 57</option>
                                                    <option value = "58"> 58</option>
                                                    <option value = "59"> 59</option>
                                                    <option value = "60"> 60</option>
                                                </select></li>
                                    <li><label> AM/PM </label>
                                            <select name = "AMPM1" required>
                                                    <option disabled selected value> -- AM/PM --</option>
                                                    <option value = "AM"> AM</option>
                                                    <option value = "PM"> PM</option>
                                                </select></li>
                                    <br>
                                    <br>
                                    <br>
                                    <li><label>Layover Flight Number 2</label> <input name="LayoverFlightNumber2"
                                                    type="text" id="LayoverFlightNumber2"  required/></li>
                                    <li><label> Layover Time 2 </label>
                                            <select name = "LayoverTimeHour2" required>
                                                    <option disabled selected value> -- Hour --</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                </select></li>
                                    <li><label>:</label>
                                            <select name = "LayoverTimeMinute2" required>
                                                    <option disabled selected value> -- Minute --</option>
                                                    <option value = "0"> 00</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                    <option value = "13"> 13</option>
                                                    <option value = "14"> 14</option>
                                                    <option value = "15"> 15</option>
                                                    <option value = "16"> 16</option>
                                                    <option value = "17"> 17</option>
                                                    <option value = "18"> 18</option>
                                                    <option value = "19"> 19</option>
                                                    <option value = "20"> 20</option>
                                                    <option value = "21"> 21</option>
                                                    <option value = "22"> 22</option>
                                                    <option value = "23"> 23</option>
                                                    <option value = "24"> 24</option>
                                                    <option value = "25"> 25</option>
                                                    <option value = "26"> 26</option>
                                                    <option value = "27"> 27</option>
                                                    <option value = "28"> 28</option>
                                                    <option value = "29"> 29</option>
                                                    <option value = "30"> 30</option>
                                                    <option value = "31"> 31</option>
                                                    <option value = "32"> 32</option>
                                                    <option value = "33"> 33</option>
                                                    <option value = "34"> 34</option>
                                                    <option value = "35"> 35</option>
                                                    <option value = "36"> 36</option>
                                                    <option value = "37"> 37</option>
                                                    <option value = "38"> 38</option>
                                                    <option value = "39"> 39</option>
                                                    <option value = "40"> 40</option>
                                                    <option value = "41"> 41</option>
                                                    <option value = "42"> 42</option>
                                                    <option value = "43"> 43</option>
                                                    <option value = "44"> 44</option>
                                                    <option value = "45"> 45</option>
                                                    <option value = "46"> 46</option>
                                                    <option value = "47"> 47</option>
                                                    <option value = "48"> 48</option>
                                                    <option value = "49"> 49</option>
                                                    <option value = "50"> 50</option>
                                                    <option value = "51"> 51</option>
                                                    <option value = "52"> 52</option>
                                                    <option value = "53"> 53</option>
                                                    <option value = "54"> 54</option>
                                                    <option value = "55"> 55</option>
                                                    <option value = "56"> 56</option>
                                                    <option value = "57"> 57</option>
                                                    <option value = "58"> 58</option>
                                                    <option value = "59"> 59</option>
                                                    <option value = "60"> 60</option>
                                                </select></li>
                                    <li><label> AM/PM </label>
                                            <select name = "AMPM2" required>
                                                    <option disabled selected value> -- AM/PM --</option>
                                                    <option value = "AM"> AM</option>
                                                    <option value = "PM"> PM</option>
                                                </select></li>
                                    <br>
                                    <br>
                                    <br>
                                    <li><label>Layover Flight Number 3</label> <input name="LayoverFlightNumber3"
                                                    type="text" id="LayoverFlightNumber3"  required/></li>
                                    <li><label> Layover Time 3 </label>
                                            <select name = "LayoverTimeHour3" required>
                                                    <option disabled selected value> -- Hour --</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                </select></li>
                                    <li><label>:</label>
                                            <select name = "LayoverTimeMinute3" required>
                                                    <option disabled selected value> -- Minute --</option>
                                                    <option value = "0"> 00</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                    <option value = "13"> 13</option>
                                                    <option value = "14"> 14</option>
                                                    <option value = "15"> 15</option>
                                                    <option value = "16"> 16</option>
                                                    <option value = "17"> 17</option>
                                                    <option value = "18"> 18</option>
                                                    <option value = "19"> 19</option>
                                                    <option value = "20"> 20</option>
                                                    <option value = "21"> 21</option>
                                                    <option value = "22"> 22</option>
                                                    <option value = "23"> 23</option>
                                                    <option value = "24"> 24</option>
                                                    <option value = "25"> 25</option>
                                                    <option value = "26"> 26</option>
                                                    <option value = "27"> 27</option>
                                                    <option value = "28"> 28</option>
                                                    <option value = "29"> 29</option>
                                                    <option value = "30"> 30</option>
                                                    <option value = "31"> 31</option>
                                                    <option value = "32"> 32</option>
                                                    <option value = "33"> 33</option>
                                                    <option value = "34"> 34</option>
                                                    <option value = "35"> 35</option>
                                                    <option value = "36"> 36</option>
                                                    <option value = "37"> 37</option>
                                                    <option value = "38"> 38</option>
                                                    <option value = "39"> 39</option>
                                                    <option value = "40"> 40</option>
                                                    <option value = "41"> 41</option>
                                                    <option value = "42"> 42</option>
                                                    <option value = "43"> 43</option>
                                                    <option value = "44"> 44</option>
                                                    <option value = "45"> 45</option>
                                                    <option value = "46"> 46</option>
                                                    <option value = "47"> 47</option>
                                                    <option value = "48"> 48</option>
                                                    <option value = "49"> 49</option>
                                                    <option value = "50"> 50</option>
                                                    <option value = "51"> 51</option>
                                                    <option value = "52"> 52</option>
                                                    <option value = "53"> 53</option>
                                                    <option value = "54"> 54</option>
                                                    <option value = "55"> 55</option>
                                                    <option value = "56"> 56</option>
                                                    <option value = "57"> 57</option>
                                                    <option value = "58"> 58</option>
                                                    <option value = "59"> 59</option>
                                                    <option value = "60"> 60</option>
                                                </select></li>
                                    <li><label> AM/PM </label>
                                            <select name = "AMPM3" required>
                                                    <option disabled selected value> -- AM/PM --</option>
                                                    <option value = "AM"> AM</option>
                                                    <option value = "PM"> PM</option>
                                                </select></li>
                                    <br>
                                    <br>
                                    <br>
                                    <li><label>Layover Cost</label> <input name="LayoverCost"
                                                    type="number" id="LayoverCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <br>
                    <font size="+3">Enter How Much an Hour is Worth to You </font>
                    <br>
                    <br>
                    <ul class = "form3">
                                <li><label>Hour Cost</label> <input name="HourCost"
                                                type="number" id="HourCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <input type = "submit" id="upload" value = "Continue"/>
    </fieldset>
</form>
</body>
</html>"""
)

if layovers == "3" :
    logging.warn("here")
    cgitb.enable()
    print("Content-type: text/html")
    print("")
    print ("""
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
ul.form1{
  display: inline;
  list-style-type: none;
}
ul.form2{
  display: inline;
  list-style-type: none;
}
ul.form3{
  display: inline;
  list-style-type: none;
}
</style>
</head>
<body>
<ul class = "nav">
  <li><a href="index.html"><img src="website.jpg" alt ="website" width ="100" height="100"></a></li>
  <li style="float:right"><a href="index.html"><img src="home.png" alt ="home" width ="100" height="100"></a></li>
</ul>
<form method="post" enctype="multipart/form-data" action="threeLayover.py">
    <fieldset>
                    <legend>Flight Info</legend>
                    <font size="+3">Enter your Direct Flight Info Below </font>
                    <br>
                    <br>
                    <ul class = "form1">
                                    <li><label>Direct Flight Number</label> <input name="DirectFlightNumber"
                                                    type="text" id="DirectFlightNumber"  required/></li>
                                    <li><label> Time </label>
                                            <select name = "DirectTimeHour" required>
                                                    <option disabled selected value> -- Hour --</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                </select></li>
                                    <li><label>:</label>
                                            <select name = "DirectTimeMinute" required>
                                                    <option disabled selected value> -- Minute --</option>
                                                    <option value = "0"> 00</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                    <option value = "13"> 13</option>
                                                    <option value = "14"> 14</option>
                                                    <option value = "15"> 15</option>
                                                    <option value = "16"> 16</option>
                                                    <option value = "17"> 17</option>
                                                    <option value = "18"> 18</option>
                                                    <option value = "19"> 19</option>
                                                    <option value = "20"> 20</option>
                                                    <option value = "21"> 21</option>
                                                    <option value = "22"> 22</option>
                                                    <option value = "23"> 23</option>
                                                    <option value = "24"> 24</option>
                                                    <option value = "25"> 25</option>
                                                    <option value = "26"> 26</option>
                                                    <option value = "27"> 27</option>
                                                    <option value = "28"> 28</option>
                                                    <option value = "29"> 29</option>
                                                    <option value = "30"> 30</option>
                                                    <option value = "31"> 31</option>
                                                    <option value = "32"> 32</option>
                                                    <option value = "33"> 33</option>
                                                    <option value = "34"> 34</option>
                                                    <option value = "35"> 35</option>
                                                    <option value = "36"> 36</option>
                                                    <option value = "37"> 37</option>
                                                    <option value = "38"> 38</option>
                                                    <option value = "39"> 39</option>
                                                    <option value = "40"> 40</option>
                                                    <option value = "41"> 41</option>
                                                    <option value = "42"> 42</option>
                                                    <option value = "43"> 43</option>
                                                    <option value = "44"> 44</option>
                                                    <option value = "45"> 45</option>
                                                    <option value = "46"> 46</option>
                                                    <option value = "47"> 47</option>
                                                    <option value = "48"> 48</option>
                                                    <option value = "49"> 49</option>
                                                    <option value = "50"> 50</option>
                                                    <option value = "51"> 51</option>
                                                    <option value = "52"> 52</option>
                                                    <option value = "53"> 53</option>
                                                    <option value = "54"> 54</option>
                                                    <option value = "55"> 55</option>
                                                    <option value = "56"> 56</option>
                                                    <option value = "57"> 57</option>
                                                    <option value = "58"> 58</option>
                                                    <option value = "59"> 59</option>
                                                    <option value = "60"> 60</option>
                                                </select></li>
                                    <li><label> AM/PM </label>
                                            <select name = "AMPM" required>
                                                    <option disabled selected value> -- AM/PM --</option>
                                                    <option value = "AM"> AM</option>
                                                    <option value = "PM"> PM</option>
                                                </select></li>
                                    <br>
                                    <br>
                                    <br>
                                    <li><label>Direct Cost</label> <input name="DirectCost"
                                                    type="number" id="DirectCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <br>
                    <font size="+3">Enter your Layover Flights Info Below </font>
                    <br>
                    <br>
                    <ul class = "form2">
                                    <li><label>Layover Flight Number 1</label> <input name="LayoverFlightNumber1"
                                                    type="text" id="LayoverFlightNumber1"  required/></li>
                                    <li><label> Layover Time 1 </label>
                                            <select name = "LayoverTimeHour1" required>
                                                    <option disabled selected value> -- Hour --</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                </select></li>
                                    <li><label>:</label>
                                            <select name = "LayoverTimeMinute1" required>
                                                    <option disabled selected value> -- Minute --</option>
                                                    <option value = "0"> 00</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                    <option value = "13"> 13</option>
                                                    <option value = "14"> 14</option>
                                                    <option value = "15"> 15</option>
                                                    <option value = "16"> 16</option>
                                                    <option value = "17"> 17</option>
                                                    <option value = "18"> 18</option>
                                                    <option value = "19"> 19</option>
                                                    <option value = "20"> 20</option>
                                                    <option value = "21"> 21</option>
                                                    <option value = "22"> 22</option>
                                                    <option value = "23"> 23</option>
                                                    <option value = "24"> 24</option>
                                                    <option value = "25"> 25</option>
                                                    <option value = "26"> 26</option>
                                                    <option value = "27"> 27</option>
                                                    <option value = "28"> 28</option>
                                                    <option value = "29"> 29</option>
                                                    <option value = "30"> 30</option>
                                                    <option value = "31"> 31</option>
                                                    <option value = "32"> 32</option>
                                                    <option value = "33"> 33</option>
                                                    <option value = "34"> 34</option>
                                                    <option value = "35"> 35</option>
                                                    <option value = "36"> 36</option>
                                                    <option value = "37"> 37</option>
                                                    <option value = "38"> 38</option>
                                                    <option value = "39"> 39</option>
                                                    <option value = "40"> 40</option>
                                                    <option value = "41"> 41</option>
                                                    <option value = "42"> 42</option>
                                                    <option value = "43"> 43</option>
                                                    <option value = "44"> 44</option>
                                                    <option value = "45"> 45</option>
                                                    <option value = "46"> 46</option>
                                                    <option value = "47"> 47</option>
                                                    <option value = "48"> 48</option>
                                                    <option value = "49"> 49</option>
                                                    <option value = "50"> 50</option>
                                                    <option value = "51"> 51</option>
                                                    <option value = "52"> 52</option>
                                                    <option value = "53"> 53</option>
                                                    <option value = "54"> 54</option>
                                                    <option value = "55"> 55</option>
                                                    <option value = "56"> 56</option>
                                                    <option value = "57"> 57</option>
                                                    <option value = "58"> 58</option>
                                                    <option value = "59"> 59</option>
                                                    <option value = "60"> 60</option>
                                                </select></li>
                                    <li><label> AM/PM </label>
                                            <select name = "AMPM1" required>
                                                    <option disabled selected value> -- AM/PM --</option>
                                                    <option value = "AM"> AM</option>
                                                    <option value = "PM"> PM</option>
                                                </select></li>
                                    <br>
                                    <br>
                                    <br>
                                    <li><label>Layover Flight Number 2</label> <input name="LayoverFlightNumber2"
                                                    type="text" id="LayoverFlightNumber2"  required/></li>
                                    <li><label> Layover Time 2 </label>
                                            <select name = "LayoverTimeHour2" required>
                                                    <option disabled selected value> -- Hour --</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                </select></li>
                                    <li><label>:</label>
                                            <select name = "LayoverTimeMinute2" required>
                                                    <option disabled selected value> -- Minute --</option>
                                                    <option value = "0"> 00</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                    <option value = "13"> 13</option>
                                                    <option value = "14"> 14</option>
                                                    <option value = "15"> 15</option>
                                                    <option value = "16"> 16</option>
                                                    <option value = "17"> 17</option>
                                                    <option value = "18"> 18</option>
                                                    <option value = "19"> 19</option>
                                                    <option value = "20"> 20</option>
                                                    <option value = "21"> 21</option>
                                                    <option value = "22"> 22</option>
                                                    <option value = "23"> 23</option>
                                                    <option value = "24"> 24</option>
                                                    <option value = "25"> 25</option>
                                                    <option value = "26"> 26</option>
                                                    <option value = "27"> 27</option>
                                                    <option value = "28"> 28</option>
                                                    <option value = "29"> 29</option>
                                                    <option value = "30"> 30</option>
                                                    <option value = "31"> 31</option>
                                                    <option value = "32"> 32</option>
                                                    <option value = "33"> 33</option>
                                                    <option value = "34"> 34</option>
                                                    <option value = "35"> 35</option>
                                                    <option value = "36"> 36</option>
                                                    <option value = "37"> 37</option>
                                                    <option value = "38"> 38</option>
                                                    <option value = "39"> 39</option>
                                                    <option value = "40"> 40</option>
                                                    <option value = "41"> 41</option>
                                                    <option value = "42"> 42</option>
                                                    <option value = "43"> 43</option>
                                                    <option value = "44"> 44</option>
                                                    <option value = "45"> 45</option>
                                                    <option value = "46"> 46</option>
                                                    <option value = "47"> 47</option>
                                                    <option value = "48"> 48</option>
                                                    <option value = "49"> 49</option>
                                                    <option value = "50"> 50</option>
                                                    <option value = "51"> 51</option>
                                                    <option value = "52"> 52</option>
                                                    <option value = "53"> 53</option>
                                                    <option value = "54"> 54</option>
                                                    <option value = "55"> 55</option>
                                                    <option value = "56"> 56</option>
                                                    <option value = "57"> 57</option>
                                                    <option value = "58"> 58</option>
                                                    <option value = "59"> 59</option>
                                                    <option value = "60"> 60</option>
                                                </select></li>
                                    <li><label> AM/PM </label>
                                            <select name = "AMPM2" required>
                                                    <option disabled selected value> -- AM/PM --</option>
                                                    <option value = "AM"> AM</option>
                                                    <option value = "PM"> PM</option>
                                                </select></li>
                                    <br>
                                    <br>
                                    <br>
                                    <li><label>Layover Flight Number 3</label> <input name="LayoverFlightNumber3"
                                                    type="text" id="LayoverFlightNumber3"  required/></li>
                                    <li><label> Layover Time 3 </label>
                                            <select name = "LayoverTimeHour3" required>
                                                    <option disabled selected value> -- Hour --</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                </select></li>
                                    <li><label>:</label>
                                            <select name = "LayoverTimeMinute3" required>
                                                    <option disabled selected value> -- Minute --</option>
                                                    <option value = "0"> 00</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                    <option value = "13"> 13</option>
                                                    <option value = "14"> 14</option>
                                                    <option value = "15"> 15</option>
                                                    <option value = "16"> 16</option>
                                                    <option value = "17"> 17</option>
                                                    <option value = "18"> 18</option>
                                                    <option value = "19"> 19</option>
                                                    <option value = "20"> 20</option>
                                                    <option value = "21"> 21</option>
                                                    <option value = "22"> 22</option>
                                                    <option value = "23"> 23</option>
                                                    <option value = "24"> 24</option>
                                                    <option value = "25"> 25</option>
                                                    <option value = "26"> 26</option>
                                                    <option value = "27"> 27</option>
                                                    <option value = "28"> 28</option>
                                                    <option value = "29"> 29</option>
                                                    <option value = "30"> 30</option>
                                                    <option value = "31"> 31</option>
                                                    <option value = "32"> 32</option>
                                                    <option value = "33"> 33</option>
                                                    <option value = "34"> 34</option>
                                                    <option value = "35"> 35</option>
                                                    <option value = "36"> 36</option>
                                                    <option value = "37"> 37</option>
                                                    <option value = "38"> 38</option>
                                                    <option value = "39"> 39</option>
                                                    <option value = "40"> 40</option>
                                                    <option value = "41"> 41</option>
                                                    <option value = "42"> 42</option>
                                                    <option value = "43"> 43</option>
                                                    <option value = "44"> 44</option>
                                                    <option value = "45"> 45</option>
                                                    <option value = "46"> 46</option>
                                                    <option value = "47"> 47</option>
                                                    <option value = "48"> 48</option>
                                                    <option value = "49"> 49</option>
                                                    <option value = "50"> 50</option>
                                                    <option value = "51"> 51</option>
                                                    <option value = "52"> 52</option>
                                                    <option value = "53"> 53</option>
                                                    <option value = "54"> 54</option>
                                                    <option value = "55"> 55</option>
                                                    <option value = "56"> 56</option>
                                                    <option value = "57"> 57</option>
                                                    <option value = "58"> 58</option>
                                                    <option value = "59"> 59</option>
                                                    <option value = "60"> 60</option>
                                                </select></li>
                                    <li><label> AM/PM </label>
                                            <select name = "AMPM3" required>
                                                    <option disabled selected value> -- AM/PM --</option>
                                                    <option value = "AM"> AM</option>
                                                    <option value = "PM"> PM</option>
                                                </select></li>
                                    <br>
                                    <br>
                                    <br>
                                    <li><label>Layover Flight Number 4</label> <input name="LayoverFlightNumber4"
                                                    type="text" id="LayoverFlightNumber4"  required/></li>
                                    <li><label> Layover Time 3 </label>
                                            <select name = "LayoverTimeHour4" required>
                                                    <option disabled selected value> -- Hour --</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                </select></li>
                                    <li><label>:</label>
                                            <select name = "LayoverTimeMinute4" required>
                                                    <option disabled selected value> -- Minute --</option>
                                                    <option value = "0"> 00</option>
                                                    <option value = "1"> 1</option>
                                                    <option value = "2"> 2</option>
                                                    <option value = "3"> 3</option>
                                                    <option value = "4"> 4</option>
                                                    <option value = "5"> 5</option>
                                                    <option value = "6"> 6</option>
                                                    <option value = "7"> 7</option>
                                                    <option value = "8"> 8</option>
                                                    <option value = "9"> 9</option>
                                                    <option value = "10"> 10</option>
                                                    <option value = "11"> 11</option>
                                                    <option value = "12"> 12</option>
                                                    <option value = "13"> 13</option>
                                                    <option value = "14"> 14</option>
                                                    <option value = "15"> 15</option>
                                                    <option value = "16"> 16</option>
                                                    <option value = "17"> 17</option>
                                                    <option value = "18"> 18</option>
                                                    <option value = "19"> 19</option>
                                                    <option value = "20"> 20</option>
                                                    <option value = "21"> 21</option>
                                                    <option value = "22"> 22</option>
                                                    <option value = "23"> 23</option>
                                                    <option value = "24"> 24</option>
                                                    <option value = "25"> 25</option>
                                                    <option value = "26"> 26</option>
                                                    <option value = "27"> 27</option>
                                                    <option value = "28"> 28</option>
                                                    <option value = "29"> 29</option>
                                                    <option value = "30"> 30</option>
                                                    <option value = "31"> 31</option>
                                                    <option value = "32"> 32</option>
                                                    <option value = "33"> 33</option>
                                                    <option value = "34"> 34</option>
                                                    <option value = "35"> 35</option>
                                                    <option value = "36"> 36</option>
                                                    <option value = "37"> 37</option>
                                                    <option value = "38"> 38</option>
                                                    <option value = "39"> 39</option>
                                                    <option value = "40"> 40</option>
                                                    <option value = "41"> 41</option>
                                                    <option value = "42"> 42</option>
                                                    <option value = "43"> 43</option>
                                                    <option value = "44"> 44</option>
                                                    <option value = "45"> 45</option>
                                                    <option value = "46"> 46</option>
                                                    <option value = "47"> 47</option>
                                                    <option value = "48"> 48</option>
                                                    <option value = "49"> 49</option>
                                                    <option value = "50"> 50</option>
                                                    <option value = "51"> 51</option>
                                                    <option value = "52"> 52</option>
                                                    <option value = "53"> 53</option>
                                                    <option value = "54"> 54</option>
                                                    <option value = "55"> 55</option>
                                                    <option value = "56"> 56</option>
                                                    <option value = "57"> 57</option>
                                                    <option value = "58"> 58</option>
                                                    <option value = "59"> 59</option>
                                                    <option value = "60"> 60</option>
                                                </select></li>
                                    <li><label> AM/PM </label>
                                            <select name = "AMPM4" required>
                                                    <option disabled selected value> -- AM/PM --</option>
                                                    <option value = "AM"> AM</option>
                                                    <option value = "PM"> PM</option>
                                                </select></li>
                                    <br>
                                    <br>
                                    <br>
                                    <li><label>Layover Cost</label> <input name="LayoverCost"
                                                    type="number" id="LayoverCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <br>
                    <font size="+3">Enter How Much an Hour is Worth to You </font>
                    <br>
                    <br>
                    <ul class = "form3">
                                <li><label>Hour Cost</label> <input name="HourCost"
                                                type="number" id="HourCost"  required/></li>
                    </ul>
                    <br>
                    <br>
                    <input type = "submit" id="upload" value = "Continue"/>
    </fieldset>
</form>
</body>
</html>"""
)