# Resource Lifecycle

!!! abstract "summary"

	How the Harvesting Guide fits into the Geoportal's Resource Lifecycle


## 5 Stages of the Resource Lifecycle

``` mermaid
flowchart LR
  
  I((1.<br> IDENTIFY)) --> H[/2. <br> HARVEST/] --> P[3. <br> EDIT] --> X[4. <br>INDEX] --> M{{5. <br>MAINTAIN}}--> H[/2. <br>HARVEST/]
   
```
**This guide primarily addresses the Harvest stage.**  Editing and publishing are described in our [Metadata Handbook.](https://z.umn.edu/gbl-handbook).

## 1. Identify

:fontawesome-solid-user: BTAA-GIN Team Members and Product Manager 

Team members seek out new content for the geoportal. See the page [How to Submit Resources to the BTAA Geoportal](https://geobtaa.github.io/metadata/submit-resources/) for more information.

## 2. Harvest

:fontawesome-solid-user: Graduate Research Assistants and Product Manager 

This stage involves obtaining the metadata for resources.  At a minimum, this will include a title and and access link. However, it will ideally also include descriptions, dates, authors, rights, keywords, and more. 

Here are the most common ways that we obtain the metadata:

1. a BTAA-GIN Team Member sends us the metadata values as individual documents or as a combined spreadsheet
2. we are provided with (or are able to find) an API that will automatically generate the metadata in a structured file, such as JSON or XML
3. we develop a customized script to scrape directly from the HTML on a source's website
4. we manually copy and paste the metadata into a spreadsheet
5. a combination of one or more of the above

This step also involves using a crosswalk to convert the metadata into the schema needed for the Geoportal. Our goal is to end up with a spreadsheet containing columns matching our [metadata template](https://z.umn.edu/b1g-template).

!!! info "Why do we rely on CSV?"

	CSV (Comma Separated Values) files are used widely in the world of harvesting and scraping data from the web, including data science because they are simple, lightweight, and widely supported. CSV files are a type of file format used to store tabular data in plain text format, where each row of data is separated by a line break, and each column of data is separated by a delimiter.
	CSV files are easy to read and write, can be opened with a simple text editor, and can be processed using many programming languages, including Python. Python has built-in libraries, such as `csv`, that allow you to read and write CSV files easily.

## 3. Edit

:fontawesome-solid-user: Graduate Research Assistants and Product Manager 

When working with metadata, it is common to come across missing or corrupted values, which require troubleshooting and manual editing in our spreadsheets. Refer to the [Collections Project Board](https://github.com/orgs/geobtaa/projects/4) for examples of this work.

After preparing the metadata, we upload the completed spreadsheet to GEOMG, which serves as the administrative interface for the Geoportal. If GEOMG detects any formatting errors, it will issue a warning and may reject the upload.

## 4. Index

:fontawesome-solid-user: Product Manager 

Once the metadata is successfully uploaded to GEOMG, we can publish the records to the Geoportal. The technology that actually stores the records and enables searching is called [Solr](https://solr.apache.org). The action of adding records is known as "Indexing."

Periodically, we need to remove records from the Geoportal. To do this, we use GEOMG to either delete them or change their status to "unpublished."

## 4. Maintain

:fontawesome-solid-user: BTAA-GIN Team Members, Graduate Research Assistants, and Product Manager 

The Geoportal is programmatically checked for broken links on a monthly basis. The are fixed either by manually repairing them or by reharvesting from the source.


##  Sequence diagram of Resource Lifecycle

``` mermaid

	
	

	sequenceDiagram
   		actor Team Member
    		actor Product Manager
    		participant GitHub
    		actor Research Assistant
    		participant GEOMG
    		participant Geoportal	
    			
    		
    		Note right of Team Member:  IDENTIFY
    		 
    		Team Member->>Product Manager: Submit Resources
    		Product Manager->>GitHub: Create GitHub issue
    		GitHub ->>Research Assistant: Assign issue
    		Note left of Research Assistant:  HARVEST
    		Note left of Research Assistant:  EDIT 
    		
    		Research Assistant->>GEOMG: Upload records
    		Research Assistant ->>GitHub: Update GitHub issue
    		Note right of GEOMG:  PUBLISH 
    		
    		Product Manager->>GEOMG: Publish records
    		GEOMG->>Geoportal: Send records online 
    		Product Manager->>GitHub: Close GitHub issue
    		Product Manager ->> Team Member: Share link to published records
    		
    		Note left of Research Assistant:  MAINTAIN 
    		
```

