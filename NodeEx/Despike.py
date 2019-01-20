# -*- coding: utf-8 -*-
# pass in Python3.6 
import sys, json
import pandas as pd
import matplotlib.pyplot as plt
import pathlib
# part 1 ----------读取JSON接口参数---------- #
argfile=sys.argv[1] #json参数  
print('debug: open//'+argfile) 
with open(argfile,'rb') as f:
    data = json.load(f)
print('debug: start//Despike.py by zhangbei')
####--------------End PART ONE--------------####

# part 2 ----------读取前节点界面参数---------- #
Threshold_str = data['pars']['Threshold']
print('debug: Threshold//'+str(Threshold_str))
Threshold = float(Threshold_str)                 
data_path = data['OutputPath']
orig_file = pathlib.Path(data_path,'gradata.txt')
na_values = None
date_format = None
print('debug: orig_file//'+str(orig_file))
####--------------End PART TWO--------------####

# part 3 ----------设置程序运行参数---------- #
thresh_hold = Threshold
pic_flag = 1 #vis method
# parameters for saving data
tmppath = pathlib.Path(__file__).parent
res_file = pathlib.Path(tmppath,'tmpData','gradata.csv')
png_file = pathlib.Path(tmppath,'tmpData','gradata.png')
html_file = pathlib.Path(tmppath,'tmpData','gradata.html')
####--------------End PART THREE--------------####

# part 4 ----------专业逻辑实现部分---------- #
if __name__ == '__main__':
    # output logging 
    import geoist as gi
    gi.log.setname('Datist_despike')
    gi.log.info('despike START')
    # data processing
    import geoist.snoopy.tsa as tsa
    d=pd.read_csv(pathlib.Path(orig_file),delimiter=';',parse_dates=True,index_col=[0],na_values=na_values)
    d['despiked'],d['flag'] = list(tsa.despike_v2(d.interpolate(),th=thresh_hold))
    d.to_csv(pathlib.Path(res_file),date_format=date_format,sep=';')
    gi.log.info('thresh_hold = ' + str(thresh_hold))
    gi.log.info('data length = ' + str(len(d['despiked'])))
    # output html
    if pic_flag == 1:
        import bokeh.plotting as bp
        from bokeh.palettes import Spectral4
        from bokeh.models import ColumnDataSource    
        p = bp.figure(title="The preliminary result by threshold = "+str(thresh_hold)
                     , plot_width=535, plot_height=350, x_axis_type="datetime")
        bp.output_file(html_file, mode = 'inline')
        source = ColumnDataSource(d)
        for data, name, color in zip([source.column_names[1], source.column_names[2]], ["ORI", "DeSpiked"], Spectral4):
           p.line(source.column_names[0], data, source=source,color=color, alpha=0.8, legend=name)
        p.xaxis.axis_label = 'Date'
        p.yaxis.axis_label = 'Value'
        p.legend.location = "top_left"
        p.legend.click_policy="hide"	
        bp.save(p)
        gi.log.info('output html finished')
     #output static pic
    if pic_flag == 1:
        SMALL_SIZE = 12
        MEDIUM_SIZE = 15
        BIGGER_SIZE = 18
        plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
        plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
        plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
        plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
        plt.rc('legend', fontsize=MEDIUM_SIZE,loc='upper left')    # legend fontsize
        plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title        
        ax = d.plot(figsize=(15,12),y=[d.columns[0],'despiked'])
        ax.set_xlabel('Date')
        ax.set_ylabel('Value')
        plt.grid()
        plt.legend()
        plt.title("The preliminary result by threshold={}".format(thresh_hold),loc='left')
        plt.savefig(str(png_file),format='png') 
        gi.log.info('output png file finished')
####--------------End PART FOUR--------------####

# part 5 ------------输出数据------------------ #
print('debug: despike is finished and output now...')
print(png_file) #输出一个图片
print(res_file) #输出数据表格文件
print('file:///' + str(html_file))   #输出网络地址
####--------------End PART FIVE--------------####