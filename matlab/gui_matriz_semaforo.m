
function varargout = gui_matriz_semaforo(varargin)
% GUI_MATRIZ_SEMAFORO MATLAB code for gui_matriz_semaforo.fig
%      GUI_MATRIZ_SEMAFORO, by itself, creates a new GUI_MATRIZ_SEMAFORO or raises the existing
%      singleton*.
%
%      H = GUI_MATRIZ_SEMAFORO returns the handle to a new GUI_MATRIZ_SEMAFORO or the handle to
%      the existing singleton*.
%
%      GUI_MATRIZ_SEMAFORO('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in GUI_MATRIZ_SEMAFORO.M with the given input arguments.
%
%      GUI_MATRIZ_SEMAFORO('Property','Value',...) creates a new GUI_MATRIZ_SEMAFORO or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before gui_matriz_semaforo_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to gui_matriz_semaforo_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help gui_matriz_semaforo

% Last Modified by GUIDE v2.5 10-Mar-2019 09:15:07

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @gui_matriz_semaforo_OpeningFcn, ...
                   'gui_OutputFcn',  @gui_matriz_semaforo_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before gui_matriz_semaforo is made visible.
function gui_matriz_semaforo_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to gui_matriz_semaforo (see VARARGIN)

% Choose default command line output for gui_matriz_semaforo
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes gui_matriz_semaforo wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = gui_matriz_semaforo_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
valor=get(hObject,'String');
if isnan(str2double(valor))
    set(handles.text4,'String','Por favor digite un numero entero superior a 8 en la casilla filas');
    handles.edit1='8';
else   
    if str2double(valor)<8
        set(handles.text4,'String','Por favor digite un numero entero superior a 8 en la casilla filas');
         handles.edit1='8';
    else 
        handles.edit1=valor;
    end    
    
end    
guidata(hObject,handles); 
% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit2_Callback(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
valor=get(hObject,'String');
if isnan(str2double(valor))
    set(handles.text4,'String','Por favor digite un numero entero superior a 8 en la casilla columnas');
    handles.edit2='8';
else   
    if str2double(valor)<8
        set(handles.text4,'String','Por favor digite un numero entero superior a 8 en la casilla columnas');
         handles.edit2='8';
    else 
        handles.edit2=valor;
    end    
    
end    
guidata(hObject,handles); 
% Hints: get(hObject,'String') returns contents of edit2 as text
%        str2double(get(hObject,'String')) returns contents of edit2 as a double


% --- Executes during object creation, after setting all properties.
function edit2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in Cargar.
function Cargar_Callback(hObject, eventdata, handles)
% hObject    handle to Cargar (see GCBO)
A=str2double(handles.edit1);
B=str2double(handles.edit2);
m=zeros(A,B);
axes(handles.axes1); image(m); background = m; axis off;  
fprintf('pulsado\n');
set(handles.text4,'String','Pasa');
%if isnan(str2double(get(hObject,'edit1')))
 %   fprintf('no es un numero valido');
    
%end    
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% --- Executes on button press in pushbutton2.


function pushbutton2_Callback(hObject, eventdata, handles)
dato=handles.edit3;
 m=str2num(dato);
 A=str2double(handles.edit1);
  B=str2double(handles.edit2);
 tam=size(m); %tam(1) filas tam(2)columnas
 %zeros(i,j) i=filas j=columnas
 set(handles.text4,'String',num2str(tam));
 m=compara(m,A,B);
%  if tam(1)==A
%     fprintf ('long adecuada');
%  elseif tam(2)<B
%      m=cat(1,m,zeros(A-tam(1),B));
%  end

 imagen=(cat(3,zeros(A,B),m,zeros(A,B)));
 axes(handles.axes1); image(imagen);axis off;
 global mA;
 mA=imagen;
 mm=size(m);


% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
ak=handles.edit8;
b=str2num(ak);


% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
dato=handles.edit3;
 m=str2num(dato);
 A=str2double(handles.edit1);
  B=str2double(handles.edit2);
 tam=size(m); %tam(1) filas tam(2)columnas
 %zeros(i,j) i=filas j=columnas
 set(handles.text4,'String',num2str(tam));
 m=compara(m,A,B);
%  if tam(1)==A
%     fprintf ('long adecuada');
%  elseif tam(2)<B
%      m=cat(1,m,zeros(A-tam(1),B));
%  end

 imagen=(cat(3,m,zeros(A,B),zeros(A,B)));
 axes(handles.axes1); image(imagen); background = m; axis off;
 global mB;
 mB=imagen;


function edit3_Callback(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% Hints: get(hObject,'String') returns contents of edit3 as text
%        str2double(get(hObject,'String')) returns contents of edit3 as a double
handles.edit3=get(hObject,'String');
guidata(hObject,handles); 


% --- Executes during object creation, after setting all properties.
function edit3_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit4_Callback(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit4 as text
%        str2double(get(hObject,'String')) returns contents of edit4 as a double


% --- Executes during object creation, after setting all properties.
function edit4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit5_Callback(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit5 as text
%        str2double(get(hObject,'String')) returns contents of edit5 as a double


% --- Executes during object creation, after setting all properties.
function edit5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes when entered data in editable cell(s) in uitable2.
function uitable2_CellEditCallback(hObject, eventdata, handles)
% hObject    handle to uitable2 (see GCBO)
% eventdata  structure with the following fields (see MATLAB.UI.CONTROL.TABLE)
%	Indices: row and column indices of the cell(s) edited
%	PreviousData: previous data for the cell(s) edited
%	EditData: string(s) entered by the user
%	NewData: EditData or its converted form set on the Data property. Empty if Data was not changed
%	Error: error string when failed to convert EditData to appropriate value for Data
% handles    structure with handles and user data (see GUIDATA)



% --- Executes during object creation, after setting all properties.
function edit6_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit8_Callback(hObject, eventdata, handles)
% hObject    handle to edit8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
daostr=get(handles.edit8,'String');
handles.edit8=daostr;
guidata(hObject,handles); 
% Hints: get(hObject,'String') returns contents of edit8 as text
%        str2double(get(hObject,'String')) returns contents of edit8 as a double


% --- Executes during object creation, after setting all properties.
function edit8_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit8 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton6.
function pushbutton6_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global mA;global mB;
A=str2double(handles.edit9);
axes(handles.axes1);image(mA);
t = timer('TimerFcn', 'stat=false; disp(''Timer!'')','StartDelay',A);
start(t)
stat=true;
n=0;
while(stat==true)
  disp('.');
  pause(1);n=1+n;
  if n>A
      break
  end    
end
axes(handles.axes1);image(mB);




function edit9_Callback(hObject, eventdata, handles)
% hObject    handle to edit9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
valor=get(hObject,'String');
if isnan(str2double(valor))
    set(handles.text4,'String','Por favor digite un numero entero superior a 0');
    handles.edit1='1';
else 
        handles.edit1=valor;   
end    
guidata(hObject,handles); 
% Hints: get(hObject,'String') returns contents of edit9 as text
%        str2double(get(hObject,'String')) returns contents of edit9 as a double


% --- Executes during object creation, after setting all properties.
function edit9_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit9 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in radiobutton1.
function radiobutton1_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% Hint: get(hObject,'Value') returns toggle state of radiobutton1


% --- If Enable == 'on', executes on mouse press in 5 pixel border.
% --- Otherwise, executes on mouse press in 5 pixel border or over radiobutton1.
function radiobutton1_ButtonDownFcn(hObject, eventdata, handles)
% hObject    handle to radiobutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes during object creation, after setting all properties.
% hObject    handle to pushbutton6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called


% --- Executes during object deletion, before destroying properties.
function pushbutton6_DeleteFcn(hObject, eventdata, handles)
% hObject    handle to pushbutton6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
