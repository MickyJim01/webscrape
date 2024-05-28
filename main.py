import mechanicalsoup
from bs4 import BeautifulSoup as bsoup
import json

# Load my username and password into variables
with open("login.json", "r") as login:
    creds = json.load(login)["credentials"]
user_ = creds["Username"]
pass_ = creds["Password"]

# create a browser using MechSoup
browser = mechanicalsoup.StatefulBrowser()
# feed browser url of logon page
browser.open("https://www.airservicesaustralia.com/naips/Account/LogOn")

# select the logon form on the page and select input fields by name, giving them values of my logon details
browser.select_form('form[id="frmLogon"]')
browser["UserName"] = user_
browser["Password"] = pass_
response = browser.submit_selected()  # submit the form
# using 'print(response, browser.url)' here would show a succesful response of 200 and the new url
# "click" a button on the page to take me to the briefing page
browser.follow_link("Briefing/Location")
# select the form on the new page and input the airport code and the validity time, then submit
browser.select_form('form[id="frmLocationBriefing"]')
browser["Locations[0]"] = "YPDN"
browser["Validity"] = "12"
response = browser.submit_selected()
# using 'print(response, browser.url)' here would show a succesful response of 200 and the new url

# now using beautiful soup to parse the document to find the first "pre" tag which contains the TAF
# second pre tab contains the NOTAMS
page = browser.page
briefing = page.find("pre").get_text()
# print("\n\n", briefing)
# print(briefing.split(metar)[1])
breakdown = briefing.split()
# print(breakdown)
metar = breakdown[breakdown.index("METAR") : breakdown.index("ATIS")]
print(" ".join(metar))
