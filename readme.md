## Basic instructions for using Nano with uproot3:

- The files are under https://cernbox.cern.ch/index.php/s/Ru7Hm4sjbP16Xtx
- Currently only copied part of the 2016 Simulation of ttbar dilepton events, with about 1M events in total. More events and more channels can be produced, if necessary.
- The most useful features should be the PF candidates. There are about 500-2500 PF candidates per event, with a mean value of 1500 and spread of 350. The saved features of PF candidates include:
    - PF_pt, PF_eta, PF_phi, PF_charge, PF_mass, 
	- PF_fromPV: the PV fitting status for charged particles
	- PF_puppiWeight: puppiWeight for PF candidates
- The root files can be read into memory with uproot (https://github.com/scikit-hep/uproot3). 

```
conda create -n DeepPuppi python=3.8
conda activate DeepPuppi
pip install uproot3

```



