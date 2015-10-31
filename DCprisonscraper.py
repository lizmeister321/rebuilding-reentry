from datetime import date, timedelta, datetime
#import urllib
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
# #### ASSUME PULL RUNS ON A SUNDAY 
data_url_prefix = 'doc.dc.gov/sites/default/files/dc/sites/doc/publication/attachements/'
data_url_suffix = start_date + '%%20through' + end_date +'.pdf'

#IF start_date_year = end+date_year, then start_date is month/day
#ELSE start_date is month/day/year
#end_date is always month/day/year 

date.weekday() = 6

end_date = 

start_date = 
	if 


print date.today().strftime("%B" + '%%20' + '%d' +  '%%20through' + '%B' + '%%20' + '%d' + '%Y' + '.pdf') 		
start_date=date.today().strftime('%B' + '%%20' + '')



#Won't print %, will likely need to move to .format() method with dates as var


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

