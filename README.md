# ftp_download_large_files
FTP: Download large files and keep connection alive for TLS server connection

This python script downloads files one after another and uses a separate thread to send the FTP server 'NOOP' data in an attempt to keep the server connection alive. 

This is setup for a TLS FTP connection.

Edit and replace the FTP variables in the py file to your infomation.

Edit the downloads list of lists for local filename save (where you want to save your file and its name) and the FTPs filename path to download the file.
