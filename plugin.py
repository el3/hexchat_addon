__module_name__ = "hexchat_translator"
__module_version__ = "0.1"
__module_description__ = "Python module to translate messages in hexchat"
__author__ = "el3"

YOUR_PYTHON = "/home/user/anaconda2/bin/python2.7" #example if you got anaconda

import hexchat
from textblob import TextBlob

def echo(word, word_eol, userdata):
    try:
        original = TextBlob(word_eol[3][1:])
        lang = original.detect_language()
        nick = word[0].split("!")[0].replace(":","")
        if lang != "en":
            res = original.translate(from_lang=lang,to='en'),"(From lang=%s)" % lang
        if len(res) > 0:
            print('\037\00304 '+ nick+" said: "+res.replace("\n",""))
        return hexchat.EAT_NONE
    except:
        return hexchat.EAT_NONE

hexchat.hook_server("PRIVMSG", echo)
