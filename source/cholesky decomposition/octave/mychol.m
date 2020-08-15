function mychol()
sizes= [1024, 2048, 4096, 8192];
times =[0, 0, 0, 0];

for i = 1 : 4
    A = SPDMatrixGenerator(sizes(i));
    tic;
    ch = chol(A);
    times(i) = toc;

end

file="result.csv";

fileID = fopen(file,'a');
for i = 1 : 4
    fprintf(fileID,'%f;',times(i));
end
fprintf(fileID,'\n');
fclose(fileID);