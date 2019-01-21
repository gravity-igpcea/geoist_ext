# -*- coding: utf-8 -*-
# pass in Python3.6
import sys, json
import pandas as pd
import matplotlib.pyplot as plt
import pathlib
import shutil

# part 1 ----------读取JSON接口参数---------- #
argfile=sys.argv[1] #json参数  
print('debug: open//'+argfile) 
with open(argfile,'rb') as f:
    data = json.load(f)
	

shutil.copy(argfile,  'C:\\DssTech\\Datist.Worker\\BinX\\Plugin\\TsTools_zhangbei\\TsTools.JSON')
	
print(argfile)
####--------------End PART ONE--------------####
