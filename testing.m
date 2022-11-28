clc
clear all
[A,B,C] = xlsread('database.xlsx','Sheet3');
fid = fopen('text.txt', 'r');
a = fscanf(fid,'%c');
% a = cellstr(a);
x = a(1:10);

car1 = C(2,1);
car1 = cell2mat(car1);
% car1 = int2str(car1);

car2 = C(3,1);
car2 = cell2mat(car2);
% car2 = int2str(car2);

car3 = C(3,1);
car3 = cell2mat(car3);
% car3 = int2str(car3);

car4 = C(3,1);
car4 = cell2mat(car4);
% car4 = int2str(car4);
valid = 0;
if x == car1
    tts ('Valid car detected.');
    set(handles.txt_stolen,'string',car1);
    valid = 1;
elseif x == car2
    tts ('Valid car detected.');
    set(handles.txt_stolen,'string',car2);
    valid = 1;
elseif x == car3
    tts ('Valid car detected.');
    set(handles.txt_stolen,'string',car3);
    valid = 1;
elseif x == car4
    tts ('Valid car detected.');
    set(handles.txt_stolen,'string',car4);
    valid = 1;
else
    tts ('Car not registered.');
    set(handles.txt_stolen,'string','Car not registered.');
end

if valid == 1
    
    [A,B,C] = xlsread('database.xlsx','Sheet1');
    a = C(2,2);
    entry = cell2mat(a);
    entry1 = int2str(entry);
    d_cell = strcat('A', entry1);
    % winopen('text.txt')%Open 'text.txt' file
    fid = fopen('text.txt', 'r');
    a = fscanf(fid,'%c');
    b = strcat('Recognised Number Plate is',a);
    disp(b)
    set(handles.txt_plate,'string',a);
    a = cellstr(a);
    qwe = xlswrite('database.xlsx', a, 'Sheet1', d_cell);
    d_cell = 'B2';
    qwe = xlswrite('database.xlsx', (entry + 1), 'Sheet1', d_cell);
    tts (b);
    fclose(fid)
    x = a(1:10);
    [A1,B1,C1] = xlsread('database.xlsx','Sheet2');
    a1 = C1(2,1);
    a1 = cell2mat(a1);
    a1 = int2str(a1);
    a2 = C1(3,1);
    a2 = cell2mat(a2);
    a2 = int2str(a2);
    if x == a1
        tts ('Alert! Stolen Vehicle Detected.');
        set(handles.txt_stolen,'string','Alert! Stolen Vehicle Detected.');
    elseif x == a2
        tts ('Alert! Stolen Vehicle Detected.');
        set(handles.txt_stolen,'string','Alert! Stolen Vehicle Detected.');
    end
end