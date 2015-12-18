import sys
from textblob import TextBlob

recieve = sys.argv[1].decode('utf8')

original = TextBlob(recieve)

lang = original.detect_language()
if lang != "en":
     print original.translate(from_lang=lang,to='en'),"(From lang=%s)" % lang
