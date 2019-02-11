def quarter_volume():
    import pandas as pd
    from pandas import Series
    data = pd.read_csv('apple.csv')
    s = Series(list(data.Volume), index=pd.to_datetime(data.Date))
    second_volume = s.resample('q').sum().sort_values()[-2]
    return second_volume
