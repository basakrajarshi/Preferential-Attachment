% the preferential attachment mechanism
n = 10^6; % size of the network
c = 3; % k_out
r = 1; % uniform attachment contribution
p = c/(c+r); % attachment probability
x = zeros(1,c*n); % stores the graph
x(1:12) = [2 3 4 1 3 4 1 2 4 1 2 3]; % a 4-clique seed graph
for t=5:n
    %disp(t)
    for j=1:c % for each out-edge
        disp(j)
        if rand(1)<p % choose by preferential attachment
            d = x(randi(c*(t-1),1));
        else % choose by uniform attachment
            d = randi(t-1,1);
        end
        x(c*(t-1)+j) = d; % record the attachment
    end
end
degs = hist(x,(1:n)); % in-degree sequence
% plot the degree distribution as a ccdf
hx = (0:max(degs))';
hc = hist(degs,hx)'./n;
hc = [[hx; hx(end)+1] 1-[0; cumsum(hc)]];
hc(hc(:,2)<10^-10,:) = [];
figure;
loglog(hc(2:end,1),hc(2:end,2),'r-','LineWidth',3);
set(gca,'FontSize',16);