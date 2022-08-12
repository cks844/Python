from statistics import mean
Estimates=[100,178,200,234,300,350,400,453,500,505,600,650,700,750,800,825,840,870,899,900,956,965,987,1000,1010]
Estimates.sort()
trim_val=int(0.1*len(Estimates)) #value is float,so typecasting it to int
Estimates=Estimates[trim_val:]
Estimates=Estimates[:-trim_val]
print(mean(Estimates))
