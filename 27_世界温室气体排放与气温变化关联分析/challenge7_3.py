import pandas as pd, matplotlib.pyplot as plt, matplotlib.ticker as ticker

def climate_plot():
    data = pd.read_excel('ClimateChange.xlsx')
    l = ['EN.ATM.CO2E.KT', 'EN.ATM.METH.KT.CE', 'EN.ATM.NOXE.KT.CE', 'EN.ATM.GHGO.KT.CE', 'EN.CLC.GHGR.MT.CE']
    data = data[data['Series code'].isin(l)].iloc[:, 6:-1]
    data.replace({'..': pd.np.nan}, inplace=True)
    data = data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1).sum()
    data = pd.DataFrame(data.values, index= data.index, columns=['Total GHG'])

    gt = pd.read_excel('GlobalTemperature.xlsx')
    gt = gt.iloc[:, [1, 4]].set_index(pd.to_datetime(gt.Date))
    gt_y = gt.resample('y').mean()['1990': '2010']
    gt_q = gt.resample('q').mean()
    df = pd.concat([gt_y.set_index(data.index), data], axis=1)
    df = df.apply(lambda x: (x-x.min())/(x.max()-x.min()))

    fig, axes = plt.subplots(nrows=2, ncols=2)
    ax1 = df.plot(kind='line', figsize=(16, 9), ax=axes[0, 0])
    ax1.set_xlabel('Years')
    ax1.set_ylabel('Values')
    ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))
    ax2 = df.plot(kind='bar', figsize=(16, 9), ax=axes[0, 1])
    ax2.set_xlabel('Years')
    ax2.set_ylabel('Values')
    ax3 = gt_q.plot(kind='area', figsize=(16, 9), ax=axes[1, 0])
    ax3.set_xlabel('Quarters')
    ax3.set_ylabel('Temperature')
    # 所谓核密度分布图，就是各个温度值(x轴)所占总数据比例(y轴)的分布图
    ax4 = gt_q.plot(kind='kde', figsize=(16, 9), ax=axes[1, 1])
    ax4.set_xlabel('Quarters')
    ax4.set_ylabel('Temperature')
    plt.show()
    return fig

print(climate_plot())

