# denso-hack
DENSO Heat Flux sensor hackthon by HackerEarth

In the instance of a fire, a quick and safe evacuation of everyone in the building is of the utmost importance. Fire and smoke spread fast and could leave people trapped in dangerous, inescapable locations if an evacuation plan is not in place and it's not accurate.

Nowadays most of the buildings having static fire exit plans which are predefined and having less awareness fire intensity. People might end up on using these exits which are sometimes are dangerous and life-threatening.

To address this problem we need to make an intiligent system which monitors heat flow directions in the emergency. According to data obtained from the various DENSO heat flux sensors, our system will decide the safest path to evacuate with user-friendly notations and also it informs the fire brigade to what is the root place which caused the fire and at what density it is reached. Hence fire safety people also can get easy accessible real-time data to extinguish fire properly.

Working Principle, 
* Connect DENSO flux sensors on different parts of the building 
* Take data of heat flow of each sensor in regular interval of time 
* If the average data reaches the threshold level make appropriate sign of firealaram 
* Keep on track of the heat flow changes and make appropropriate evacuation plan with reference of predefined floar plans and other sensors data. 
* The evacuation plans has to be dependent on other DENSO sensors data and floar building plan, Central system will decides the evacuation plan and appropriate sings and info will be displayed on display units 
* From central data processing system it will be informed to outside world through web interface or other media interface

To demonstrate above idea our prototype will includes, 
Hardware: 
* RasberryPi 2 running linux 
* LCD display 
* DENSO Heat flux Sensors
* LED's 

Software: 
* Wiring PI C libraries 
* Digital ocean or opneshift Web API's
