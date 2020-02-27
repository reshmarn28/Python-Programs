#program for retrieving different parts of url

import urllib.parse
url = "http://www.dreamtechpress.com:80/engineering/computer-science.html"
tpl = urllib.parse.urlparse(url)
print(tpl)
print("scheme = ",tpl.scheme)
print("net location = ",tpl.netloc)
print("path =",tpl.path)
print("parameter=",tpl.params)
print("port number=",tpl.port)
print("total url=",tpl.geturl())