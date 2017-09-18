# slurps up one-per-task profiles dumps, sorts by x, and spits it back out in 1 piece
import numpy as np
import os

def profcat(prefix,ncol,nx1,nfiles):
   ntmp=0
   ipad=int(np.ceil(np.log10(nfiles)))
   for p in range(nfiles):
      zefile=prefix+str(p).zfill(ipad)
      if os.access(zefile,os.F_OK):
         tmp=np.loadtxt(zefile)
         ntmp=ntmp+1
         if ntmp==1:
            fullprof=tmp
         else:
            fullprof=np.vstack((fullprof,tmp))
   fullprof=fullprof.reshape((-1,nx1,ncol))
   vertices=fullprof[:,0,0]
   fullprof=fullprof[vertices.argsort(),:,:].reshape((-1,ncol))
   return fullprof
