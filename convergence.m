% use proferr to sweep the cases here and do a convergence analysis
exact=load('e1rpex.out');
exact=exact(:,1:2);
orders=[4,8,12,16];
nelms=[50,100,200];
nord=max(size(orders));
nh=max(size(nelms));
pref='profiles';
fname='prof020001.h5';
err=zeros(nord,nh);
for k=1:nh
   kelm=nelms(k);
   for j=1:nord
      p=orders(j);
      casename=strcat('N',num2str(kelm),'_p',num2str(p));
      zefile=strcat(casename,'/',pref,'/',fname);
      [L1,ebar,cbar,xtest]=proferr(zefile,'d',exact,0.0,1.0,0.0);
      oname=strcat(casename,'avgs.dat');
      vsave=[xtest(1,:)',ebar',cbar'];
      save(oname,'vsave','-ascii','-double')
      pause
      close all
      err(j,k)=L1;
   end
end
