import nltk
import re
import RAKE

from tika import parser


raw = parser.from_file("JavaBasics-notes.pdf")

text = raw['content']
subs = [r'[A-Za-z \[\]]*=.*;', '//.*\n']
#subs = []
for sub in subs:
    text = re.sub(sub, '', text)
text = text.replace('\n',' ')   
text = re.sub(r'\{(.*?)\}', '', text)
text = re.sub(r'\[(.*?)\]', '', text)

#print(text)

unwanted_chars = '<([{\^-=$!|]})?*+.>•©'
for ch in unwanted_chars:
    text = text.replace(ch, ' ')


my_additional_stops = ['null', 'pointer', 'abstract','continue','switch','assert','goto','package','synchronized','private','this','break','double','implements','protected','throw','byte','else','import','public','throws','case','enum','instanceof','return','transient','catch','extends','int','short','try','char','final','interface','static','void','class','finally','long	strictfp','volatile','const','float','native','super','while']
new_stop_list = my_additional_stops + RAKE.SmartStopList()

Rake = RAKE.Rake(new_stop_list)
Rake.run(text, minCharacters=4, maxWords=4, minFrequency=2)

