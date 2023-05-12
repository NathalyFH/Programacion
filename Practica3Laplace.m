%llamamos la imagen y la declaramos como alguna variable para almacenarla
foto= imread('tarea3ByN.jpg');

%asignamos las dimensiones de la imagen
[x,y]= size(foto);

%covertimos a double la imagen
foto=double(foto);
A=zeros(size(foto));

%Se aplica el filtro Laplaciano mediante un ciclo for
for f=2:x-1
       for c=2:y-1
           A(f,c)=foto(f-1,c)+foto(f,c-1)-4*foto(f,c)+foto(f,c+1)+foto(f+1,c);
       end
end

%matriz entera de 8bits
A=uint8(A);

%mostramos la imagen original
foto=uint8(foto);
figure
subplot(2,2,1)
imshow(foto);
title('Original')

%mostramos la imagen tratada
subplot(2,2,2);
imshow(A);
title('Filtro Laplaciano')