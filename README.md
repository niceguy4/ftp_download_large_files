# ftp_download_large_files
##FTP: Download large files and keep connection alive for TLS server connection

This python script downloads files one after another and uses a separate thread to send the FTP server 'NOOP' data in an attempt to keep the server connection alive. 

This is setup for a TLS FTP connection.
'''
ftp = FTP_TLS()
'''

Edit and replace the FTP variables in the py file to your infomation.
'''
FTPURL = 'mylittlepony.someurl.com'
Port = 6969
Username = 'xXxSlayerxXx'
Password = 'hunter1'
'''

Edit the downloads list of lists for local filename save (where you want to save your file and its name) and the FTPs filename path to download the file.
'''
downloads = [['How.to.Count.Sand.Grains.as.a.Hobby.S15E59.VHS.mkv', '/files/morefiles/lessfiles/downloads/How.to.Count.Sand.Grains.as.a.Hobby.S15E59.VHS.mkv'],
             ['How.to.Count.Sand.Grains.as.a.Hobby.S15E60.VHS.mkv',
                 '/files/morefiles/lessfiles/downloads/How.to.Count.Sand.Grains.as.a.Hobby.S15E60.VHS.mkv'],
             ['How.to.Count.Sand.Grains.as.a.Hobby.S15E61.VHS.mkv', '/files/morefiles/lessfiles/downloads/How.to.Count.Sand.Grains.as.a.Hobby.S15E61.VHS.mkv']]

'''
