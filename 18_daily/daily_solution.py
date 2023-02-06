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
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
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
import pickle
history_filepath = os.path.join('model_history.pickle')
with open(history_filepath, 'wb') as hist_file:
    pickle.dump(history.history, hist_file)
    
import pandas as pd
hist_obj = pd.read_pickle(r'model_history.pickle')        
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
def get_filename_info(filefullname):
    (folderpath,filename) = os.path.split(filefullname)
    (shotname,extension) = os.path.splitext(filename)
    return folderpath, filename, shotname, extension
###########################################################################

# mirrored_strategy = tf.distribute.MirroredStrategy(devices=["/gpu:0", "/gpu:1"], cross_device_ops = tf.distribute.HierarchicalCopyAllReduce())
mirrored_strategy = tf.distribute.MirroredStrategy(devices=["/gpu:0"], cross_device_ops = tf.distribute.HierarchicalCopyAllReduce())

with mirrored_strategy.scope():
#     input_img = (img_height, img_width, img_depth, channels)
    model = cascaded_unet3d(input_size = (224, 224, 64, 1), n_classes=1, dropout=0, out_activation='sigmoid', 
                            padding = 'same', filter_size1 = [64, 128, 256, 256], filter_size2 = [32, 64, 128, 128])
    model.summary()
    model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

###########################################################################

def makedirs(path): 
    try: 
        os.makedirs(path) 
    except OSError: 
        if not os.path.isdir(path): 
            raise


###########################################################################


''' -------------define save names and paths-------------'''
trained_model_architecture_filepath = os.path.join(trained_model_dir, PROJECT_NAME +'_model_architecture.h5')
trained_model_weights_filepath = os.path.join(trained_model_dir, PROJECT_NAME +'_model_weights.h5')
checkpoint_filepath = os.path.join(trained_model_dir, PROJECT_NAME +'_best_weights.h5')
history_filepath = os.path.join(trained_model_dir, PROJECT_NAME +'_history.pickle')
json_filepath = os.path.join(trained_model_dir, PROJECT_NAME +'_model_architecture.json')
csv_logger_filepath = os.path.join(log_dir, PROJECT_NAME +'_training.csv')
# -----------------------------------------------------#
csv_logger = CSVLogger(csv_logger_filepath, separator=',', append=False)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=2, min_lr=0.000001, min_delta=1e-4, verbose=1)
checkpoint = ModelCheckpoint(filepath = checkpoint_filepath, monitor = 'val_loss', verbose = 1, save_best_only = True, save_weights_only = False, mode='auto')

tensorboard_callback = TensorBoard(log_dir, histogram_freq=1)
callbacks = [reduce_lr, checkpoint, csv_logger, tensorboard_callback]
# -----------------------------------------------------#
initial_learning_rate = 0.003
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(initial_learning_rate, decay_steps=1000, decay_rate=0.96, staircase=True)

###########################################################################

def split(img_list, mask_list, split_size): 
    
    x_train,x_test,y_train,y_test = train_test_split(img_list, mask_list, test_size = split_size)
    return x_train, x_test, y_train, y_test

def data_generator(img_list, mask_list, batch_size):
    c = 0
    n = [i for i in range(len(img_list))]
    random.shuffle(n)
    
    while (True):
        img = np.zeros((batch_size, 224, 224, 64,1)).astype('float')   #adding extra dimensions as conv3d takes file of size 5
        mask = np.zeros((batch_size, 224,224, 64,1)).astype('float')
        
        for i in range(c, c+batch_size):
            train_img = nib.load(img_list[n[i]]).get_data()

            train_img = np.expand_dims(train_img,-1)
            train_mask = nib.load(mask_list[n[i]]).get_data()

            train_mask=np.expand_dims(train_mask,-1)

            img[i-c] = train_img
            mask[i-c] = train_mask
            
        c+=batch_size
        
        if(c+batch_size>=len(img_list)):
            c=0
            random.shuffle(n)

        yield img, mask


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
    
###########################################################################
from tensorflow import keras
loaded_model = keras.models.load_model('model_0.0001_architecture.h5',  custom_objects={'dice_loss':dice_loss, 'dice_coef': dice_coef, 
                                                                    'precision': precision, 'recall': recall})
###########################################################################
from tensorflow.keras.models import load_model

