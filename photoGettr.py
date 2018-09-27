#!/usr/bin/env python3
import lxml.etree as etree
import re

'''
need to grab:
https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{o-secret}_o.(jpg|gif|png)
farm id
server id
id
original secret
file format/extension
title (parsed and stripped of non alphanumerics)
tags
description
'''
photoDataPath = "FlickrphotoData1.xml"

photoDestDir = "."

with open(photoDataPath,'rb') as f:
	data = etree.parse(f)

coolPhotos = {}
counter = 0

# there is a photo element nested in each child photo element
# we only want the higher one and will grip its contents shortly
photos = data.xpath('/flickr/photo')
for element in photos:
	if not len(element) == 0:
		coolPhotos[counter] = {}
		coolPhotos[counter]['id'] = _id = element.get('id')
		coolPhotos[counter]['farm'] = farm = element.get('farm')
		coolPhotos[counter]['server'] = server = element.get('server')
		title = element.get('title')
		# now parse the shit out of the title to get only alphanumerics
		# going to use it to build a (temp) filename on download
		title = re.sub('[^0-9a-zA-Z\ ]+', '', title.lower())
		coolPhotos[counter]['title'] = title = title.replace(' ','-')
		
		child = element.xpath('photo')[0]
		originalSecret = child.get('originalsecret')
		coolPhotos[counter]['originalsecret'] = originalSecret
		coolPhotos[counter]['extension'] = extension = child.get('originalformat')
		coolTags = []
		tags = child.xpath('tags')[0]
		for _tag in tags:
			coolTags.append(_tag.get('raw'))
		# we use semicolon as tag separator in Piction
		coolPhotos[counter]['tags'] = ';'.join(coolTags)
		description = child.xpath('description')[0].text
		coolPhotos[counter]['description'] = description

		url = "https://farm{}.staticflickr.com/{}/{}_{}_o.{}".format(
			farm,
			server,
			_id,
			originalSecret,
			extension
			)
		coolPhotos[counter]['url'] = url
		tempFileName = "{}_{}.{}".format(title,_id,extension)
		coolPhotos[counter]['filename'] = tempFileName

		counter += 1

print(coolPhotos)


