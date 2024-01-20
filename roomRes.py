from selenium import webdriver
import time


######################################################################################################################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################

str = """Personal Projects and Popcorn 

Date: Feb 6

Time: 6PM - 7PM

Location: CSE, Little, or L136

Details: Emily Jiji will be hosting a workshop about how to start your own personal project and eventually turn it into a startup. There will be popcorn and this event is interactive and social as well.

Attendees: 30


"""

######################################################################################################################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################

months = {'Jan': '01',
          'Feb': '02',
          'March': '03',
          'April': '04',
          'May': '05',
          'June': '06',
          'July': '07',
          'Aug': '08',
          'Sept': '09',
          'Oct': '10',
          'Nov': '11',
          'Dec': '12'
          }
# Split the string by newline character
lines = str.strip().split('\n')

# Create a list to hold the split elements
split_elements = []

# Iterate over each line
for line in lines:
    if line:  # Check if line is not empty
        # Split the line by colon and strip whitespaces
        elements = [elem.strip() for elem in line.split(':', 1)]
        split_elements.append(elements)

dictData = {}

# Print the list of split elements
for elements in split_elements:
    print(elements)
    if len(elements) == 1:
        dictData["EventName"] = elements[0]
    else:
        dictData[elements[0]] = elements[1]

dateStr = dictData['Date'].split(' ')

if len(dateStr[1]) == 1:
    dateStr[1] = '0' + dateStr[1]

eventName = dictData['EventName']
eventDate = months[dateStr[0]] + dateStr[1] +'2024'
theTime = dictData['Time']
location = dictData['Location']
details = dictData["Details"]
attendees = dictData['Attendees']

print('event name: ', eventName)
print("date: ",eventDate)
print("time: ",time)
print("location: ",location)
print("details: ",details)
print("attendees: ",attendees)



# Replace this with the actual path to your downloaded ChromeDriver
path_to_chromedriver = '/Users/tina/Desktop/WiCSE/chromedriver'  # e.g., '/Users/tina/Desktop/chromedriver'
web = webdriver.Chrome(executable_path=path_to_chromedriver)
web.get('https://docs.google.com/forms/d/e/1FAIpQLSd06SPaVb5FATgwpmv0taz9mJQiqLrmde0dkZjKvNvrSDvlhQ/viewform')

time.sleep(1)

myEmail = 'tinac.592@yahoo.com'
email = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
email.send_keys(myEmail)

myName = 'Tina Chi'
name = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys(myName)

event = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
event.send_keys(eventName)

event = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
event.send_keys(details)

date = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
date.send_keys(eventDate)

theEventTime = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
theEventTime.send_keys(theTime)


numAtt = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
numAtt.send_keys(attendees)

roomPref = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
roomPref.send_keys(location)

speakerQNo = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[2]/div/span')
speakerQNo.click()

nextButton = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
nextButton.click()

submitButton = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[3]/div[1]/div[2]/span/span')
submitButton.click()
