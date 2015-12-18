__module_name__ = "hexchat_translator"
__module_version__ = "0.2"
__module_description__ = "Python module to translate messages in hexchat"
__author__ = "el3 and aq2"

try:
    import hexchat
except ImportError:
    exit("This program is a HexChat plugin, not a standalone program.")
from textblob import TextBlob
import threading

# Change this to set a different language
my_language = "en"


threads = []

def echo(word, word_eol, userdata):
    global my_language
    try:
        original = TextBlob(word_eol[3][1:].decode("utf-8"))
        lang = original.detect_language()
        nick = word[0].split("!")[0].replace(":","")
        if lang != my_language:
            res = original.translate(from_lang=lang, to=my_language)
        if len(res) > 0:
            print("\037\00312" + nick + " said: " + str(res).replace( \
                  "\n","") + " (From lang=%s)" % str(lang))
        return hexchat.EAT_NONE
    except:
        return hexchat.EAT_NONE

def echothread(word, word_eol, userdata):
    global threads
    threads.append(threading.Thread())
    threads[-1].run = lambda: echo(word, word_eol, userdata)
    threads[-1].start()

def unload_cb(userdata):
    print("Hexchat Translator unloaded")

hexchat.hook_server("PRIVMSG", echothread)
hexchat.hook_unload(unload_cb)

print("Hexchat Translator loaded")