model = load_model('model.h5')
model = load_weights('model_weights_2.h5')
###########################################################################
def load_model(model_path):
    """ Load the model from path
    :param model_path: the path to the model .h5 file
    :return: the Keras model
    """
    sm_dice_loss = sm.losses.DiceLoss(class_weights=np.array([0.1, 0.9]))
    focal_loss = sm.losses.BinaryFocalLoss()
    total_loss = sm_dice_loss + (1 * focal_loss)
    
#     dice_loss = sm.losses.DiceLoss()
#     jaccard_loss = sm.losses.JaccardLoss()
#     total_loss = dice_loss + jaccard_loss
    inference_model = keras.models.load_model(
        model_path,
        custom_objects={
            'binary_focal_loss': focal_loss,
            'iou_score':sm.metrics.IOUScore(threshold=0.5), 
            'f1-score':sm.metrics.FScore(threshold=0.5), 
            'recall':sm.metrics.Recall(threshold=0.5), 
            'precision':sm.metrics.Precision(threshold=0.5), 
#             'accuracy': accuracy
        }
    )
    return inference_model
  
  
  
  
  # Load binary or multiclass model
    binary_mode = False
    if num_classes == 2:
        binary_mode = True

    if binary_mode:
        print(f"\nLoading binary segmentation model: {model_path}")
        if model_loss == "focal_loss":
            model = load_model(
                model_path,
                custom_objects={'binary_focal_loss': focal_loss,'iou_score':sm.metrics.IOUScore(threshold=0.5), 'f1-score':sm.metrics.FScore(threshold=0.5), 'recall':sm.metrics.Recall(threshold=0.5), 'precision':sm.metrics.Precision(threshold=0.5) } )
###########################################################################

    # -------- save history --------
    save_history_path = os.path.join(cfg.save_root_path, "metrics.xlsx")
    data = []
    index = []
    for metrics in hist.history:
        index.append(metrics)
        data.append(hist.history.get(metrics))
    df = pd.DataFrame(data=data, index=index, columns=None)
    df.to_excel(save_history_path)

###########################################################################
    predict_value = model.predict(x_predict)

    np.unique(predict_value[...,0], return_counts=True)
    np.sum(predict_value[...,0]<=0.5)


###########################################################################

# Verify generator
img, msk = train_img_datagen.__next__()

next(iter(test_generator))
###########################################################################

    if activate == 'relu':
        atensor = Activation('relu')(input_tensor)
    elif activate == 'elu':
        atensor = Activation('elu')(input_tensor)
    elif activate == 'bn':
        atensor = BatchNormalization(axis=1,momentum=0.5)(input_tensor)
        atensor = Activation(bnacti)(input_tensor)
    elif activate == 'leakyrelu':
        atensor = LeakyReLU(alpha=0.3)(input_tensor)
    elif activate == 'gelu':
        get_custom_objects().update({'gelu': Activation(gelu)})
        atensor = Activation(gelu)(input_tensor)
    elif activate == 'selu':
        atensor = Activation('selu')(input_tensor)

###########################################################################

for current_batch_id in test_id:
    current_batch,current_label=get_data_single3d(current_batch_id)
    
    pred_label=predict_single_image(current_batch)

    
    pred_label=np.squeeze(pred_label)
    current_label=np.squeeze(current_label)
    pred_label[pred_label>.9]=1
    pred_label[pred_label<1]=0
    dice_coeff1=(np.sum(pred_label*current_label)*2.0 +1.e-10)/ (np.sum(pred_label) + np.sum(current_label)+1.e-10)
    #dice_coeff_total.append(dice_coeff1)
    print(current_batch_id,dice_coeff1)


    name=current_batch_id.split('/')[-1]
    name=name.replace(".nii", "pred.nii")



    nib.save(nib.Nifti1Image(np.asarray(pred_label, dtype=np.float32), nib.load(current_batch_id).get_affine()),save_folder_loc1+'/'+   name )

###########################################################################


from keras.utils.layer_utils import count_params  

# count_params(model.trainable_weights)
trainable_count = count_params(model.trainable_weights)
non_trainable_count = count_params(model.non_trainable_weights)

print_fn("Total params: {:,}".format(trainable_count + non_trainable_count))
print_fn("Trainable params: {:,}".format(trainable_count))
print_fn("Non-trainable params: {:,}".format(non_trainable_count))

