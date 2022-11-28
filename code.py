import numpy as np
import matplotlib.pyplot as plt
    
def code(varargin = None): 
    # CODE M-file for code.fig
#      CODE, by itself, creates a new CODE or raises the existing
#      singleton*.
    
    #      H = CODE returns the handle to a new CODE or the handle to
#      the existing singleton*.
    
    #      CODE('CALLBACK',hObject,eventData,handles,...) calls the local
#      function named CALLBACK in CODE.M with the given input arguments.
    
    #      CODE('Property','Value',...) creates a new CODE or raises the
#      existing singleton*.  Starting from the left, property value pairs are
#      applied to the GUI before code_OpeningFcn gets called.  An
#      unrecognized property name or invalid value makes property application
#      stop.  All inputs are passed to code_OpeningFcn via varargin.
    
    #      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
#      instance to run (singleton)".
    
    # See also: GUIDE, GUIDATA, GUIHANDLES
    
    # Edit the above text to modify the response to help code
    
    # Last Modified by GUIDE v2.5 29-Dec-2015 18:03:22
    
    # Begin initialization code - DO NOT EDIT
    gui_Singleton = 1
    gui_State = struct('gui_Name',mfilename,'gui_Singleton',gui_Singleton,'gui_OpeningFcn',code_OpeningFcn,'gui_OutputFcn',code_OutputFcn,'gui_LayoutFcn',[],'gui_Callback',[])
    if len(varargin) and ischar(varargin[0]):
        gui_State.gui_Callback = str2func(varargin[0])
    
    if nargout:
        varargout[np.arange[1,nargout+1]] = gui_mainfcn(gui_State,varargin[:])
    else:
        gui_mainfcn(gui_State,varargin[:])
    
    # End initialization code - DO NOT EDIT
    
    # --- Executes just before code is made visible.
    
def code_OpeningFcn(hObject = None,eventdata = None,handles = None,varargin = None): 
    # This function has no output args, see OutputFcn.
# hObject    handle to figure
# eventdata  reserved - to be defined in a future version of MATLAB
# handles    structure with handles and user data (see GUIDATA)
# varargin   command line arguments to code (see VARARGIN)
    
    # Choose default command line output for code
    handles.output = hObject
    ser = serial('COM3')
    # Update handles structure
    handles.ser = ser
    guidata(hObject,handles)
    # UIWAIT makes code wait for user response (see UIRESUME)
# uiwait(handles.figure1);
    
    # --- Outputs from this function are returned to the command line.
    
def code_OutputFcn(hObject = None,eventdata = None,handles = None): 
    # varargout  cell array for returning output args (see VARARGOUT);
# hObject    handle to figure
# eventdata  reserved - to be defined in a future version of MATLAB
# handles    structure with handles and user data (see GUIDATA)
    
    # Get default command line output from handles structure
    varargout[0] = handles.output
    # --- Executes on button press in cmd_start.
    
def cmd_start_Callback(hObject = None,eventdata = None,handles = None): 
    # hObject    handle to cmd_start (see GCBO)
# eventdata  reserved - to be defined in a future version of MATLAB
# handles    structure with handles and user data (see GUIDATA)
    handles.output = hObject
    ser = handles.ser
    # Video 1 code
# vid=videoinput('winvideo',1,'YUY2_320x240');
# videoRes = get(vid, 'VideoResolution');
# numberOfBands = get(vid, 'NumberOfBands');
# axes(handles.axes3)
# handleToImage = image( zeros([videoRes(2), videoRes(1), numberOfBands], 'uint8') );
# preview(vid,handleToImage)
    
    vid1 = videoinput('winvideo',2,'YUY2_320x240')
    videoRes1 = get(vid1,'VideoResolution')
    numberOfBands = get(vid1,'NumberOfBands')
    axes(handles.axes2)
    handleToImage1 = image(np.zeros((np.array([videoRes1(2),videoRes1(1),numberOfBands]),'uint8')))
    preview(vid1,handleToImage1)
    # preview(vid)
