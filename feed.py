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


def write_log(logfile):
	f = open(str(logfile),'a')
	#f.writelines(count + "  " + url+ '\n')
	f.writelines('yah!' + '\n')
	f.close() 

#main yo
def main():
	# filename, Mode , noise, footprint, smart, fpok, bad, learn = cmd_options() 

	
	#load URL's, move to seperate def soon
	exc = {}
	#Exchange Name, URL
	exc[0] = {"test1",""}
	exc[1] = {"test2"," "}
	exc[2] = {"test3",""}
	
	
	for i in exc:
		logfile = str(i[1]) + "_log"
		write_log(logfile)
		# exc[i] =  		
		# begin(url) #research 


/* 
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
*/


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


# Ready Begin
if __name__ == "__main__":
	main()
