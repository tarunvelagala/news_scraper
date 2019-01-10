from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# grab the url as the first command line argument
from selenium.webdriver.chrome.options import Options

url = 'https://www.cnet.com'
url_parse_obj = urlparse(url)
page = requests.get(url)
url_rel = url_parse_obj.scheme + '://' + url_parse_obj.netloc
# create a Chrome browser
options = Options()
opt_args = ['--headless', '--disable-gpu', 'start-maximized', 'disable-infobars',
            "--disable-extensions", "--enable-javascript", '--window-size=1420,1080']
for i in opt_args:
    options.add_argument(i)
driver = webdriver.Chrome('utilities/chromedriver.exe', chrome_options=options)

# open the url from the command line
driver.get(url)

# Selenium hands the page source to Beautiful Soup
soup_obj = BeautifulSoup(driver.page_source, 'lxml')

# wait for the comments to load
"""while True:
    # if comments load, then break out of the while loop
    try:
        driver.find_element_by_class_name("latestScrollItems")
        break
    # otherwise, sleep for three seconds and try again
    except:
        time.sleep(2)
        continue"""

lst_items = soup_obj.find("div", {"class": "latestScrollItems"})
# print(lst_items)

time = lst_items.find_all("span", {'class': 'col-1'})[0:6]

# headline_div = lst_items.find_all('div', {'class': 'col-4'})
# print(headline_div)

headline = lst_items.find_all('h3')[0:6]
# print(headline

headline_links = [i.a['href'] for i in headline]
# print(headline_links)

paragraph = lst_items.find_all('p')[0:6]
# print(paragraph)
# img = lst_items.find_all('img')[0:6]
# print(img)

# filter the outputs
time_filtered = [i.span.text for i in time]
headline_filtered = [i.text for i in headline]
# paragraph_filtered = [p.text for p in paragraph]
headline_links_filtered = [url_rel + i for i in headline_links]

contents_list = list(zip(time_filtered, headline_filtered))
# print(contents_list)
"""
print('-' * 80)
print('\n'.join(time_filtered))
print('-' * 80)
print('\n'.join(headline_filtered))
print('-' * 80)
print('\n'.join(paragraph_filtered))
print('-' * 80)
print('\n'.join(headline_links_filtered))"""

"""for link in headline_links_filtered:
    driver.get(link)
    next_page = soup_obj.find("div", {'class': 'col-10 articleHead'})
    topic = next_page.find_all('a', {'class': 'bc-2'})
    heading_n = next_page.find('h1', {'class': 'speakableText'})
    paragraph_n = next_page.find('p', {'class': 'article-dek col-8'})
    author_details = next_page.find('div', {'class': 'profileInfo'})
    print(author_details)
    driver.back()"""
