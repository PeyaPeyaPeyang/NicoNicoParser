# NicoNicoParser

## 概要

ニコニコ大百科と掲示板データを分かち書き可能なレベルまでパースします。

## 動作環境
+ Python 3.7+

### NicoNicoIME2Mecab

ニコニコ大百科IME辞書\(通称ニコニコIME\)を、Mecabが読める状態までパースします。  
+ Microsoft IME 用のインプットファイルが動作します。

#### 使用法

+ 1.書き換え
```
5: fname = "niconicoime_msime.txt" => 自分が持つファイルに変更
```
+ 2.実行
```
$ python ms2ime.py

```
### NicoNicoExtractor

#### 使用法

+ 1.実行  
```
$ python nikonikoparser.py
```
+ 2.年を入力  
大百科とかのパースで、年ごとにファイルが違うことがあるため  
+ 3.待つ  
CPUの性能で大幅に変わります。(メモリは1GBもいりません)  

### 作成されるディレクトリとか

+ complete  
パースされたデータが入ります。すべて完了すると、../<year>.archive として保存されます。  
