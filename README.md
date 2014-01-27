python-colossus
===============

Python tools for manipulating extremely large images

This tool suite can be used as a python library or as standalone commands. Future 
directions may include a Gimp plugin.

It was originally built in order to make it easier to manually manipulate extremely 
large images. The first use case was 10k-by-10x pixels (100 megapixels), but there's 
no obvious reason why it wouldn't scale up a few orders of magnitude. Users of the 
tools check in and check out portions of an image, and at any given time are working 
with a rectangular subset of the full image. When checked in, the image data is 
stored in a prescribed directory hierarchy. The tools also provide a mechanism for 
the creation of multiple discrete zoom levels of the original image, which can be 
stored alongside each other and edited independently. The varying zoom levels and 
tiles are stored in a manner that allows them to all be easily viewed using Google 
maps, thus providing a quick mechanism of panning and zooming through scales of many 
orders of magnitude.

Installation:
------------

Assuming you have a python installation and can use pip for package management:
  pip install colossus

Other installation mechanisms may be added later.


Getting started:
---------------

Gather small images that constitute tiles of the image at highest resolution.
Helpers: Google maps tile downloader at specified resolution
or
Start with single large image, and check it in to generate data for a given zoom level.


Check-in/check-out:
------------------

Checking out a particular pixel range of the image means that you are creating one new 
image file (your checked out copy) that is composed of the data from some portion of a 
subset of tiles, cropped and joined as necessary to accommodate your requested pixel range.

Checking in a particular range means that, for a given zoom level, you clobber the data 
for some subset of tiles in the hierarchy with the data from the image that you are 
checking in. In the future, we may add some versioning capabilities for the affected tiles 
rather than just clobbering them.

Viewing:
-------

Use the google maps javascript code to view the image, or try out the layers thing. If 
desired, check out the full image at a given zoom level to stitch the entire thing together.



