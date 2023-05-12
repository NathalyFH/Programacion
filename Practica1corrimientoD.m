foto = imread ('Tarea3nueva.jpg');
byn = mat2gray (foto);
r = foto(:,:,1);
g = foto(:,:,2);
b = foto(:,:,3);

image(r)
image(g)
image(b)
h = [1,1,1;1,1,1;1,1,1];
[f,c] = size(foto);
k = 3;

%h1 = zeros(3,3);
h1 = [h(1,1:end),h(2,1:end),h(3,1:end)];

%kernel
for i = length(h):f-length(h)+1
    for j = length(h):c-length(h)+1
        xr(k,:)=255*[byn(i,j:j+2),byn(i+1,j:j+2),byn(i+2,j:j+2)];
        yr(k,:) = conv(xr(k,:),h1);
        ir(i,j) = yr(k,10);
        k = k+1;
    end
end

imshow(foto)
title ('Original');
subplot(2, 2, 2);

imshow (byn);
title ('corrimiento');