# preview(vid1)
    pause(15)
    a1 = getsnapshot(vid1)
    g = a1(::1)
    
    imtool(g)
    log = roicolor(g,210,255)
    axes(handles.axes2)
    imshow(log)
    lab1,num1 = bwlabel(log,8)
    #imtool(lab)
    sizeBlob1 = np.zeros((1,num1))
    j = 0
    for i in np.arange(1,num1+1).reshape(-1):
        sizeblob1[i] = len(find(lab1 == i))
    
    maxno,largestBlobNo = np.amax(sizeblob1)
    outim = np.zeros((log.shape,'uint8'))
    outim[find[lab1 == largestBlobNo]] = 1
    last = 255 * outim
    vehicle = 0
    sizeblob1(largestBlobNo)
    if (sizeblob1(largestBlobNo) > 3000):
        set(handles.txt_vehicle,'string','Vehicle Type:HMV')
        vehicle = 80
    else:
        set(handles.txt_vehicle,'string','Vehicle Type:LMV')
        vehicle = 40
    
    #   sizeblob1
    
    #I=getsnapshot(vid);
    I = imread('MATLAB\19.jpg')
    axes(handles.axes3)
    imshow(I)
    ## Plate Extraction Code
    plt.figure(1)
    imshow(I)
    # Extract Y component (Convert an Image to Gray)
    Igray = rgb2gray(I)
    rows,cols = Igray.shape
    ## Dilate and Erode Image in order to remove noise
    Idilate = Igray
    for i in np.arange(1,rows+1).reshape(-1):
        for j in np.arange(2,cols - 1+1).reshape(-1):
            temp = np.amax(Igray(i,j - 1),Igray(i,j))
            Idilate[i,j] = np.amax(temp,Igray(i,j + 1))
    
    I = Idilate
    plt.figure(2)
    imshow(Igray)
    plt.figure(3)
    plt.title('Dilated Image')
    imshow(Idilate)
    plt.figure(4)
    imshow(I)
    difference = 0
    sum = 0
    total_sum = 0
    difference = uint32(difference)
    ## PROCESS EDGES IN HORIZONTAL DIRECTION disp('Processing Edges Horizontally...');
    max_horz = 0
    maximum = 0
    for i in np.arange(2,cols+1).reshape(-1):
        sum = 0
        for j in np.arange(2,rows+1).reshape(-1):
            if (I(j,i) > I(j - 1,i)):
                difference = uint32(I(j,i) - I(j - 1,i))
            else:
                difference = uint32(I(j - 1,i) - I(j,i))
            if (difference > 20):
                sum = sum + difference
        horz1[i] = sum
        # Find Peak Value
        if (sum > maximum):
            max_horz = i
            maximum = sum
        total_sum = total_sum + sum
    
    average = total_sum / cols
    plt.figure(5)
    # Plot the Histogram for analysis subplot(3,1,1);
    plt.plot(horz1)
    plt.title('Horizontal Edge Processing Histogram')
    plt.xlabel('Column Number ->')
    plt.ylabel('Difference ->')
    ## Smoothen the Horizontal Histogram by applying Low Pass Filter disp('Passing Horizontal Histogram through Low Pass Filter...');
    sum = 0
    horz = horz1
    for i in np.arange(21,(cols - 21)+1).reshape(-1):
        sum = 0
        for j in np.arange((i - 20),(i + 20)+1).reshape(-1):
            sum = sum + horz1(j)
        horz[i] = sum / 41
    
    subplot(3,1,2)
    plt.plot(horz)
    plt.title('Histogram after passing through Low Pass Filter')
    plt.xlabel('Column Number ->')
    plt.ylabel('Difference ->')
    ## Filter out Horizontal Histogram Values by applying Dynamic Threshold disp('Filter out Horizontal Histogram...');
    for i in np.arange(1,cols+1).reshape(-1):
        if (horz(i) < average):
            horz[i] = 0
            for j in np.arange(1,rows+1).reshape(-1):
                I[j,i] = 0
    
    subplot(3,1,3)
    plt.plot(horz)
    plt.title('Histogram after Filtering')
    plt.xlabel('Column Number ->')
    plt.ylabel('Difference ->')
    plt.figure(10)
    imshow(I)
    ## PROCESS EDGES IN VERTICAL DIRECTION
    difference = 0
    total_sum = 0
    difference = uint32(difference)
    print('Processing Edges Vertically...')
    maximum = 0
    max_vert = 0
    for i in np.arange(2,rows+1).reshape(-1):
        sum = 0
        for j in np.arange(2,cols+1).reshape(-1):
            #cols
            if (I(i,j) > I(i,j - 1)):
                difference = uint32(I(i,j) - I(i,j - 1))
            if (I(i,j) <= I(i,j - 1)):
                difference = uint32(I(i,j - 1) - I(i,j))
            if (difference > 20):
                sum = sum + difference
        vert1[i] = sum
        ## Find Peak in Vertical Histogram
        if (sum > maximum):
            max_vert = i
            maximum = sum
        total_sum = total_sum + sum
    
    average = total_sum / rows
    plt.figure(6)
    subplot(3,1,1)
    plt.plot(vert1)
    plt.title('Vertical Edge Processing Histogram')
    plt.xlabel('Row Number ->')
    plt.ylabel('Difference ->')
    ## Smoothen the Vertical Histogram by applying Low Pass Filter disp('Passing Vertical Histogram through Low Pass Filter...');
    sum = 0
    vert = vert1
    for i in np.arange(21,(rows - 21)+1).reshape(-1):
        sum = 0
        for j in np.arange((i - 20),(i + 20)+1).reshape(-1):
            sum = sum + vert1(j)
        vert[i] = sum / 41
    
    subplot(3,1,2)
    plt.plot(vert)
    plt.title('Histogram after passing through Low Pass Filter')
    plt.xlabel('Row Number ->')
    plt.ylabel('Difference ->')
    ## Filter out Vertical Histogram Values by applying Dynamic Threshold disp('Filter out Vertical Histogram...');
    for i in np.arange(1,rows+1).reshape(-1):
        if (vert(i) < average):
            vert[i] = 0
            for j in np.arange(1,cols+1).reshape(-1):
                I[i,j] = 0
    
    subplot(3,1,3)
    plt.plot(vert)
    plt.title('Histogram after Filtering')
    plt.xlabel('Row Number ->')
    plt.ylabel('Difference ->')
    plt.figure(7)
    imshow(I)
    ## Find Probable candidates for Number Plate
    j = 1
    for i in np.arange(2,cols - 2+1).reshape(-1):
        if (horz(i) != 0 and horz(i - 1) == 0 and horz(i + 1) == 0):
            column[j] = i
            column[j + 1] = i
            j = j + 2
        else:
            if ((horz(i) != 0 and horz(i - 1) == 0) or (horz(i) != 0 and horz(i + 1) == 0)):
                column[j] = i
                j = j + 1
    
    j = 1
    for i in np.arange(2,rows - 2+1).reshape(-1):
        if (vert(i) != 0 and vert(i - 1) == 0 and vert(i + 1) == 0):
            row[j] = i
            row[j + 1] = i
            j = j + 2
        else:
            if ((vert(i) != 0 and vert(i - 1) == 0) or (vert(i) != 0 and vert(i + 1) == 0)):
                row[j] = i
                j = j + 1
    
    temp,column_size = column.shape
    if (np.mod(column_size,2)):
        column[column_size + 1] = cols
    
    temp,row_size = row.shape
    if (np.mod(row_size,2)):
        row[row_size + 1] = rows
    
    ## Region of Interest Extraction
