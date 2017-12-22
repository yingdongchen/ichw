"""wcount.py: count words from an Internet file.

__author__ = "Yingdongchen"
__pkuid__  = "1700011748"
__email__  = "1700011748@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """

    m=lines
    for c in string.punctuation:   
        m = m.replace(c,'') 
        k=m.split()
        q=[]
    for i in k:
        if i not in q:
            q=q.append(i)
    t=0
    d=0
    p={}
    for t in q:
        for i in k:
            if i==t:
                d=d+1
            else:
                d=d
        p[t]=d
    sorted(p.items(), key=lambda kv:kv[1],reverse=True)
for key in p:  
    print(key, p[key])
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
