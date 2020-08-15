function A = SPDMatrixGenerator(n)
%A = randi([0,100],n, n);
A = rand(n);
A = 0.5*(A+A');
A = A + n*eye(n);
end