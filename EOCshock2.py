import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
fsize=24
pconv=np.loadtxt("conv",usecols=(2,))
pconv=pconv[1:]
hconv=np.loadtxt("conv",skiprows=2)
hconv=hconv[0,1:]
h=[0.02,0.01,0.005]
orders=[4,8,12]
#del m_hconv m_pconv b_hconv b_pconv
m_hconv, b_hconv= np.polyfit(np.log10(h),np.log10(hconv),1)
m_pconv, b_pconv= np.polyfit(np.log10(orders),np.log10(pconv),1)
plt.loglog(h,h**m_hconv*(10**b_hconv),'r-',h,hconv,'bo-')
print m_hconv #0.996033980523
plt.xlabel(r'$h$',fontsize=fsize)
plt.tick_params(axis='both',labelsize=fsize,length=7,width=1.2)
plt.ylabel(r'$L_1(E(\langle\rho\rangle_{\Omega_e}))$',fontsize=fsize)
plt.tight_layout()
plt.savefig('shock2_rho_hconv_p8.pdf')                                                                             
plt.close()
print m_pconv # -1.07797773187
plt.loglog(orders,orders**m_pconv*(10**b_pconv)*1.1,'r-',orders,pconv,'bo-')
plt.xlabel(r'$N-1$',fontsize=fsize)
plt.tick_params(axis='both',labelsize=fsize,length=7,width=1.2)
plt.ylabel(r'$L_1(E(\langle\rho\rangle_{\Omega_e}))$',fontsize=fsize)
plt.tight_layout()
plt.savefig('shock2_rho_pconv_K100.pdf')                                                                             

p=8
#   m_hconv, b_hconv= np.polyfit(np.log10(spacings),np.log10(err[i,:]),1)
#   EOCh.append(m_hconv)
print hconv #[ 0.75354069  0.2458658   0.18942378]
localdiff=np.divide(np.diff(np.log10(hconv)),np.diff(np.log10(h)))
print h # [0.02, 0.01, 0.005]
print hconv  #[ 0.75354069  0.2458658   0.18942378]
print localdiff #[ 1.61581435  0.37625361]
