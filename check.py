#! python3
# -*- coding: utf-8 -*-

import glob
import re
from collections import deque

token_re = re.compile(r'([一-鿐]+[A-Za-z][0-9A-Za-z_]*|[\u30A1-\u30FF]+)')
token_pos = {}

for fname in glob.glob('ch*md'):
    print(fname)
    with open(fname, 'r', encoding='utf-8') as f:
        n = 0
        for line in f:
            n += 1
            if  line.startswitch('> ■'):
                continue
            tokens = token_re.findall(line)
            for t in tokens:
                token_pos.setdefault(t,[])
                token_pos[t].append(fname + ':' + str(n))
                
last_tokens = deque([('', 0)] * 3)
def p_and_print(t, length):
    last_tokens.popleft()
    last_tokens.append((t, length))
    if last_tokens[1][1] == 1:
        t1 = last_tokens[1][0]
        print(t1 + ',' + str(token_pos[t1][0]), end=',')
        print(str(last_tokens[0]) + ',' + str(last_tokens[2]))
    
for t in sorted(token_pos.keys()):
    p_and_print(t, len(token_pos[t]))