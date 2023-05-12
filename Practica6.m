foto = imread('FigurasGeometricas.png');
imshow (foto);

%se obtiene una línea de medición
d = imdistline;

%indicamos los parámetros de detección de radios de los círculos a detectar
[cor, rad] = imfindcircles (foto, [107 112], 'ObjectPolarity', ...
    'dark','Sensitivity',0.994)

%indicamos la visualización de los radios de los círculos
viscircles(cor, rad, 'EdgeColor', 'g')