#!/usr/bin/python
import re, os

def get_authinfo_password_gmail(machine, login, port):
    s = "machine %s login %s password ([^ ]*) port %s" % (machine, login, port)
    p = re.compile(s)
    authinfo = os.popen("gpg -q --no-tty -d ~/.password-store/offlineimap/gmail.gpg").read()
    return p.search(authinfo).group(1)

def get_authinfo_password_tekno(machine, login, port):
    s = "machine %s login %s password ([^ ]*) port %s" % (machine, login, port)
    p = re.compile(s)
    authinfo = os.popen("gpg -q --no-tty -d ~/.password-store/offlineimap/tekno.gpg").read()
    return p.search(authinfo).group(1)
