# taken directly as a copy past from https://www.binpress.com/tutorial/manipulating-pdfs-with-python/167
# this function reads in a pdf and save it out as a python variable
#requires that pdfminer is installed, pip install works fine
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text 
    
#now using this function look at whatever pdf file it is
#here I've named is test.pdf, obviously this is a placeholder at the momentito
    
text = convert('301pdf.pdf')
#now let's tokenize this sucker into something meaningful
#splitting on the new line
token_text = text.split('\n')
new_text = []
#let's get rid of everything that's just nothing
for token in token_text:
    if token != '':
        if not token.isspace():

            new_text.append(token)

## the pdf set up changed sometime in 2012-2013 so let's
#make sure we're doing the right thing.
if new_text[0] == 'DAILY OPERATING POPULATION COUNTS BY FACILITY':
    new_flag = True
elif new_text[0] == 'DAILY POPULATION REPORT':
    new_flag = False
else:
    new_flag = 'Unknown pdf type!!'
#Starting simple with Adult Males at the central detention facility operations
#look for the 'males'
#def find_data_for_column(column_name):
    
for num, words in enumerate(new_text):
    if "Males" in words:
        adult_spot = num + 1
        break
#treatments
for num, words in enumerate(new_text):
    if words == 'USMS Greenbelt MD Inmates':
        adul_mal_treat = num + 1
        break
    
print new_flag
        
        