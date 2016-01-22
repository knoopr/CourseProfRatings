import json
import MySQLdb
import string.ascii_lowercase as letters
import urllib2.urlopen as request

site = "http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=10&callback=jQuery1110039665828784927726_1453392246657&q=*%3A*+AND+schoolid_s%3A1426+AND+teacherlastname_engram%3Aa&defType=edismax&qf=teacherfullname_t%5E1000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=&siteName=rmp&rows=100&start=0&fl=pk_id+teacherfirstname_t+teacherlastname_t+total_number_of_ratings_i+averageratingscore_rf+schoolid_s

for char in letters:
	site[186] = char
	