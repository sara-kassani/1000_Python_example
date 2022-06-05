%% Read in an Image
firstimage = imread('brain-mri2.jpg');

% Get information about variable
size(firstimage);
imshow(firstimage);
title('Brain MRI');


% Accessing to an individual pixel element. (Pixel value of row=300, column=410, red channel=1) 
firstimage(300,410,1);

%% Display only red channel

figure(2)
imshow(firstimage(:, :, 1))
title('Brain MRI - Red Channel')

%% Read in an grascale image
mri= imread('mri-gray.png');
size(mri)
imshow(mri);
title('MRI - Grayscale image')

max(mri(:))
min(mri(:))


