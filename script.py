import json
import MySQLdb
from string import ascii_lowercase as letters
from urllib2 import urlopen

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


site = list("http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=10&callback=jQuery1110039665828784927726_1453392246657&q=*%3A*+AND+schoolid_s%3A1426+AND+teacherlastname_engram%3Aa&defType=edismax&qf=teacherfullname_t%5E1000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=&siteName=rmp&rows=100&start=0&fl=pk_id+teacherfirstname_t+teacherlastname_t+total_number_of_ratings_i+averageratingscore_rf+schoolid_s")


'''
for char in letters:
	site[186] = char
	data = urlopen("".join(site)).read()
	results = data[43:-2] #remove leading and trailing non json data
	parsed_json = json.loads(results)
	break
'''
for char in letters:
	site[186] = char
	data = urlopen("".join(site)).read()
	results = data[43:-2] #remove leading and trailing non json data
	parsed_json = json.loads(results)
	prof_data = parsed_json["response"]["docs"][0]
	statement = "INSERT INTO profDetails (LastName, FirstInitial, LinkID) VALUES ('%s', '%c', '%d');" % (prof_data["teacherlastname_t"], prof_data["teacherfirstname_t"][:1], prof_data["pk_id"])
	x.execute(statement)
	conn.commit()
	break
	

'''try:
	for char in letters:
		site[186] = char
		data = urlopen("".join(site)).read()
		results = data[43:-2] #remove leading and trailing non json data
		parsed_json = json.loads(results)
		prof_data = parsed_json["response"]["docs"][0]
		statement = "INSERT INTO profDetails VALUES (%s, %c, %d)" % (prof_data["teacherlastname_t"], prof_data["teacherfirstname_t"][:1], prof_data["pk_id"])
		x.execute(statement)
		conn.commit()
		break

except:
	conn.rollback()
	conn.close()
	print "There was an error inserting into the database"
	exit()
'''
conn.close()