import urllib
from bs4 import BeautifulSoup

url = "US08621662-20140107.XML"
xml = urllib.urlopen(url)
soup = BeautifulSoup(xml, "xml")

invention_title_tag = soup.find("invention-title")
print invention_title_tag.get_text()
