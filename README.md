Beautiful Soup Practice Code

This Python script is designed for practicing and exploring various functionalities of the Beautiful Soup library, which is widely used for web scraping and parsing HTML/XML documents. The code showcases common operations you can perform with Beautiful Soup to manipulate and extract data from an HTML document.

Features and Functionalities
Reading an HTML File

The script begins by reading an HTML file (sample.html) and parsing it using Beautiful Soup with the html.parser.
Basic HTML Parsing

Prettify the entire HTML content for better readability:
python
Copy
Edit
soup.prettify()
Access specific tags like <title> and extract their content:
soup.title retrieves the <title> tag.
soup.title.string gets the inner text of the <title> tag.
soup.title.name retrieves the tag name itself.
Navigating the HTML Tree

Access the parent of a specific tag, such as the parent of <title> using soup.title.parent.name.
Locate the first occurrence of a tag (e.g., <p>) or retrieve all occurrences using soup.find_all("p").
Attributes and Text Extraction

Extract specific attributes of tags:
soup.p['class'] retrieves the class name of the first <p> tag.
soup.find(id="ali").text retrieves the text of an element with a specific id.
Get all text content from the HTML file:
python
Copy
Edit
soup.get_text()
Working with Links

Retrieve and manipulate anchor (<a>) tags:
Extract the text within the first <a> tag using soup.a.get_text().
Find and extract the href attribute from multiple <a> tags using a loop.
CSS Selectors

Use soup.select() to find elements by CSS selectors:
Example: Get all <div> tags with the class italic or retrieve the content of a <div> with a specific id.
Manipulating the HTML Document

Finding and Editing Elements:
Modify tags, classes, and inner text of elements.
Example: Change a <div> with class cont to a <span> with a new class container and new content (Saeed).
Adding New Tags:
Create new tags dynamically using soup.new_tag() and append content to them.
Insert the new tags into the existing HTML structure (e.g., creating a <ul> with <li> items like Home and About).
Writing Modified HTML:
Save the updated HTML content into a new file (modified.html).
Iterating Through the HTML Structure

Use .children to loop through child elements of a specific tag (e.g., finding all children of a tag with class cont).
Key Libraries Used
requests (Imported but unused in the provided script): Often used for sending HTTP requests to fetch HTML content from a webpage.
BeautifulSoup (from bs4): Used for parsing and navigating the HTML document.
Use Case
This script is ideal for:

Learning the basics of HTML parsing and manipulation.
Practicing real-world web scraping techniques.
Experimenting with modifying and restructuring HTML content programmatically.
