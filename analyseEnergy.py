import math
import numpy as np
import ctypes
import sys
import glob
import argparse
import os
import time
from ROOT import gSystem
gSystem.Load("libDmpEvent.so")
import ROOT
import cPickle as pickle
import gc
gc.enable()

def openRootFile(efilelist): 
	'''
	Returns a TChain from a filelist
	'''
	chain = ROOT.DmpChain("CollectionTree")
	for f in efilelist:
		chain.Add(f)
	if not chain.GetEntries():
		raise IOError("0 events in DmpChain - something went wrong")
	return chain
	
	
def analysis(files,nr):
	'''
	Select good events from a filelist and saves them as a numpy array
	'''

	dmpch = openRootFile(files)
	nvts = dmpch.GetEntries()
	
	a = []
	for i in xrange(nvts):
		pev = dmpch.GetDmpEvent(i)
		
		a.append(  pev.pEvtSimuPrimaries().pvpart_ekin  )

	return a
	
if __name__ == "__main__" :
	
	t0 = time.time()

	filelist = []
	with open(sys.argv[1],'r') as f:
		for lines in f:
			filelist.append(lines.replace('\n',''))
	
	nrofchunks = 300
	chunksize = len(filelist)/nrofchunks
	
	true_energies = []
	
	for i in xrange(nrofchunks):
		print "--- Chunk ", i
		
		if len(filelist) < chunksize: break
		
		chunk = []
		for k in xrange(chunksize):
			chunk.append( filelist.pop(0) )
		
		true_energies = true_energies + analysis(chunk,i)
		
	true_energies = true_energies + analysis(filelist,nrofchunks)
	
	with open('true_energies.pick','w') as f:
		pickle.dump(true_energies,f)
	
	print 'Run time: ', str(time.strftime('%H:%M:%S', time.gmtime( time.time() - t0 )))
