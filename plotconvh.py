import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import os
import tables
from mpl_toolkits.axes_grid.inset_locator import(inset_axes,InsetPosition,mark_inset)
from matplotlib.ticker import FormatStrFormatter

#def plotalot(ax,x,y,xlim,ylim,xlabel,ylabel,xticks,yticks,lab,fsize):
def plotalot(ax,x,y,xlim,ylim,xticks=None,yticks=None,lab=None):#,fsize)
   ax.plot(x,y,label=lab)
   ax.set_xlim(xlim)
   ax.set_ylim(ylim)
   if xticks is not None:
      ax.set_xticks(xticks)
   if yticks is not None:
      ax.set_yticks(yticks)
#  if xlabel is not None:
#     ax.set_xlabel(r'$x$',fontsize=fsize)
#  if ylabel is not None:
#     ax.set_ylabel(r'$x$',fontsize=fsize)


mks=['.','x','v','None']
h=[0.02,0.01,0.005]
# one in h, one in p
width=8.5
height=5
fsize=18

exact=np.loadtxt("e1rpex.out",usecols=(0,2)) # u
#exact=np.loadtxt("e1rpex.out",usecols=(0,1)) # rho

p=8
plt.figure(figsize=(width,height))
main=plt.axes() # FIDELIUM ANIMAE de whoever gave this SANE DEFAULTS!!!!
i1=plt.axes([0.35,0.55,0.5,0.3]) #u
#i1=plt.axes([0.3,0.17,0.32,0.22]) #rho, slow-shock
#i2=plt.axes([0.20,0.5,0.25,0.32]) #rho, contact
for k,K in enumerate(h):
   case='h'+str(K)+'/p'+str(p).zfill(2)
   zefile=case+'/profiles/prof035000.h5'
   print zefile
   if os.access(zefile,os.F_OK):
      if (os.stat(zefile).st_size>0):
         fid=tables.open_file(zefile,'r')
         prof=fid.root.profiles
         x=fid.root.x.read()
         x=x+0.4
         hdr=prof._v_attrs
         print p-(hdr.nx1-1)
#
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
#        zelab='p ='+str(N)+', t='+t+step+cmax+ce+isc
         zelab='h ='+str(K)
         plotalot(main,x,u,(0.35,1.05),(-10.0,35.0),lab=zelab)
#        plotalot(main,x,rho,(0.35,1.05),(0.0,35.0),lab=zelab)
#        plotalot(i1,x,rho,(0.4,0.75),(14.0,14.6),xticks=[0.4,0.5,0.6,0.7],yticks=[14.0,14.2,14.4,14.6])
#        plotalot(i2,x,rho,(0.7,0.85),(30.6,31.2),xticks=[0.7,0.75,0.8,0.85],yticks=[30.6,30.8,31.0,31.2])
         main.set_xlabel(r'$x$',fontsize=fsize)
k        main.set_ylabel(r'$u$',fontsize=fsize)
#        main.set_ylabel(r'$\rho$',fontsize=fsize)
         plotalot(i1,x,u,(0.4,0.85),(8.66,8.72),xticks=[0.4,0.5,0.6,0.7,0.8],yticks=[8.66,8.68,8.70,8.72])
         fid.close()

main.plot(exact[:,0],exact[:,1],label="exact",ls='--')
i1.plot(exact[:,0],exact[:,1],ls='--')
#i2.plot(exact[:,0],exact[:,1],ls='--')
main.legend(loc='lower left') #u
#main.legend(loc='upper right') #rho

pname='shock2_u_t35_p'+str(p)+'.pdf'
#pname='shock2_d_t35_p'+str(p)+'.pdf'
plt.savefig(pname)
plt.close()
