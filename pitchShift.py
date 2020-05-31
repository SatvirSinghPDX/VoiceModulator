import numpy as np
import playsound as ps
import wave as wv

wr = wv.open('you-are-acting-so-weird.wav', 'r')
ww = wv.open('new_test.wav', 'w')

par = list(wr.getparams())
ww.setparams(par)

frame_per_sec = wr.getframerate()//20
file_sz = int(wr.getnframes()/frame_per_sec)
shift = 100//20

for num in range(file_sz):
    data = np.fromstring(wr.readframes(frame_per_sec), dtype=np.int16)
    left = data[0::2]
    right = data[1::2]
    #Take DFT
    left_freq = np.fft.rfft(left)
    right_freq = np.fft.rfft(right)
    #Scale It Up or Down
    left_freq = np.roll(left_freq, shift)
    right_freq = np.roll(right_freq, shift)
    left_freq[0:shift] = 0
    right_freq[0:shift] = 0
    #Take inverse DFT
    left = np.fft.irfft(left_freq)
    right = np.fft.irfft(right_freq)
    #Put it altogether
    sig = np.column_stack((left, right)).ravel().astype(np.int16)
    ww.writeframes(sig.tostring())

wr.close()
ww.close()

ps.playsound('you-are-acting-so-weird.wav')
ps.playsound('new_test.wav')
