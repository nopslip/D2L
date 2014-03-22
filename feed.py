#!/usr/bin/env python

import requests
import sys
import codecs
from optparse import OptionParser
from urlparse import urlparse 
import sqlite3 as lite
import sys
import time
import simplejson as json
import hashlib
import datetime
import re 
import os.path




#main yo
def main():
	filename, Mode , noise, footprint, smart, fpok, bad, learn = cmd_options() 

	if filename == None: # then a list was not specfied
		url = get_url() # request user input, return status code		
		begin(url) #research 

	else:# grab the list and get busy
		logfile = filename + "_log"
		f = codecs.open(filename,'r',"utf-8-sig")
		count = 0
		for line in f:
			url = str(line).strip()	
			write_logfile(str(count),url,logfile)
			# url = urlparse(url)
			# url = url.get_url()					
			if url != "": 
				begin(url) #research 
				count = count + 1
		f.close()





def cmd_options():
	parser = OptionParser()
	parser.add_option("-f", dest="filename", help="file name to read url's from", metavar="url_list.txt")
	parser.add_option("-M", dest="mode", help="set the output mode, defualt is stdout, options include ES for ElasticSearch and SQLite for SQLite", default="STDout") 
	parser.add_option("--fpok", action="store_true", help="If we detect an error on our inital (non-malicous) request it's very likely that you will get a false positive for the given URL. by defualt, we will not test URL's with a high FP potential (better if running pyLobster against a large list of URL's). If you would like to test the URL anyway set this switch")
	parser.add_option("-v", action="store_true", help="Show verbose output.")
	parser.add_option("-g", action="store_true", help="Enable footprint mode. Please see manual (non-existant) for additional info on what is needed here and what this feature does.")
	parser.add_option("-l", action="store_true", help="Enable learning mode. If we don't hit regEx error but do get 500 then lets save the HTML for later review.")
	parser.add_option("-s", action="store_true", help="Enable smart mode. This will look at what Headers the webserver is using and test those")
	parser.add_option("--bad", action="store_true", help="Enable Byte Anomaly Detection.")
	(options, args) = parser.parse_args()
	return (options.filename, options.mode, options.v, options.g, options.s, options.fpok, options.bad, options.l)


# Ready Begin
if __name__ == "__main__":
	main()
