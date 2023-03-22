## About pandas

Pandas is a Python library that contains many functions for analyzing data. For the GeoBTAA workflows, we are most interested in how it eases transformations between JSON and CSV files:

*CSV files*: Pandas can easily read and write CSV files using its `read_csv()` and `to_csv()` methods, respectively. These methods can handle many CSV formats, including different delimiter characters, header options, and data types. Once the CSV data is loaded into a Pandas DataFrame, it can be easily manipulated and analyzed using Pandas' powerful data manipulation tools, such as filtering, grouping, and aggregation.

*JSON data*: Pandas can also read and write JSON data using its `read_json()` and `to_json()` methods. These methods can handle various JSON formats, such as normal JSON objects, JSON arrays, and JSON lines. Once the JSON data is loaded into a Pandas DataFrame, it can be easily manipulated and analyzed using the same data manipulation tools used for CSV data.

*pandas DataFrame* A DataFrame is similar to a Python list or dictionary, but it has rows and columns, similar to a spreadsheet. This makes it a simpler task to convert between JSON and CSV. To review these Python terms, refer to the glossary.