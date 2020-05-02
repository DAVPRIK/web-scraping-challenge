from splinter import Browser
from bs4 import BeautifulSoup 
import requests
from selenium import webdriver
import time
from time import sleep
import pandas as pd
import numpy as np
import re

# Initialize browser
def init_browser(): 
    # Replace the path with your actual path to the chromedriver

    #Windows Users
    # executable_path = {'executable_path': 'chromedriver.exe'}
    # return Browser('chrome', **executable_path, headless=False)
    exec_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', headless=True, **exec_path)

   # Create Mission to Mars global dictionary that can be imported into Mongo
mars_info = {}

# NASA MARS NEWS
def scrape_mars_news():
    try: 

        # Initialize browser 
        browser = init_browser()

        #browser.is_element_present_by_css("div.content_title", wait_time=1)

        # Visit Nasa news url through splinter module
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)
        sleep(5)
        html = browser.html
# Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

# Retrieve the latest element that contains news title and news_paragraph
    

        # Dictionary entry from MARS NEWS
        mars_info['news_title'] = news_title
        mars_info['news_paragraph'] = news_p

        return mars_info

    finally:

        browser.quit()


# JPL Mars Space Images - Featured Image
    
def scrape_mars_image():

    try: 

        # Initialize browser 
        browser = init_browser()
        url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(url)  
    # Sleep script to ensure the page fully loads
        sleep(7)

    # Click on FULL IMAGE
        browser.click_link_by_partial_text('FULL IMAGE')
        html_image=browser.html
        soup= BeautifulSoup(browser.html,"html.parser")
        image=soup.find("img",class_="fancybox-image").get("src")
    # print(image)
        browser.url
        featured_image_url=browser.url+image
        

    # Dictionary entry from FEATURED IMAGE
        mars_info['featured_image_url'] = featured_image_url 
        
        return mars_info
    finally:

        browser.quit()

  




    # url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    # browser.visit(url)  
    # # Sleep script to ensure the page fully loads
    # sleep(7)

    # # Click on FULL IMAGE
    # browser.click_link_by_partial_text('FULL IMAGE')
    # html_image=browser.html
    # soup= BeautifulSoup(browser.html,"html.parser")
    # image=soup.find("img",class_="fancybox-image").get("src")
    # # print(image)
    # browser.url
    # mars["featured_image_url"]=browser.url+image
    # print(featured_image_url)

# Mars Weather
def scrape_mars_weather():

    try: 

        # Initialize browser 
        browser = init_browser()
    
        url='https://twitter.com/marswxreport?lang=en'
        browser.visit(url)
        sleep(7)
        tweet=browser.html
        soup= BeautifulSoup(browser.html,"html.parser")
        pattern = re.compile(r'sol')
        mars_weather = soup.find('span', text=pattern).text
    # Dictionary entry from WEATHER TWEET
        mars_info['mars_weather'] = mars_weather
        
        return mars_info
    finally:

        browser.quit()



# Mars Facts
def scrape_mars_facts():

    url='https://space-facts.com/mars/'
    tables=pd.read_html(url)
    df = tables[0]
    df.columns = ['Description','Values']
    df.set_index('Description', inplace=True)
    df.head()
    mars_facts = df.to_html()
    mars_info['mars_facts']=mars_facts
    return mars_info


# Mars Hemispheres
def scrape_mars_hemispheres():

    try: 

        # Initialize browser 
        browser = init_browser()
   
        url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(url)

        html = browser.html
        bsoup = BeautifulSoup(html, 'html.parser')
        hemisphere_image_urls = []
        dict = {}
# 
        url='https://astrogeology.usgs.gov'
        image = bsoup.find_all('a', class_='itemLink product-item')
        for i in image:
            if(i.get_text() != ''):

                browser.visit(url + i['href'])    
        
                html = browser.html
                bsoup = BeautifulSoup(html, 'html.parser')
        
                componentlnk = bsoup.find('div', class_='downloads').find('a')['href']
                dict = {'title': i.get_text(),
                'img_url' : componentlnk}        

                hemisphere_image_urls.append(dict)


                browser.back()
        mars_info["hemisphere_image_urls"]=hemisphere_image_urls
        return mars_info 
    finally:

        browser.quit()    


# def scrape_all():
#     return_json = [{
#         "weather_data": scrape_mars_weather(),
#         "mars_facts": scrape_mars_facts()
#     }]
#     return jsonify(return_json)
    
# mars_data = {"news_title": news_title,"news_p": news_p,"featured_image_url": featured_image_url,"table" : dictionary,"hemisphere_image_urls" : hemisphere_image_urls,"Weather" : mars_weather}

