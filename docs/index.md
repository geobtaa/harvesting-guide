# Home

The BTAA Geoportal holds metadata records that point to geospatial data, maps, aerial imagery, web services, and websites hosted online by external organizations.

The most common way of obtaining this metadata is to programmatically harvest it from an organization's website. These websites may be in the form of a data portal, a static page, or custom platform.

Due to the variation of how the websites are structured, we have written several different Python harvesting scripts. 

Here are the main categories:

## HTML parsing

If a data portal or website does not have an API, we may be able to parse the HTML pages to obtain the metadata needed to create GeoBlacklight schema records.


## API

DCAT enabled portals: ArcGIS Open Data Portals (HUB), Socrata portals, and some others share metadata in the DCAT standard.

CKAN / DKAN portals: This application uses a custom metadata schema for their API.