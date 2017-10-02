from matplotlib import pyplot as plt
import numpy as np
import os

orders=[4,8,12,16]
nelms=[50,100,200]
#    time umin umax
zecols=(1,2,4)

plt.figure()
for p in orders:
   for K in nelms:
      case='N'+str(K)+'_p'+str(p)
      zefile=case+'/umax'
      if os.access(zefile,os.F_OK):
         if (os.stat(zefile).st_size>0):
            tmp=np.loadtxt(zefile,usecols=zecols)
            x=tmp[:,0]
            umin=tmp[:,1]
            umax=tmp[:,2]
            plt.plot(x,umax,label=case)
plt.legend()
plt.show()
