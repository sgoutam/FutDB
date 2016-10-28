# FutDB
#Commentary Recommendation Portal  
The project can be easily implemented using Python and related tools/packages.  
For the implementation of this project, we considered building a website using Python Flask as the backend programming language and used bootstrap to design the front end.  
Furthermore, for the Natural Language Processing we considered using NLTK (Natural Language Toolkit 3.0) in python, for its ease of use and robustness. We also used BeautifulSoup4 package in Python to scrape articles from web to obtain the text required for summarization.  
For the website, we obtained an open source database from Github, and used it on a local server to cater to the queries of the user. The data is obtained in the form of JSON files.   
JSON: JavaScript Object Notation. JSON is a syntax for storing and exchanging data. JSON is an easier-to-use alternative to XML.  
For querying the database, we used MongoDB. MongoDB (from humongous) is a cross-platform document-oriented database.   
Classified as a NoSQL database, MongoDB eschews the traditional table-based relational database structure in favor of JSON-like documents with dynamic schemas (MongoDB calls the format BSON), making the integration of data in certain types of applications easier and faster.  
As mentioned, MongoDB converts the JSON files into BSON files while querying and then looks up the file for an exact match of the query.  
Once the match is found, it returns the corresponding JSON object to Flask. Now, we can use this object to display its contents on the webpage using Flask.  
A similar approach is undertaken when fetching News articles for the queried player/team.  
We use Google News API to fetch the news content, dynamically, for the query.  
The API returns a JSON object for the query and using flask, we can decide how many news headlines we want to show on the webpage.    
To implement the Text Summarization, we used Wikipedia API to fetch the Wikipedia page about the query and then scrape their content to obtain the text for Summarization.   
We used BeautifulSoup4 for Web Scraping. Once the scraped text is available to use, it can be passed on to the NLTK script to perform the Text Summarization.
