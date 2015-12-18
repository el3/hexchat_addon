# hexchat translate

To use this addon you will need to install textblob
<pre>
pip install -U textblob
python -m textblob.download_corpora
</pre>

Place the translate.py in /home/user folder

Place plugin.py in /home/user/.config/hexchat/addons

mkdir if addons does not exist

Change the YOUR_PYTHON variable in plugin.py to the python version you installed textblob.

This is because hexchat uses default python, so subprocess is used to call the translate.py script from your python version.
