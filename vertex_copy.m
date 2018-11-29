% the vertex copy mechanism
n = 1000; % size of network
q = 0.5; % probability to copy a connection
x = zeros(n,2); % edge list
% initial condition: a reciprocally connected triple
x(1,:) = [1 2]; % node 1 points to node 2
x(2,:) = [2 1]; % node 2 points to node 1
x(3,:) = [2 3]; % node 2 points to node 3
x(4,:) = [3 1]; % node 3 points to node 2
m = 4; % number of edges
% start copying
for t=4:n
v = ceil(rand(1)*(t-1)); % vertex to copy
g = x(x(:,1)==v,2); % copied endpoints
k = length(g); % its degree
u = ceil(rand(k,1).*(t-1)); % uniformly random endpoints
s = rand(size(g,1),1)<q; % these endpoints are copied
g(~s) = u(~s); % these endpoints are not
% make those edges
x(m+1:m+k,:) = [t*ones(k,1) g];
m = m+k; % increment edge count
end;
% make an undirected adjacency matrix
B = zeros(n,n);
for i=1:size(x,1)
if x(i,2)~=x(i,1)
B(x(i,1),x(i,2)) = 1;
B(x(i,2),x(i,1)) = 1;
end;
end;
degs = sum(B); % get degree sequence
% plot the degree distribution as a ccdf
pdf = hist(degs,unique(degs));
cdf = [[unique(degs)'; length(pdf)+1] 1-[0 cumsum(pdf./sum(pdf))]'];
cdf(cdf(:,2)<1/n,:) = [];
figure(1);
loglog(cdf(:,1),cdf(:,2),'bo-','LineWidth',2,'MarkerFaceColor',[1 1 1]);
set(gca,'FontSize',16);
xlabel('degree, k','FontSize',16);
ylabel('Pr(K\geq k)','FontSize',16);