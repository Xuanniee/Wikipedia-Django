# Wikipedia (Django)

## Project Description
Wikipedia (Django) is a basic clone of Wikipedia, a free online encyclopedia that is widely used around the world. However, instead of using Wikitext to store encyclopedia entries, Markdown is used instead.

## Content

### 1. Index Page
![Picture of Index Page](./Images/Index%20Page.png?raw=true "Index Page")
The Index Page of Wikipedia (Django) shows a list of all the entries that can be found on the web application. 

Clicking any of of the entries will bring up the desired page.

### 2. Entry Page
![Picture of an Encyclopedia Entry Page](./Images/Valid%20Entry%20Page.png?raw=true "Entry Page")
If the Entry Page is valid, the User will be brought to the entry, with information about the topic of the page, along with an Edit Button to edit the page. If the page contains any references to topics with existing entry pages (as it is shown being highlighted in blue), Users can click into these entry pages as well.

![Picture of Invalid Entry Page](./Images/Error%20in%20Creating%20Existing%20Page.png?raw=true "Invalid Page")
However, if the Page is invalid, or doesn't exist, the User will be shown an Error Page and informed of the issue as shown above.

### 3. Search
![Picture of Search Results](./Images/Search%20Results.png?raw=true "Search")
Every page on the web application has a navigation bar on the left, which contains a few links and a search box. If the query made by the User matches an existing entry, the User will be redirected to the corresponding entry. 

However, if there isn't an exact match, the User will be brought to a page filled with search results that have the User's query as a substring, as shown above. Clicking any of the entries listed in the search results will also bring the User to the desired entry.

### 4. New Page
![Picture of Creating a New Entry](./Images/Creating%20New%20Entry%20Page.png?raw=true "Creating New Page")
The sidebar contains a link to a page that allows Users to create new encyclopedia entries for topics that are not yet, existing. Users can then provide information on the title and content of the entry in the fields provided.

![Picture of Error](./Images/Error%20in%20Creating%20Existing%20Page.png?raw=true "Error in Creating New Page")
However, if the User attempts to create an entry for an existing topic, they will be redirected to a page with an error message, informing them of such.

### 5. Edit Page
![Picture of Edit Page](./Images/Editing%20Wiki%20Page.png?raw=true "Editing Entries")
Clicking "Edit" on any entry will bring the User to a page that contains the existing markdown content of the entry, allowing the User to edit the content as they like. However, the User is prevented from editing the title of the entry. 

After the edits are saved, the User will then be redirected back to the corresponding entry page.

### 6. Random Page
Similarly, the sidebar contains a link that will bring the User to one out of all the existing entries in the web application randomly.

## How to Use
Django, Python-Markdown2 has to be installed before trying to use this web application. Running python3 manage.py runserver will allow you to run the code on a local server.

## Learning Outcomes

* Learnt and Familiarised with the Django Framework
* Learnt about Django Templating
* Learnt how to use filters within Django Templates
* Learnt about the HyperText Transfer Protocol (HTTP) requests and responses. Specifically, GET and POST requests.
* Learnt about URL Routes
* Learnt how to write and use Django Forms
* Learnt about Sessions to store data for Users.
* Learnt about the Bootstrap Framework.

## Video Link
https://youtu.be/8Dw67lThVFY