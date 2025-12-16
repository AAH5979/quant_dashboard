import statsmodels.api as sm

def hedge_ratio(x, y):
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    return model.params[1]

def calculate_spread(df1, df2):
    hr = hedge_ratio(df1["price"], df2["price"])
    return df1["price"] - hr * df2["price"]

def z_score(series, window=30):
    mean = series.rolling(window).mean()
    std = series.rolling(window).std()
    return (series - mean) / std
