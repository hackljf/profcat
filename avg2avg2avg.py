import os
import numpy as np
orders=[4,8,12,16]
the_N=50
exact=np.loadtxt('N50_p4avgs.dat',usecols=(0,1))
nelms=[100,200]
err=np.zeros((4,2))
for i,k in enumerate(nelms):
   idim=k/the_N
   for j,p in enumerate(orders):
      zefile='N'+str(k)+'_p'+str(p)+'avgs.dat'
      if os.access(zefile,os.F_OK):
         if (os.stat(zefile).st_size>0):
            tmp=np.loadtxt(zefile,usecols=(0,2))
            xfine=np.reshape(tmp[:,0],(-1,idim))
            xvert=np.transpose(xfine[:,0])
            ufine=np.reshape(tmp[:,1],(-1,idim))
            avgavg=np.mean(ufine,1)
            oname='N'+str(k)+'_p'+str(p)+'avgavg.dat'
            bob=np.hstack((xvert.reshape(the_N,1),avgavg.reshape(the_N,1)))
            np.savetxt(oname,bob)
            err[j,i]=np.mean(np.abs(avgavg-exact[:,1]))

np.savetxt("conv_sod_avg2avg2avg",err,header="p\h=0.01 0.005")
