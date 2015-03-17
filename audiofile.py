import numpy as np
from scikits.audiolab import wavread, wavwrite

class audioFile:
	def __init__(self, fileName):
		''' 
		Audio file class (useful for multiple file tests)
		Constructor inputs: 
		-------------------
			- filename = name of file with extension. (Accepts only .wav files)
		Members:
		--------
		audio = audiofile
		Fs = Sample rate
		dtype = A string containing information about sample data type.
		length = Length of audio in samples.
		RMS = Can be used to store RMS signal information. (Initialized to zero)
		t = Time array. Useful for time plots. 
		Dependencies:
		numpy as np
		wavread and wavwrite from scikits.audiolab

		Methods:
		--------
		downmixL(self)	: Downmixes to mono using only the L channel
		downmixR(self)	: Downmixes to mono using only the R channel
		downmixLR(self) : Downmixes to mono using L+R channels 
			-- Warning! This replaces self.audio with the mono file. 
		'''
		self.fileName = fileName
		# Read audio file
		self.packedfile = wavread(fileName)
		# Unpack audio file
		self.audio = np.array(self.packedfile[0])
		self.Fs = self.packedfile[1]
		self.dtype = self.packedfile[2]
		# Other Details
		shape = np.shape(self.audio)
		if len(shape) == 1:
			self.length = len(self.audio)
			self.nchannels = 1
		else:
			(self.length, self.nchannels) = self.audio.shape
		self.RMS = 0
		# For plotting with respect to time
		self.t = np.true_divide( np.array(range(self.length)), self.Fs)


	def downmixLR(self):
		self.audio = 0.5*( self.audio[:,0] + self.audio[:,1] )
		return

	def downmixR(self):
		self.audio = self.audio[:,1]
		return

	def downmixL(self):
		self.audio = self.audio[:,0]
		return


