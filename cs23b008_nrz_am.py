import numpy as np

seq = [1,0,1,0,1,1,0]
seq = np.array(seq)

def nrz(seq: np.array, bps: int) -> np.array:
    seq = seq*2 - 1
    return np.repeat(seq, bps)

print(nrz(seq, 200))