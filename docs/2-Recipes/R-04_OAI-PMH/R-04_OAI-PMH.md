## Harvest via OAI-PMH

Using Illinois Library Digital Collections as example

Steps:

### Part 1: get the files via oai
1. Use this OAI-PMH validator tool at https://validator.oaipmh.com
2. Go to the Download XML tab
3. Enter the base URL (https://digital.library.illinois.edu/oai-pmh) and the set name (6ff64b00-072d-0130-c5bb-0019b9e633c5-2)
4. Wait for the app to pull all the XML files and download them (ideally in a ZIP, but sometimes that doesn't work and you need to click on each file)

### Part 2: turn the records into a CSV via OpenRefine
1. start OpenRefine
2. Choose "Get Data from this Computer" and upload the XML files
3. From the parsing options, select from the Header "record"

### Part 3: Collapse multivalued cells
1. The multi-valued cells will start out being grouped together by which XML file they came from. We don't want that, so remove the column called File.
2. Now, they are grouped by a value "[http://www.openarchives.org/OAI/2.0/oai_dc/ ](http://www.openarchives.org/OAI/2.0/oai_dc/)http://www.openarchives.org/OAI/2.0/oai_dc.xsd" Leave this for now.
3. There are multiple Identifiers (dc:identifier), so select that column, Edit Cells - Join multi-valued cells
4. Move the Identifier column to the beginning so that items will be grouped by these unique values
5. Collapse the remaining cells with the same Join Multi-valued cells function
6. Export to CSV
