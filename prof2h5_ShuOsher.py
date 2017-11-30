from profcat import *
import tables

Np=5
numtasks=48
num="300001"

fid=tables.open_file("profiles/prof"+num+".h5",'w')
profiles=fid.create_group('/','profiles')
profiles._v_attrs.nx1=Np
profiles._v_attrs.dt=0.6e-5
profiles._v_attrs.time=1.8
profiles._v_attrs.eos="CPG"
profiles._v_attrs.case="Shu-Osher"
profiles._v_attrs.gamma=1.4
profiles._v_attrs.rgas=1.0


cmtdata=fid.create_group(profiles,'cmt')
cmtdata._v_attrs.isc=0.75
cmtdata._v_attrs.cmax=0.5 # ask rahul what these were
cmtdata._v_attrs.ce=40.0 # ask rahul what these were
cmtdata._v_attrs.nxd=6


# PLease start using num here instead of hardcoding filename prefixes
tmp=profcat('profiles/uprof300001p',2,Np,numtasks)

x=tmp[:,0]
fid.create_array('/','x',x)

fid.create_array(cmtdata,'u',tmp[:,1])

tmp=profcat('profiles/Tprof300001p',2,Np,numtasks)
print np.amax(x-tmp[:,0])
fid.create_array(cmtdata,'T',tmp[:,1])

tmp=profcat('profiles/rprof300001p',2,Np,numtasks)
print np.amax(x-tmp[:,0])
fid.create_array(cmtdata,'d',tmp[:,1])

tmp=profcat('profiles/muprof300001p',4,Np,numtasks)
print np.amax(x-tmp[:,0])
fid.create_array(cmtdata,'halfmurho',tmp[:,1]) # don't bother
fid.create_array(cmtdata,'artdiff',tmp[:,2])
fid.create_array(cmtdata,'mumax',tmp[:,-1])

fid.close()
