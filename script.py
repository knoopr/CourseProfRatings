#coding=utf-8

import json
import MySQLdb
import time
from random import randint as random
from string import ascii_lowercase as letters
from urllib2 import urlopen
from bs4 import BeautifulSoup

try:
	file = open('/var/www/html/knoop/CourseProfRatings/dbCredentials').read()
	credentials = eval(file)
except ImportError:
	print "Error loading credentials"
	exit();


conn = MySQLdb.connect(host = "localhost",
					user = credentials['username'],
					passwd = credentials['password'],
					db = "profRATINGS")
					
x = conn.cursor()


site = list("http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=10&callback=jQuery1110039665828784927726_1453392246657&q=*%3A*+AND+schoolid_s%3A1426+AND+teacherlastname_engram%3Aa&defType=edismax&qf=teacherfullname_t%5E1000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=&siteName=rmp&rows=200&start=0&fl=pk_id+teacherfirstname_t+teacherlastname_t+total_number_of_ratings_i")


pk_id = 0
curLetter = 'a'
try:
	for char in letters:
		curLetter = char
		site[185] = char
		data = urlopen("".join(site)).read()
		results = data[43:-2] #remove leading and trailing non json data
		parsed_json = json.loads(results)
		for prof in parsed_json["response"]["docs"]:
			pk_id = prof["pk_id"]
			try:
				if prof["total_number_of_ratings_i"] != 0:
					wait = random(1,25)
					time.sleep(wait)
					ratingSite = "http://www.ratemyprofessors.com/ShowRatings.jsp?tid=%s" %prof["pk_id"]
					html_Doc = urlopen(ratingSite);
					soup = BeautifulSoup(html_Doc, 'html.parser')
					if soup.find(class_="headline") == None:
						ratings = []
						for div in soup.find(class_="faux-slides").find_all(class_="rating"):
							ratings.append(div.string)
						statement = "INSERT INTO profDetails VALUES ('%d', '%s', '%s', '%s', '%s', '%s');" % (prof["pk_id"], prof["teacherlastname_t"], prof["teacherfirstname_t"], ratings[0], ratings[1], ratings[2])
						x.execute(statement)
						conn.commit()
				else:
					statement = "INSERT INTO profDetails VALUES ('%d', '%s', '%s', NULL, NULL, NULL);" % (prof["pk_id"], prof["teacherlastname_t"], prof["teacherfirstname_t"])
					x.execute(statement)
					conn.commit()
			except:
				print "Error was caused by SQL statement: " + statement
except:
	conn.rollback()
	conn.close()
	print "There was a fatal error on prof with pk_id: %d" %pk_id
	print "The current letter is: %c" %curLetter
	exit()

conn.close()
