import urllib2, socket
from netaddr import *
import pprint

socket.setdefaulttimeout(180)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
proxyList=[]
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
ip= ip+"/24"
print ip
for i in IPNetwork(ip):
	proxyList.append(str(i)+':3128')

s.close()




def is_bad_proxy(pip):    
    try:        
        proxy_handler = urllib2.ProxyHandler({'http': pip})        
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)        
        req=urllib2.Request('http://www.google.com')  # change the url address here
        sock=urllib2.urlopen(req)
    except urllib2.HTTPError, e:        
        print 'Error code: ', e.code
        return e.code
    except Exception, detail:

        print "ERROR:", detail
        return 1
    return 0

for item in proxyList:
    if is_bad_proxy(item):
        print "Bad Proxy", item
    else:
        print item, "is working"