#!/usr/bin/env python
# coding: utf-8

# In[44]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# 1) Write a python program to display IMDB’s Top rated 100 Indian movies’ data
# https://www.imdb.com/list/ls056092300/ (i.e. name, rating, year ofrelease) and make data frame

# In[45]:


url = 'https://www.imdb.com/list/ls056092300/'

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

names = []
ratings = []
years = []

for item in soup.find_all('div', class_='lister-item mode-detail'):

    name = item.find('h3', class_='lister-item-header').find('a').text.strip()
    
    rating = item.find('span', class_='ipl-rating-star__rating').text.strip()

    year = item.find('span', class_='lister-item-year').text.strip().strip('()')
    
    names.append(name)
    ratings.append(rating)
    years.append(year)

movies_df = pd.DataFrame({
    'Name': names,
    'Rating': ratings,
    'Year': years
})

print(movies_df)


# 2) Write a python program to scrape details of all the posts from https://www.patreon.com/coreyms .Scrape the
# heading, date, content and the likes for the video from the link for the youtube video from the post.

# In[36]:


url = "https://www.patreon.com/coreyms"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

posts = soup.find_all('div', class_='post')

for post in posts:
    heading_element = post.find('h3', class_='post__title')
    heading = heading_element.text.strip() if heading_element else "No heading found"
    
    date_element = post.find('time', class_='datetime')
    date = date_element.text.strip() if date_element else "No date found"

    content_element = post.find('div', class_='Post_Content')
    content = content_element.text.strip() if content_element else "No content found"

    youtube_link_element = post.find('a', class_='post__youtube-link')
    youtube_link = youtube_link_element['href'] if youtube_link_element else "No YouTube link found"

    likes_element = post.find('span', class_='post__likes')
    likes = likes_element.text.strip() if likes_element else "No likes found"

    print("Heading:", heading)
    print("Date:", date)
    print("Content:", content)
    print("YouTube Link:", youtube_link)
    print("Likes:", likes)
    print()


# 3) Write a python program to scrape house details from mentioned URL. It should include house title, location,
# area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar,
# Rajaji Nagar.

# In[43]:


localities = ["Indira Nagar", "Jayanagar", "Rajaji Nagar"]

for locality in localities:
    url = f"https://www.nobroker.in/property/sale/bangalore/{locality.lower().replace(' ', '-')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    print(f"Scraping houses in {locality}...\n")

    houses = soup.find_all('div', class_='card')
    
    for house in houses:
        title_element = house.find('h2', class_='heading-6')
        title = title_element.text.strip() if title_element else "No title found"

        location_element = house.find('h1', class_='text-16')
        location = location_element.text.strip() if location_element else "No location found"

        area_element = house.find('p', class_='text-left pl-1.5p ab:p-0 tab:text-12 tab:mt-0.5p tab:mb-0 tab:pl-0') 
        area = area_element.text.strip() if area_element else "No area found"

        emi_element = house.find('div', class_='font-semi-bold')
        emi = emi_element.text.strip() if emi_element else "No EMI found"

        price_element = house.find('span', class_='text-18 font-bold')
        price = price_element.text.strip() if price_element else "No price found"

        print("Title:", title)
        print("Location:", location)
        print("Area:", area)
        print("EMI:", emi)
        print("Price:", price)
        print()
    
    print("="*50)


# 4) Write a python program to scrape first 10 product details which include product name , price , Image URL from
# https://www.bewakoof.com/bestseller?sort=popular .

# In[39]:


url = "https://www.bewakoof.com/bestseller?sort=popular"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

products = soup.find_all('div', class_='categoryWrapper')[:10]

for product in products:
    # Product Name
    name_element = product.find('h1', class_='ProductName')
    name = name_element.text.strip() if name_element else "No name found"
    
    # Product Price
    price_element = product.find('div', class_='discountedPriceText clr-p-black   false')
    price = price_element.text.strip() if price_element else "No price found"
    
    # Image URL
    image_element = product.find('div',class_='productImg')
    if image_element and 'data-src' in image_element.attrs:
        image_url = image_element['data-src']
    else:
        image_url = "No image URL found"

    print(f"Product Name: {name}")
    print(f"Price: {price}")
    print(f"Image URL: {image_url}\n")


# 5) Please visit https://www.cnbc.com/world/?region=world and scrap-
#  a) headings
# b) date
# c) News link

# In[ ]:


url = "https://www.cnbc.com/world/?region=world"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('div', class_='Card-titleContainer')  

for article in articles:
    heading_element = article.find('a', class_='Card-title')
    if heading_element:
        heading = heading_element.text.strip()
    else:
        heading = "No heading found"

    date_element = article.find('time', class_='Card-time')  
    if date_element:
        date = date_element.text.strip()
    else:
        date = "No date found"

    link_element = article.find('a', href=True)
    if link_element:
        news_link = link_element['href']
    else:
        news_link = "No link found"

    print(f"Heading: {heading}")
    print(f"Date: {date}")
    print(f"News Link: {news_link}\n")


# 6) Please visit https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloadedarticles/ and scrapa) Paper title
#  b) date
# c) Author

# In[29]:


url = "https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

articles = soup.find_all('div', class_='article-listing')

for article in articles:
    title_element = article.find('h2', class_='h5 article-title')
    title = title_element.text.strip() if title_element else "No title found"

    date_element = article.find('p', class_= 'article-date')
    date = date_element.text.strip() if date_element else "No date found"

    author_element = article.find('p', class_='article-authors')
    author = author_element.text.strip() if author_element else "No author found"

    print(f"Paper Title: {title}")
    print(f"Date: {date}")
    print(f"Author: {author}\n")

