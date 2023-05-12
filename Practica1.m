%Llamamos a nuestra imagen a color
I = imread('Tarea3.jpg');

%Convertimos la imagen a escala de grises
I1 = rgb2gray(I);

%Configuramos nuestro kernel
kernel = [0 1 0 ; 1 -4 1; 0 1 0];

%Sharpeamos la imagen sobreponiendo el kernel
r = uint8(filter2 (kernel, I1, 'same'));
sharpedim =imsubtract (I1, r);
subplot (1,2,1);

%Mostramos la imagen original en escala de grises y nuestra imagen ajustada
imshow(I1);
title('original');
subplot(1,2,2);
imshow(sharpedim);
title('sharp');