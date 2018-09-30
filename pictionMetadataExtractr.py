#!/usr/env python3
'''
this may or may not be a useful tool for interns to create CSVs of existing
metadata for uploading images to piction, in addition to or instead of the 
other flickr scripts in this repo.
'''
import argparse
import json
import os
import subprocess
import sys
import time

ALL_HEADERS = [
	"FILENAME","BAMPFA.TITLE","BAMPFA.ARTISTFILMMAKER","BAMPFA.YEAR",
	"EVENTS.DC-COVERAGE","EVENTS.DC-PUBLISHER","EVENTS.RELATED_EXHIBITIONS",
	"EVENTS.EVENT_LOCATION","EVENTS.DC-DESCRIPTION","EVENTS.DC-TYPE",
	"EVENTS.DC-SUBJECT","EVENTS.TOPICAL_SUBJECT","EVENTS.ORGANIZER",
	"EVENTS.DC-CONTRIBUTOR","EVENTS.DC-RIGHTS","EVENTS.DC-AUTHOR",
	"EVENTS.TAGS","EVENTS.BAM_PFA_CAPTION","EVENTS.RESTRICTIONS",
	"EVENTS.DC-CREATOR","FILM.BAM_PFA_CAPTION","FILM.DC-CONTRIBUTOR",
	"FILM.DC-CREATOR","FILM.DC-DESCRIPTION","FILM.DC-PUBLISHER",
	"FILM.DC-RIGHTS","FILM.DC-SUBJECT","FILM.DC-TYPE","FILM.RESTRICTIONS",
	"FILM.TAGS","GALLERY EXHIBITION.ARTWORK_CREDIT_LINE",
	"GALLERY EXHIBITION.ARTWORK_MEDIUM","GALLERY EXHIBITION.BAM_PFA_CAPTION",
	"GALLERY EXHIBITION.CURATOR","GALLERY EXHIBITION.DC-CONTRIBUTOR",
	"GALLERY EXHIBITION.DC-COVERAGE","GALLERY EXHIBITION.DC-CREATOR",
	"GALLERY EXHIBITION.DC-DESCRIPTION","GALLERY EXHIBITION.DC-PUBLISHER",
	"GALLERY EXHIBITION.DC-RIGHTS","GALLERY EXHIBITION.DC-TITLE",
	"GALLERY EXHIBITION.DC-TYPE","GALLERY EXHIBITION.EXHIBITION LOCATION",
	"GALLERY EXHIBITION.FULL_EXHIBIT_DATE","GALLERY EXHIBITION.PHOTO_CREDIT",
	"GALLERY EXHIBITION.RESTRICTIONS","GALLERY EXHIBITION.TAGS",
	"XMP.USAGETERMS","INSTITUTIONAL.DC-DESCRIPTION","INSTITUTIONAL.DC-SUBJECT",
	"INSTITUTIONAL.LOCATION_PICTURED","INSTITUTIONAL.DC-RIGHTS",
	"INSTITUTIONAL.RESTRICTIONS","INSTITUTIONAL.BAM_PFA_CAPTION",
	"INSTITUTIONAL.TAGS","INSTITUTIONAL.DC-CONTRIBUTOR",
	"INSTITUTIONAL.DC-AUTHOR"
	]
eventFTPprefix = "K:\\ftp_ucbcspace\\BAMPFA\\Event_Images\\"
filmFTPprefix = "K:\\ftp_ucbcspace\\BAMPFA\\Film_Images\\"
exhibitionFTPprefix = "K:\\ftp_ucbcspace\\BAMPFA\\Gallery_Exhibition_Images\\"
instutionalFTPprefix = "K:\\ftp_ucbcspace\\BAMPFA\\Institutional_Images\\"

def get_exif_json(path):
	out = subprocess.run(
		[
			'exiftool','-j',
			path
			]
		)
	exifJSON = json.loads(out.stdout)[0]
	return exifJSON

def get_needed_value(exifJSON,tag):
	try:
		value = exifJSON[tag]
	except KeyError:
		value = ''

	return value

def csv_builder(imageDict):
	pass


def make_image_dict(path,inputType,ftpPrefix):
	if inputType == 

	imageDict = {}
	exifJSON = get_exif_json(path)
	imageDict['FILENAME'] = ftpPrefix+os.path.basename(path)
	imageDict["BAMPFA.TITLE"] = get_needed_value(exifJSON,'')


def csv_maker(destPath):
	pass

def strip_path(_path):
	_path = _path.replace('\\','').rstrip()
	return _path

def ask_input():
	inputFolder = input("Please drag a folder containing images to extract metadata from, then hit enter: ")
	inputFolder = inputFolder.replace('\\','').rstrip()
	return inputFolder

def ask_dest():
	outFolder = input("Please drag in a folder where you want your CSV to live, then hit enter: ")
	outFolder = outFolder.replace('\\','').rstrip()
	return outFolder

def interview():
	inputFolder = ask_input()
	csvDest = ask_dest()
	for folder in (inputFolder,csvDest):
		if not os.path.isdir(inputFolder):
			print("HEY! The folder you specified ({}) is not valid. "
				"Quitting now, try again!".format(inputFolder))
			sys.exit()
	inputType = input("Choose an image type then hit Enter: \nE for events\nF for film\nG for gallery images\nI for institutional images:")
	inputType, ftpPrefix = parse_type(inputType)
	if not ftpPrefix:
		print("Sorry you entered a bogus image type. Quitting now. Try again. :/")
		sys.exit()
	return inputFolder, csvDest, inputType, ftpPrefix

def parse_type(inputType):
	if inputType in ('E','e'):
		inputType = 'event'
		ftpPrefix = eventFTPprefix
	elif inputType in ('F','f'):
		inputType = 'film'
		ftpPrefix = filmFTPprefix
	elif inputType in ('G','g'):
		inputType = 'gallery'
		ftpPrefix = exhibitionFTPprefix
	elif inputType in ('I','i'):
		inputType = 'institutional'
		ftpPrefix = 'instutionalFTPprefix'
	else:
		ftpPrefix = None

	return inputType, ftpPrefix

def main():
	inputFolder, csvDest, inputType, ftpPrefix = interview()
	contents = os.scandir(inputFolder)
	for element in contents:
		imageDict = make_image_dict(element.path, inputType, ftpPrefix)

	# iterate over folder to get json per file
	# extract needed tags that are present per file json
	# write tags per file
