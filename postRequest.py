from selenium import webdriver
import time


######################################################################################################################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################

str = """Data Science Workshop Classification

Date: Feb 13

Time: 4PM - 5PM

Location: Matherly 0018 

Details: Rida will covering Classification. I’ll be going over the concept as well as having live coding for the attendees to work on

Instagram Caption:  N/a

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
instagramCaption = dictData['Instagram Caption']


timeHour = 0
timeMin = 0

AMPM = ''


timeSplitArray = dictData['Time'].split('-')
if dictData['Time'].find(':') != -1:
    timeStartSplitArray = timeSplitArray[0].split(':')
    temp = timeStartSplitArray[0].find('M')
    AMPM = timeStartSplitArray[0][temp - 1: temp]
    timeHour = timeStartSplitArray[0]
    timeMin = timeStartSplitArray[1][0:temp-2]
else:
    temp = timeSplitArray[0].find('M')
    timeHour = timeSplitArray[0][0:temp-1]
    AMPM = timeSplitArray[0][temp-1:]
 



    


print('event name: ', eventName)
print("date: ",eventDate)
print("time: ",theTime)
print("location: ",location)
print("details: ",details)
print("attendees: ",attendees)




# Replace this with the actual path to your downloaded ChromeDriver
path_to_chromedriver = '/Users/tina/Desktop/WiCSE/chromedriver'  # e.g., '/Users/tina/Desktop/chromedriver'
web = webdriver.Chrome(executable_path=path_to_chromedriver)
web.get('https://docs.google.com/forms/d/e/1FAIpQLSevalh5lbihgs04yfd-b4_2mGXSWsjVf3j0kyiqLVQUm5d5aQ/viewform')


myEmail = 'tinac.592@yahoo.com'
email = web.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
email.send_keys(myEmail)



# event = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
# event.send_keys(eventName)






# numAtt = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
# numAtt.send_keys(attendees)

# roomPref = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
# roomPref.send_keys(location)

# speakerQNo = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[2]/div/span')
# speakerQNo.click()


yesButton = web.find_element('xpath','//*[@id="i9"]/div[3]/div')
yesButton.click()


nextButton = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
nextButton.click()

# if AMPM == 'PM' or AMPM == ' PM' or AMPM == 'PM ':
#     AMButton = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[4]/div[2]/div[1]')
#     AMButton.click()
# else:
#     PMButton = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[4]/div[2]/div[2]/span')
#     PMButton.click()


myName = 'Tina Chi'
name = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
name.send_keys(myName)

event = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
event.send_keys(eventName)

date = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
date.send_keys(eventDate)


theEventTimeHour = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input')
theEventTimeHour.send_keys(timeHour)


theEventTimeMin = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input')
theEventTimeMin.send_keys(timeMin)


# time.sleep(2)
# caption = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/textarea')

# caption.send_keys(instagramCaption)



print(AMPM)