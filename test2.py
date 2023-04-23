import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体
plt.rcParams['font.family'] = ['MvengNaManHuaTi-Regular']


data = [['f1','鲤鱼','杂食性',300],
        ['f2','草鱼','食草性',240],
        ['f3','鲫鱼','温水性',500],
        ['f4','鳙鱼','温水性',400],
        ['f5','黑鱼','肉食性',480]]

df = pd.DataFrame(data,columns=['鱼号','鱼名','习性','产量'])

fish_names = df['鱼名']
fish_production = df['产量']

plt.plot(fish_names, fish_production)

plt.title('淡水鱼产量统计图')
plt.xlabel(' Fish Name')
plt.ylabel('产量')

plt.savefig('fish_production.png')

plt.show()

