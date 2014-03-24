#!/usr/bin/env python
 
import requests
import sys
import codecs
from optparse import OptionParser
from urlparse import urlparse
import sys
import time
import datetime
import re
import os.path
 
# import hashlib
# import simplejson as json
 
def write_log(logfile, html, exn):
        ensure_dir(logfile)    
        f = open(str(logfile),'a')
        now = datetime.datetime.now()
        f.writelines(str(now) + "|" + exn + "|" + html + '\n')
        f.close()
 
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
 
def load_URIs():
        exc = {}        
        exc[0] = {'Exchange' : 'BTC-E', 'URL' : 'https://btc-e.com/api/2/btc_usd/ticker'}
        exc[1] = {'Exchange' : 'Bitstamp', 'URL' : 'https://bitstamp.net/api/ticker/'}
        # exc[2] = {'Exchange' : 'BTCChina', 'URL' : 'https://vip.bitchina.com/bc/ticker'}      
        exc[3] = {'Exchange' : 'BTCtrade', 'URL' : 'http://www.btctrade.com/api/ticker'}
        exc[4] = {'Exchange' : 'BTER', 'URL' : 'http://data.bter.com/api/1/ticker/btc_cny'}    
        # exc[5] = {'Exchange' : 'Huboi', 'URL' : 'http://www.huobi.com/help/index.php?a=market_help#con_1'}
        return(exc)
       
#main yo
def main():
        # filename, Mode , noise, footprint, smart, fpok, bad, learn = cmd_options()
        freq = cmd_options()
        exc = load_URIs()              
        while True:
                #Here is where we go out and pull back the data for each Excahnge/Tracker
                #you will need to add your oun API URL's for now
                               
                for i in exc:
                        try:
                                r = requests.get(exc[i]['URL'])
                        except:      
                                print 'Failed on exchange ' + exc[i]['Exchange']                       
                                         
                        html = r.text
                        name = exc[i]['Exchange']
                        #insert reGex processing module is necessary
                        logfile = ("./log/" + name + "_log")
                        write_log(logfile, html, name)      
 
                #sleep                        
                time.sleep(float(freq))
                 
                           
 
def cmd_options():
        parser = OptionParser()
        parser.add_option("-f", dest="freq", help="-f is for GET frequency in seconds. Defualt is 15 seconds ", default="15")
        (options, args) = parser.parse_args()  
        return (options.freq)
 
#       parser.add_option("-f", dest="filename", help="file name to read url's from", metavar="url_list.txt")
#       parser.add_option("-M", dest="mode", help="set the output mode, defualt is stdout, options include ES for ElasticSearch and SQLite for SQLite", default="STDout")
#       parser.add_option("--fpok", action="store_true", help="If we detect an error on our inital (non-malicous) request it's very likely that you will get a false positive for the given URL. by defualt, we will not test URL's with a high FP potential (better if running pyLobster against a large list of URL's). If you would like to test the URL anyway set this switch")
#       parser.add_option("-v", action="store_true", help="Show verbose output.")
#       parser.add_option("-g", action="store_true", help="Enable footprint mode. Please see manual (non-existant) for additional info on what is needed here and what this feature does.")
#       parser.add_option("-l", action="store_true", help="Enable learning mode. If we don't hit regEx error but do get 500 then lets save the HTML for later review.")
#       parser.add_option("-s", action="store_true", help="Enable smart mode. This will look at what Headers the webserver is using and test those")
#       parser.add_option("--bad", action="store_true", help="Enable Byte Anomaly Detection.")
#       (options, args) = parser.parse_args()
#       return (options.filename, options.mode, options.v, options.g, options.s, options.fpok, options.bad, options.l)
 
 
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
