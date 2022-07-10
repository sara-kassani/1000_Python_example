import random

# 1. create RandomOrder of patients (without replacement)
def shuffled(patients):
    random.shuffle(patients)
    return patients
###########################################################################
from tensorflow.compat.v1.keras import backend as K
with tf.device('/gpu:1'):
    model = create_unet(size_x, size_y, size_z)
    history = model.fit(train_images, train_masks, epochs=5, batch_size=1, verbose=1,
                  validation_data=(validation_images, validation_masks))
###########################################################################
from os import listdir
from os.path import isfile, join
dcmfiles = [f for f in listdir(input_dir) if isfile(join(input_dir, f))]
dcmfiles = sorted(dcmfiles)
# dcmfiles
###########################################################################
dcmfiles = []
jpgfiles = []
matfiles = []
for file in all_files:
    if '.dcm' in file:
        dcmfiles.append(file)
    elif '.jpeg' in file:
        jpgfiles.append(file)
    elif '.mat' in file:
        matfiles.append(file)
###########################################################################        
from os import listdir
from os.path import isfile, join
allfiles = [f for f in listdir(input_dir) if isfile(join(input_dir, f))]
allfiles = sorted(allfiles)
allfiles

       
###########################################################################
# pandas-related
pd.set_option('max_colwidth', -1)
###########################################################################
# get filename from glob.glob file paths
# dcmfiles = [os.path.basename(x) for x in files_path_list]
dcmfiles = list(map(os.path.basename, files_path_list))
###########################################################################
class="alert-warning"
class="alert-danger"
class="alert-success"
class="alert-info"

###########################################################################

def plot_sample(input_img, input_mask, color_map = 'nipy_spectral'):
    '''
    Plots and a slice with all available annotations
    '''
    fig = plt.figure(figsize=(20,16), dpi=100)

    plt.subplot(1,3,1)
    plt.imshow(img_slice, cmap='bone')
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1,3,2)
    plt.imshow(mask_slice, alpha=0.5, cmap=color_map)
    plt.title('Mask')
    plt.axis('off')
    
    plt.subplot(1,3,3)
    plt.imshow(img_slice, cmap='bone')
    plt.imshow(mask_slice, alpha=0.5, cmap=color_map)
    plt.title('Liver & Mask')
    plt.axis('off')
    
    plt.show()

###########################################################################
# extract filename from path list
img_filenames = [os.path.basename(x) for x in img_files]

###########################################################################
# run interactive command line
!apt install --allow-change-held-packages libcudnn8=8.1.0.77-1+cuda11.2 -y

###########################################################################
# slices first: (40, 69, 224, 224, 1) 40:number of slices, 69 number of images
def read_nifti_z(image_paths, mask_paths):
    
    if len(image_paths) != len(mask_paths):
        """ValueError: when user gives an invalid value to a function."""
        raise ValueError('The number of input files and segmentation masks are different.')
        
    if len(image_paths) == 0:
        raise ValueError('There is no image in the directory.')
        
    if len(mask_paths) == 0:
        raise ValueError('There is no mask in the directory.')
        
    num_images = len(image_paths)
    for index in range(num_images):
#         print(index)
        image_path = image_paths[index]
#         print(image_path)
        mask_path = mask_paths[index]
#         print(mask_path)
        
        if not os.path.isfile(image_path):
            raise ValueError(f'File {iamge_path} does not exist.')
            
        if not os.path.isfile(mask_path):
            raise ValueError(f'File {mask_path} does not exist.')
            
    input_images = nib.load(image_paths[0]) # load one volume to get the dimensions (x,y,z)
#     print(image_paths[0]) # data/train/images\f_2396.nii
    (nx, ny, nz) = input_images.shape[0:3] # 224 224 29
    
    input_images = np.ndarray((num_images, nx, ny, nz, 1), dtype= np.float32) # (69, 224, 224, 40, 1)
    mask_images = np.ndarray((num_images, nx, ny, nz, 1), dtype= np.float32) # (69, 224, 224, 40, 1)
     
    
    for index in range(0, num_images):
        input_image = nib.load(image_paths[index]) # data/train/images\f_2396.nii
        mask_image = nib.load(mask_paths[index]) # data/train/masks\f_2396.nii
        
        input_images[index, :, :, :, 0]= input_image.get_fdata(dtype= np.float32)
        mask_images[index, :, :, :, 0] = mask_image.get_fdata(dtype= np.float32)
        
        
        input_images = np.moveaxis(input_images, 3, 0)
        mask_images =  np.moveaxis(mask_images, 3, 0)
    
        return input_images, mask_images


