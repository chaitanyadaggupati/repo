import urllib
from lxml import etree
from lxml.html import fromstring
url='http://www.imd.gov.in/section/hydro/distrainfall/districtrain.html'
f=urllib.urlopen(url)
resp=f.read()
doc=fromstring(resp)
for i in doc.findall('.//li/a'):
    print i.text
