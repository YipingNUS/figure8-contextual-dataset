#!/usr/bin/env python
# coding: utf-8

#install newspaper dependency
get_ipython().system('pip install newspaper3k')

import os.path as path
from os import mkdir
from tqdm.notebook import trange
import requests

from newspaper import fulltext

#parameters, change if necessary
CORPUS_ROOT_PATH = 'corpus/'

OFFSET = 0

with open('figure8_iab.csv', 'r') as f:
    lines = [line.strip() for line in f.readlines()][OFFSET+1:]


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'}

for i in trange(len(lines)):
    line = lines[i]
    t1, t2, url = line.split(",")
    text = None
    try:
        if not url.startswith("http"):
            url = "http://" + url
        res = requests.get(url, headers=headers, timeout=10)
        html = res.text
        text = fulltext(html)
    except Exception as e:
        print(e)
    if not text or res.status_code != 200:
        print("cannot scrap url:", url)
        continue
        
    t1_path = path.join(CORPUS_ROOT_PATH, t1)
    if not path.exists(t1_path):
        mkdir(t1_path)
    if t2:
        t2_path = path.join(t1_path, t2)
        if not path.exists(t2_path):
            mkdir(t2_path)
        out_path = path.join(t2_path, str(i+OFFSET)+".txt")
    else:
        out_path = path.join(t1_path, str(i+OFFSET)+".txt")
        
    with open(out_path, "w+") as f_out:
        print(out_path)
        f_out.write(text)

