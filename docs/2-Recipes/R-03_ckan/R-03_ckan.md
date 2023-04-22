## Purpose

This script will harvest from a set of CKAN data portals. It saves metadata files and will compare the output between runs. The result will be two CSVs: new items and deleted items.

Set up your directory to contain these four items:

* harvest.ipynb
* CKANportals.csv includes some basic information about each CKAN portal.
* resource folder: collects existing resource names by portal for each re-accession. The new one will be compared with the latest one to get both the created and deleted datasets.
* reports folder: stores the metadata CSV files for all new and deleted datasets.


## Run the script

https://github.com/geobtaa/harvesting-guide/blob/main/docs/2-Recipes/R-03_ckan/R-03_ckan.ipynb