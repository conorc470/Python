# Web Scraping
webbrowser      #Comes with Python and opens a browser to a specific page.
Requests        #Downloads files and web pages from the Internet.
Beautiful Soup  #Parses HTML, the format that web pages are written in.
Selenium        #Launches and controls a web browser. Selenium is able to fill in forms and simulate mouse clicks in this browser.

# webbrowser
import webbrowser
webbrowser.open('http://google.com/')

# requests
>>> import requests
>>> res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
>>> res.raise_for_status() #will raise an exception if there was an error downloading the file
>>> type(res)
<class 'requests.models.Response'>
>>> res.status_code == requests.codes.ok
True
>>> len(res.text)
178981
>>> print(res.text[:250])
# downloads a web page and prints first 250 characters

# Saving downloaded files to the hard drive
>>> import requests
>>> res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
>>> res.raise_for_status()
>>> playFile = open('RomeoAndJuliet.txt', 'wb') #wb used to maintain unicode encoding of text
>>> for chunk in res.iter_content(100000): #iter_content returns chunks of the content on each iteration of loop
        playFile.write(chunk) #write content to the file
>>> playFile.close()

# Beautiful Soup - a module for extracting information from an HTML page
pip install beautifulsoup4  #to install
import bs4                  #to import

# download main page from website and pass the text attribute of response to bs4.BeautifulSoup
>>> import requests, bs4
>>> res = requests.get('http://nostarch.com')
>>> res.raise_for_status()
>>> noStarchSoup = bs4.BeautifulSoup(res.text)

# Finding an element with select() method
soup.select('div') # gets all elements named <div>

# get() method passes string of an attribute name and returns that attributes value
>>> spanElem.get('id')
'author'

