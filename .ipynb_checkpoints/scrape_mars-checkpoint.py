{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup \n",
    "import requests\n",
    "from selenium import webdriver\n",
    "\n",
    "import time\n",
    "from time import sleep\n",
    "# from splinter import Browser\n",
    "\n",
    "\n",
    "\n",
    "# from bs4 import BeautifulSoup as bs\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "# from selenium import webdriver\n",
    "# import requests as req\n",
    "import re\n",
    "\n",
    "# from splinter import browser\n",
    "# from selenium import webdriver"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# NASA Mars News\n",
    "# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. \n",
    "# Assign the text to variables that you can reference later.\n",
    "\n",
    "\n",
    "# nasaurl='https://mars.nasa.gov/news/'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# response=requests.get(nasaurl)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# soup=BeautifulSoup(response.text,'html.parser')\n",
    "# soup=BeautifulSoup(response.text,'html')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "# Visit Nasa news url through splinter module\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)\n",
    "sleep(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# print(soup.prettify())\n",
    "# HTML Object\n",
    "html = browser.html\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "# Retrieve the latest element that contains news title and news_paragraph\n",
    "news_title = soup.find('div', class_='content_title').text\n",
    "news_p = soup.find('div', class_='article_teaser_body').text\n",
    "\n",
    "# Display scrapped data \n",
    "print(news_title)\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# JPL Mars Space Images - Featured Image\n",
    "# Visit the url for JPL Featured Space Image here.\n",
    "# Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.\n",
    "# Make sure to find the image url to the full size .jpg image.\n",
    "# Make sure to save a complete url string for this image.\n",
    "\n",
    "\n",
    "# https://splinter.readthedocs.io/en/latest/drivers/chrome.html\n",
    "!which chromedriver"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# browser.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sleep script to ensure the page fully loads\n",
    "sleep(7)\n",
    "\n",
    "# Click on FULL IMAGE\n",
    "browser.click_link_by_partial_text('FULL IMAGE')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "html_image=browser.html\n",
    "soup= BeautifulSoup(browser.html,\"html.parser\")\n",
    "image=soup.find(\"img\",class_=\"fancybox-image\").get(\"src\")\n",
    "print(image)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "browser.url\n",
    "featured_image_url=browser.url+image\n",
    "print(featured_image_url)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# featured_img_url = \"https://www.jpl.nasa.gov\" + image_url\n",
    "\n",
    "# print(featured_img_url)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# https://splinter.readthedocs.io/en/latest/drivers/chrome.html\n",
    "!which chromedriver\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars Weather\n",
    "# Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. \n",
    "# Save the tweet text for the weather report as a variable called mars_weather.\n",
    "# https://splinter.readthedocs.io/en/latest/drivers/chrome.html\n",
    "!which chromedriver\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "url='https://twitter.com/marswxreport?lang=en'\n",
    "browser.visit(url)\n",
    "sleep(7)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tweet=browser.html\n",
    "soup= BeautifulSoup(browser.html,\"html.parser\")\n",
    "pattern = re.compile(r'sol')\n",
    "mars_weather = soup.find('span', text=pattern).text\n",
    "print(mars_weather)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars Facts\n",
    "\n",
    "url='https://space-facts.com/mars/'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tables=pd.read_html(url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "type(tables)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = tables[0]\n",
    "df.columns = ['Description','Values']\n",
    "df.set_index('Description', inplace=True)\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "mars_facts = df.to_html()\n",
    "mars_facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "executable_path = {\"executable_path\": \"chromedriver.exe\"}\n",
    "browser = Browser(\"chrome\", **executable_path, headless=True)\n",
    "url = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "browser.visit(url)\n",
    "\n",
    "html = browser.html\n",
    "bsoup = BeautifulSoup(html, 'html.parser')\n",
    "hemisphere_image_urls = []\n",
    "dict = {}\n",
    "# \n",
    "url='https://astrogeology.usgs.gov'\n",
    "image = bsoup.find_all('a', class_='itemLink product-item')\n",
    "for i in image:\n",
    "    if(i.get_text() != ''):\n",
    "\n",
    "        browser.visit(url + i['href'])    \n",
    "        \n",
    "        html = browser.html\n",
    "        bsoup = BeautifulSoup(html, 'html.parser')\n",
    "        \n",
    "        componentlnk = bsoup.find('div', class_='downloads').find('a')['href']\n",
    "        dict = {'title': i.get_text(),\n",
    "                'img_url' : componentlnk}        \n",
    "\n",
    "        hemisphere_image_urls.append(dict)\n",
    "\n",
    "        \n",
    "        browser.back()\n",
    "hemisphere_image_urls\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
