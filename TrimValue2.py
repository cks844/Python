from scipy import stats
Estimates=[100,178,200,234,300,350,400,453,500,505,600,650,700,750,800,825,840,870,899,900,956,965,987,1000,1010]
Estimates.sort()
m=stats.trim_mean(Estimates,0.1)
print(m)
