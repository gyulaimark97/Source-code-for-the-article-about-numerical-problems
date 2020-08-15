function interp()
sizes= [100000, 200000, 300000, 400000];
times =[0, 0, 0, 0];

x = 0:1:30; 
y = 0:1:30;

for i = 1:length(x)
    y(i)=0;
    y(i) = (x(i)*x(i)*x(i))/4;
end

for i = 1 : 4
    tic;
    v = interp1(x,y,sizes(i));
    times(i) = toc;
end

file="result.csv";

fileID = fopen(file,'a');
for i = 1 : 4
    fprintf(fileID,'%f;',times(i));
end
fprintf(fileID,'\n');
fclose(fileID);