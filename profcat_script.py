#!/usr/bin/python
# slurps up one-per-task profiles dumps, sorts by x, and spits it back out in 1 piece
import numpy as np
import os
import sys

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

arglist=sys.argv
numargs=len(arglist)
if numargs < 5:
   print(
   '''
   usage: profcat_script 'prefix' np ncol numtasks
          prefix: character string prefix/root filename
          np: number of GLL nodes in each element. 1 for non-SEM input
          ncol: number of columns
          numtasks: number of files
   ''')
else:
   print(arglist)
   prefix=arglist[1]
   Np=int(arglist[2])
   ncol=int(arglist[3])
   numtasks=int(arglist[4])
   profiles=profcat(prefix,ncol,Np,numtasks)
   fname=prefix+'.dat'
   np.savetxt(fname,profiles)
