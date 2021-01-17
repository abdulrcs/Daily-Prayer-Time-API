# Daily Prayer Time API 🌙
<p align="center">
  <img src="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/facebook/230/mosque_1f54c.png" >
</p>  

It's an easy to use API to get today's prayer time based on **Muslim Pro.**  
Written in Python using _Flask, Beautiful Soup, and Google-Search-Python_.
### Example Response:
```json
{
    "city": "Mecca",
    "date": "17 January 2021",
    "prayers": {
        "Fajr": "05:41",
        "Sunrise": "07:01",
        "Dhuhr": "12:31",
        "Asr": "15:39",
        "Maghrib": "18:01",
        "Isha'a": "19:31"
}
```
## Get Started
To use the API, you can simply fetch the data using the public API in  
https://dailyprayer.abdulrcs.repl.co/api/(City Name)  
## Here's an example 😉
### Print the Data in Python:
```python
import requests
import json

url = "https://dailyprayer.abdulrcs.repl.co/api/singapore"
response = requests.get(url)
data = response.json()
print(data['city'])
print(data['date'])
for prayer in data["prayers"]:
  print(prayer + ": " + data["prayers"][prayer])  
```

### Print the Data in Node.js:
```javascript
const https = require('https');
let url = "https://dailyprayer.abdulrcs.repl.co/api/singapore";

https.get(url,(res) => {
    let body = "";

    res.on("data", (chunk) => {
        body += chunk;
    });

    res.on("end", () => {
        try {
            let json = JSON.parse(body);
            console.log(json["city"])
            console.log(json["date"])
            for(prayer in json["prayers"])
              console.log(prayer + ": " + json["prayers"][prayer])
        } catch (error) {
            console.error(error.message);
        };
    });

}).on("error", (error) => {
    console.error(error.message);
});
```
### Output:
```
Singapore
17 January 2021
Fajr: 05:52
Sunrise: 07:14
Dhuhr: 13:17
Asr: 16:40
Maghrib: 19:17
Isha'a: 20:31
```
