import numpy as np
#import matplotlib as mpl
#mpl.use('Agg')
#from matplotlib import pyplot as plt
#fsize=20

# set up for files of this format
# p\h= 0.02 0.01 0.005
# 4   7.1788956e-03   4.0286219e-03   2.2356768e-03
# 8   3.6054882e-03   1.9682076e-03   1.1964447e-03
# 12   2.3256098e-03   1.2906252e-03   8.9164813e-04
# 16   1.6363029e-03   9.1666984e-04   6.7556901e-04

#tmp=np.loadtxt("conv_sod_avg2avg",usecols=(1,2,3))
tmp=np.loadtxt("convLinf",usecols=(1,2,3))
err=tmp[1:,:]
spacings=tmp[0,:]
#orders=np.loadtxt("conv_sod_avg2avg",usecols=(0,),skiprows=1)
orders=np.loadtxt("convLinf",usecols=(0,),skiprows=1)
EOCh=[]

#plt.figure()
for i,p in enumerate(orders):
#   m_hconv, b_hconv= np.polyfit(np.log10(spacings),np.log10(err[i,:]),1)
#   EOCh.append(m_hconv)
   localdiff=np.divide(np.diff(np.log10(err[i,:])),np.diff(np.log10(spacings)))
   print p
   print np.hstack((spacings.reshape(-1,1),err[i,:].reshape(-1,1),np.vstack((-99999,localdiff.reshape(-1,1)))))

#   plt.loglog(spacings,spacings**m_hconv*(10**b_hconv),'r-',spacings,err[i,:],'bo')
#   plt.xlim((1.0e-3,1.0e-1))
#   plt.ylim((1.0e-4,1.0e-2))
#plt.xlabel(r'$h$',fontsize=fsize)
#plt.tick_params(which='major',axis='both',direction='in',labelsize=fsize,length=10,width=1.2)
#plt.tick_params(which='minor',axis='both',direction='in',labelsize=fsize,length=7,width=1.2)
#plt.ylabel(r'$L_1(E(\langle\rho\rangle_{\Omega_e}))$',fontsize=fsize)
#plt.tight_layout()
#plt.grid()
#plt.savefig('sod3_rho_hconv.pdf')
#plt.close()


#EOCp=[]
#for j,h in enumerate(spacings):
#   m_pconv, b_pconv= np.polyfit(np.log10(orders),np.log10(err[:,j]),1)
#   EOCp.append(m_pconv)
##   plt.loglog(orders,orders**m_pconv*(10**b_pconv),'r-',orders,err[:,j],'bo')
##   plt.xlim((1.0,1.0e2))
##   plt.ylim((1.0e-4,1.0e-2))
##plt.xlabel(r'$N-1$',fontsize=fsize)
##plt.tick_params(which='major',axis='both',direction='in',labelsize=fsize,length=10,width=1.2)
##plt.tick_params(which='minor',axis='both',direction='in',labelsize=fsize,length=7,width=1.2)
##plt.ylabel(r'$L_1(E(\langle\rho\rangle_{\Omega_e}))$',fontsize=fsize)
##plt.tight_layout()
##plt.savefig('sod3_rho_pconv.pdf')
##plt.close()

#EOCh=np.array(EOCh)
#EOCp=np.array(EOCp)

#print spacings
#print np.hstack((err,EOCh.reshape(-1,1)))
#print EOCp
