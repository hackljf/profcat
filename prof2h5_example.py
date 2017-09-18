from profcat import *
import tables

Np=13
numtasks=48

fid=tables.open_file("prof350000.h5",'w')
profiles=fid.create_group('/','profiles')
profiles._v_attrs.nx1=Np
profiles._v_attrs.dt=1.0e-7
profiles._v_attrs.time=0.035
profiles._v_attrs.eos="CPG"
profiles._v_attrs.case="2shock"
profiles._v_attrs.gamma=1.4
profiles._v_attrs.rgas=1.0


cmtdata=fid.create_group(profiles,'cmt')
cmtdata._v_attrs.isc=0.75
cmtdata._v_attrs.cmax=1.0
cmtdata._v_attrs.ce=40.0
cmtdata._v_attrs.nxd=18

exact=fid.create_group(profiles,'exact')
exact._v_attrs.solver="e1rpex"

tmp=profcat('profiles/uprof350000p',3,Np,numtasks)

x=tmp[:,0]
fid.create_array('/','x',x)

fid.create_array(cmtdata,'u',tmp[:,1])
fid.create_array(exact,'u',tmp[:,-1])

tmp=profcat('profiles/Tprof350000p',3,Np,numtasks)
print np.amax(x-tmp[:,0])
fid.create_array(cmtdata,'T',tmp[:,1])
fid.create_array(exact,'T',tmp[:,-1])

tmp=profcat('profiles/rhoprof350000p',3,Np,numtasks)
print np.amax(x-tmp[:,0])
fid.create_array(cmtdata,'d',tmp[:,1])
fid.create_array(exact,'d',tmp[:,-1])

tmp=profcat('profiles/viscprof350000p',4,Np,numtasks)
print np.amax(x-tmp[:,0])
fid.create_array(cmtdata,'artdiff',tmp[:,1])
fid.create_array(cmtdata,'mumax',tmp[:,2])
fid.create_array(cmtdata,'resid',tmp[:,-1])

fid.close()
