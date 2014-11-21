 #-*- coding: utf-8 -*- 

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

data_frame = pd.read_csv('seoung_nam_floating_population_data.csv', \
	sep=",", header=0,quotechar="'", encoding='cp949',lineterminator="\n", \
	index_col=[u'날씨', u'행정구역명'])


group_data = data_frame.groupby(level=[u'날씨',u'행정구역명']).sum()
print group_data
ax = group_data.ix[u'맑음'][u'남자10대'].plot(kind='barh')

axis = ax.yaxis
font = font_manager.FontProperties(fname='C:\\WINDOWS\\Fonts\\NGULIM.TTF')

for text in axis.get_ticklabels():
	text.set_font_properties(font)

plt.show()

