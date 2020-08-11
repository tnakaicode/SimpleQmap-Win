# -*- coding:utf-8 -*- 
"""

SimpleQmap は量子カオス系数値計算の入門を目的として作りました．
ソースコードの大半はpythonで実装しています.
一部c言語をctypesから読んでいますが，opiton扱いです．

2016年に若干の修正とチュートリアルと加筆しました．
SimpleQmapはできの良いプログラムではないので，
最終的に自身ですべてのプログラムを再構築することをおすすめします．


"""

__version__='0.3.1'


from SimpleQmap.state import *
from SimpleQmap.qmap import *
from SimpleQmap.maps import *

import SimpleQmap.utility
