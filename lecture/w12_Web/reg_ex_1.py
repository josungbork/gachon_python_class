import re
import urllib

url = "http://goo.gl/U7mSQl"
html = urllib.urlopen(url)
html_contents = str(html.read())
id_results = re.findall(r"([A-Za-z0-9]+\*\*\*)", html_contents)

for result in id_results: print result
