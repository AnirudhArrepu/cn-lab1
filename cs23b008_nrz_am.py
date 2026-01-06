import numpy as np

seq = [1,0,1,0,1,1,0]
seq = np.array(seq)

def nrz(seq: np.array, bps: int) -> np.array:
    seq = seq*2 - 1
    return np.repeat(seq, bps)

msg = nrz(seq, 200)
print(f"nrz encoding for seq {seq}: {msg}")
print(len(msg))

def sin_carrier_wave(fc: int, dur:int = 0.1, sam_rate: int =1000)->np.array:
    x = np.linspace(0, dur, int(sam_rate*dur))
    y = np.sin(2*np.pi*fc*x)
    return y

sin_wave = sin_carrier_wave(20)

def amp_mod(sin_wave: np.array, msg_nrz: np.array)->np.array:
    sin_wave = np.repeat(sin_wave, int(np.ceil(len(msg_nrz)/len(sin_wave))))[:len(msg_nrz)]
    return sin_wave*msg_nrz

amp_wave = amp_mod(sin_wave, msg)

