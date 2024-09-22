#!/usr/bin/env python
# coding: utf-8

# # WEB SCRAPING – ASSIGNMENT 2

# ## 1. All the questions must be done in a single Jupyternotebook. 

# ### Q1: In this question you have to scrape data using the filters available on the webpage You have to use the location and salary filter. 

# In[1]:


get_ipython().system('pip install selenium')


# In[30]:


import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import warnings
warnings.filterwarnings('ignore')


# In[3]:


driver = webdriver.Chrome()


# In[4]:


driver.get("https://www.naukri.com/")


# In[5]:


designation = driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Analyst')


# In[6]:


location = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
location.send_keys('Delhi/NCR')


# In[7]:


search = driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[8]:


salary_range = driver.find_element(By.XPATH,'//span [@class="styles_ellipsis__cvWP1 styles_filterLabel__jRP04"]')
salary_range.click()


# In[ ]:


job_title =[]
job_location = []
company_name = []
experience_required = []


# In[ ]:


title_tags = driver.find_elements(By.XPATH,'//div[@class="cust-job-tuple layout-wrapper lay-2 sjw__tuple "]/div/a')[:10]
for i in title_tags:
    title = i.text
    job_title.append(title)
    
location_tags = driver.find_elements(By.XPATH,'//span[@class="locWdth"]')[:10]    
for i in location_tags:
    location = i.text
    job_location.append(location)
    
company_tags = driver.find_elements(By.XPATH,'//a [@class=" comp-name mw-25"] ')[:10]   
for i in company_tags:
    company = i.text
    company_name.append(company)
    
experience_tags = driver.find_elements(By.XPATH,'//SPAN[@class="expwdth"]')[:10]   
for i in experience_tags:
    experience = i.text
    experience_required.append(experience)


# In[ ]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[ ]:


df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name,'Experience':experience_required})
df


# ### Q2: Write a python program to scrape data for “Data Scientist” Job position in “Bangalore” location. You have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10 jobs data

# In[ ]:


driver = webdriver.Chrome()


# In[ ]:


driver.get("https://www.shine.com/")


# In[ ]:


designation = driver.find_element(By.XPATH,'//*[@id="id_q"]')
designation.send_keys('Data Analyst')


# In[ ]:


location= driver.find_element(By.XPATH,'//div [@id="select_container_id_loc"] /input')
location.send_keys('Bangalore')


# In[ ]:


search = driver.find_element(By.XPATH,'//div [@class="searchForm_btnWrap_advance__VYBHN"]')
search.click()


# In[ ]:


job_title = []
job_location = []
company_name = []
experience_required = []


# In[ ]:


title_tags = driver.find_elements(By.XPATH,'//strong [@class="jobCard_pReplaceH2__xWmHg"] ')[:10]
for i in title_tags:
    title = i.text
    job_title.append(title)
    
location_tags = driver.find_elements(By.XPATH,'//div [@class="jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')[:10]    
for i in location_tags:
    location = i.text
    job_location.append(location)
    
company_tags = driver.find_elements(By.XPATH,'//div [@class="jobCard_jobCard_cName__mYnow"]')[:10]  
for i in company_tags:
    company = i.text
    company_name.append(company)
    
experience_tags = driver.find_elements(By.XPATH,'//div [@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')[:10]   
for i in experience_tags:
    experience = i.text
    experience_required.append(experience) 


# In[ ]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[ ]:


import pandas as pd
df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company':company_name,'Experience':experience_required})
df


# ### Q3: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:
# https://www.flipkart.com/apple-iphone-11-black-64-gb/productreviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=F
# LIPKART

# In[ ]:


driver = webdriver.Chrome()


# In[ ]:


driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/product-reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&marketplace=FLIPKART")


# In[ ]:


product_ratings = []
review_summaries =[]
full_reviews =[]


# In[ ]:


