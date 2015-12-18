__module_name__ = "hexchat_translator"
__module_version__ = "0.2"
__module_description__ = "Python module to translate messages in hexchat"
__author__ = "el3"

import hexchat
from textblob import TextBlob

print "Hexchat Translator loaded"

def echo(word, word_eol, userdata):
    try:
        original = TextBlob(word_eol[3][1:].decode("utf-8"))
        lang = original.detect_language()
        nick = word[0].split("!")[0].replace(":","")
        if lang != "en":
            res = original.translate(from_lang=lang,to='en')
        if len(res) > 0:
            print('\037\00304 ' + nick + " said: " + str(res).replace("\n","") + " (From lang=%s)" % str(lang))
        return hexchat.EAT_NONE
    except:
        return hexchat.EAT_NONE

hexchat.hook_server("PRIVMSG", echo)
