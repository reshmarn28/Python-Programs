#reading a source code for a website
import urllib.request
file = urllib.request.urlopen("www.google.com")
print(file.read())