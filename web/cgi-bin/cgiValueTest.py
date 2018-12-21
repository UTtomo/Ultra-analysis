#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi

html_body = """
<!DOCTYPE html>
<html>
<head>
<title>受信したデータを表示</title>
<style>
h1 {
font-size: 3em;
}
</style>
</head>
<body>
<p>%s</p>
<p>%s</p>
<p>%s</p>
<p>%s</p>
<p>%s</p>


</body>
</html>
"""

form = cgi.FieldStorage()
text1 = form.getvalue('value','')
text2 = form.getvalue('value2','')
text3 = form.getvalue('value3','')
text4 = form.getvalue('value4','')
text5 = form.getvalue('value5','')
mari = 1


print(html_body % (text1,text2,text3,text4,text5))
print("%s%s%s%s%s"% (text1,text2,text3,text4,text5))


