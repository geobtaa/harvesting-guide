## Standard data portals

### ArcGIS Hubs

ArcGIS Hub is an architecture consisting of ArcGIS Enterprise at the global level, which provides the foundation for hosting services on ArcGIS Server via REST API, portals, and data stores. It is a platform designed for creating and sharing geospatial data with the public, and can be used by organizations, communities, and government agencies. The architecture of ArcGIS Hub allows for centralized management and control of data, making it easy to manage and share data across multiple portals.


* ArcGIS Hub architecture (consisting of ArcGIS Enterprise at the global level, and then hosting these services on ArcGIS Server via REST API, Portals, and Data Stores (also ArcGIS Server)
* Vs ArcGIS Online (cloud-based and usable in fieldwork) BUT incomparable as Open services URLs are more stable in portals than from IDs, because of REST API web points.
* IDs are not persistent and metadata from ArcGIS Open Portals (via different agencies) varies, when these change, links break
* Original referenced portals that are updated or re-published retain the same ID, but not if deleted (if content is re-uploaded with a new ID administered).
* ArcGIS Online and ArcGIS Hubs if using ArcGIS Contents pane retain metadata for upload.
* Organizations should adhere to one metadata standard (ISO, ArcGIS, etc) so it would be efficient in upgrading or transitioning from an ArcGIS Server to another app based portal.

### CKAN
# CKAN Site Structure and Harvesting Sample Walkthrough Guide

- This guide will assist users in deconstructing the Comprehensive Knowledge Archive Network (CKAN) site structure and Application Programming Interface (API) design and how they are created through harvesting from selected portals.  
- A simple harvest sample will be presented to simulate the larger process and understand how the harvesting-metadata workflow is done.

## CKAN Site Structure and API Breakdown

### The following is a description of the CKAN API and screenshots of the structure of CKAN sites pertaining to metadata harvesting: 

### CKAN is a tool for making open data websites, it helps you manage and publish collections of data.  For CKAN purposes, data is published in units called “datasets”.

   - A dataset contains two things:

   > Information or “metadata” about the data. For example, the title and publisher, date, what formats it is available in, what license it is released under, etc.

   > A number of “resources”, which hold the data itself. CKAN does not mind what format the data is in. A resource can be a CSV or Excel spreadsheet, XML file, PDF document, image file, linked data in RDF format, etc. CKAN can store the resource internally, or store it simply as a link, the resource itself being elsewhere on the web. A dataset can contain any number of resources. For example, different resources might contain the data for different years, or they might contain the same data in different formats.


## The following screenshots exemplify the site structure of CKAN and then how it is generated for harvesting metadata purposes. 

## This is the Raw site format breakdown for how data is compiled by web notation headers and other indicators in the BTAA format denoted by the harvest.py script for metadata purposes.
### Note, for CKAN it is a series of networks that interlink data units through JSON APIs similar to DCAT but are hosted on storage drives like databases and datastores.
![image-3.png](attachment:image-3.png)

### Only the site/portal would be harvested in this instance and the datastores/databases it contains.

![image.png](attachment:image.png)
