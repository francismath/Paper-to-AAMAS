clear all;
%k=0.1; delta=0.039; beta=0.997; %b=0.2;
%y=1; tau_f=0.023;
%phi=0.7; rho_u=0.6; xi = 1.3595; 
y=1;g0=0.2;l=0.3;
g=0.0778*0.417;
rho_u=0.1;tau_f=0.23;beta=1/1.003;
xi=1.3595;delta=0.039;phi=0.7;k=4;

pbe1 = phi/(1-beta*(1-delta));

f=@(x)(1+x.^(-xi)).^(-1/xi);
q=@(x)(1+x.^xi).^(-1/xi);
w=@(x)y-k*(1-beta*(1-delta))/(q(x)*(1-tau_f));
Theta=0.01:0.05:2;
   N=length(Theta);
   U1=zeros(N,1);
   U2=zeros(N,1);
   Tau_w=zeros(N,1);
   coeff=zeros(N,1);
   wag=zeros(N,1);
   qq=zeros(N,1);
   
for i=1:1:N
   theta=Theta(i);
   qq(i)=q(theta);
   syms u1 u2 t s;% t, s represent tau_w and (1-tau_w-rho_u)/(1-tau_w);
coeff(i) = (1-phi)/(1-beta+beta*delta+f(theta)*beta);
wag(i) = w(theta);
%s = (1-t-rho_u)/(1-t);
eq0 = w(theta) -(pbe1*y+coeff(i)*l/(1-t))/(pbe1+coeff(i)*(1-t-rho_u)/(1-t))==0;% the wage g s equation (4)
tauw(i) = vpasolve(eq0);
eq1 = u1 - delta/(delta+f(theta))==0;
eq2 = (1-u2)*(tau_f*(y-w(theta))+tauw(i)*w(theta))-u2*rho_u*w(theta)-g*w(theta)-g0==0;
   % substitute wage g s equation (4) into gov budget equation (3), and eliminate tau_w
   U1(i)=vpasolve(eq1);
   U2(i)=vpasolve(eq2);
   
    
end
figure(1)
plot(Theta,U1,Theta,U2)
xlabel('theta')
legend('u1:SS flow condition','u2:entry and other conditions')
Umin=(U1-U2).^2;
find(Umin<0.001)

figure(2)
subplot(1,2,1)
plot(Theta,wag)
xlabel('theta')
ylabel('wage')
subplot(1,2,2)
plot(Theta,tauw)
xlabel('theta')
ylabel('\tau_w')
