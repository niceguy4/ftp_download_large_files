# ftp_download_large_files
## Download large files and keep connection alive over FTP TLS using Python's ftplib

This python script connects to FTP server using TLS connection, downloads files one after another, and uses a separate processing thread to send the FTP server 'NOOP' data in an attempt to keep the server connection alive. 

The code may throw exceptions from ftplib ***and*** still continue with the download. 

FTP connects with TLS
```
ftp = FTP_TLS()
```

Edit and replace the FTP server variables in py file to your FTP infomation.
```
FTPURL = 'mylittlepony.someurl.com'
Port = 6969
Username = 'xXxSlayerxXx'
Password = 'hunter1'
```

Edit the downloads variable (this is a list of lists) to indicate the name of your local (your computer) file save and the FTP's file pathname to download the file.
```
downloads = [['How.to.Count.Sand.Grains.as.a.Hobby.S15E59.VHS.mkv', '/files/morefiles/lessfiles/downloads/How.to.Count.Sand.Grains.as.a.Hobby.S15E59.VHS.mkv'],
             ['How.to.Count.Sand.Grains.as.a.Hobby.S15E60.VHS.mkv', '/files/morefiles/lessfiles/downloads/How.to.Count.Sand.Grains.as.a.Hobby.S15E60.VHS.mkv'],
             ['How.to.Count.Sand.Grains.as.a.Hobby.S15E61.VHS.mkv', '/files/morefiles/lessfiles/downloads/How.to.Count.Sand.Grains.as.a.Hobby.S15E61.VHS.mkv']]
```

Semi-related issues found on *stackoverflow* that this script attempts to resolve. These links talk about issues with downloading large files and the server dropping the connection. Also discussed is how to handle 'NOOP' command *'ping'* to keep the connection alive.

[ftplib-error-perm-550-operation-not-permitted-when-trying-to-download-the-sec](https://stackoverflow.com/questions/73534659/ftplib-error-perm-550-operation-not-permitted-when-trying-to-download-the-sec)

[python-file-download-using-ftplib-hangs-forever-after-file-is-successfully-down/49988443#49988443](https://stackoverflow.com/questions/49976095/python-file-download-using-ftplib-hangs-forever-after-file-is-successfully-down/49988443#49988443)

[ftplib-error-perm-550-operation-not-permitted-when-trying-to-download-the-sec](https://stackoverflow.com/questions/73534659/ftplib-error-perm-550-operation-not-permitted-when-trying-to-download-the-sec)

## Run
```
python ftp_download_large_files.py
```
