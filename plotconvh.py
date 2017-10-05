import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import os
import tables
from mpl_toolkits.axes_grid.inset_locator import(inset_axes,InsetPosition,mark_inset)
from matplotlib.ticker import FormatStrFormatter


#orders=[4,8,12,16]
orders=[4,8,16]
mks=['.','x','v','None']
nelms=[50,100,200]
h=[0.02,0.01,0.005]
# one in h, one in p
width=8.5
height=5
fsize=18

for k,K in enumerate(nelms):
   plt.figure(figsize=(width,height))
   main=plt.axes() # FIDELIUM ANIMAE de whoever gave this SANE DEFAULTS!!!!
   i1=plt.axes([0.4,0.175,0.33,0.45])
   for i,p in enumerate(orders):
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
            T=prof.cmt.T.read()
            rho=prof.cmt.d.read()
            mumax=prof.cmt.mumax.read()
            nus=prof.cmt.artdiff.read()
            mu=nus/ipr
            zelab='p ='+str(N)
#           plt.plot(x,rho,label=zelab)
#           plt.plot(x,T,label=zelab)
            main.plot(x,u,label=zelab)
            main.set_xlabel(r'$x$',fontsize=fsize)
            main.set_ylabel(r'$u$',fontsize=fsize)
            main.set_xlim((0.2,1.0)) # need to start storing and
            i1.set_xlim((0.475,0.85)) # need to start storing and
            i1.set_ylim((0.926,0.930))# func-ifying these xlims
            i1.set_xticks([0.5,0.6,0.7,0.8])
            i1.set_yticks([0.926,0.928,0.93])
            i1.plot(x,u)

            fid.close()

   main.legend(loc='upper left')

   pname='sod3_u_t02_N'+str(K)+'.pdf'
   plt.savefig(pname)
   plt.close()
