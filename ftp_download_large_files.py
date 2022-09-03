# this script downloads files one after another and attempts to keep the
# ftp server connection alive during large file downloads
# script is setup for FTP TLS connections

from ftplib import FTP_TLS
import threading
import time


# variables with example inputs.
# add your ftp server information
# FTP URL, FTP PORT, FTP Username/Password
FTPURL = 'mylittlepony.someurl.com'
Port = 6969
Username = 'xXxSlayerxXx'
Password = 'hunter1'

# downloads varbiable is a list of lists.
# the 1st place is for the local file download save name
# the 2nd place is for the FTP filename download path
downloads = [['How.to.Count.Sand.Grains.as.a.Hobby.S15E59.VHS.mkv', '/files/morefiles/lessfiles/downloads/How.to.Count.Sand.Grains.as.a.Hobby.S15E59.VHS.mkv'],
             ['How.to.Count.Sand.Grains.as.a.Hobby.S15E60.VHS.mkv',
                 '/files/morefiles/lessfiles/downloads/How.to.Count.Sand.Grains.as.a.Hobby.S15E60.VHS.mkv'],
             ['How.to.Count.Sand.Grains.as.a.Hobby.S15E61.VHS.mkv', '/files/morefiles/lessfiles/downloads/How.to.Count.Sand.Grains.as.a.Hobby.S15E61.VHS.mkv']]


def start_download(item_download):
    with open(str(item_download[0]), 'wb') as f:
        try:
            with ftp.transfercmd(f"RETR {str(item_download[1])}") as sock:
                print(f'Saving: {item_download[0]}')
                while True:
                    block = sock.recv(1024*1024)
                    if not block:
                        break
                    f.write(block)
                sock.close()
                ftp.voidresp()
            print('Download complete.')
        except Exception as handle_errors:
            # may receive errors from connection but still
            # continue with successful download
            print(f'handle_error msg: {handle_errors}')
            pass


# ftp connection
try:
    ftp = FTP_TLS()

    # remove # for debuglevel if you are having issues. will provide debug details
    # ftp.set_debuglevel(2)

    # connect to ftp server and login
    ftp.connect(FTPURL, Port)
    print(f'Connecting to {FTPURL}')
    ftp.login(Username, Password)
    print(f'Login requested.')

    # ftp server may require prot_p for secure ftp connections
    ftp.prot_p()

    ftp.voidcmd('TYPE I')

except Exception as ftp_setup_error:
    print(f'Issue with connection setup: {ftp_setup_error}')

# call start_download function
# keep connection alive by sending 'NOOP' posts
for item_download in downloads:

    # start separate download thread
    thread1 = threading.Thread(
        target=start_download, args=[item_download])
    thread1.start()
    time.sleep(.5)

    # while in start_download thread/function this sends pings/cmds to server
    # and then waits for the thread to be complete before continuing forward
    count = 0
    while thread1.is_alive():
        try:
            # this is waiting start_download thread/function to complete
            # and it being checked every 60 seconds. in-between waits
            # a 'ping-style' command is sent to server
            thread1.join(60)
            print('Pinging ftp server to keep connection alive...')
            count = count + 1
            ftp.putcmd('NOOP')
        except:
            pass

    # pings are sent to server from above while function
    # this for loops accepts/receives the server NOOP responses
    for _ in range(count):
        try:
            ftp.getresp()
        except:
            pass