###########################################################################

# 2d slices from a 3D NIfti volume
# nii_rotate = np.rot90(np.array(img_data))
nii_slice = img_data[:, :, 20]
mask_slice = mask_data[:, :, 20]


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize= (20, 10))
ax1.imshow(nii_slice, cmap= 'bone')
ax1.set_title('Image')

ax2.imshow(mask_slice, cmap= 'bone')
ax2.set_title('Mask')

ax3.imshow(nii_slice, cmap='gray')
ax3.imshow(mask_slice, cmap='bwr', alpha=0.5*(mask_slice>0))
ax3.set_title('Mask Overlay')

plt.savefig("data_overview.png")

###########################################################################
img_data = nib.load(img_files[4]).get_fdata()
mask_data = nib.load(mask_files[4]).get_fdata()

# 2d slices from a 3D NIfti volume
# nii_rotate = np.rot90(np.array(img_data))
nii_slice = img_data[:, :, 20]
mask_slice = mask_data[:, :, 20]


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize= (20, 10))
ax1.imshow(nii_slice, cmap= 'bone')
ax1.set_title('Image')

ax2.imshow(mask_slice, cmap= 'bone')
ax2.set_title('Mask')

ax3.imshow(nii_slice, cmap='gray')
ax3.imshow(mask_slice, cmap='bwr', alpha=0.5*(mask_slice>0))
ax3.set_title('Mask Overlay')

plt.savefig("data_overview.png")

###########################################################################

new_dir_path= os.path.split(os.path.split(newpath)[0])[0]

###########################################################################

next(iter(test_generator))

###########################################################################
import os
import glob
import numpy as np
import nibabel as nib
import cv2
from imageio import imread

def nii2png(in_dir, out_dir, is_mask=False):
    file_paths= glob.glob(in_dir + "/*.nii")
    
    for file_path in file_paths:
        nii_img = nib.load(file_path).get_fdata()
        num = 0
        for i in range(nii_img.shape[2]):
            nii_arr = nii_img[:, :, i].astype(np.uint8)
            
            
            if is_mask:
                nii_arr = np.where(nii_arr == 1, 255, nii_arr)

            save_path= os.path.join(out_dir, os.path.basename(file_path)[:-4] + '_slice' + str(num) + '.png')
            cv2.imwrite(save_path, nii_arr)
            num += 1
            
in_dir= "data_nii/train/images/"
out_dir= "data_png/train/images/"

nii2png(in_dir, out_dir, is_mask=False)
###########################################################################
from imageio import imread
def sanity_check2d(in_dir):
    file_names= os.listdir(in_dir)
    for file_name in file_names:
        file_path= os.path.join(in_dir, file_name)
        img= imread(file_path)
        print("{}, min val: {}, max val: {}, shape: {}, dtype: {},  ndim: {}".format(file_name, np.min(img), np.max(img), img.shape, img.dtype, img.ndim))
        print(np.unique(img))
#         print(np.unique(img))

in_dir= "data_png/validation/masks/"
sanity_check2d(in_dir)
###########################################################################


def copy_files(file_names, in_dir, out_dir):
    for file_name in file_names:
        in_path= os.path.join(in_dir, file_name)
        out_path= os.path.join(out_dir, file_name)
        shutil.copy(in_path, out_path)
        
###########################################################################



def white_masks(in_dir):
    white_masks_names=[]
    file_names= os.listdir(in_dir)
    for file_name in file_names:
        file_path= os.path.join(in_dir, file_name)
        img_data= imageio.imread(file_path)
        if img_data.max() == 255:
            white_masks_names.append(file_name)
    return white_masks_names
                 
def copy_white_masks(in_dir_mask, out_dir_mask, in_dir_img, out_dir_img):
    white_masks_names= white_masks(in_dir_mask)
    print(np.shape(white_masks_names))
    for file_name in white_masks_names:
        in_path_mask= os.path.join(in_dir_mask, file_name)
        out_path_mask= os.path.join(out_dir_mask, file_name)
        
        in_path_img= os.path.join(in_dir_img, file_name)
        out_path_img= os.path.join(out_dir_img, file_name)
        
        shutil.copy(in_path_mask, out_path_mask)
        shutil.copy(in_path_img, out_path_img)
    return white_masks_names
        