start = 0
end = 10
for page in range(start,end):

    product_rating_lists = driver.find_elements(By.XPATH,'//div [@class="XQDdHH Ga3i8K"]')
    for product_rating in product_rating_lists:
        rating = product_rating.text
        product_ratings.append(rating)
        
    review_summary_elements = driver.find_elements(By.XPATH,'//p [@class="z9E0IG"]')
    for review_summary in review_summary_elements:
        summary_text = review_summary.text
        review_summaries.append(summary_text)  
        
    full_review_elements = driver.find_elements(By.XPATH,'//div [@class="ZmyHeo"]')
    for full_review_element in full_review_elements:
        review_text = full_review_element.text
        full_reviews.append(review_text)
    
next_button = driver.find_element(By.XPATH,'//a [@class="_9QVEpD" ]')
next_button.click()
time.sleep(3)   


# In[ ]:


print(len(product_ratings),len(review_summaries),len(full_reviews))


# In[ ]:


df=pd.DataFrame({'Rating':product_ratings,'Review Summary':review_summaries,'Full Review':full_reviews})
df


# ### Q4: Scrape data forfirst 100 sneakers you find whenyouvisitflipkart.com and search for “sneakers” inthe search
# field.

# In[ ]:


driver = webdriver.Chrome()


# In[ ]:


driver.get("https://www.flipkart.com/")


# In[ ]:


product_detail = driver.find_element(By.CLASS_NAME,"Pke_EE")
product_detail.send_keys('Sneakers')


# In[ ]:


search = driver.find_element(By.CLASS_NAME,"_2iLD__"  )
search.click()


# In[ ]:


product_brands =[]
product_descriptions =[]
product_prices=[]


# In[ ]:


while len(product_brands) < 100:
    product_brand_lists = driver.find_elements(By.XPATH,'//div [@class="syl9yP"]')
    for product_brand in product_brand_lists:
        if len(product_brands) >= 100:
            break
        brand = product_brand.text
        product_brands.append(brand)
        
    product_description_lists = driver.find_elements(By.XPATH,'//a [@class="WKTcLC"]')
    for product_description in product_description_lists:
        if len(product_descriptions) >= 100:
            break
        description = product_description.text
        product_descriptions.append(description)
        
    product_price_lists = driver.find_elements(By.XPATH,'//div [@class="Nx9bqj"]')
    for product_price in product_price_lists:
        if len(product_prices) >= 100:
            break
        price = product_price.text
        product_prices.append(price)
        
    if len(product_descriptions) == 100:      
        next_button = driver.find_element(By.XPATH,'//a [@class="_9QVEpD"]')
        next_button.click()
        time.sleep(3)  


# In[ ]:


print(len(product_brands),len(product_descriptions),len(product_prices))


# In[ ]:


import pandas as pd
df=pd.DataFrame({'Brand':product_brands,'Description':product_descriptions,'Price':product_prices})
df


# ### Q5: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then set CPU Type filter to “Intel Core i7” as shown in the below image:

# In[ ]:


import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import warnings
warnings.filterwarnings('ignore')


# In[ ]:


driver = webdriver.Chrome()


# In[ ]:


driver.get("https://www.amazon.in/")


# In[ ]:


product = driver.find_element(By.ID, "twotabsearchtextbox")
product.send_keys('Laptop')


# In[ ]:


search = driver.find_element(By.ID,"nav-search-submit-button")
search.click()


# In[ ]:


filter_product = driver.find_element(By.XPATH,'//*[@id="p_n_feature_thirteen_browse-bin/12598163031"]/span/a/div/label/i') 
filter_product.click()


# In[ ]:


product_title =[]
product_rating =[]
product_price =[]


# In[ ]:


title_tag = driver.find_elements(By.XPATH,'//div [@class="a-section a-spacing-none puis-padding-right-small s-title-instructions-style"]')[:10]
for i in title_tag:
    title = i.text
    product_title.append(title)
    
product_rating_list = driver.find_elements(By.XPATH,'//i [@class="a-icon a-icon-star-small a-star-small-4 aok-align-bottom"]')[:10]
for i in product_rating_list:
    rating = i.text
    product_rating.append(rating)  
    
product_price_list = driver.find_elements(By.XPATH,'//span [@class="a-price-whole"]')[:10]
for i in product_price_list:
    price = i.text
    product_price.append(price)


