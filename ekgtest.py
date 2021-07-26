import numpy as np
import pandas as pd
import neurokit2 as nk
import struct

ecg1 = nk.ecg_simulate(duration=10, sampling_rate=44100, heart_rate=70)
ecg2 = nk.ecg_simulate(duration=20, sampling_rate=44100, heart_rate=120)
ecg3 = nk.ecg_simulate(duration=30, sampling_rate=44100, heart_rate=80)

# Process it
# signals = nk.ecg_process(ecg, sampling_rate=500)

# # Visualise the processing
# nk.ecg_plot(signals, sampling_rate=500)

# sampling_rate = 44100
# freq = 440

f = open('test.wav', 'wb')
for i in ecg1:
    f.write(struct.pack('b', int(i)))
for i in ecg2:
    f.write(struct.pack('b', int(i)))
for i in ecg3:
    f.write(struct.pack('b', int(i)))

f.close()
