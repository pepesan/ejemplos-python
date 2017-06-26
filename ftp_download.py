# -*- coding: utf-8 -*-


import os
from ftplib import FTP

ftp = FTP("www.myWebsite.com", "USERNAME", "PASSWORD")
ftp.login()
ftp.retrlines("LIST")

ftp.cwd("folderOne")
ftp.cwd("subFolder")  # or ftp.cwd("folderOne/subFolder")

listing = []
ftp.retrlines("LIST", listing.append)
words = listing[0].split(None, 8)
filename = words[-1].lstrip()

# download the file
local_filename = os.path.join(r"c:\myfolder", filename)
lf = open(local_filename, "wb")
ftp.retrbinary("RETR " + filename, lf.write, 8 * 1024)
lf.close()