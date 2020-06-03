import playsound as ps
import soundfile as sf

data, fs = sf.read('you-are-acting-so-weird.wav')
delay = .25
gain = .75

delay_index = int(delay * fs)
output = [0]*len(data)

for i in range(0, len(data)):
    output[i] = data[i][0] + gain*data[i-delay_index][0]

print(output)
sf.write('test_output.wav', output, fs)
ps.playsound('test_output.wav')