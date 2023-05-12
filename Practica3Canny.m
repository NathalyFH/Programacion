%llamamos a nuestra imagen y la asignamos a una variable
foto = imread('Tarea3.jpg');

%convertimos la imagen a escala de grises
foto1 = rgb2gray(foto);

%aplicamos el filtro canny
foto2 = edge(foto1, 'canny');
subplot(2, 2, 1)

%mostramos la foto original
imshow(foto)
title ('Original');
subplot(2, 2, 2);

%mostramos la foto tratada
imshow (foto2);
title ('Filtro Canny');