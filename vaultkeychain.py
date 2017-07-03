#!/usr/bin/env python
# -*- coding: utf-8 -*-

import keyring
import re
import os
import sys
from subprocess import Popen, PIPE
import getpass

import __builtin__
def raw_input(prompt=None):
    if prompt:
        sys.stderr.write(str(prompt))
    return __builtin__.raw_input()

out, err = Popen(["git", "config", "--get", "remote.origin.url"], stdout=PIPE, stderr=PIPE).communicate()
repo=re.sub(r'http(s)?:[/]{2}([^/]+)[/]', r'git@\2:', out.split('\n')[0])

if re.search('\S', repo):
    KEYRING_SERVICE = repo
else:
    KEYRING_SERVICE = os.getcwd()

username = "ansible-vault"

password = keyring.get_password(KEYRING_SERVICE, username )
if not password:
    password = getpass.getpass("Enter password for '%s':" % KEYRING_SERVICE)
    try:
        keyring.set_password(KEYRING_SERVICE, username, password)
    except keyring.errors.PasswordSetError:
        print >> sys.stderr, "failed to store password"

print password
