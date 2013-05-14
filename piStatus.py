#!/usr/bin/python

import socket;
import os;
import commands;


output = commands.getoutput('ps -A')
if 'sshd' in output:
    print "ITS ALIVE!!!"

print(socket.gethostbyname(socket.gethostname()));
