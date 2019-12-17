#!/usr/bin/env python3
'''
This takes the dict that is built from the Flickr API result pages
and parses them into a single XML tree, which will later be used to 
flesh out data per image.
'''

import ast
import copy
import lxml.etree

# this is a dict of {(flickr result page#): (page result XML)}
inputFile = "FlickrPageOutput.txt"
outputFile = "Flickrphotos.xml"
with open(inputFile,'r') as f:
	text = f.read()
flickrDict = ast.literal_eval(text)
# set up an empty <flick> tag to hold all the photo data
flickrRoot = lxml.etree.fromstring("<flickr/>")

counter = 0
for key in flickrDict.keys():
	page = flickrDict[key]
	pageXML = lxml.etree.fromstring(page)
	# we are only interested in the <photo> elements
	# contained in each page of results.
	for element in pageXML.iter('photo'):
		counter += 1
		child = copy.deepcopy(element)
		# insert the copied element into the <flickr> root.
		flickrRoot.insert(counter,child)

	del page
	del pageXML

flickrTree = lxml.etree.ElementTree(flickrRoot)
with open(outputFile,'wb') as f:
	flickrTree.write(f)

