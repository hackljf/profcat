from matplotlib import pyplot as plt
import os
import tables

def hdr2lab(profgrp): # betta be HDF5 file written by prof2h5
# extract simulation parameters from header
# there has got to be a better way of doing this. dictionary view?
   hdr=profgrp._v_attrs
   if hdr.__contains__('time'):
      t='%.2e' % header.time
   else:
      t='???'

   param=profgrp.cmt._v_attrs
   if param.__contains__('CFL'):
      step=', CFL= %.1f' % param.cfl
   elif param.__contains__('dt'):
      step=', $\Delta t$= %.1e' % param.dt
   else:
      step=''
   if param.__contains__('cmax'):
      cmax=', $c_{max}$= %.1e' % param.cmax
   else:
      cmax=''
   if param.__contains__('ce'):
      ce=', $c_{E}$= %.1e' % param.ce
   else:
      ce=''
   if param.__contains__('isc'):
      ipr=param.isc
      isc=', $\mathscr{P}$= %.1e' % ipr
   else:
      isc=''
      ipr=1
   lab=t+step+cmax+ce+isc
   return lab

orders=[4,8,12,16]
mks=['.','x','v','None']
nelms=[50,100,200]
h=[0.02,0.01,0.005]
# one in h, one in p

i=0
plt.figure()
for k,K in enumerate(nelms):
   case='N'+str(K)+'_p'+str(orders[i])
   zefile=case+'/profiles/prof020001.h5'
   print zefile
   if os.access(zefile,os.F_OK):
      if (os.stat(zefile).st_size>0):
         fid=tables.open_file(zefile,'r')
         g=[];
         for group in fid.walk_groups():
            g.append(group)
         root=g[0]
         prof=root.profiles
         x=root.x.read()
         hdr=prof._v_attrs
         N=hdr.nx1-1

         zelab=hdr2lab(prof)
      
         u=prof.cmt.u.read()
         T=prof.cmt.T.read()
         rho=prof.cmt.d.read()
         mumax=prof.cmt.mumax.read()
         nus=prof.cmt.artdiff.read()
         mu=nus/ipr
         zelab='h ='+str(h[k])+', t='+zelab
         plt.plot(x,rho,label=zelab)
#        plt.plot(x,T,label=zelab)
#        plt.plot(x,u,label=zelab)
         fid.close()

#for i,p in enumerate(orders):
## there has got to be a better way of doing this. dictionary view?
#   if hdr.__contains__('time'):
#      t='%.2e' % hdr.time
#   else:
#      t='???'
#
#   param=prof.cmt._v_attrs
#   if param.__contains__('CFL'):
#      step=', CFL= %.1f' % param.cfl
#   elif param.__contains__('dt'):
#      step=', $\Delta t$= %.1e' % param.dt
#   else:
#      step=''
#   if param.__contains__('cmax'):
#      cmax=', $c_{max}$= %.1e' % param.cmax
#   else:
#      cmax=''
#   if param.__contains__('ce'):
#      ce=', $c_{E}$= %.1e' % param.ce
#   else:
#      ce=''
#   if param.__contains__('isc'):
#      ipr=param.isc
#      isc=', $\mathscr{P}$= %.1e' % ipr
#   else:
#      isc=''
#      ipr=1
#
#   u=prof.cmt.u.read()
#   T=prof.cmt.T.read()
#   mumax=prof.cmt.mumax.read()
#   nus=prof.cmt.artdiff.read()
#   mu=nus/ipr
#
#   zelab='N ='+str(N)+', t='+t+step+cmax+ce+isc
#   plt.subplot(221)
#   plt.plot(x,u,label=zelab)
#   plt.subplot(222)
#   plt.plot(x,T,label=zelab)
#   plt.subplot(223)
#   plt.plot(x,mumax,label=zelab)
#   plt.subplot(224)
#   plt.plot(x,mu,label=zelab)
#   fid.close()
#
plt.legend()
plt.show()
