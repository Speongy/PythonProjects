'''
scan given hostname for anonymous ftp connection

let's us input anonymous as the user and grant access to file transfer
'''

import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print('\n [+] ' + str(hostname) + ' anon login success.')
        ftp.quit()
        return True
    except Exception:   
        print('\n [-] ' + str(hostname) + ' anon login failed.')
        return False

if __name__ == '__main__':
    anonLogin('90.130.70.73')   #IP for speedtest.tele2.net

#? I think they got tired of everyone spamming anonymous ftp login, so it keeps failing