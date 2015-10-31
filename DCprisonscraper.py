from datetime import date, timedelta, datetime
import urllib
import urllib2

#import slate 


#GOAL: Create a weekly tracker of DC prison populations in a web-searchable database
#STEPS: 
#    1. Access DC DOC webpage and save stats sheet locally to github folder
#    2. Scrape PDF and convert to a usable table of data
#    3. Save data into some kind of database
#    4. Create some kind of web interface to quickly access data
#		--include graphical representation?
#		--Post files to web interface for download?



# STEP 1: Access DC DOC website--url changes weekly
# #### NOTE: Week in data runs Sat-Friday
# #### ASSUME PULL RUNS ON A SATURDAY 

start_date= date.today()-timedelta(7)
end_date=date.today()-timedelta(1)

start_month=start_date.strftime('%B')
start_day= start_date.strftime('%d')
start_year=start_date.strftime('%Y')

end_month=end_date.strftime('%B')
end_day=end_date.strftime('%d')
end_year=end_date.strftime('%Y')

data_url_prefix = 'doc.dc.gov/sites/default/files/dc/sites/doc/publication/attachments/'



	data_url_suffix = start_month + ' ' + start_day +  ' through ' + end_month + ' ' + end_day + ' ' + year+ '.pdf'
	data_url_full= data_url_prefix + data_url_suffix	
	clean_url=urllib.quote(data_url_full)

clean_file='STATS_' + start_month + '-' + start_day + '_to_' + end_month + '-' + end_day + '-' + year


##CURRENTLY STUCK HERE: 
urllib.urlretrieve(urllib.quote(data_url_full),'test.pdf')
##returns the following:

# Traceback (most recent call last):
#   File "/Users/Lellis/Desktop/PythonStuff/Rebuilding-Reentry/DCprisonscraper.py", line 41, in <module>
#     urllib.urlretrieve(urllib.quote(data_url_full),'test.pdf')
#   File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib.py", line 98, in urlretrieve
#     return opener.retrieve(url, filename, reporthook, data)
#   File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib.py", line 245, in retrieve
#     fp = self.open(url, data)
#   File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib.py", line 213, in open
#     return getattr(self, name)(url)
#   File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib.py", line 469, in open_file
#     return self.open_local_file(url)
#   File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib.py", line 483, in open_local_file
#     raise IOError(e.errno, e.strerror, e.filename)
# IOError: [Errno 2] No such file or directory: 'doc.dc.gov/sites/default/files/dc/sites/doc/publication/attachments/October 24 through October 30 2015.pdf'
# [Finished in 0.1s with exit code 1]


#IF start_date_year = end+date_year, then start_date is month/day
#ELSE start_date is month/day/year
#end_date is always month/day/year 











# from cStringIO import StringIO
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage





# output = StringIO()
# manager = PDFResourceManager()
# converter = TextConverter(manager, output, laparams=LAParams())
# interpreter = PDFPageInterpreter(manager, converter)

# pdf_file = file('August 1 through August 7 2015.pdf', "r")