# In[ ]:


print(len(product_title),len(product_rating),len(product_price))


# In[ ]:


import pandas as pd
df=pd.DataFrame({'Title':product_title,'Rating':product_rating,'Price':product_price})
df


# ### Q6: Write a python program to scrape data for Top 1000 Quotes of All Time.

# In[9]:


driver = webdriver.Chrome()


# In[10]:


driver.get("https://www.azquotes.com/")


# In[11]:


quote = driver.find_element(By.XPATH,'//*[@id="menu"]/div/div[3]/ul/li[5]/a')
quote.click()


# In[12]:


quotes =[]
authors =[]
quotes_type=[]


# In[13]:


start = 0
end = 10
for page in range(start,end):

    top_quotes = driver.find_elements(By.XPATH,'//a [@class="title"] ')[:1000]
    for i in top_quotes:
        quote = i.text
        quotes.append(quote)
        
    authors_list = driver.find_elements(By.XPATH,'//div [@class="author"]')[:1000]  
    for i in authors_list:
        author = i.text
        authors.append(author)
        
    type_of_quotes = driver.find_elements(By.XPATH,'//div [@class="tags"]') [:1000] 
    for i in type_of_quotes:
        quote_type = i.text
        quotes_type.append(quote_type)
        
next_button = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/div/div[3]/li[12]/a')
next_button.click()
time.sleep(3)


# In[14]:


print(len(quotes),len(authors),len(quotes_type))


# In[15]:


df=pd.DataFrame({'Quote':quotes,'Author':authors,'Type':quotes_type})
df


# ### Q7: Write a python program to display list of respected former Prime Ministers of India (i.e. Name,Born-Dead, Term of office, Remarks)
# 

# In[22]:


pip install requests beautifulsoup4 pandas


# In[23]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[24]:


url = 'https://www.jagranjosh.com/general-knowledge/list-of-all-prime-ministers-of-india-1473165149-1'
response = requests.get(url)


# In[25]:


soup = BeautifulSoup(response.text, 'html.parser')


# In[26]:


table = soup.find('table')
rows = table.find_all('tr')[1:]  # Skip the header row


# In[27]:


pm_data = []

for row in rows:
    cols = row.find_all('td')
    name = cols[0].text.strip()
    born_dead = cols[1].text.strip()
    term_of_office = cols[2].text.strip()
    remarks = cols[3].text.strip()

    pm_data.append({
        'Name': name,
        'Born-Dead': born_dead,
        'Term of Office': term_of_office,
        'Remarks': remarks
    })


# In[29]:


df = pd.DataFrame(pm_data)
print(df)


# ### Q8: Write a python program to display list of 50 Most expensive cars in the world (i.e. Car name and Price) from https://www.motor1.com/

# In[31]:


import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import warnings
warnings.filterwarnings('ignore')


# In[32]:


driver = webdriver.Chrome()


# In[33]:


driver.get("https://www.motor1.com/")


# In[34]:


search = driver.find_element(By.XPATH,'//*[@id="search_input"]')
search.send_keys('50 most expensive cars')


# In[35]:


search_button = driver.find_element(By.XPATH,'//*[@id="header_search_form"]/button[1]')
search_button.click()


# In[36]:


click_content = driver.find_element(By.XPATH,'//*[@id="page_index_articles_search"]/div[9]/div/div[1]/div/div/div[1]/div/div[1]/h3/a')
click_content.click()


# In[37]:


car_name = []
car_price = []


# In[38]:


names_of_car = driver.find_elements(By.XPATH,'//* [@class="subheader"]')[:50]
for i in names_of_car:
    car = i.text
    car_name.append(car)
    
price_of_car = driver.find_elements(By.XPATH,'//p/strong')[:50]  
for i in price_of_car:
    price = i.text
    car_price.append(price)


# In[39]:


print(len(car_name),len(car_price))


# In[40]:


import pandas as pd
df=pd.DataFrame({'Car_Name':car_name,'Car_Price':car_price})
df


# In[ ]:




