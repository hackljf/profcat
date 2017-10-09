import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import os
import tables
from mpl_toolkits.axes_grid.inset_locator import(inset_axes,InsetPosition,mark_inset)
from matplotlib.ticker import FormatStrFormatter


orders=[4,8,12,16]
mks=['.','x','v','None']
nelms=[50,100,200]
h=[0.02,0.01,0.005]
# one in h, one in p
width=8.5
height=5
fsize=18

exact=np.loadtxt("e1rpex.out",usecols=(0,2))

for i,p in enumerate(orders):
   plt.figure(figsize=(width,height))
   main=plt.axes() # FIDELIUM ANIMAE de whoever gave this SANE DEFAULTS!!!!
   for k,K in enumerate(nelms):
      case='N'+str(K)+'_p'+str(p)
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
   
# there has got to be a better way of doing this. dictionary view?
#           if hdr.__contains__('time'):
#              t=hdr.time
         
            param=prof.cmt._v_attrs
            if param.__contains__('isc'):
               ipr=param.isc
            else:
               ipr=1

            u=prof.cmt.u.read()
#           mumax=prof.cmt.mumax.read()
#           nus=prof.cmt.artdiff.read()
#           mu=nus/ipr
#           zelab='p ='+str(N)+', t='+t+step+cmax+ce+isc
            zelab='h ='+str(h[k])
            main.plot(x,u,label=zelab)
            main.set_xlabel(r'$x$',fontsize=fsize)
            main.set_ylabel(r'$u$',fontsize=fsize)
            main.set_xlim((0.2,1.0)) # need to start storing and

            fid.close()

   main.plot(exact[:,0],exact[:,1],label="exact")
   main.legend(loc='upper left') #u

   pname='sod3_u_t02_p'+str(p)+'noinset.pdf'
   plt.savefig(pname)
   plt.close()
