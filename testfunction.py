# -*- coding: utf-8 -*-
"""
Created on %27.12.20
@author: %Igor
"""

import numpy as np
from scipy import fft 
from scipy.signal import butter, sosfilt
from scipy.io import wavfile
import matplotlib.pyplot as plt



def butterworth_filter_signal_searching(filepath: str,fsmpl=44100, order=10, max_freq=10000, a = 5000, b = 7500, threshold = 0.4e7):
    """Function dedicated to finding particular signal in noice environment. 
    Parameters:
    filepath: filepath to wav file 
    fsmpl: sampling frequency
    order : order of Butterworth filter
    max_freq : max freq for lowpass filter
    a: min frequency of wanted signal
    b: max frequency of wanted signal
    threshold : 
    Results:
    bool : wheater signal was found wheater not
    """
   
   _, data = wavfile.read(filepath)
   plt.plot(data)
   plt.title('Time domain - sygnał czasowy')
   plt.xlabel('time')
   
   #exaple filtering

   sos = butter(order,max_freq,'lowpass',fs=fsmpl, output='sos')
   filtered = sosfilt(sos, data)
   
   
   #frequency spectrum of signal
   
   plt.figure()
   y=np.abs(fft(data))
   plt.plot(y)
   plt.title('Frequency domain - widmo sygnału')
   plt.xlabel('frequency')
   plt.xlim(0,20000)
   
    #frequency spectrum of filtered signal

   plt.figure()
   y=np.abs(fft(filtered))
   plt.plot(y)
   plt.title('Frequency domain - widmo sygnału filtrowanego')
   plt.xlabel('frequency')
   plt.xlim(0,20000)
   

   a = 5000
   b=7500
   threshold = 0.4e7
   

   if np.any(y[a:b]) > threshold:
       return True 
        
butterworth_filter_signal_searching('noice.wav')