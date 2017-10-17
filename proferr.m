function [L1,exctav,cmtavg]=proferr(prof,dset,exact,xl,xr,xshift)

% Read profile dset from HDF5 file prof, compare to reference solution called exact,
% and compare averages over elements to averages of reference solution
% between vertices.

% L1    : average taken over elements of L1 error between dset in prof and exact
% prof  : file name of HDF5 file with CMT-nek solution
% exact : 2D array with a column of x and a column of reference solution
%         whatever dset is supposed to be.
% dest  : string with dataset named in it
% idset : index>1 from 1 of column in exact with quantity to compare to 

Globals1D;

hdr = h5info(prof,'/profiles');
Np  = double(hdr.Attributes(4).Value); % HOW DO I ACCESS nx1 BY NAME SO I DON'T HAVE TO KNOW AHEAD OF TIME?!?!? DICTIONARY OR METHOD PLZ!
N   = Np-1;

xtest= h5read(prof,'/x');xmin=min(xtest);xmax=max(xtest);

% sanity check before doing anything else
% if xmin>xl
%     disp('xl out of bounds
%     return
u   = h5read(prof,strcat('/profiles/cmt/',dset));

Nelm_dum = max(size(xtest))/Np;
xtest    = reshape(xtest,Np,Nelm_dum);
u        = reshape(u,Np,Nelm_dum);

% Generate mesh for sanity check with connectivity and quadrature
% operators.

[Nv, VX, K, EToV] = MeshGen1D(xmin,xmax,Nelm_dum);

K-Nelm_dum

% Initialize quadrature for error analysis and construct grid and metric
% for sanity check.

StartUp1D;

max(max(abs(x-xtest)))
[z,w]=zwgll(N);
max(abs(z-r))

% Compute averages using full power quadrature.
cmtavg=w'*(J.*u)./diff(VX);

% Now the stupid part. Average the reference solution. Assume it's
% a piecewise constant (so averages are already given) and its mesh is
% uniformly spaced, cell centers given. That means we count from
% A. the first x-cell-center greater than x(1,e) to 
% B. the last cell center less than x(Np,e).
% If NCELLS in E1RPEX is correctly chosen (I checked), such a choice
% guarantees that cell faces at i+1/2 fall on vertices within some close
% precision

xcell=exact(:,1)-xshift; uexact=exact(:,2);
ncells=max(size(xcell)); exctav=zeros(1,K);
icell=1;
e=1;
dx=xcell(2)-xcell(1); % lol assume uniform reference grid
nelm=0;
while xcell(icell)<xr
    if xcell(icell) > x(Np,e)
        exctav(e)=exctav(e)/nelm;
        nelm=0;
        e=e+1;
    end
    if e > K
        break
    end
    if xcell(icell)>xl
%         exctav(e)=exctav(e)+dx*uexact(icell); % plagued with cancellation
%         errors
        nelm=nelm+1;
        exctav(e)=exctav(e)+uexact(icell);
    end
    icell=icell+1;
    if icell>ncells
        exctav(e)=exctav(e)/nelm;
        break
    end
end

%exctav=exctav./diff(VX); Too much cancellation error

%flavor sanity plot

uavg=zeros(Np,K,2);
for e=1:K
   uavg(:,e,1)=cmtavg(e);
   uavg(:,e,2)=exctav(e);
end
uavg=reshape(uavg,[Np*K,2]);
plot(x(:),u(:),'r.-',x(:),uavg(:,1),'b-',x(:),uavg(:,2),'m-',xcell,uexact,'k--')
legend('CMT-nek solution','CMT-nek element average','E1RPEX element average','E1RPEX solution')
xlabel 'x'
ylabel '\rho'

% L1 error at long last
% L1=mean(abs(cmtavg-exctav)); % ONLY IF perfect overlap between domain and
% stuff

L1=0;
nelm=0;
for e=1:K
    if exctav(e)>0 % this won't work with velocity. GET SMARTERER
        nelm=nelm+1
        L1=L1+abs(exctav(e)-cmtavg(e));
    end
end
if nelm>0
    L1=L1/nelm;
end
