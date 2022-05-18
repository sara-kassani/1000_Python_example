from genericpath import exists
from ntpath import join
import os
import glob
import numpy as np
import pandas as pd
import nibabel as nib
import SimpleITK as sitk
import matplotlib.pyplot as plt
from nilearn import plotting
import requests
import shutil
import random
import sys
import copy
from dipy.align.reslice import reslice

pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 500)
np.set_printoptions(threshold=sys.maxsize)

# first install all of the requirements
# requirements = requests.get('https://raw.githubusercontent.com/ljchang/dartbrains/master/requirements.txt').text
# requirements = [x for x in requirements.split('\n')][3:-1]

# for r in requirements:
#     !pip install {r}


def read_nii(file_path):
    '''
    Reads .nii file and returns pixel array 
    '''
    # if os.path.isfile(file_path):
    if file_path.endswith('nii'):
        # read file and get raw data
        nii_data = nib.load(str(file_path)).get_fdata()    #  return floating point of image data
    return nii_data

def read_nii_header(file_path):
    
    img_obj = nib.load(str(file_path))    #  read file
    img_data = img_obj.get_fdata()    #  # get raw data
    img_hdr = img_obj.header

    res_dict = {}
    res_dict['voxel_spacing']=[img_hdr['srow_x'][0], img_hdr['srow_y'][1], img_hdr['srow_z'][2]]
    return img_data, res_dict

def read_nii_header_affine(file_path):
    img_obj = nib.load(str(file_path))
    img_data = img_obj.get_fdata()
    img_shape = img_obj.shape
    img_hdr = img_obj.header
    img_affine = img_obj.affine
    return img_obj, img_data, img_shape, img_hdr, img_affine

def show_histogram(image):
    plt.figure()
    plt.hist(image.flatten(), bins=50, color='c')
    # plt.xlim(0.1, 0.9)
    plt.ylim(0, 5000)
    plt.xlabel('Hounsfield Units (HU)')
    plt.ylabel('Frequency')
    plt.show()

def plot_slices(num_rows, num_columns, width, height, data):
    '''Plot a montage of CT slices'''
    data= np.rot90(np.array(data))
    data= np.transpose(data)
    data = np.reshape(data, (num_rows, num_columns, width, height))
    rows_data, columns_data = data.shape[0], data.shape[1]
    heights = [slc[0].shape[0] for slc in data]
    widths = [slc.shape[1] for slc in data[0]]
    fig_width = 12.0
    fig_height = fig_width + sum(heights) / sum(widths)
    f, axarr = plt.subplots(rows_data, columns_data, figsize=(fig_width, fig_height), gridspec_kw={"height_ratios": heights},)

    for i in range(rows_data):
        for j in range(columns_data):
            axarr[i, j].imshow(data[i][j], cmap= 'gray')
            axarr[i, j].axis('off')
    plt.subplots_adjust(wspace=0, hspace=0, left=0, right=1, bottom=0, top=1)
    plt.show()


def normalize(volume):
    '''Normalize the volume'''
    # min = -1000
    # max = 400
    min= np.min(volume)
    max= np.max(volume)
    volume[volume < min] = min
    volume[volume > max] = max
    volume = (volume - min) / (max-min)
    volume = volume.astype('float32')
    return volume

''' I need to use the slices in a deep learning framework and 
for data augmentation, I need them to be resampled in a new spacing 
which is (1.0, 1.0, 1.0)'''
def resample_image(itk_image, out_spacing=(1.0, 1.0, 1.0)):
    """
    Resample itk_image to new out_spacing
    :param itk_image: the input image
    :param out_spacing: the desired spacing
    :return: the resampled image
    """
    # get original spacing and size
    original_spacing = itk_image.GetSpacing()
    original_size = itk_image.GetSize()
    # calculate new size
    out_size = [
        int(np.round(original_size[0] * (original_spacing[0] / out_spacing[0]))),
        int(np.round(original_size[1] * (original_spacing[1] / out_spacing[1]))),
        int(np.round(original_size[2] * (original_spacing[2] / out_spacing[2])))
    ]
    # instantiate resample filter with properties and execute it
    resample = sitk.ResampleImageFilter()
    resample.SetOutputSpacing(out_spacing)
    resample.SetSize(out_size)
    resample.SetOutputDirection(itk_image.GetDirection())
    resample.SetOutputOrigin(itk_image.GetOrigin())
    resample.SetTransform(sitk.Transform())
    resample.SetDefaultPixelValue(itk_image.GetPixelIDValue())
    resample.SetInterpolator(sitk.sitkNearestNeighbor)
    return resample.Execute(itk_image)

# https://stackoverflow.com/questions/70645577/translate-image-orientation-into-axial-sagittal-or-coronal-plane
def get_orientation(dcm):
    """Get orientation of dicom object.

    Returns one of
        Transverse
        Coronal
        Sagittal
        NA  (if ImageOrientationPatient not available)
    """

    iop = getattr(dcm, 'ImageOrientationPatient', None)

    if iop is None:
        return 'NA'

    iop_rounded = [round(x) for x in iop]
    plane_cross = np.cross(iop_rounded[0:3], iop_rounded[3:6])
    plane = [abs(x) for x in plane_cross]

    if plane[0] == 1:
        return 'Sagittal'
    elif plane[1] == 1:
        return 'Coronal'
    elif plane[2] == 1:
        return 'Transverse'
    else:
        return 'NA'

def make_zip(in_dir, out_file_name):
    shutil.make_archive(out_file_name, 'zip', in_dir)


