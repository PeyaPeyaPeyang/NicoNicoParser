import re
import csv
import shutil
import os
import glob

files = glob.glob("*.csv")
year = input("Enter Year >")
if os.path.exists('complete') != False:
    os.mkdir('complete')
target = 1  #1なら大百科、3が掲示板
for f in files:
    fName = f[:-4]
    s = []
    with open(fName + ".csv", mode="r",encoding="utf-8_sig") as p:
        s = p.readlines()
    csv.field_size_limit(1145141919)
    reader = csv.reader(s)
    fars = []
    for far in reader:
        fars.append(far[target])
    reader = None
    re1 = re.compile("\\\\$")
    re2 = re.compile("<.*?>")
    fars1 = []
    for ava in fars:
        with open(fName + ".raw.txt", mode="a",encoding="utf-8_sig") as p:
            p.write(re.sub(re1, "", re.sub(re2, "", ava)))
    s = None
    fars = None
    re1 = None
    re2 = None
    fars1 = None
    
    
    
    s = []
    
    with open(fName + ".raw.txt", mode="r",encoding="utf-8_sig") as p:
        s = p.readlines()
    sp = []
    cmp = re.compile("^\\\\$")
    with open(fName + ".raw2raw.txt", mode="a", encoding="utf-8_sig") as w:
        for ss in s:
            if cmp.match(ss):
                continue
            w.write(ss[:-2] + "\n")
            print(ss[:-2] + "\n")
    os.remove(fName + ".csv")
    os.remove(fName + ".raw.txt")
    shutil.move(fName + ".raw2raw.txt", "completed/" + fName + ".raw2raw.txt")
cfiles = glob.glob("completed/*.txt")
for cfile in cfiles:
    shutil.move(cfile, "./")

read_files = glob.glob("*.txt")

with open(year + ".archive", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
for f in read_files:
    os.remove(f)
