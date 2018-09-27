#!/usr/bin/env python3
import configparser
import os
import flickr_api.api

def read_config():
	mydir = os.path.dirname(os.path.abspath(__file__))
	configPath = os.path.join(mydir,'config.ini') 
	config = configparser.SafeConfigParser()
	config.read(configPath)
	return config

def setup():
	config = read_config()
	api_key = config['secrets']['api_key']
	api_secret = config['secrets']['api_secret']
	api_auth_file = config['secrets']['api_auth_file_path']

	flickr_api.set_keys(api_key=api_key,api_secret=api_secret)
	flickr_api.set_auth_handler(api_auth_file)