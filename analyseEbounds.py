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

	ch = ROOT.TChain("RunMetadataTree")
	for f in filelist:
		ch.Add(f)
		
	nentries = ch.GetEntries()
	h1 = ROOT.TH1D("h1","hEnergy",10,ROOT.TMath.Log10(10000),ROOT.TMath.Log10(100000000))
	ch.Project("h1","TMath::Log10(DmpRunSimuHeader.fMaxEne)")
	
		
	h1.Draw()
	c.SaveAs("MyHisto.png")
