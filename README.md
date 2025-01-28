🛠️ Beautiful Soup Practice Code 🥣
This Python script is a hands-on exercise for exploring the power of Beautiful Soup, a fantastic library for web scraping and parsing HTML/XML documents. 🕸️ The code demonstrates how to extract, manipulate, and even modify HTML content effortlessly.

✨ Key Features
📂 Reading and Parsing HTML

Loads an HTML file (sample.html) and parses it using Beautiful Soup’s html.parser.
Prettifies the HTML structure for better readability.
🔎 HTML Parsing Basics

Access and manipulate specific tags like <title>:
Get the <title> tag with soup.title.
Extract its text content: soup.title.string.
Retrieve the tag name: soup.title.name.
🌳 Navigating the HTML Tree

Locate the parent of an element, e.g., soup.title.parent.name.
Find the first occurrence of a tag (soup.p) or fetch all occurrences using soup.find_all("p").
📝 Attributes and Text Extraction

Extract attributes of tags:
Get the class of the first <p> tag: soup.p['class'].
Fetch the text of an element by id: soup.find(id="ali").text.
Retrieve all text from the HTML document:
python
Copy
Edit
soup.get_text()  
🔗 Link Handling

Access anchor tags (<a>):
Extract text inside the first <a>: soup.a.get_text().
Loop through multiple links and get their href attributes.
🎨 CSS Selectors

Use soup.select() to target elements by CSS selectors:
Get all <div> elements with the class italic.
Retrieve content of <div> tags with specific id.
🛠️ Modifying HTML

Editing Elements:
Change tag names, classes, and inner text dynamically.
Example: Convert a <div> with class cont into a <span> with a new class and content (Saeed).
Adding New Tags:
Create new tags like <ul> and <li> dynamically with soup.new_tag().
Add new items such as Home and About to the HTML structure.
Save Changes:
Write the updated HTML into a new file: modified.html.
🔄 Iterating Through HTML Elements

Use .children to loop through all child elements of a tag (e.g., find all children of a tag with class cont).
📦 Libraries Used
requests (imported but not used here): Typically used for fetching HTML content from websites.
BeautifulSoup (from bs4): The main library for parsing and navigating HTML documents.
🎯 Use Cases
This script is perfect for:

🚀 Learning the basics of web scraping and HTML manipulation.
🧪 Experimenting with real-world web scraping scenarios.
💻 Automating tasks like modifying or restructuring HTML programmatically.
💡 How to Use
Install Beautiful Soup:

bash
Copy
Edit
pip install beautifulsoup4  
Run the Script:

Save your HTML content in sample.html.
Execute the script and observe the output.
⚠️ Disclaimer
This script is for educational purposes only! 🌟 Ensure you comply with website terms of service and avoid unauthorized scraping of private data. 🚨

Happy Coding! 💻✨

