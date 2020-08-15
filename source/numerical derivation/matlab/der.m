function der()
times =[0, 0, 0, 0];

x = 0:0.1:100; 
step = 100/1000;
der1 = zeros(1,1001);
der2 = 0:0.1:100;
der3 = 0:0.1:100;
der4 = 0:0.1:100;

tic;
for i = 1 : 1001
    der1(i) = secondd(@f, x(i), step);
end
times(1) = toc;
    
tic;
for i = 1 : 1001
    der2(i) = secondd(@g, x(i), step);
end
times(2) = toc;
    
tic;
for i = 1 : 1001
    der3(i) = secondd(@h, x(i), step);
end
times(3) = toc;
    
tic;
for i = 1 : 1001
    der4(i) = firstd(@t, x(i), step);
end
times(4) = toc;


file="result.csv";

fileID = fopen(file,'a');
for i = 1 : 4
    fprintf(fileID,'%f;',times(i));
end
fprintf(fileID,'\n');
fclose(fileID);