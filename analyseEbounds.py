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


	
if __name__ == "__main__" :
	
	t0 = time.time()

	filelist = []
	with open(sys.argv[1],'r') as f:
		for lines in f:
			filelist.append(lines.replace('\n',''))
	
	mins = []
	maxs = []
	
	for f in filelist:
		fo = ROOT.TFile.Open(f)
		rmt = fo.Get("RunMetadataTree")
		simuheader = ROOT.DmpRunSimuHeader()
		rmt.SetBranchAddress("DmpRunSimuHeader",simuheader)
		rmt.GetEntry(0)
		maxEne = simuheader.GetMaxEne()
		minEne = simuheader.GetMinEne()
		fo.Close()
		mins.append(minEne)
		maxs.append(maxEne)
	
	with open('E_bounds.pick','w') as f:
		pickle.dump([mins,maxs,filelist],f)
	
	print 'Run time: ', str(time.strftime('%H:%M:%S', time.gmtime( time.time() - t0 )))
