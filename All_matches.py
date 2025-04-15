from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

# Topics: Locate a button, select element within dropdown and extract data from a table

# define the website to scrape and path where the chromediver is located
website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = 'write the path of Chrom driver here'


driver = webdriver.Chrome(path)

# open Google Chrome with chromedriver
driver.get(website)

# locate a button
all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')

# click on a button
all_matches_button.click()

matches = driver.find_elements_by_tag_name('tr')

date = []
home_team = []
score = []
away_team = []

for match in matches:

    date.append(match.find_elements_by_xpath('./td[1]').text)
    home_team.append(match.find_elements_by_xpath('./td[2]').text)
    score.append(match.find_elements_by_xpath('./td[3]').text)
    away_team.append(match.find_elements_by_xpath('./td[4]').text)


#quit drive we opened in the beginning
driver.quit()

# Bonus: Create Dataframe in Pandas and export to CSV (Excel)
df = pd.DataFrame({'date':date, 'home_team':home_team, 'score':score, 'away_team':away_team})
df.to_csv('Football_data.csv', index=False)