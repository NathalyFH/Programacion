%llamamos la imagen y la declaramos como alguna variable para almacenarla
foto = imread ('Tarea3nueva.jpg');

%Mostramos la imagen original
imshow(foto)

%La convertimos a escala de grises con ayuda del comando im2gray y
%llamandola con la variable antes mencionada.
foto1 = im2gray(foto);

%con ayuda de figure creamos una ventana de figura nueva utilizando valores
%de propiedades predeterminados en la que mostraremos la imagen en escala
%de grises
figure()
imshow(foto1)

%En otra ventana se desplegará el histograma
figure()
imhist(foto1)