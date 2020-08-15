function solving()
sizes= [512, 1024, 1536, 2048];
times =[0, 0, 0, 0];

for i = 1 : 4
    A = rand(sizes(i), sizes(i));
    tic;
    [V,D] = eig(A);
    times(i) = toc;
end

file="result.csv";

fileID = fopen(file,'a');
for i = 1 : 4
    fprintf(fileID,'%f;',times(i));
end
fprintf(fileID,'\n');
fclose(fileID);