###########################################################################

full_name =  '.'.join([file_name, file_extension])

###########################################################################

import tensorflow.python.platform.build_info as build
print("cuda version: ", build.build_info['cuda_version'])
print("cudnn: ", build.build_info['cudnn_version'])

###########################################################################

cd C:\Windows\System32
nvidia-smi.exe -l 10
*********
cd C:\Program Files\NVIDIA Corporation\NVSMI
nvidia-smi.exe -l 10

###########################################################################

def set_seed(seed=0):
    np.random.seed(seed)
    tf.random.set_seed(seed)
set_seed()

###########################################################################

rows,cols=3,3
fig=plt.figure(figsize=(10,10))
for i in range(1,rows*cols+1):
    fig.add_subplot(rows,cols,i)
    img_path=train_files[i]
    msk_path=mask_files[i]
    img=cv2.imread(img_path)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    msk=cv2.imread(msk_path)
    plt.imshow(img)
    plt.imshow(msk,alpha=0.4)
plt.show()

###########################################################################

import pandas as pd
df1 = pd.DataFrame(validation_results, index=['loss', 'iou_score', 'f1-score'], columns=['validation'])
df2 = pd.DataFrame(test_eval_results, index=['loss', 'iou_score', 'f1-score'], columns=['test_eval'])
df3 = pd.DataFrame(test_eval_results_gen, index=['loss', 'iou_score', 'f1-score'], columns=['test_eval_gen'])
df_results= pd.concat([df1, df2, df3], axis=1)
# df_results.transpose()
df_results.transpose()

###########################################################################
masks_path = 'masks/'
    seg_names = os.listdir(masks_path)

###########################################################################

print (keras.backend.image_data_format())

###########################################################################
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]
###########################################################################

denseunet_model = Model(inputs=model.input,outputs=model.get_layer('mid_feature').output)

###########################################################################

'''-----------------Data Generator-----------------'''
# https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly

class DataGenerator(tf.keras.utils.Sequence):

    def __init__(self, img_paths, mask_paths, batch_size, n_classes):
        self.x, self.y = img_paths, mask_paths
        self.batch_size = batch_size
        self.n_classes = n_classes

    def __len__(self):
        return math.ceil(len(self.x) / self.batch_size)

    def read_nifti(self, filepath):
        volume = nib.load(filepath).get_fdata()
        volume = np.array(volume)
        return volume


    def __getitem__(self, idx):

        batch_x = self.x[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_y = self.y[idx * self.batch_size:(idx + 1) * self.batch_size]

        image = [self.read_nifti(image_file) for image_file in batch_x]
        image = np.array(image, dtype=np.float32)
        image = tf.expand_dims(image, axis=-1)
        
        label = [self.read_nifti(mask_file) for mask_file in batch_y]
        label = np.array(label, dtype=np.float32)
        label = tf.keras.utils.to_categorical(label, num_classes=self.n_classes)
        
        return image, label
      
'''---------------------creating the train and validation generators-------------------'''
train_data = DataGenerator(train_images, train_masks, BATCH_SIZE, N_CLASSES)
valid_data = DataGenerator(valid_images, valid_masks, BATCH_SIZE, N_CLASSES)
test_data = DataGenerator(test_images, test_masks, BATCH_SIZE, N_CLASSES) 


###########################################################################

# Set numpy to print only 2 decimal digits for neatness
np.set_printoptions(precision=2, suppress=True)

###########################################################################



###########################################################################



###########################################################################



###########################################################################



###########################################################################



###########################################################################




###########################################################################



###########################################################################



###########################################################################



###########################################################################



###########################################################################



###########################################################################



###########################################################################



###########################################################################



###########################################################################




###########################################################################



###########################################################################



###########################################################################



###########################################################################



###########################################################################



###########################################################################



###########################################################################
