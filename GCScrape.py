from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import csv

#login and go to the search page

driver = webdriver.Firefox()
driver.get('https://gc.com/login')
email = driver.find_element_by_id('email')
email.send_keys("jenniferlist@hotmail.com")
password = driver.find_element_by_id('login_password')
password.send_keys("Annika99")
login = driver.find_element_by_id('login')
login.click()
driver.get('https://gc.com/search')

#telling the bot to look at the first result first

x = 0
y = 0

#determining list of players who debut in 15 or 16

data = open('DEBUT1516.csv')
reader = csv.reader(data)
interestingrows = [i[1] for i in reader]

#typing in players name and hitting search

fullsearch = driver.find_element_by_class_name('yui3-g')
fullsearch.send_keys(interestingrows[y+20])
searchbutton = driver.find_element_by_class_name('yui3-u-1-8')
searchbutton.click()

#clicking the players tab

results = driver.find_element_by_class_name('nav.nav-tabs.supersize-tabs.plainColorTabs.searchTabs')
playersbutton = results.find_element_by_xpath('//*[@title="Search Players"]')
playersbutton.click()


#determining the search results and clicking the first name

chartOfResults = driver.find_element_by_class_name('withDividers')
firstResult = chartOfResults.find_elements_by_tag_name('li')
firstNameButton = firstResult[x].find_element_by_tag_name('h1')
firstNameButton.click()
driver.implicitly_wait(2)

def new():
    
    driver.get('https://gc.com/search')
    fullsearch = driver.find_element_by_class_name('yui3-g')
    fullsearch.send_keys(interestingrows[y+20])
    searchbutton = driver.find_element_by_class_name('yui3-u-1-8')
    searchbutton.click()
        
    results = driver.find_element_by_class_name('nav.nav-tabs.supersize-tabs.plainColorTabs.searchTabs')
    playersbutton = results.find_element_by_xpath('//*[@title="Search Players"]')
    playersbutton.click()
        
    chartOfResults = driver.find_element_by_class_name('withDividers')
    firstResult = chartOfResults.find_elements_by_tag_name('li')
    firstNameButton = firstResult[x].find_element_by_tag_name('h1')
    firstNameButton.click()
    driver.implicitly_wait(2)

#the redo function attempts to receive data from the specific player, but if it doesn't, it tries the next result

def redo():
    
	try:
		sprayCharts = driver.find_element_by_xpath('//*[@title="Spray Charts"]')
		#sprayCharts.click()
		total = driver.find_element_by_tag_name('tfoot')
		alltotals = total.find_element_by_class_name('totals.totals_all')

		with open('gc.csv', 'w') as f:
		    csvwriter = csv.writer(f)
		    headers = ['NAME','PA','AB','H', 'Single', 'Double', 'Triple', 'HR', 'RBI', 
			'R', 'HBP', 'ROE', 'FC', 'CI', 'BB', 'K', 'AVG', 'OBP', 'SLG', 'OPS']
		    csvwriter.writerow(headers)
                for row in alltotals:
                    columns = alltotals.find_elements_by_class_name('td')
                    NAME = interestingrows[y]
                    PA = columns[1].text
                    AB = columns[2].text
                    H = columns[3].text
                    Single = columns[4].text
                    Double = columns[5].text
                    Triple = columns[6].text
                    HR = columns[7].text
                    RBI = columns[8].text
                    R = columns[9].text
                    HBP = columns[10].text
                    ROE = columns[11].text
                    FC = columns[12].text
                    CI = columns[13].text
                    BB = columns[14].text
                    K = columns[15].text
                    AVG = columns[16].text
                    OBP = columns[17].text
                    SLG = columns[18].text
                    OPS = columns[19].text
                tempList = [NAME, PA, AB, H, Single, Double, Triple, HR, RBI, R, HBP, ROE, FC, CI, BB, K, AVG, OBP, SLG, OPS]
                csvwriter.writerow(tempList)
                y = y + 1
                new()

	except NoSuchElementException:
        # x-ing out of the error, re-searching the players name, clicking the players button, clicking the result after the error
		error = driver.find_element_by_class_name('ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.gcWall')
		xbutton = error.find_element_by_tag_name('button')
		xbutton.click()
		fullsearch = driver.find_element_by_class_name('yui3-g')
		fullsearch.send_keys("")
		searchbutton = driver.find_element_by_class_name('yui3-u-1-8')
		searchbutton.click()

		results = driver.find_element_by_class_name('nav.nav-tabs.supersize-tabs.plainColorTabs.searchTabs')
		playersbutton = results.find_element_by_xpath('//*[@title="Search Players"]')
		playersbutton.click()

		chartOfResults = driver.find_element_by_class_name('withDividers')
		firstResult = chartOfResults.find_elements_by_tag_name('li')
		firstNameButton = firstResult[x+1].find_element_by_tag_name('h1')
		firstNameButton.click()


#this is saying to run redo until there are no more search results to look at. It goes down another result each time
#The except part is saying when there is some sort of error other than the privacy thing, it will go back to the search bar and restart

#for x in xrange(len(firstResult)):

while True:

    x = x + 1
    
    try:
        
        redo()


    except NoSuchElementException:

        new()

        redo()