#Check each probable candidate
    for i in np.arange(1,row_size+2,2).reshape(-1):
        for j in np.arange(1,column_size+2,2).reshape(-1):
            # If it is not the most probable region remove it from image
            if (not ((max_horz >= column(j) and max_horz <= column(j + 1)) and (max_vert >= row(i) and max_vert <= row(i + 1))) ):
                #This loop is only for displaying proper output to User
                for m in np.arange(row(i),row(i + 1)+1).reshape(-1):
                    for n in np.arange(column(j),column(j + 1)+1).reshape(-1):
                        I[m,n] = 0
    
    plt.figure(8)
    imshow(I)
    ##Cropping the Image
    for i in np.arange(2,cols+1).reshape(-1):
        for j in np.arange(2,rows+1).reshape(-1):
            if (I(j,i) != 0):
                temp_x = i
                temp_y = j
                break
        if (I(j,i) != 0):
            break
    
    x = temp_x
    y = temp_y
    for i in np.arange(temp_x,cols+1).reshape(-1):
        for j in np.arange(temp_y,rows+1).reshape(-1):
            if (I(j,i) != 0):
                temp_x = i
                temp_y = j
    
    cl = temp_x - x
    ch = temp_y - y
    a = imcrop(I,np.array([x + 10,y,cl - 20,ch]))
    ##Making it Perfect
# for i = 1:20
#     for j = 1:ch
#         if(I2(j,i)<=150)
#             I2(j,1)=0;
#         end
#     end
# end
    
    plt.figure(9)
    imshow(a)
    g = a(:,:,1)
    
    log = roicolor(g,0,100)
    
    imagen = clip(log)
    #imtool(log);
    axes(handles.axes3)
    imshow(imagen)
    
    #*-*-*Filter Image Noise*-*-*-*
    if len(imagen.shape) == 3:
        imagen = rgb2gray(imagen)
    
    imagen = medfilt2(imagen)
    f,c = imagen.shape
    imagen[1,1] = 255
    imagen[f,1] = 255
    imagen[1,c] = 255
    imagen[f,c] = 255
    #imtool(imagen);
#*-*-*END Filter Image Noise*-*-*-*
    word = []
    
    re = imagen
    fid = open('text.txt','wt')
    
    while 1:

        fl,re = lines(re)
        rq = fl
        while 1:

            fl1,rq = columns(rq)
            imgn = not fl1 
            #*-*Uncomment line below to see lines one by one*-*-*-*
