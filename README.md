# ftp_download_large_files
## Download large files and keep connection alive over FTP TLS

This python script connects to FTP server using TLS connection, downloads files one after another, and uses a separate processing thread to send the FTP server 'NOOP' data in an attempt to keep the server connection alive. 

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

Edit the downloads list of lists for local filename save (where you want to save your file and its name) and the FTPs filename path to download the file.
```
downloads = [['How.to.Count.Sand.Grains.as.a.Hobby.S15E59.VHS.mkv', '/files/morefiles/lessfiles/downloads/How.to.Count.Sand.Grains.as.a.Hobby.S15E59.VHS.mkv'],
             ['How.to.Count.Sand.Grains.as.a.Hobby.S15E60.VHS.mkv',
                 '/files/morefiles/lessfiles/downloads/How.to.Count.Sand.Grains.as.a.Hobby.S15E60.VHS.mkv'],
             ['How.to.Count.Sand.Grains.as.a.Hobby.S15E61.VHS.mkv', '/files/morefiles/lessfiles/downloads/How.to.Count.Sand.Grains.as.a.Hobby.S15E61.VHS.mkv']]
```
