import urllib.request
url = urllib.request.urlopen("https://www.youtube.com/user/guru99com")
print("result code:"+str(url.getcode()))
data = url.read()
print(data)