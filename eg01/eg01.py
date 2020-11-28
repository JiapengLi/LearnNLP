import jieba
import sys
import json
import os
from datetime import datetime

def word_freq(folder, stpw_list):
    words = {}
    for filename in os.listdir(folder):
        if filename.endswith(".md") or filename.endswith(".html"): 
            with open(os.path.join(folder, filename), 'r', encoding = 'utf-8') as f:
                for line in f:
                    seg_list = jieba.cut_for_search(line.strip())
                    for seg in seg_list:
                        # remove unused data
                        if seg in stpw_list:
                            continue
                        
                        if seg in words.keys():
                            words[seg] += 1
                        else:
                            words[seg] = 1
    return words

def char_freq(folder, stpw_list):
    chars = {}
    for filename in os.listdir(folder):
        if filename.endswith(".md") or filename.endswith(".html"): 
            with open(os.path.join(folder, filename), 'r', encoding = 'utf-8') as f:
                for line in f:
                    for c in line.strip():
                        if c in chars.keys():
                            chars[c] += 1
                        else:
                            chars[c] = 1
    return chars

stpw = open('stop_words.txt', 'r', encoding='utf-8')
stpw_content = stpw.read()
seg_list = jieba.cut(stpw_content)
stpw_list = ['images', ' ', 'jpg', '###', '\n']
for seg in seg_list:
    if seg != '\n':
        stpw_list.append(seg)

# print(stpw_list)
# exit()

date_time = datetime.now().strftime("%Y%m%d-%H%M%S")

words = word_freq(sys.argv[1], stpw_list)
words = dict(sorted(words.items(), key=lambda item: item[0],reverse=True))
words = dict(sorted(words.items(), key=lambda item: item[1],reverse=True))

f = open(sys.argv[1] + f"/results-{date_time}.json", 'w', encoding='utf-8')
print(json.dumps(words, indent=4, default=str, ensure_ascii=False), file=f)
print(f'总词数：{len(words.keys())}', file=f)
f.close()


# words = char_freq(sys.argv[1], stpw_list)
# words = dict(sorted(words.items(), key=lambda item: item[0],reverse=True))
# words = dict(sorted(words.items(), key=lambda item: item[1],reverse=True))

# f = open(sys.argv[1] + f"/results-{date_time}.json", 'w', encoding='utf-8')
# print(json.dumps(words, indent=4, default=str, ensure_ascii=False), file=f)
# print(f'总词数：{len(words.keys())}', file=f)
# f.close()