###########################################################################

    def create_df(self, X):
        predictions = self.model.predict(X)
        df = pd.DataFrame(predictions, columns=["relative_x", "relative_y", "size"])
        df.to_csv('features.csv', sep=',')
        print("Created file...")
        
        return

###########################################################################

ef make_dir_img_mask(base_dir='data'):
    '''create train, validation, test,  images and masks'''
    train_dir = os.path.join(base_dir, 'train/')
    val_dir = os.path.join(base_dir, 'validation/')
    test_dir = os.path.join(base_dir, 'test/')

    img_train_dir = os.path.join(train_dir, 'images/')
    mask_train_dir = os.path.join(train_dir, 'masks/')
    img_val_dir = os.path.join(val_dir, 'images/')
    mask_val_dir = os.path.join(val_dir, 'masks/')
    img_test_dir = os.path.join(test_dir, 'images/')
    mask_test_dir = os.path.join(test_dir, 'masks/')

    if not os.path.exists(train_dir):
        os.mkdir(train_dir)

    if not os.path.exists(val_dir):
        os.mkdir(val_dir)

    if not os.path.exists(test_dir):
        os.mkdir(test_dir)
        
    if not os.path.exists(img_train_dir):
        os.mkdir(img_train_dir)

    if not os.path.exists(mask_train_dir):
        os.mkdir(mask_train_dir)

    if not os.path.exists(img_val_dir):
        os.mkdir(img_val_dir)

    if not os.path.exists(mask_val_dir):
        os.mkdir(mask_val_dir)

    if not os.path.exists(img_test_dir):
        os.mkdir(img_test_dir)

    if not os.path.exists(mask_test_dir):
        os.mkdir(mask_test_dir)
        
###########################################################################
# dcm2png
import os
import glob
import pandas as pd
import numpy as np
import pydicom
import tqdm
import cv2
import SimpleITK as sitk
from PIL import Image

def get_names(path):
    names = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext in ['.dcm']:
                path= os.path.join(root, filename)
                names.append(path)
    return names

def convert_dcm_png(path):
    filename= os.path.basename(path)[:-4]
    print(filename)
    root=os.path.dirname(path)
    print(root)
    
    im = pydicom.dcmread(path)
    im = im.pixel_array.astype(float)
    rescaled_image = (np.maximum(im,0)/im.max())*255 # float pixels
    final_image = np.uint8(rescaled_image) # integers pixels
    final_image = Image.fromarray(final_image)
    
    final_image.save(os.path.join(root, filename+'.png'))

    return final_image

names = get_names('dicom')
for name in names:
    image = convert_dcm_png(name)
###########################################################################

def get_names(path):
    names = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext in ['.dcm']:
                path= os.path.join(root, filename)
                names.append(path)
    return names
        
###########################################################################
data_dicts = [{"image": image_name, "mask": mask_name}
              for image_name, mask_name in zip(train_images, train_masks)]


###########################################################################

def seed_it_all(seed=7):
    """ Attempt to be Reproducible """
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)
seed_it_all()        
###########################################################################

