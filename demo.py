import uproot
import awkward as ak
import matplotlib.pyplot as plt


# read the ttree
tree = uproot.open("myNanoProdMc2016_NANO_1.root")["Events"]
# read the pf candidates information into akward arrays
pfcands = tree.arrays(tree.keys('PF_*') + ['nPF'], entry_start=0, entry_stop=1000)

# plot the number of PF candidates per event
plt.figure()
plt.hist( ak.to_numpy(pfcands['nPF']), bins=50, range=(0,3000), histtype='step')
plt.savefig("nPF.png")

# calculate the average of abs(PF_dxy) for charged pf candidates 
dxyavg_PV = ak.to_numpy(ak.mean(abs(pfcands['PF_dxy']),weight=((pfcands['PF_charge']!=0) * (pfcands['PF_puppiWeight']==1)), axis=1), allow_missing=False)
dxyavg_PU = ak.to_numpy(ak.mean(abs(pfcands['PF_dxy']),weight=((pfcands['PF_charge']!=0) * (pfcands['PF_puppiWeight']==0)), axis=1), allow_missing=False)

plt.figure()
plt.hist(dxyavg_PU, bins=50, range=(0,1.0), histtype='step', label='Charged PU')
plt.hist(dxyavg_PV, bins=50, range=(0,1.0), histtype='step', label='Charged PV')
plt.legend(loc="upper right")
plt.xlabel('Average |PF_dxy| for charged particles [cm]')
plt.savefig('PF_absdxy_charged.png')
