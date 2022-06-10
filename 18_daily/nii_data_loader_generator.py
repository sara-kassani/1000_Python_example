
# nii loader as a list
images = []
image_list = sorted(glob.glob(os.path.join(input_dir, 'images/') + '*.nii'))
for i, image_name in enumerate(image_list):
    if (image_name.split('.')[1] == 'nii'):
        image = nib.load(image_list[i]).get_fdata()
        images.append(image)
        
print(np.shape(images))       # (111, 224, 224, 64)
type(images)        # list
# ***********************************************************************************
# nii loader as a numpy array
images = []
image_list = sorted(glob.glob(os.path.join(input_dir, 'images/') + '*.nii'))


for i, image_name in enumerate(image_list):
    if (image_name.split('.')[1] == 'nii'):
        image = nib.load(image_name).get_fdata()
        images.append(image)
images = np.array(images)

print(np.shape(images))     # (111, 224, 224, 64)

type(images)    # numpy.ndarray
# ***********************************************************************************





















