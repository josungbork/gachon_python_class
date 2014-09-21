# -*- coding: utf-8 -*-

import sys
import urllib

reload(sys)
company_code = ''
itooza_url = "http://www.itooza.com/vclub/y10_page.php?cmp_cd=005930&mode=dy&ss=10&sv=1&lsmode=1&accmode=1&lkmode=2"
url_data = urllib.urlopen(itooza_url)
htmlcontents = url_data.read()
print htmlcontents.encode("UTF-8")
