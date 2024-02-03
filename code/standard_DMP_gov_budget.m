clear all;
k=0.1774; delta=0.039; beta=0.997; b=0.2;
y=1; tau_f=0.001;
phi=0.7; rho_u=0.60; xi = 1.3595; z=0.05;
f=@(x)(1+x.^(-xi)).^(-1/xi);
q=@(x)(1+x.^xi).^(-1/xi);
w=@(x)(q(x)*(1-tau_f)*y-k*beta*(1-delta))/(q(x)*(1-tau_f));
Theta=0.01:0.01:1;
   N=length(Theta);
   U1=zeros(N,1);
   U2=zeros(N,1);
   Tau_w=zeros(N,1);
 

  
for i=1:1:N
   theta=Theta(i);
   
   syms u1 u2;
eq1 = u1 - delta/(delta+f(theta))==0;
eq2 = (w(theta)-u2*rho_u*w(theta)/(1-u2)+tau_f*(y-w(theta)))...
    /(1-beta+beta*delta+f(theta)*beta)...
    -phi*k/((1-phi)*q(theta))-(rho_u*w(theta)+z)/(1-beta+beta*delta+f(theta)*beta)==0;
   
   U1(i)=vpasolve(eq1);
   U2(i)=vpasolve(eq2);
   W(i)=phi*k/((1-phi)*q(theta))-b/(1-beta+beta*delta+f(theta)*beta);
   Tau_w(i)=U2(i)*rho_u/(1-U2(i))-tau_f*(y/W(i)-1);
   
end
figure(1)
plot(Theta,U1,Theta,U2)
xlabel('theta')
legend('u1:SS flow condition','u2:entry and other conditions')
Umin=(U1-U2).^2;
find(Umin<0.001)

% figure(1)
% subplot(1,2,1)
% plot(Theta,U1)
% xlabel('theta')
% ylabel('u1:SS flow condition')
% subplot(1,2,2)
% plot(Theta,U2)
% xlabel('theta')
% ylabel('u2:entry and other conditions')