images = []
image_list = sorted(glob.glob(os.path.join(input_dir, 'images/') + '*.nii'))


for i, image_name in enumerate(image_list):
    if (image_name.split('.')[1] == 'npy'):
        image = np.load(image_name)
        images.append(image)
images = np.array(images)
