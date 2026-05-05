# from scipy import stats
# data = [10, 12, 345, 56, 45, 23, 234, 3]

# sd = stats.tstd(data)
# mean = sum(data)/len(data)

# print(stats.norm.cdf(70, loc = mean, scale = sd))
# print(sd, mean)

from scipy import stats
print(stats.norm.ppf(.975))



