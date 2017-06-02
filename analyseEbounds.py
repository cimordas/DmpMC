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
	
	
	c = ROOT.TCanvas("MyTitle","MyTitle",1000,1000)
	
	histoMax = ROOT.TH1F("MaxEne","MaxEne",10,1000,100000000)  # See for logarithmic binning
	#~ histoMin = ROOT.TH1F("MinEne","MinEne",10,1000,100000000)
	
	for f in filelist:
		fo = ROOT.TFile.Open(f)
		rmt = fo.Get("RunMetadataTree")
		simuheader = ROOT.DmpRunSimuHeader()
		rmt.SetBranchAddress("DmpRunSimuHeader",simuheader)
		rmt.GetEntry(0)
		
		histoMax.Fill( simuheader.GetMaxEne() )
		#~ histoMin.Fill( simuheader.GetMinEne() )
		
		fo.Close()
		
	histoMax.Draw()
	c.SaveAs("MyHisto.png")
