# ftp_download_large_files
FTP: Download large files and keep connection alive for TLS server connection

This script downloads files one after another using a separate thread and also sends the FTP server 'NOOP' data in an attempt to keep the ftp server connection alive
