import urllib
file = urllib.urlopen('http://www.korea.kr/main')
htmlcontents = file.read()
print htmlcontents
