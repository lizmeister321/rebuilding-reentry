from bs4 import BeautifulSoup

# Load up the search results page
doc = open("search_results.html", "r")
data = doc.read()
doc.close()

# Use BeautifulSoup to pull out all the links
soup = BeautifulSoup(data, 'html.parser')
links = soup.find_all("a")

# Build an array of all the links to PDFs
pdfs = []
for link in links:
     try:
             url = link['href']
             if re.search('\.pdf$', url):
                     pdfs.append(url)
     except KeyError: # Some of the links don't have hrefs, skip 'em 
             pass
