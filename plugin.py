__module_name__ = "hexchat_translator"
__module_version__ = "0.1"
__module_description__ = "Python module to translate messages in hexchat"
__author__ = "el3"

YOUR_PYTHON = "/home/user/anaconda2/bin/python2.7" #example if you got anaconda

import hexchat
import sys,os
print sys.version
from subprocess import Popen,PIPE

print os.getcwd()

def echo(word, word_eol, userdata):
    try:
        p1 = Popen([YOUR_PYTHON, "translate.py", word_eol[3][1:]], stdout=PIPE,stderr=PIPE)
        res,err = p1.communicate()
        #print err
        nick = word[0].split("!")[0].replace(":","")
        if len(res) > 0:
            print('\037\00304 '+ nick+" said: "+res.replace("\n",""))
        return hexchat.EAT_NONE
    except:
        return hexchat.EAT_NONE

hexchat.hook_server("PRIVMSG", echo)

