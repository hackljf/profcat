import matplotlib as mpl
#mpl.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import os
import tables
from mpl_toolkits.axes_grid.inset_locator import(inset_axes,InsetPosition,mark_inset)
from matplotlib.ticker import FormatStrFormatter


orders=[4,16]
mks=['o','None']
lst=['None','-']
nelms=[50,100,200]
h=[0.02,0.01,0.005]
col=['red','green','blue']
width=8.5
height=5
fsize=18
xdiaph=0.5

plt.figure(figsize=(width,height))
for i,p in enumerate(orders):
   for k,K in enumerate(nelms):
      case='N'+str(K)+'_p'+str(p)
      zefile=case+'/profiles/prof020001.h5'
      print zefile
      if os.access(zefile,os.F_OK):
         if (os.stat(zefile).st_size>0):
            fid=tables.open_file(zefile,'r')
            prof=fid.root.profiles
            x=fid.root.x.read()
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

            rho=prof.cmt.d.read()
            mumax=prof.cmt.mumax.read()
            nus=prof.cmt.artdiff.read()
            mu=nus/ipr
            if p>4:
               zelab=''
            else:
               zelab='h ='+str(h[k])
            plt.subplot(211)
            plt.plot(x,rho,label=zelab,marker=mks[i],linestyle=lst[i],color=col[k])
            plt.xlabel(r'$x$',fontsize=fsize)
            plt.ylabel(r'$\rho$',fontsize=fsize)
            plt.xlim((0.82,0.88)) # need to start storing and
            plt.ylim((0.1,0.3))# u func-ifying these xlims
            plt.subplot(212)
            plt.plot(x,mu,label=zelab,marker=mks[i],linestyle=lst[i],color=col[k])
            plt.xlabel(r'$x$',fontsize=fsize)
            plt.ylabel(r'$\mu_s$',fontsize=fsize)
            plt.xlim((0.82,0.88)) # need to start storing and
# JUST SHOW THE DAMN SHOCK AND DONT BOTHER WITH HOW BADLY p=4 SMEARS THE CONTACT
#           i1.set_yticks([0.926,0.928,0.93]) #u
#           i1.plot(x,u)
#         plt.subplot(133)
#	 plt.plot(x,rho,label=zelab)
#	 plt.xlabel(r'$x$',fontsize=fsize)
#	 plt.ylabel(r'$\rho$',fontsize=fsize)
#	 plt.xlim((0.62,0.72)) # need to start storing and
#         plt.ylim((0.25,0.45))# func-ifying these xlims

            fid.close()

plt.legend(loc='upper right')
#plt.show()

pname='sod3_rhovisc_t02_sweep.pdf'
plt.savefig(pname)
plt.close()
