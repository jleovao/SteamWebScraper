#!/usr/bin/env python
# Filename: steam_specials_web_scrape.py
# Programmer: Joseph Leovao
# Date: March 6, 2018
# Purpose: I was studying python and discovered web scraping.
#          I also like games and like to keep up with trends
#          so I decided to web scrape the current top selling
# 		   games on Steam, that way I can just run this Python
# 		   script to see what's trending.
# 
# Run Program: ./steam_specials_web_scrape.py
# Future ideas: 
# 	- Keep track of more top sellers (just change the link in my_url to p=1
# 	  or p=2 ...). Prompt the user if they would like to look at the next 20 best
# 	  sellers, or just do the top 40 sellers instead of 20.
# 	- Just found out about bundle_base_discount, which are discounts for bundles
# 	  so I need to account for that.

# Import beautiful soup package that is up-to-date
import bs4
# Need a web client to grab something from the internet
from urllib.request import urlopen as uReq
# modularize the import of beautiful soup here
from bs4 import BeautifulSoup as soup

# Ran into unicode problem: ordinal not in range(128)
# This definition just replaces the violations with ""
def removeNonAscii(s): 
	return "".join(filter(lambda x: ord(x)<128, s))

# url to web scrape from
my_url = "http://store.steampowered.com/macos#p=0&tab=TopSellers"

# open web client - opens connection, grabs web page and downloads it
uClient = uReq(my_url)
# Read in the page and store it
page_html = uClient.read()
uClient.close()

# Now we need to parse the html
page_soup = soup(page_html, "html.parser")

# Use findAll to grab each product
containers = page_soup.findAll("div",{"id":"TopSellersRows"})
containers = containers[0].findAll("a",{"class":"tab_item"})

# Open file to write out data
filename = "Steam_top_sellers.csv"
f = open(filename,"w")

# Write the header in the first line of the file
# csv files are deliminated by a newline
headers = "ItemName, Tags, DiscountPercentage, CurrentPrice, OriginalPrice, Link\n"
f.write(headers)

print("\nHere are Steam's top sellers for today:\n")

# Iterate through all containers and grab the information
for container in containers:
	# Retrive name of sale specials
	name_container = container.findAll("div",{"class":"tab_item_name"})
	item_name = name_container[0].text

	# Get the related tags
	tag_container = container.findAll("span",{"class":"top_tag"})
	item_tags = ''
	if len(tag_container) <= 0:
		item_tags = 'None'
	else:
		for tag in tag_container:
			item_tags += tag.text

	# Retrive prices
	price_container = container.findAll("div",{"class":"discount_final_price"})
	item_price = price_container[0].text

	# Get the original price (if available)
	# If original price is available, there should be a discount_pct, so we keep track
	# that as well.
	original_price_container = container.findAll("div",{"class":"discount_original_price"})
	if len(original_price_container) <= 0:
		# If there is no discount, the original price is the same as the current price
		original_price = item_price
		discount_pct = '0%'
		sale = False
	else:
		sale = True
		# Get the original price
		original_price = original_price_container[0].text
		# Since there exists an original price, there must exist
		# a discount percentage as well.
		discount_pct_container = container.findAll("div",{"class":"discount_pct"})
		discount_pct = discount_pct_container[0].text

	# Retrive link
	item_link = container['href']
	
	# Print data - name, tags, discount percent, current price, original price.
	# If there's no discount, no need to print it out
	print("Name: " + item_name)
	print("Tags: " + item_tags)
	if(sale):
		print("Discount percentage: " + discount_pct)
	print("Current Price: " + item_price)
	if(sale):
		print("Original Price: " + original_price)
	print("Link: " + item_link)
	print()
	
	# Notice that some product names contains commas, which is a delimiter in csv files.
	# replace the commas with any other character
	f.write(removeNonAscii(item_name) + "," +
		item_tags.replace(",","|") + "," +
		discount_pct + "," +
		item_price + "," +
		original_price + "," +
		item_link +
		"\n")
f.close()


