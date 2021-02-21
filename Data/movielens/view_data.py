import pickle
import numpy as np
train = np.load(open('train.npy', 'rb'))
print(len(train))
audio = np.load(open('FeatureAudio_avg_normal.npy', 'rb'))
print(len(audio[0]), ' ', len(audio))