def make_dir_img_mask(base_dir='data'):
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

def fetch_delete_ds_store(base_dir):
    for item in os.listdir(base_dir):
        if item ==  '.DS_Store':
            print('.DS_Store found')
            os.remove(base_dir + "/" + item)
        if not (os.path.isdir(base_dir + "/" + item)):
            fetch_delete_ds_store(base_dir + "/" + item)
        # else:
        #     if not os.path.exists(base_dir + "/" + item):
        #         print('Found Nothing')

def move_files(source_dir, target_dir):
    file_names = os.listdir(source_dir)
    
    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)

        
def split_train_test(img_train_dir, mask_train_dir, img_dest_dir, mask_dest_dir, test_ratio = 0.2):
    """at first all data are in train directory (images and mask dirs)"""
    imgs = [os.path.join(img_train_dir, f) for f in os.listdir(img_train_dir)]
    masks = [os.path.join(mask_train_dir, f) for f in os.listdir(mask_train_dir)]
    imgs.sort()
    masks.sort()
    imgs_masks = list(zip(imgs, masks))
#     print(imgs_masks)
    random.Random(42).shuffle(imgs_masks)
    
    valid_cutoff = int(len(imgs_masks) * test_ratio)
    print(valid_cutoff)
    files_to_move = imgs_masks[:valid_cutoff]
    print(files_to_move)
#     print(len(files_to_move))
    for img, mask in files_to_move:
        shutil.move(img, img_dest_dir)
        shutil.move(mask, mask_dest_dir)




# def split_train_test(img_train_dir, mask_train_dir, img_dest_dir, mask_dest_dir, test_ratio = 0.2):
#     """at first all data are in train directory (images and mask dirs)"""
#     imgs = [os.path.join(img_train_dir, f) for f in os.listdir(img_train_dir)]
#     masks = [os.path.join(mask_train_dir, f) for f in os.listdir(mask_train_dir)]
#     imgs.sort()
#     masks.sort()
#     imgs_masks = list(zip(imgs, masks))
# #     print(imgs_masks)
#     random.Random(42).shuffle(imgs_masks)
    
#     valid_cutoff = int(len(imgs_masks) * test_ratio)
#     print(valid_cutoff)
#     files_to_move = imgs_masks[:valid_cutoff]
#     print(files_to_move)
# #     print(len(files_to_move))
#     for img, mask in files_to_move:
#         shutil.move(img, img_dest_dir)
#         shutil.move(mask, mask_dest_dir)

def sanity_check_volume_spacing_slices(dir_path):
    file_paths= glob.glob(dir_path + '*.nii')
    volume_data = []
    
    for fullname in file_paths:
        nii_obj = nib.load(fullname)
        (nx, ny, nz) = nii_obj.shape[0:3]
        nii_hdr= nii_obj.header
#         srow_x= nii_hdr['srow_x'][0]
#         srow_y= nii_hdr['srow_y'][1]
#         srow_z= nii_hdr['srow_z'][2]
        
        (sx, sy, sz) = nii_obj.header.get_zooms()    #  Slice thickness
        
        voxel_spacing = sx * sy* sz 
        
        filename = fullname.split(os.sep)[-1]
        data = [filename, nx, ny, nz, sx, sy, sz, voxel_spacing]
        volume_data.append(data)
        df_total = pd.DataFrame(volume_data, columns= ['volume', 'width', 'height', '#_slices', 'sx', 'sy', 'sz', 'voxel_spacing'])
    

    return volume_data, df_total

def max_num_slice(input_path):
    num_slices = []
        
    for volume_path in sorted(glob.glob(os.path.join(input_path,'*.nii'))):

        volume_obj= nib.load(volume_path)
        volume_data= volume_obj.get_fdata()
        x, y, z = volume_data.shape
        num_slices.append(z)
    
    return num_slices, max(num_slices)



def volume_depth_correction(input_path, output_path):
    _, max_slices = max_num_slice(input_path)

    for volume_path in sorted(glob.glob(os.path.join(input_path,'*.nii'))):
        volume_obj= nib.load(volume_path)
        volume_data= volume_obj.get_fdata()
        x, y, z = volume_data.shape

        num_slices, max_slice= max_num_slice(input_path)
    
        if z == max_slice:
            print(volume_path)
            volume_name= os.path.split(volume_path)[-1]
            print(volume_name)
            shutil.copy(volume_path, os.path.join(output_path, volume_name))

        if z < max_slice:
            sx, sy, sz = volume_obj.header.get_zooms()
            voxel_volume = sx * sy * sz
            
            print("processing original voume: ", volume_path, x, y, z, voxel_volume)
            print(max_slice)
            last_slice = volume_data[:, :, z-1]

            black_slice = copy.deepcopy(last_slice)
            black_slice[:,:] = 0

            delta_slices = (max_slices - z)
            print("delta", delta_slices)
            b = np.dstack([black_slice]*(delta_slices))
            volume_depth_corrected = np.dstack((volume_data, b))
            
            final_volume = nib.Nifti1Image(volume_depth_corrected, volume_obj.affine, header=volume_obj.header)
            volume_name = os.path.split(volume_path)[-1]
            nib.save(final_volume, os.path.join(output_path, volume_name))       

            volume_corrected_data = final_volume.get_fdata()
            x, y, z = volume_corrected_data.shape

            sx, sy, sz = final_volume.header.get_zooms()
            voxel_volume_corrected = sx * sy * sz

            print("corrected volume:", x, y, z, voxel_volume_corrected)
            print("********************")
    