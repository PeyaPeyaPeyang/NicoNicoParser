import glob
import shutil
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
year = ""

def b(f, size=1024*1024):
    l = os.path.getsize(f)
    div_num = (l + size - 1) / size
    last = (size * div_num) - l

    b = open(f, 'rb')
    for i in range(int(div_num)):
        read_size = last if i == div_num-1 else size
        data = b.read(read_size)
        out = open(f + str(i) + '.frac', 'wb')
        out.write(data)
        out.close()
    b.close()

def a(read_files):
    with open(year + ".text8", "wb") as outfile:
        for f in read_files:
            with open(f, "rb") as infile:
                outfile.write(infile.read())

def thread(command):
    subprocess.call(command)


while True:
    year = input("Input year >")

    if not os.path.exists("resources/"):
        os.mkdir("resources")
    if not os.path.exists("trashbox/"):
        os.mkdir("trashbox")
    if not os.path.exists("completed/"):
        os.mkdir("completed")

    shutil.move("resources/" + year + ".archive", "./")
    b(year + ".archive", 1024*1024*10)
    shutil.move(year + ".archive", "trashbox/")
    count = 0
    with ThreadPoolExecutor(max_workers=8) as executor:
        for dra in glob.glob("*.frac"):
            count += 1
            executor.submit(thread, "mecab -Owakati -b 1145141919 -o " + str(year) + "-" + str(count) + ".text8 " + dra)
    a(glob.glob("*.text8"))
    shutil.move(str(year) + ".text8", "completed/")
    for frac in glob.glob("*.frac"):
        os.remove(frac)
    for frac in glob.glob("*.text8"):
        os.remove(frac)
