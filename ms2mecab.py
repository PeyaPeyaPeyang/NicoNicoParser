import pandas
import jaconv
import csv

fname = "nicoime_msime.txt"

cols = []

with open(fname, mode="r", encoding="utf-8") as f:
    cols = pandas.read_csv(f, sep="\t", header=None, names=("yomi","kaki","type"))

tar = []

for index, item in cols.iterrows():
    yomi = item[0]
    kaki = item[1]
    type = item[2]
    kata = jaconv.hira2kata(yomi)
    tar.append([kaki, -1, -1, -1, "名詞", type, "一般", "*", "*", "*", kaki, kata, kata])

with open("output.csv", "w", encoding="utf-8") as w:
    wri = csv.writer(w, lineterminator="\n")
    wri.writerows(tar)
