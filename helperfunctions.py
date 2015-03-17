"""
MAT 201A - Final Project
Winter 2015
UC Santa Barbara

Author:Akshay Cadambi
akshay19.92@gmail.com

This file contains all the helper functions used by the final IPython notebook. This is merely to de-clutter the notebook and have more room for explanation. 

"""

from matplotlib.pyplot import *
import scipy.signal as scp
from scipy.stats import norm
import glob

def generateSpecgram(audioFile, windowFn = np.hanning, NFFT=1024, hop_size=-1):
    """ Generates a spectrogram of audio. Input audio must be in the form of an audioFile class instance """
    
    #Inits
    audio = audioFile.audio.copy()
    L = audioFile.length
    if hop_size < 0:
        hop_size = NFFT
        
    nslices = int( (L-NFFT)*1.0/hop_size )
    
    window = windowFn(NFFT)

    time_slice = audio[0 : NFFT]                      
    analysis_window = np.multiply(time_slice, window)
    stft = np.fft.fft(analysis_window, n=NFFT)    
    spectrogram = stft       

    for w_index in range(1, nslices):
        time_slice = audio[w_index*hop_size : w_index*hop_size + NFFT]                      
        analysis_window = np.multiply(time_slice, window)
        stft = np.fft.fft(analysis_window, n=NFFT)    
        spectrogram = np.c_[spectrogram, stft]       
        
    return spectrogram    

def half_wave_rectify(array):
    """ Returns 0 if negative, returns number if positive.
        (Vectorized) """
    return 0.5*(array+np.abs(array))

def histPlot(histogram, stem_plot=True):
    """ Histogram plotting function
            The histogram must be input as a Mx2 matrix, with the first column
             containing the IOI-bins and the second containing the frequency of 
             occurance. 
    """
    if stem_plot:
        stem(histogram[:,0], histogram[:,1])
    else:
        plot(histogram[:,0], histogram[:,1])
    title("A histogram of the Inter-Onset Intervals")
    ylabel("Frequency of occurance")
    xlabel("IOI")
