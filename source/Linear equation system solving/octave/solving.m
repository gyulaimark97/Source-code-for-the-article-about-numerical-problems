function solving()
sizes= [512, 768, 1024, 1280];
times =[0, 0, 0, 0];

for i = 1 : 4
    A = SPDMatrixGenerator(sizes(i));
    b = randi([0,1000],sizes(i), sizes(i));
    tic;
    x = linsolve(A,b);
    times(i) = toc;
end

file="result.csv";

fileID = fopen(file,'a');
for i = 1 : 4
    fprintf(fileID,'%f;',times(i));
end
fprintf(fileID,'\n');
fclose(fileID);