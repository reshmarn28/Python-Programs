#program for reading a web page from internet and saving it in our system
import urllib.request
try:
    fi = urllib.request.urlopen("https://www.python.org/")
    content = fi.read()
except urllib.error.HTTPError:
    print("webpage does not exist")
    exit()
f = open("myfile.html",'wb')
f.write(content)
f.close()