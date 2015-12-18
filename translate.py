import sys
from textblob import TextBlob


original = TextBlob(unicode(sys.argv[1]))
lang = original.detect_language()
if lang != "en":
     print original.translate(from_lang=lang,to='en'),"(From lang=%s)" % lang
