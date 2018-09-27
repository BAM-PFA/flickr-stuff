# Flickr stuff

These are some WIP scripts to deal with the dead weight of Flickr photos that [BAMPFA](https://www.flickr.com/photos/bampfa/) has not dealt with or added to since 2016. The ultimate goal is to get the stuff off of Flickr and into Piction, our DAMS where this stuff should have been in the first place.

Working with the API is less than ideal but doable. 

Relies on the [flickr_api](https://github.com/alexis-mignon/python-flickr-api) library for Python. I'm using python3, which does not seem to be fully supported (see this [PR](https://github.com/alexis-mignon/python-flickr-api/pull/101)) but is definitely doable. They have a pretty good authentication module documented on their wiki. Installs with `pip3 install flickr_api`

Not totally sure if this is the route we will ultimately take, but the metadata added through the Flickr interface is not otherwise accessible.

Also depends on lxml (`pip3 install lxml`).

`configi.ini` looks like this:
```
[secrets]
api_key:
api_secret:
api_auth_file_path:
```