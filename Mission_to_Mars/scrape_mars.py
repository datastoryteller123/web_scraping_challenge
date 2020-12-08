import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests



def init_browser():
    # Path to the ChromeDriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

mars_mongo = {}

def scrape_mars_news():
        # Visit https://mars.nasa.gov/news/
        browser = init_browser()
        url = "https://mars.nasa.gov/news/"
        browser.visit(url)

        # Scrape page into Soup
        html = browser.html
        soup = bs(html, "html.parser")
        news_soup = soup.select_one('ul.item_list  li.slide')
            
        # Scraping the latest News Title and Paragraph Text
        news_title = news_soup.find('div', class_='content_title').find('a').text
        paragraph_text = news_soup.find('div', class_='article_teaser_body').text
            
        # Print the News Title and Paragraph Text
        print(news_title)
        print(paragraph_text)

        return mars_mongo

        browser.quit()

def scrape_mars_featured():
        # Visit https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
        browser = init_browser()
        featured_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(featured_url)

        # Scrape page into Soup
        featured_html = browser.html
        featured_soup = bs(featured_html, "html.parser")

        base_url = 'https://www.jpl.nasa.gov/'
        featured_image_url = base_url + featured_soup.find('a', class_= 'fancybox')['data-fancybox-href']
        featured_image_url

        return mars_mongo

        browser.quit()

def scrape_mars_facts():

    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    mars_facts_df = tables[2]
    mars_facts_df.columns = ['Description', 'Value']
    mars_facts_df
    mars_facts_html = mars_facts_df.to_html()
    mars_facts_html.replace('\n','')
    mars_mongo['mars_facts_df'] = mars_facts_html

    return mars_mongo

def scrape_mars_hemisphere():
        browser = init_browser()
        # Visit https://astrogeology.usgs.gov/
        usgs_url = 'https://astrogeology.usgs.gov/'
        hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemis_url)

        # Scrape page into Soup
        hemis_html = browser.html
        hemis_soup = bs(hemis_html, "html.parser")

        # Retrieve all of the Hemispheres Information
        hemis = hemis_soup.find_all('div', class_='item')
        hemis
        
        hemis_image_url = []

        for a in hemis:

            title = a.find('h3').text
            
            img_url = a.find('a', class_='itemLink product-item')['href']
            
            browser.visit(usgs_url + img_url)
            
            partial_image_html = browser.html
                    
            img_soup = bs(partial_image_html, 'html.parser')
                            
            partial_image_url = usgs_url + img_soup.find('img', class_='wide-image')['src']
            
            hemis_image_url.append({'title': title, 
                                    'img_url':partial_image_url})

        mars_mongo['hemis_image_url'] = hemis_image_url

        return mars_mongo

        browser.quit()



    

