clc
clear all
[A,B,C] = xlsread('database.xlsx','Sheet1');
a = C(2,2);
entry = cell2mat(a);
fid = fopen('text.txt', 'r');
a = fscanf(fid,'%c');
a = cellstr(a);
entry1 = int2str(entry);
d_cell = strcat('A', entry1);
qwe = xlswrite('database.xlsx', a, 'Sheet1', d_cell);
d_cell = 'B2';
qwe = xlswrite('database.xlsx', (entry + 1), 'Sheet1', d_cell);
