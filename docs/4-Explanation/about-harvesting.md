# About harvesting

This page describes some of the processes and terminology associated with extracting metadata from various sources.

## What is web scraping?

Web scraping is the process of programmatically collecting and extracting information from websites using automated scripts or bots. Common web scraping tools include pandas, Beautiful Soup, and WGET.

## What is data harvesting?

Data harvesting refers to the process of collecting large volumes of data from various sources, such as websites, social media, or other online platforms. This can involve using automated scripts or tools to extract structured or unstructured data, such as text, images, videos, or other types of content. The collected data can be used for various purposes, such as data analysis or content aggregation.

## What is metadata harvesting?

Metadata harvesting refers specifically to the process of collecting metadata from digital resources, such as websites, online databases, or digital libraries. Metadata is information that describes other data, such as the title, author, date, format, or subject of a document. Metadata harvesting involves extracting this information from digital resources and storing it in a structured format, such as a database or a metadata record.

Metadata harvesting is often used in the context of digital libraries, archives, or repositories, where the metadata is used to organize and manage large collections of digital resources. Metadata harvesting can be done using specialized tools or protocols, such as the Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH), which is a widely used standard for sharing metadata among digital repositories.

## Do "scraping" and "harvesting" mean the same thing?

The terms "harvesting" and "scraping" are often used interchangeably. However, there may be subtle differences in the way these terms are used, depending on the context.

In general, scraping refers to the process of programmatically extracting data from websites using automated scripts or bots. The term "scraping" often implies a more aggressive approach, where data is extracted without explicit permission from the website owner. Scraping may involve parsing HTML pages, following links, and using techniques such as web crawling or screen scraping to extract data from websites.

On the other hand, harvesting may refer to a more structured and systematic approach to extracting data from websites. The term "harvesting" often implies a more collaborative approach, where data is extracted with the explicit permission of the website owner or through APIs or web services provided by the website. Harvesting may involve using specialized software or tools to extract metadata, documents, or other resources from websites.

## What is web parsing?

Web parsing refers to the process of scanning structured documents and extracting information. Although, it usually refers to parsing HTML pages, it can also describe parsing XML or JSON documents. Tools designed for this purpose, such as Beautiful Soup, are often called "parsers."


## What is Extract-Transform-Load (ETL)?

ETL (Extract Transform Load) is a process of extracting data from one or more sources, transforming it to fit the target system's data model, and then loading it into the target system, such as a database or a data warehouse.

The ETL process typically involves three main stages:

* **Extract**: This stage involves retrieving data from one or more sources, which may include databases, files, APIs, web services, or other data sources.
* **Transform**: This stage involves converting, cleaning, and restructuring the extracted data to fit the target system's data model and business rules. This may include tasks such as data mapping, data validation, data enrichment, data aggregation, or data cleansing.
* **Load**: This stage involves inserting or updating the transformed data into the target system, such as a database or a data warehouse. This may involve tasks such as data partitioning, indexing, or data quality checks.
