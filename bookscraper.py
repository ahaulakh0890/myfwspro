import requests
from bs4 import BeautifulSoup
import csv
import os

response = requests.get(url = 'http://books.toscrape.com/')

page_source = response.content

soup = BeautifulSoup(page_source, 'html.parser')

headings = soup.find_all('h3')

price_tags = soup.find_all('p', class_='price_color')
complete_data = []
for each_heading, each_price in zip(headings, price_tags):

    book_name = each_heading.get_text()

    each_link = each_heading.find('a') 

    book_link = 'http://books.toscrape.com/' + each_link.get('href')
    book_price = each_price.get_text()
    complete_data.append({ 'book_name' : book_name, 'book_link' : book_link, 'book_price' : book_price })

csv_file = 'scraped_books.csv'
fieldNames = ['book_name', 'book_link', 'book_price']
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
    writer.writeheader()
    writer.writerows(complete_data)
print(f"Data has been written in to {csv_file}")   

# os.remove('scraped_books.csv')


