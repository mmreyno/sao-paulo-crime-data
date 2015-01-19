from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# set paths
path_to_chromedriver = '/usr/lib/python2.7/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'http://www.ssp.sp.gov.br/novaestatistica/Pesquisa.aspx'
browser.get(url)

# find the years menu
years = browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_ddlAnos"]') 
allyears = years.find_elements_by_tag_name('option') #find possible years
allyears[3].click() #'4' returns 2012 results, '3' returns 2013, '2' returns 2014
time.sleep(5)

# find region menu
regions = browser.find_element_by_id('ContentPlaceHolder1_ddlRegioes')
allregions = regions.find_elements_by_tag_name('option') #find possible regions	
allregions[1].click() #gives capital as region
time.sleep(5)

# find municipality menu
municip = browser.find_element_by_id('ContentPlaceHolder1_ddlMunicipios')
allmunicip = municip.find_elements_by_tag_name('option') #find possible munic	
allmunicip[1].click() #gives SP as municipality
time.sleep(5)

# find the monthly crime statistics option
monthlydata = browser.find_element_by_id('ContentPlaceHolder1_btnMensal')
monthlydata.click() #chose monthly stats
time.sleep(5)


# get the districts as numeric values so we can plug them in later
districtsrequired = [] 
alldelegations = browser.find_element_by_id('ContentPlaceHolder1_ddlDelegacias').find_elements_by_tag_name('option') #find possible delegations
for i in alldelegations: #make a list of districts
	districtsrequired.append(i.get_attribute('value'))

# iterate through the menu and select each district
for i in districtsrequired:
	delegations = Select(browser.find_element_by_id('ContentPlaceHolder1_ddlDelegacias'))		
	delegations.select_by_value(str(i))
	time.sleep(5)
	browser.find_element_by_id('ContentPlaceHolder1_btnExcel').click() #download the CSV we need!!!


