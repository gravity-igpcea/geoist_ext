# -*- coding: utf-8 -*-
# Python3.6
import sys
import json
import codecs
 
argfile=sys.argv[1] #'par2.json'  
print('debug:'+argfile) #json缓存地址
#data=json.loads(open(argfile).read().decode('utf-8-sig'))
#data=json.loads(open(argfile).read())
with open(argfile,'rb') as f:
    data = json.load(f)

#前节点的输出文件名 
print('--NodeTest.py by bushyao--')
print('debug: 1st debug Info!')

print('magdata:' + data['magdata'])
print('magdata2:' + data['magdata2'])
print('OutputPath:' + data['OutputPath'])
print('ResultFile:' + data['ResultFile'])

print('中s文永远是个坑')
print('title:' + data['pars']['title'])
print('desc:' + data['pars']['desc'])

print('Debug:2st debug Info!')
#输出一个文件
print("D:\\MyProgram\\RDMS\\PPTAnalysis\\binX\\Plugin\\test\\tmpData\\asia150dpi.png")

#输出数据表格文件
print("D:\\MyProgram\\RDMS\\PPTAnalysis\\binX\\Plugin\\test\\tmpData\\tmp5DAC.csv")

#输出网页
print("http://www.baidu.com")   #输出网络地址
 
