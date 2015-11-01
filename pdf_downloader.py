import urllib2

remote_urls = [line.rstrip('\n') for line in open('remote_urls')]

for url in remote_urls:
     print "Downloading " + url
     file_name = url.split('/')[-1]
     u = urllib2.urlopen(url)
     f = open('pdf_files/' + file_name, 'wb')
     f.write(u.read())
     f.close()
     u.close()
