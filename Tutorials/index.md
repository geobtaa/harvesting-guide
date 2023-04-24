---
hide:
  - navigation
  - toc
---

These tutorials are short, easy to complete exercises to help someone get the basics of running and writing scripts to harvest metadata. They are available as Jupyter Notebooks hosted in GitHub.

### 1. [Getting started with Jupyter Notebook](https://github.com/geobtaa/harvesting-guide/tree/main/docs/1-Tutorials/T-01_getting-started-jupyter)

This guide will show users how to install Jupyter Notebooks on their machines locally via their command line terminal, how to run a notebook, how cells function with code, markdown semantics, and other basic fundamentals.

### 2. [Iterating over files](https://github.com/geobtaa/harvesting-guide/blob/main/docs/1-Tutorials/T-02_iterating-files)

* This guide will assist users in how to open, read, and print the results of a CSV.
* The module os.Walk will be given special emphasis as this allows you to work down directories of your files and sift through multiple files.
* Including a brief display of the pandas module and Dataframe capablites in displaying a CSV for records.

### 3. [Parsing HTML with Beautiful Soup](https://github.com/geobtaa/harvesting-guide/tree/main/docs/1-Tutorials/T-03_parsing-html-beautiful-soup)

* This tutorial will guide users through Hyper Text Mark-Up Language (HTML) site parsing using the BeautifulSoup Python module with BTAA's UMedia portal site.
* In addition how to install the BeautifulSoup module, scan and list web pages, return titles, descriptions, and dates, then writing these to CSV format.

### 4. [Setting up your environment](https://github.com/geobtaa/harvesting-guide/blob/main/docs/1-Tutorials/Environment%20Setup%20Tutorial)

* This tutorial will guide users on how to set environments for harvesting portals via DCAT, CKAN, and other API types via widely used scripts (for more on APIs see DCAT and CKAN architecture tutorials).
* Then guide them in setting the right directory/path so that the correct files will be utilized and harvested for said APIs.
* Along with a brief overview of environmental settings in GitHub for having "repositories", "branches", "pull requests" and "committed" changes with a walkthrough of creating a repository.

### 5. [Transform a batch of JSON files into a single CSV file](https://github.com/geobtaa/harvesting-guide/blob/main/docs/1-Tutorials/Other/json2csv.ipynb)

This tutorial uses the Python module pandas (Python Data Analysis Library) to open a batch of JSON files and transform the contents into a single CSV.

### 6. [Extract Place Names](https://github.com/geobtaa/harvesting-guide/blob/main/docs/1-Tutorials/Other/extractPlaceNames.ipynb)

This tutorial scans the two columns from a CSV file ('Title' and 'Description') to look for known place names and writes the values to a separate field.

### 7. [Merge CSV files based on a shared column](https://github.com/geobtaa/harvesting-guide/blob/main/docs/1-Tutorials/Other/Merge%20CSV%20files%20based%20on%20a%20shared%20column.ipynb)

This script tutorial allow us to take two CSV files and combine them using a shared key.

### 8. [Use OpenStreetMap to generate bounding boxes](https://github.com/geobtaa/harvesting-guide/blob/main/docs/1-Tutorials/Other/osm.py)


