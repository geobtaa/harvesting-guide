---
hide:

---

## Conda

- Conda is an open source package management system and environment management system that runs on Windows, macOS, and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer. It was created for Python programs, but it can package and distribute software for any language.

## Conda Package Manager

- Conda as a package manager helps you find and install packages. If you need a package that requires a different version of Python, you do not need to switch to a different environment manager, because conda is also an environment manager. With just a few commands, you can set up a totally separate environment to run that different version of Python, while continuing to run your usual version of Python in your normal environment.

**For more information on Conda and environments, refer to this website: 
https://docs.conda.io/projects/conda/en/stable/user-guide/index.html**

## Pandas DataFrame 

Pandas DataFrame is a 2-dimensional table-like data structure that is used for data manipulation and analysis. It is a powerful tool for handling and processing structured data. A DataFrame has rows and columns, similar to a spreadsheet. It can contain heterogeneous data types and can be indexed and sliced in various ways. It is part of the Pandas library and provides powerful features for data analysis and manipulation. [https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html?highlight=dataframe#pandas-dataframe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html?highlight=dataframe#pandas-dataframe)

## Python List 

A list is a basic data structure in Python that is used to store a collection of items of different data types. It is an ordered collection of elements, and each element is indexed by an integer starting from 0. A list can contain elements of different data types, including other lists and dictionaries. A list is mutable, meaning its elements can be added, removed, or modified. It is a simple, general-purpose data structure that is commonly used for storing and manipulating small to medium-sized data sets.

## Python Dictionary

A dictionary is another data structure in Python that is used to store data in the form of key-value pairs. It is an unordered collection of elements, where each element is identified by a unique key instead of an index. The keys can be of any hashable data type, and the values can be of any data type. A dictionary is also mutable, meaning its elements can be added, removed, or modified. It is commonly used to store and manipulate structured data, such as user profiles or configuration settings.

## Python Object(s)

In Python, everything is an object. An object is an instance of a class, which is a blueprint for creating objects. It contains data and functions (also called methods) that operate on that data. Objects are created dynamically, which means that you don't have to declare the type of a variable or allocate memory for it explicitly. When you assign a value to a variable, Python creates an object of the appropriate type and associates it with that variable.

For example, an integer in Python is an object of the int class, and a string is an object of the str class. Each object of a class has its own set of data attributes, which store the values of its properties, and methods, which operate on those properties.

## Python Interface

In Python, an interface refers to the set of methods that a class or an object exposes to the outside world. It defines the way in which an object can be interacted with, and the methods that are available to be called. An interface can be thought of as a contract that specifies how a class can be used, and what methods are available to a programmer when working with that class.

Python is an object-oriented programming language, and as such, it supports the concept of an interface. Python does not have a specific language construct for creating an interface. Instead, interfaces are implemented using a combination of abstract base classes and duck typing.

An abstract base class is a class that cannot be instantiated directly, but instead, is intended to be subclassed. It defines a set of abstract methods that must be implemented by any subclass. This allows for the creation of a common interface that can be shared among multiple classes.

Duck typing is a concept in Python that allows for the determination of an object's type based on its behavior, rather than its actual type. This means that if an object behaves like a certain type, it is considered to be of that type. This allows for more flexibility in programming, as it allows for the creation of classes that can be used interchangeably, as long as they implement the same methods.

## Beautiful Soup

HTML and XML parser

## Pandas

Pandas is a Python library that contains many functions for analyzing data. For the GeoBTAA workflows, we are most interested in how it eases transformations between JSON and CSV files:

*CSV files*: Pandas can easily read and write CSV files using its `read_csv()` and `to_csv()` methods, respectively. These methods can handle many CSV formats, including different delimiter characters, header options, and data types. Once the CSV data is loaded into a Pandas DataFrame, it can be easily manipulated and analyzed using Pandas' powerful data manipulation tools, such as filtering, grouping, and aggregation.

*JSON data*: Pandas can also read and write JSON data using its `read_json()` and `to_json()` methods. These methods can handle various JSON formats, such as normal JSON objects, JSON arrays, and JSON lines. Once the JSON data is loaded into a Pandas DataFrame, it can be easily manipulated and analyzed using the same data manipulation tools used for CSV data.

*pandas DataFrame* A DataFrame is similar to a Python list or dictionary, but it has rows and columns, similar to a spreadsheet. This makes it a simpler task to convert between JSON and CSV. To review these Python terms, refer to the glossary.

## SpaCy

[SpaCy](https://spacy.io) is a python module that uses natural language processing (NLP) to comb through text help us find and extract patterns. To extract place names, it uses named entity recognition (NER) by searching a list of place names. This list is called "GPE", which stands for Geopolitical Entity.

This article in the Code4Lib journal, [From Text to Map: Combing Named Entity Recognition and Geographic Information Systems](https://journal.code4lib.org/articles/15405), explains the process we use to extract place names.

## Metadata Standards

This chart provides links to documentation about the common metadata standards and schemas we encounter when harvesting.

{{ read_csv('metadataStandards.csv') }}