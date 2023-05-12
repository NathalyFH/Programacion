%llamamos la imagen y la declaramos como alguna variable para almacenarla
foto = imread('tarea3ByN.jpg');
foto = rgb2gray(foto);

%aplicamos nuestro filtro gradiente
[gx, gy] = imgradientxy(foto, 'sobel');

%asignamos valores vectoriales de dirección y magnitud
[gmag, gdir]=imgradient(gx,gy);
%subplot(2,2,1);

%mostramos la imagen original
imshow(foto);
title('Original');
%subplot(2,2,2);

%mostramos la imagen tratada en los ejes X y Y
figure;
imshow(gx);
title ('Gradiente (dx)');
imshow(gy);
title ('Gradiente (dy)');