def plot_img_mask(img1, img2):
    fig = plt.figure(figsize=(8, 6),dpi= 100)
    plt.subplot(231)
    plt.title("original maks", fontsize=8)
    plt.imshow(img1[:,:, img1.shape[2]//2],cmap='gray')

    plt.subplot(232)
    plt.title("resized mask", fontsize=8)
    plt.imshow(img2[:,:,img2.shape[2]//2],cmap='gray')

    plt.subplot(233)
    plt.title("Mask Overlay", fontsize=8)
    plt.imshow(img1[:, :, img1.shape[2]//2], cmap='gray')
    plt.imshow(img2[:, :, img2.shape[2]//2], alpha=0.5, cmap= 'gray')
    plt.show()
    
    
for mask_filename in train_masks:
    mask= nib.load(mask_filename).get_fdata()
    print(mask.shape)
    resized_mask= resize_volume(mask, desired_width, desired_height, desired_depth, order)
    print(mask_filename)
    print(resized_mask.shape)
    print(np.unique(resized_mask)) # sure the values are [0, 1] for binary segmentation
    plot_img_mask(mask, resized_mask)
    print("======" * 10)
    
###########################################################################

def get_model_memory_usage(batch_size, model):
    import numpy as np
    try:
        from keras import backend as K
    except:
        from tensorflow.keras import backend as K

    shapes_mem_count = 0
    internal_model_mem_count = 0
    for l in model.layers:
        layer_type = l.__class__.__name__
        if layer_type == 'Model':
            internal_model_mem_count += get_model_memory_usage(batch_size, l)
        single_layer_mem = 1
        out_shape = l.output_shape
        if type(out_shape) is list:
            out_shape = out_shape[0]
        for s in out_shape:
            if s is None:
                continue
            single_layer_mem *= s
        shapes_mem_count += single_layer_mem

    trainable_count = np.sum([K.count_params(p) for p in model.trainable_weights])
    non_trainable_count = np.sum([K.count_params(p) for p in model.non_trainable_weights])

    number_size = 4.0
    if K.floatx() == 'float16':
        number_size = 2.0
    if K.floatx() == 'float64':
        number_size = 8.0

    total_memory = number_size * (batch_size * shapes_mem_count + trainable_count + non_trainable_count)
    gbytes = np.round(total_memory / (1024.0 ** 3), 3) + internal_model_mem_count
    return gbytes

        
###########################################################################
from skimage.morphology import remove_small_objects
from skimage.measure import label, regionprops
def remove_conn_components(pred_mask, num_cc=1):

    labels = label(pred_mask)

    if num_cc == 1:

        maxArea = 0
        for region in regionprops(labels):
            if region.area > maxArea:
                maxArea = region.area
                print(maxArea)

        mask = remove_small_objects(labels, maxArea - 1)

    else:
        mask = remove_small_objects(labels, 3000, connectivity=2)

    return mask.astype(np.float64)


    kernel = np.ones((5,5),np.uint8)
    closing = cv2.morphologyEx(pred, cv2.MORPH_CLOSE, kernel)
    cleaned= remove_conn_components(closing)


###########################################################################
import numpy as np
import os
import nibabel as nib
import imageio
import skimage.exposure
from tqdm.notebook import tqdm


def ct_window(ct_volume, level, window):
    lower= level - (window/2)
    upper= level + (window/2)
    clipped = np.clip(ct_volume, lower, upper).astype('float32')
    return skimage.exposure.rescale_intensity(clipped, in_range=(lower, upper), out_range=(0., 255.))

def encode_mask(input_mask):
    mask = np.asarray(input_mask)
    mask = mask.astype(int)
    mask[mask == 0] = 0   # background
    mask[mask == 127] = 1
    mask[mask == 255] = 2
    mask = mask.astype(np.uint8)
    return mask

def nii_to_image(indir, outdir, is_mask= None):
    file_names = os.listdir(indir)
    for idx, file_name in enumerate(tqdm(file_names[:144])):
        img_path = os.path.join(indir, file_name)
        img = nib.load(img_path)
        img_data = img.get_fdata()
        
        if is_mask:
            fname= os.path.basename(img_path)
            fname = fname.replace('.nii.gz', '')
            img_f_path = os.path.join(outdir, fname)
            (x, y, z) = img.shape
            for i in range(z):
                nii_slice = (img_data[:, :, i])
                nii_slice[np.where(nii_slice == 0)] = 0
                nii_slice[np.where(nii_slice == 255)] = 1
                nii_slice[np.where(nii_slice == 127)] = 2
                imageio.imwrite(img_f_path+'-{}.png'.format(i), nii_slice)

        if not is_mask:
            img_data= ct_window(img_data, level=level, window=window)
            fname= os.path.basename(img_path)
            fname = fname.replace('.nii.gz', '')
            print("processing: {} {} ".format(idx, fname))
            img_f_path = os.path.join(outdir, fname)

            (x, y, z) = img.shape
            for i in range(z):
                nii_slice = (img_data[:, :, i]).astype(np.uint8)
                nii_slice = encode_mask(nii_slice)

                imageio.imwrite(img_f_path+'-{}.png'.format(i), nii_slice)


        
###########################################################################

useless_masks= []
for val_mask in val_masks:
    mask_data= cv2.imread(val_mask, -1)
    mask_name= os.path.basename(val_mask)
    val, counts = np.unique(mask_data, return_counts=True)
#     for pix_val, pix_counts in zip(val, counts):
#         print(pix_val, pix_counts, end=' -- ', flush=True)
    
    if len(counts) == 3:
        condition= ((counts[1] + counts[2])/counts.sum())*100
        if condition < 0.1: 
            useless_masks.append(val_mask)
            plt.figure(figsize=(8, 6))
            plt.subplot(231) # control the plot size
            plt.imshow(mask_data, cmap= 'gray')
            plt.title("{} -- {:.4f}%".format(mask_name, condition), fontsize=9)
            plt.show()
        
    if len(counts) == 2: 
        condition= (counts[1]/counts.sum())*100
        if condition < 0.1: 
            useless_masks.append(val_mask)
            plt.figure(figsize=(8, 6))
            plt.subplot(231) # control the plot size
            plt.imshow(mask_data, cmap= 'gray')
            plt.title("{} -- {:.4f}%".format(mask_name, condition), fontsize=9)
            plt.show()
            
for filename in useless_masks:
    print("removing {}".format(filename))
    os.remove(filename)  

## don't forget to remove corresponding images    
val_img_dir= "Liver_png_encoded/val/images/"
for filepath in useless_masks:
    fname= os.path.basename(filepath)
    img_path= os.path.join(val_img_dir, fname)
    print("removing {}".format(img_path))
    os.remove(img_path)
    
print(len(glob.glob("Liver_png_encoded/val/images/*.png")))
print(len(glob.glob("Liver_png_encoded/val/masks/*.png")))    
###########################################################################
###  move files based on dataframe
for _, row in df.iterrows():
    dest = os.path.join("lirad_classification/", row["Category"], row["filepath"])
    src= os.path.join("final_rsna_data", row["filepath"])
    shutil.copy(src, dest)
    

        
###########################################################################
# mask_onehot_encoding

 # Use RGB dictionary in 'RGBtoTarget.txt' to convert RGB to target
new_mask_arr[np.where(np.all(mask_arr == [216, 124, 18], axis=-1))] = 0
new_mask_arr[np.where(np.all(mask_arr == [255, 255, 255], axis=-1))] = 1
new_mask_arr[np.where(np.all(mask_arr == [216, 67, 82], axis=-1))] = 2

*******************************
def encode_mask(input_mask):
    mask = np.asarray(input_mask)
    mask = mask.astype(int)
    mask[mask == 0] = 0   # background
    mask[mask == 127] = 1
    mask[mask == 255] = 2
    mask = mask.astype(np.uint8)
    return mask


###########################################################################

fig = plt.figure(figsize=(15, 40), tight_layout=True)
for idx, width in enumerate(width_lst):
    img_obj= nib.load(img_paths[0])
    img_data= img_obj.get_fdata()
    pos = idx + 1
    plt.subplot(13, 5, pos)
    img_data= ct_window(img_data, level=level, width=width)
    img_slice_data = img_data[:, :, slice_idx]
    plt.imshow(img_slice_data.T, cmap='gray')
    plt.title("idx: {}, width: {}, level: {}".format(idx, width, level), fontsize=9)
    plt.xticks([]) 
    plt.yticks([]) 

###########################################################################
def ct_window(ct_volume, level, width):
    lower= level - (width/2)
    upper= level + (width/2)
    clipped = np.clip(ct_volume, lower, upper).astype('float32')
    return skimage.exposure.rescale_intensity(clipped, in_range=(lower, upper), out_range=(0., 1.))

def brute_force_windowing(slice_idx, plt_nrows, plt_ncols):
    fig = plt.figure(figsize=(15, 40), tight_layout=True)
    for idx, width in enumerate(width_lst):
        img_obj= nib.load(img_paths[0])
        img_data= img_obj.get_fdata()
        pos = idx + 1
        plt.subplot(plt_nrows, plt_ncols, pos)
        img_data= ct_window(img_data, level=level, width=width)
        img_slice_data = img_data[:, :, slice_idx]
        plt.imshow(img_slice_data.T, cmap='gray')
        plt.title("idx: {}, width: {}, level: {}".format(idx, width, level), fontsize=9)
        plt.xticks([])
        plt.yticks([])

###########################################################################
saveFile = f'{fname.strip(".dcm")}-{"decompressed"}.dcm'
print(saveFile)
###########################################################################


#### helper functions ####
import os
import glob
import pydicom
import SimpleITK as sitk
import numpy as np
from skimage import exposure
from scipy import stats
import cv2
from PIL import Image
import io

import matplotlib.pyplot as plt
%matplotlib inline

def make_lut(dcm_data, width, center, p_i):
    """
    LUT: look-up tables
    VOI: volume of interest
    """
    slope= 1.0
    intercept= 0.0
    min_px= int(np.amin(dcm_data))
    max_px= int(np.amax(dcm_data))

    lut= [0] * (max_px + 1)
    invert= False
    if p_i == "MONOCHROME1":
        invert= True
    else:
        center = (max_px - min_px) - center
    
    for px_value in range(min_px, max_px):
        lut_value = px_value * slope + intercept
        voi_value= (((lut_value - center) / width + 0.5) * 255.0)
        
        clamped_value= min(max(voi_value, 0), 255)
        
        if invert: 
            lut[px_value] = round(255 - clamped_value)
        else:
            lut[px_value] = round(clamped_value)
    
    return lut

def apply_lut(pixels_in, lut):
    pixels= pixels_in.flatten()
    pixels_out= [0] * len(pixels)
    
    for i in range (0, len(pixels)):
        pixel= pixels[i]
        if pixel > 0:
            pixels_out[i] = int(lut[pixel])
    return np.reshape(pixels_out, (pixels_in.shape[0], pixels_in.shape[1]))

def mr_windowing(in_dir, out_dir, mode= None, ww= None, wc= None):
    """
    # MODES: auot_lut, default_lut, auto_voilut, manual_lut, clahe, normalization
    """
    for root, _, fnames in os.walk(in_dir):
        for fname in fnames:
            print(f"processing: {fname}")
            dcm_path= os.path.join(root, fname)
            
            dcm_obj= pydicom.dcmread(dcm_path)
            dcm_pixels = dcm_obj.pixel_array
            
            if mode == "manual_lut":
                lut_ww= ww
                lut_wc= wc
                
                lut= make_lut(dcm_pixels, lut_ww, lut_wc, dcm_obj.PhotometricInterpretation)
                windowed_dcm= apply_lut(dcm_pixels, lut)
                
            if mode == "default_lut":
                if dcm_obj.WindowWidth != "" and dcm_obj.WindowCenter != "":
                    lut_ww = dcm_obj.WindowWidth
                    lut_wc = dcm_obj.WindowCenter
                    
                    lut= make_lut(dcm_pixels, lut_ww, lut_wc, dcm_obj.PhotometricInterpretation)
                    windowed_dcm= apply_lut(dcm_pixels, lut)
                    
            if mode == "auto_lut":
                lut_ww= np.max(dcm_pixels)
                lut_wc= lut_ww / 2
                
                lut= make_lut(dcm_pixels, lut_ww, lut_wc, dcm_obj.PhotometricInterpretation)
                windowed_dcm= apply_lut(dcm_pixels, lut)
                
            if mode == "auto_voilut":
                lut_ww = np.max(dcm_pixels)
                lut_wc= ((np.max(dcm_pixels)) - (np.min(dcm_pixels))) / (2 + np.min(dcm_pixels))
                
                lut= make_lut(dcm_pixels, lut_ww, lut_wc, dcm_obj.PhotometricInterpretation)
                windowed_dcm= apply_lut(dcm_pixels, lut)
                
            if mode == "clahe":
                dcm_clahe= exposure.equalize_adapthist(dcm_pixels)
                windowed_dcm= (dcm_clahe*255).astype(np.uint8)
                
            if mode == "normalization":
                windowed_dcm= (((raw_pixels - np.min(raw_pixels)) / np.max(raw_pixels))* 255).astype(np.uint8)
                
            windowed_dcm= np.uint8(windowed_dcm) 
            print(f"min: {np.min(windowed_dcm)}, max: {np.max(windowed_dcm)}")
#             plt.imshow(windowed_dcm, cmap= 'gray')
            print("====="*15)
            path_dirs = os.path.dirname(dcm_path)
            out_path = path_dirs.replace(in_dir, out_dir)
            if not os.path.isdir(out_path):
                os.makedirs(out_path)
                
            final_dcm= sitk.GetImageFromArray(windowed_dcm)
            save_path= os.path.join(out_path, fname)
            sitk.WriteImage(final_dcm, save_path)
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


