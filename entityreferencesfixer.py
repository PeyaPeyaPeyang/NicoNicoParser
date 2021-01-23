import glob
import shutil
import os
import subprocess
import logging

from concurrent.futures import ProcessPoolExecutor
year = ""

def b(infilepath, chunksize):
    fname, ext = infilepath.rsplit('.',1)
    i = 0
    written = False
    with open(infilepath, encoding="utf_8_sig",errors="ignore") as infile:
        while True:
            outfilepath = "{}{}.{}".format(year, i, "frac")
            with open(outfilepath, 'w', encoding="utf_8_sig",errors="ignore") as outfile:
                for line in (infile.readline() for _ in range(chunksize)):
                    outfile.write(line)
                written = bool(line)
            if not written:
                break
            i += 1

def a(read_files):
    with open(year + ".p.text8", "w", encoding="utf_8_sig",errors="ignore") as outfile:
        for f in read_files:
            with open(f, "r", encoding="utf_8_sig",errors="ignore") as infile:
                outfile.write(infile.read())

def thread(command,year):
    gh = []
    try:
        with open(year + ".fyn", "a", encoding="utf_8_sig",errors="ignore") as g:
            with open(command,"r", encoding="utf_8_sig",errors="ignore") as b:
                for f in b.readlines():
                    if f in gh:
                        continue
                    gh.append(f)
                    f = f.replace("&nbsp;", "　").replace("& nbsp ;", "　").replace("&amp;", "&").replace("& amp ;", "&").replace("&lt;","<").replace("&gt;",">").replace("& lt ;","<").replace("& gt ;",">")
                    g.write(f)
        os.remove(command)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    while True:
        year = input("Input year >")

        if not os.path.exists("resources/"):
            os.mkdir("resources")
        if not os.path.exists("trashbox/"):
            os.mkdir("trashbox")
        if not os.path.exists("completed/"):
            os.mkdir("completed")
        shutil.move("completed/" + year + ".text8", "./")
        b(year + ".text8", 1024*10)
        shutil.move(year + ".text8", "trashbox/")
        count = 0
        with ProcessPoolExecutor(max_workers=4) as executor:
            for dra in glob.glob("*.frac"):
                count += 1
                executor.submit(thread, dra, year)
        a(glob.glob("*.fyn"))
        shutil.move(str(year) + ".p.text8", "completed/")
        for frac in glob.glob("*.fyn"):
            os.remove(frac)
