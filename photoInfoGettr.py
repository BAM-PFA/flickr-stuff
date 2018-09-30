#!/usr/bin/env python3
'''
This takes in a <flickr> root element that contains all the skeletal
<photo> elements returned by flickr.photos.search.
It uses the 'id' and 'secret' attributes in each <photo> and queries
flickr.photos.getInfo to retrieve the fuller set of data 
'''
import copy
import flickr_api.api
import lxml.etree
import time
import utils

# set the api key, authentication, and stuff
utils.setup()
# This is a dict of file paths to use sequentially with each round of queries. 
# I wanted to keep them separate in case of failure or something that would 
# overwrite existing data.... 
# dataFile 0 is the original data set from flickrPager.py and pageExtractor.py
# it's a <flickr> element with X number of <photo> elements
dataFiles = {0:"/path/to/Flickrphotos.xml",
	# at the end of the first pass, dataFile 1 will contain all the original data
	# plus the augmented data from the query. I know there are 8800 photos,
	# so to keep in the API limit of 3600 queries per hour I will run three passes. 
	1: "/path/to/FlickrphotoData1.xml",
	2: "/path/to/FlickrphotoData2.xml",
	3: "/path/to/FlickrphotoData3.xml"
	}

def do_query(sourceFile,outFile,fileCounter):
	# read in data from the source file
	with open(sourceFile,'rb') as f:
		data = lxml.etree.parse(f)
	info = flickr_api.api.FlickrMethodProxy('flickr.photos.getInfo')
	counter = 0
	for element in data.iter('photo'):
		if len(element) == 0:
			counter += 1
			if counter < 3500:
				photo_id = element.get('id')
				photo_secret = element.get('secret')
				photoResult = info.__call__(photo_id=photo_id,secret=photo_secret)
				print(photoResult)
				try:
					resultRoot = lxml.etree.fromstring(photoResult)
					status = resultRoot.get('stat')
					if status == 'ok':
						photoData = resultRoot.xpath('photo')[0]
						child = copy.deepcopy(photoData)
						element.insert(0,child)
					else:
						pass
				except:
					pass

				with open(outFile,'wb') as f:
					data.write(f)
			else:
				break
		else:
			pass
	fileCounter += 1
	return fileCounter

def main():
	fileCounter = 0
	while fileCounter < 3:
		sourceFile = dataFiles[fileCounter]
		outFile = dataFiles[fileCounter+1]
		fileCounter = do_query(sourceFile,outFile,fileCounter)
		# wait an hour for the API to chill out.
		time.sleep(3600)
	if fileCounter == 3:
		sourceFile = outFile = dataFiles[fileCounter]
		do_query(sourceFile,outFile,fileCounter)

if __name__ == "__main__":
	main()




