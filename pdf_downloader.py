execfile('constants')

import urllib2
for url in remote_urls:
     print "Downloading " + url
     file_name = url.split('/')[-1]
     u = urllib2.urlopen(url)
     f = open('pdf_files/' + file_name, 'wb')
     f.write(u.read())
     f.close()
     u.close()
