'''
分析抓取的数据
'''
from pyecharts.charts import Bar,Pie
import pandas as pd
from pyecharts import options as opts

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)

df = pd.read_excel('lagou.xls')


# 薪资对比
salary_list = ['10k-20k','12k-20k','15k-25k','15k-30k','20k-40k','25k-50k']
df_python = df[(df['职位类型']=='python')&(df['薪资'].isin (salary_list))]\
    .groupby(['薪资'],as_index=False)['职位类型'].size().reset_index(name='count')
print(df_python)

df_java = df[(df['职位类型']=='java')&(df['薪资'].isin (salary_list))]\
    .groupby(['薪资'],as_index=False)['职位类型'].size().reset_index(name='count')

df_go = df[(df['职位类型']=='go')&(df['薪资'].isin (salary_list))]\
    .groupby(['薪资'],as_index=False)['职位类型'].size().reset_index(name='count')

df_php = df[(df['职位类型']=='php')&(df['薪资'].isin (salary_list))]\
    .groupby(['薪资'],as_index=False)['职位类型'].size().reset_index(name='count')
# print(df_python['薪资'], df_python['count'])
# exit()

bar = Bar()
bar.add_xaxis(salary_list)
bar.add_yaxis("python薪资分布", list(df_python['count']))
bar.add_yaxis("java薪资分布", list(df_java['count']))
bar.add_yaxis("go薪资分布", list(df_go['count']))
bar.add_yaxis("php薪资分布", list(df_php['count']))
bar.set_global_opts(
    title_opts=opts.TitleOpts(title="薪资分布图"),
    yaxis_opts=opts.AxisOpts(name="数量"),
    xaxis_opts=opts.AxisOpts(name="薪资范围"),
)
bar.render('薪资分布图.html')  # 生成本地 HTML 文件


# 职位总需求量
city_list = ['北京', '上海', '深圳', '成都', '广州', '杭州', '武汉', '南京', '苏州', '郑州','西安']
df_python_pos = df[(df['职位类型']=='python')&(df['城市'].isin (city_list))]\
    .groupby(['城市'],as_index=False)['职位类型'].size().reset_index(name='count')
print(df_python_pos)

df_java_pos = df[(df['职位类型']=='java')&(df['城市'].isin (city_list))]\
    .groupby(['城市'],as_index=False)['职位类型'].size().reset_index(name='count')

df_go_pos = df[(df['职位类型']=='go')&(df['城市'].isin (city_list))]\
    .groupby(['城市'],as_index=False)['职位类型'].size().reset_index(name='count')

df_php_pos = df[(df['职位类型']=='php')&(df['城市'].isin (city_list))]\
    .groupby(['城市'],as_index=False)['职位类型'].size().reset_index(name='count')

bar = Bar()
bar.add_xaxis(city_list)
bar.add_yaxis("python需求量分布", list(df_python_pos['count']))
bar.add_yaxis("java需求量分布", list(df_java_pos['count']))
bar.add_yaxis("go需求量分布", list(df_go_pos['count']))
bar.add_yaxis("php需求量分布", list(df_php_pos['count']))
bar.set_global_opts(
    title_opts=opts.TitleOpts(title="职位需求量分布图"),
    yaxis_opts=opts.AxisOpts(name="数量"),
    xaxis_opts=opts.AxisOpts(name="薪资范围"),
)
bar.render('各大城市职位需求量大致分布图.html')  # 生成本地 HTML 文件




