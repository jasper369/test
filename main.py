import numpy as np


power = 15
final_length = 2**power
prob = 0.5
final_result = np.random.rand(final_length)

computations = np.zeros((final_length,power+1))
computations[:,power]=final_result

for i in range(power-1,-1,-1):
    for j in range(0,int(2**(i))):
        computations[j,i]=prob*computations[2*j,i+1]+(1-prob)*computations[2*j+1,i+1]

print(computations[0,0])