# imtool(fl);pause(1)
#*-*--*-*-*-*-*-*-
#*-*-*-*-*-Calculating connected components*-*-*-*-*-
            L = bwlabel(imgn)
            mx = np.amax(np.amax(L))
            BW = edge(double(imgn),'sobel')
            imx,imy = BW.shape
            for n in np.arange(1,mx+1).reshape(-1):
                r,c = find(L == n)
                rc = np.array([r,c])
                sx,sy = rc.shape
                n1 = np.zeros((imx,imy))
                for i in np.arange(1,sx+1).reshape(-1):
                    x1 = rc(i,1)
                    y1 = rc(i,2)
                    n1[x1,y1] = 255
                #*-*-*-*-*-END Calculating connected components*-*-*-*-*
                n1 = not n1 
                n1 = not clip(n1) 
                img_r = same_dim(n1)
                #*-*Uncomment line below to see letters one by one*-*-*-*
#imshow(img_r);pause(1)
#*-*-*-*-*-*-*-*
                letter = genetic(img_r)
                word = np.array([word,letter])
            if len(rq)==0:
                fid = open('text.txt','wt')
                fid.write('%s\n' % (word))
            else:
                fid.write('%s\n' % (word.lower()))
                fid.write('%s\t' % (word))
            #     word=[];#Clear 'word' variable
            if len(rq)==0:
                break

        if len(rq)==0:
            if len(re)==0:
                break
        #*-*-*When the sentences finish, breaks the loop*-*-*-*
        #*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

    
    fid.close()
    A,B,C = xlsread('database.xlsx','Sheet3')
    fid = open('text.txt','r')
    # a = fscanf(fid,'#c');
# a = cellstr(a);
    a = word
    x = a(np.arange(1,10+1))
    car1 = C(2,1)
    car1 = cell2mat(car1)
    # car1 = int2str(car1);
    
    car2 = C(3,1)
    car2 = cell2mat(car2)
    # car2 = int2str(car2);
    
    car3 = C(4,1)
    car3 = cell2mat(car3)
    # car3 = int2str(car3);
    
    car4 = C(6,1)
    car4 = cell2mat(car4)
    # car4 = int2str(car4);
    valid = 0
    if x == car1:
        tts('Valid car detected.')
        set(handles.txt_break,'string',car1)
        valid = 1
    else:
        if x == car2:
            tts('Valid car detected.')
            set(handles.txt_break,'string',car2)
            valid = 1
        else:
            if x == car3:
                tts('Valid car detected.')
                set(handles.txt_break,'string',car3)
                valid = 1
            else:
                if x == car4:
                    tts('Valid car detected.')
                    set(handles.txt_break,'string',car4)
                    valid = 1
                else:
                    tts('Car not registered.')
                    set(handles.txt_break,'string','Car not registered.')
    
    if valid == 1:
        A,B,C = xlsread('database.xlsx','Sheet1')
        a = C(2,2)
        entry = cell2mat(a)
        entry1 = int2str(entry)
        d_cell = strcat('A',entry1)
        # winopen('text.txt')#Open 'text.txt' file
        fid = open('text.txt','r')
        a = fscanf(fid,'%c')
        b = strcat('Recognised Number Plate is',a)
        print(b)
        set(handles.txt_plate,'string',a)
        a = cellstr(a)
        qwe = xlswrite('database.xlsx',a,'Sheet1',d_cell)
        d_cell = 'B2'
        qwe = xlswrite('database.xlsx',(entry + 1),'Sheet1',d_cell)
        tts(b)
        fid.close()
        fid = open('text.txt','r')
        #     a = fscanf(fid,'#c');
        a = word
        x = a(np.arange(1,10+1))
        A1,B1,C1 = xlsread('database.xlsx','Sheet2')
        a1 = C1(2,1)
        a1 = cell2mat(a1)
        #     a1 = int2str(a1);
        a2 = C1(3,1)
        a2 = cell2mat(a2)
        #     a2 = int2str(a2);
        if x == a1:
            tts('Alert! Stolen Vehicle Detected.')
            set(handles.txt_stolen,'string','Alert! Stolen Vehicle Detected.')
            open(ser)
            ser.write('E' % ())
            pause(1)
            ser.write('X' % ())
            ser.close()
        else:
            if x == a2:
                tts('Alert! Stolen Vehicle Detected.')
                set(handles.txt_stolen,'string','Alert! Stolen Vehicle Detected.')
                open(ser)
                ser.write('E' % ())
                pause(1)
                ser.write('X' % ())
                ser.close()
            else:
                if vehicle == 40:
                    open(ser)
                    ser.write('Q' % ())
                    pause(1)
                    ser.write('X' % ())
                    ser.close()
                else:
                    if vehicle == 80:
                        open(ser)
                        ser.write('W' % ())
                        pause(1)
                        ser.write('X' % ())
                        ser.close()
    else:
        open(ser)
        ser.write('R' % ())
        pause(1)
        ser.write('X' % ())
        ser.close()
    
    guidata(hObject,handles)
    return varargout
