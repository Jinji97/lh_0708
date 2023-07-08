
url = "http://jky.yangtzeu.edu.cn/system/resource/code/datainput.jsp?owner=1739830867&e=1&w=1707&h=960&treeid=1265&refer=aHR0cDovL2preS55YW5ndHpldS5lZHUuY24vaW5kZXguaHRt&pagename=L2NvbnQuanNw&newsid=3926"

import requests

i = 0
while i < 1000:
    requests.get(url)
    i = i+1
    print(i)