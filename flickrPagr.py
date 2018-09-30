#!/usr/bin/env python3
'''
The Flickr API returns 100 images per page by default. So you have
to deal with paginated results. This writes all the pages returned
into a dictionary that is then parsed by another script.
'''
import flickr_api.api
import utils
# set the api key and authentication
utils.setup()

outputFile = './FlickrPageOutput1.txt'
pageSearch = flickr_api.api.FlickrMethodProxy('flickr.photos.search')
pagesDict = {}
# i know that there are 89 pages of images
for i in range(1,90):
	# setting user_id to 'me' restricts the query to our stuff only
	thepage = pageSearch.__call__(user_id='me',page=i)
	# strip out some crap included in the XML string
	thepage = thepage.replace(b'\n',b'')
	thepage = thepage.replace(b'\t',b'')
	pagesDict[i] = thepage

with open(outputFile,'w') as f:
	f.write(str(pagesDict))