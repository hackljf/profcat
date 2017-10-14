import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import os
import tables
from mpl_toolkits.axes_grid.inset_locator import(inset_axes,InsetPosition,mark_inset)
from matplotlib.ticker import FormatStrFormatter

def plotalot(ax,x,y,xlim,ylim,xticks=None,yticks=None,lab=None):#,fsize)
   ax.plot(x,y,label=lab)
   if xlim is not None:
      ax.set_xlim(xlim)
   if ylim is not None:
      ax.set_ylim(ylim)
   if xticks is not None:
      ax.set_xticks(xticks)
   if yticks is not None:
      ax.set_yticks(yticks)
files=["ce60cmax1isc75meshh/prof035000.h5",\
"ce85cmax1isc75meshh/h0.01/p08/prof035000.h5",\
"ce100cmax1isc75/prof035000.h5"]

#exact=np.loadtxt("e1rpex.out",usecols=(0,1,2)) # x,rho,u
#iy=1 # rho
iy=2 #u
mks=['.','x','v','None']
width=8.5
height=5
fsize=18

plt.figure(figsize=(width,height))
main=plt.axes() # FIDELIUM ANIMAE de whoever gave this SANE DEFAULTS!!!!
#i1=plt.axes([0.27,0.5,0.20,0.32]) #u
#i2=plt.axes([0.55,0.5,0.35,0.32]) #u
#i1=plt.axes([0.3,0.17,0.32,0.22]) #rho, slow-shock
#i2=plt.axes([0.20,0.5,0.25,0.32]) #rho, contact
for fname in files:
   if os.access(fname,os.F_OK):
      if (os.stat(fname).st_size>0):
         fid=tables.open_file(fname,'r')
         prof=fid.root.profiles
         x=fid.root.x.read()
         x=x+0.4 # diaphragm
         hdr=prof._v_attrs
         print fname
         print hdr.nx1-1
         param=prof.cmt._v_attrs
         ipr=param.isc
         ce=param.ce
         cmax=param.cmax
         u=prof.cmt.u.read()
         rho=prof.cmt.d.read()
#        T=prof.cmt.T.read()
         mumax=prof.cmt.mumax.read()
         nus=prof.cmt.artdiff.read()
         mu=nus/ipr
         zelab='cE ='+str(ce)
#        plotalot(main,x,rho,(0.35,1.05),(0.0,35.0),lab=zelab)
#        plotalot(main,x,u,(0.35,1.05),(-10.0,35.0),lab=zelab)
         plotalot(main,x,mu,(0.4,0.9),None,lab=zelab)
         plotalot(main,x,mumax,(0.4,0.9),None,lab=None)
         main.set_xlabel(r'$x$',fontsize=fsize)
#        main.set_ylabel(r'$u$',fontsize=fsize)
#        plotalot(i1,x,u,(0.4,0.43),(19.55,19.65))
#        plotalot(i2,x,u,(0.4,0.85),(8.66,8.72),xticks=[0.4,0.5,0.6,0.7,0.8],yticks=[8.66,8.68,8.70,8.72])
#        main.set_ylabel(r'$\rho$',fontsize=fsize)
#        plotalot(i1,x,rho,(0.4,0.75),(14.2,14.4),xticks=[0.4,0.5,0.6,0.7],yticks=[14.2,14.3,14.4])
#        plotalot(i2,x,rho,(0.7,0.85),(30.6,31.2),xticks=[0.7,0.75,0.8,0.85],yticks=[30.6,30.8,31.0,31.2])
         fid.close()

#main.plot(exact[:,0],exact[:,iy],label="exact",ls='--')
#i1.plot(exact[:,0],exact[:,iy],ls='--')
#i2.plot(exact[:,0],exact[:,iy],ls='--')
#i2.plot(exact[:,0],exact[:,iy],ls='--')

#main.legend(loc='lower left') #u
main.legend(loc='upper right') #rho, visc
pname='shock2_visc_t35_crisis.pdf'
#pname='shock2_d_t35_crisis.pdf'

plt.savefig(pname)
plt.close()
