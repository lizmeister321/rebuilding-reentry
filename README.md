# rebuilding-reentry
The DC DOC publishes weekly prison population stats in PDF form on their website. The aim of this project is to download the weekly PDF stats, scrape, and collect the data...somewhere.

Tied to the Rebuilding Re-Entry project at Techlady Hackathon #3 (more here:https://techlady.hackpad.com/)

Also part of Rebuildilng Re-entry Hackathon Oct 31, 2015. Project Hackpad here: https://hackpad.com/Scraping-DC-Prison-PDFs-6tmwUOzdXFo

Latest stats URL (as of August 8, 2015):
http://doc.dc.gov/sites/default/files/dc/sites/doc/publication/attachments/August%201%20through%20August%207%202015.pdf

## Valerie's Scraper Instructions
tl;dr Valerie scraped the PDF files she found via Google and ran them through Tabula. The PDF files are in the `pdf_files` folder, the csvs generated are in the `csv_files` folder, the script used to generate them (which can probably be tweaked to get better results is `tabula_extractor.rb`

### The long (hacky) version
**Finding the PDFs**
The Google search `DAILY OPERATING POPULATION COUNTS BY FACILITY site:doc.dc.gov/sites/default/files/dc/sites/doc/publication/attachments/` returns a bunch of past PDFs. [Link to these search results](https://www.google.com/search?q=DAILY+OPERATING+POPULATION+COUNTS+BY+FACILITY+site:doc.dc.gov/sites/default/files/dc/sites/doc/publication/attachments/&num=100&biw=1415&bih=725&filter=0).

**Getting the PDFs**
I saved the HTML page of these search results locally as `search_results.html` (my version of this file is also stored in this repo).

I then parsed through this file in Python using [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/). If you've never used this before, you may need to run `pip install beautifulsoup4` to install it first. The script I used is in `results_parser.py`. In plain English, it:
* Loads the contents of a page into a Python string
* Calls BeautifulSoup's HTML parser on the string
* Uses BeautifulSoup's functionality to find all the links on the page
* Extracts the url of these links
* Saves the links ending in '.pdf' in an array

Now I had a list of all of the URLs I wanted to download. (Available in the `constants` file)

From there, I wrote a script, `pdf_downloader.py` to download each of them. Those PDFs are now in the `pdf_files` directory in this repo.

**Parsing into CSV**
This part was the trickiest in terms of configuration. It requires both JRuby and Tabula. The best way we found to install JRuby was via [RVM](https://rvm.io/). Once you've got RVM installed, run:
```
rvm install jruby
rvm use jruby
```

Now install tabula with:
```
jruby -S gem install tabula-extractor
```

The script used for generating the (admittedly wonky) csvs in `csv_files` is at `tabula_extractor.rb`

**Next steps**
* Play with tabula to see if we can get better parsing results
* Filter the PDFs to just the ones with just the information/formatting we want
* Try automated ways of figuring out if there are more PDFs than the ones in the search results (without DDoSing the DC DOC)
* Make the information available in a REST API type format
* Look at/allow other people to play with the data to see what they find
* Automatically scrape new PDFs from the DOC website and parse them
