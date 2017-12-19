# slurps up one-per-task profiles dumps, sorts by x, and spits it back out in 1 piece
import numpy as np
import os

def profcat(prefix,ncol,nx1,nfiles,suffix=''):
   ntmp=0
   ipad=int(np.ceil(np.log10(nfiles)))
   for p in range(nfiles):
      if nfiles>1:
         zefile=prefix+str(p).zfill(ipad)+suffix
      else:
         zefile=prefix
      print zefile
      if os.access(zefile,os.F_OK):
         if (os.stat(zefile).st_size>0):
            tmp=np.loadtxt(zefile)
            ntmp=ntmp+1
            if ntmp==1:
               fullprof=tmp
            else:
               fullprof=np.vstack((fullprof,tmp))
   if ntmp==0:
      print 'bad prefix'
      print prefix
      print 'no files found!!!!!!!!!!'
   else:
      fullprof=fullprof.reshape((-1,nx1,ncol))
      vertices=fullprof[:,0,0]
      fullprof=fullprof[vertices.argsort(),:,:].reshape((-1,ncol))
      return fullprof

#profiles=profcat('rhoprof.nid.','.step.0300',5,5,10000)
#np.savetxt('profiles.step.0300',profiles)
