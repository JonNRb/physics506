from scipy import stats

def regress(data):
    slope, intercept, r, p, std_err = stats.linregress(data)
    return slope, intercept, std_err
