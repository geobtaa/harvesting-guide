# List of tutorials

The tutorial section contains short, easy to complete exercises to help someone get the basics of running and writing scripts to harvest metadata.

*Here are some suggestions:*

## Environment

We use Python scripts with a number of additional modules. This section aids the user in getting their computer environment set up.

### Python modules

- This tutorial would help someone set up their computer to work with the files. 
- Using Conda / anaconda environment has worked for MACs and Windows

### Jupyter Notebook

- Installation
- Running a notebook
- The different cells: markdown vs code
- a few more basics 



## CSV

The most basic goal of the BTAA-GIN metadata harvesting is to convert external metadata into a CSV file for processing.  This section has a few tutorials about working with CSV files.

### Walking through files

- open a CSV of URLs
- walking through the URLs (os.walk)
- printing out the list or URLs 

### Writing to a CSV

- combine the parsing and the walking tutorials and add a step to write to a CSV

### other?



## Parsing web pages 

### HTML sites (Beautiful Soup)

- (how to install Beautiful soup)
- open & scan a list of web pages
- return a title value
- return a description value
- return a date value
- print results to a CSV

Use this site: [https://umedia.lib.umn.edu](https://umedia.lib.umn.edu)


### HTML sites with tables of metadata (Pandas)

- (how to install Pandas)
- open & scan a list of web pages
- return a Pandas data frame
- print results to a CSV

Use this site: [https://www.mngeo.state.mn.us/glo/Index.htm](https://www.mngeo.state.mn.us/glo/Index.htm)


## Parsing metadata using APIS

### DCAT
- user learns about the structure of a DCAT JSON file
- user runs a modified version of a DCAT harvest to see one to three portals, (similar to this: https://github.com/geobtaa/geo4libcamp-metadata-workshop/tree/master/DCAT)

### CKAN
- users learns about the structure of a CKAN site
- user runs a simple version of a CKAN harvest

