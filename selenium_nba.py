from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import string
import pdb
from urllib import urlopen
import re

def main():
	letters = list(string.ascii_lowercase)
	full_urls = get_full_urls(letters)

	# driver = webdriver.Firefox()
	# for url in full_urls:
	# 	driver.get(url)

	print(full_urls)

def get_full_urls(letters):
	top_url_list = []
	for letter in letters:
		top_url_list.append("http://www.basketball-reference.com/players/%s" % letter)


	player_files = []
	for i in top_url_list:
		result = re.findall("\/([a-z]+[0-9][0-9]\W[a-z]+)", str(urlopen(i).read()))
		player_files.extend(result) 
	
	full_urls = []
	base_url = "http://www.basketball-reference.com/players"
	for item in player_files:
		full_urls.append("%s/%s/%s" % (base_url, item[0], item))


	return full_urls


if __name__ == '__main__':
	main()


