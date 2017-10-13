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
   ax.set_xlim(xlim)
   ax.set_ylim(ylim)
   if xticks is not None:
      ax.set_xticks(xticks)
   if yticks is not None:
      ax.set_yticks(yticks)

orders=[4,8,12]
mks=['.','x','v','None']
width=8.5
height=5
fsize=18

exact=np.loadtxt("e1rpex.out",usecols=(0,1)) # rho
#exact=np.loadtxt("e1rpex.out",usecols=(0,2)) #u

h=0.01
plt.figure(figsize=(width,height))
main=plt.axes() # FIDELIUM ANIMAE de whoever gave this SANE DEFAULTS!!!!
#i1=plt.axes([0.35,0.55,0.5,0.3]) #u
i1=plt.axes([0.3,0.17,0.32,0.22]) #rho, slow-shock
i2=plt.axes([0.20,0.5,0.25,0.32]) #rho, contact
for i,p in enumerate(orders):
   case='h0.01/p'+str(p).zfill(2)
   zefile=case+'/profiles/prof035000.h5'
   print zefile
   if os.access(zefile,os.F_OK):
      if (os.stat(zefile).st_size>0):
         fid=tables.open_file(zefile,'r')
         prof=fid.root.profiles
         x=fid.root.x.read()
         x=x+0.4 # diaphragm
         hdr=prof._v_attrs
         print p-(hdr.nx1-1)

         param=prof.cmt._v_attrs
         if param.__contains__('isc'):
            ipr=param.isc
         else:
            ipr=1

         u=prof.cmt.u.read()
         print u.shape
         T=prof.cmt.T.read()
         rho=prof.cmt.d.read()
         mumax=prof.cmt.mumax.read()
         nus=prof.cmt.artdiff.read()
         mu=nus/ipr
         zelab='p ='+str(p)
#        plotalot(main,x,rho,(0.35,1.05),(-10.0,35.0),lab=zelab)
         plotalot(main,x,rho,(0.35,1.05),(0.0,35.0),lab=zelab)
         main.set_xlabel(r'$x$',fontsize=fsize)
#        main.set_ylabel(r'$u$',fontsize=fsize)
         main.set_ylabel(r'$\rho$',fontsize=fsize)
#        plotalot(i1,x,rho,(0.4,0.75),(14.0,14.6),xticks=[0.4,0.5,0.6,0.7],yticks=[14.0,14.2,14.4,14.6])
         plotalot(i1,x,rho,(0.4,0.75),(14.2,14.4),xticks=[0.4,0.5,0.6,0.7],yticks=[14.2,14.3,14.4])
         plotalot(i2,x,rho,(0.7,0.85),(30.6,31.2),xticks=[0.7,0.75,0.8,0.85],yticks=[30.6,30.8,31.0,31.2])
#        i1.set_xlim((0.4,0.85)) # u need to start storing and
#        i1.set_ylim((8.66,8.72))# u func-ifying these xlims
#        i1.set_xticks([0.5,0.6,0.7,0.8]) #u
#        i1.set_yticks([8.66,8.68,8.70,8.72]) #u
#        i1.plot(x,u)

         fid.close()

#  main.legend(loc='upper left') #u
main.plot(exact[:,0],exact[:,1],label="exact",ls='--')
i1.plot(exact[:,0],exact[:,1],ls='--')
i2.plot(exact[:,0],exact[:,1],ls='--')
#main.legend(loc='lower left') #u
main.legend(loc='upper right') #rho

pname='shock2_d_t02_K100.pdf'
plt.savefig(pname)
plt.close()
