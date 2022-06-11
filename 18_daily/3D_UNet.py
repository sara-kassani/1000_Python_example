   # slices need correction --> should be divisable by 32
  def get_unet(slices, img_rows, img_cols):

        inputs = Input((slices, img_rows, img_cols,1))
        print ("inputs shape:",inputs.shape)
        conv1 = Conv3D(64, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(inputs)
        print ("conv1 shape:",conv1.shape)
        conv1 = Conv3D(64, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv1)
        print ("conv1 shape:",conv1.shape)
        pool1 = MaxPooling3D(pool_size=(2, 2, 2))(conv1)
        print ("pool1 shape:",pool1.shape)

        conv2 = Conv3D(128, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(pool1)
        print ("conv2 shape:",conv2.shape)
        conv2 = Conv3D(128, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv2)
        print ("conv2 shape:",conv2.shape)
        pool2 = MaxPooling3D(pool_size=(2, 2, 2))(conv2)
        print ("pool2 shape:",pool2.shape)

        conv3 = Conv3D(256, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(pool2)
        print ("conv3 shape:",conv3.shape)
        conv3 = Conv3D(256, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv3)
        print ("conv3 shape:",conv3.shape)
        pool3 = MaxPooling3D(pool_size=(2, 2, 2))(conv3)
        print ("pool3 shape:",pool3.shape)

        conv4 = Conv3D(512, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(pool3)
        print ("conv4 shape:",conv4.shape)
        conv4 = Conv3D(512, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv4)
        print ("conv4 shape:",conv4.shape)
        drop4 = Dropout(0.1)(conv4)
        print ("drop4 shape:",drop4.shape)
        pool4 = MaxPooling3D(pool_size=(2, 2, 2))(drop4)
        print ("pool4 shape:",pool4.shape)

        conv5 = Conv3D(1024, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(pool4)
        print ("conv5 shape:",conv5.shape)
        conv5 = Conv3D(1024, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv5)
        print ("conv5 shape:",conv5.shape)
        drop5 = Dropout(0.1)(conv5)
        print ("drop5 shape:",drop5.shape)

        up6 = Conv3D(512, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(UpSampling3D(size = (2,2,2))(drop5))
#        merge6 = merge([drop4,up6], mode = 'concat', concat_axis = 4)
        print ("up6 shape:",up6.shape)
        merge6 = concatenate([drop4,up6], axis = 4)
        print ("merge6 shape:",merge6.shape)
        conv6 = Conv3D(512, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(merge6)
        print ("conv6 shape:",conv6.shape)
        conv6 = Conv3D(512, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv6)
        print ("conv6 shape:",conv6.shape)

        up7 = Conv3D(256, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(UpSampling3D(size = (2,2,2))(conv6))
#        merge7 = merge([conv3,up7], mode = 'concat', concat_axis = 4)
        print ("up7 shape:",up7.shape)
        merge7 = concatenate([conv3,up7], axis = 4)
        print ("merge7 shape:",merge7.shape)
        conv7 = Conv3D(256, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(merge7)
        print ("conv7 shape:",conv7.shape)
        conv7 = Conv3D(256, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv7)
        print ("conv7 shape:",conv7.shape)

        up8 = Conv3D(128, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(UpSampling3D(size = (2,2,2))(conv7))
#        merge8 = merge([conv2,up8], mode = 'concat', concat_axis = 4)
        print ("up8 shape:",up8.shape)
        merge8 = concatenate([conv2,up8], axis = 4)
        print ("merge8 shape:",merge8.shape)
        conv8 = Conv3D(128, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(merge8)
        print ("conv8 shape:",conv8.shape)
        conv8 = Conv3D(128, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv8)
        print ("conv8 shape:",conv8.shape)

        up9 = Conv3D(64, 2, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(UpSampling3D(size = (2,2,2))(conv8))
#        merge9 = merge([conv1,up9], mode = 'concat', concat_axis = 4)
        print ("up9 shape:",up9.shape)
        merge9 = concatenate([conv1,up9], axis = 4)
        print ("merge9 shape:",merge9.shape)
        conv9 = Conv3D(64, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(merge9)
        print ("conv9 shape:",conv9.shape)
        conv9 = Conv3D(64, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv9)
        print ("conv9 shape:",conv9.shape)
        conv9 = Conv3D(2, 3, activation = 'relu', padding = 'same', kernel_initializer = 'he_normal')(conv9)
        print ("conv9 shape:",conv9.shape)
        conv10 = Conv3D(1, 1, activation = 'sigmoid')(conv9)
        print ("conv10 shape:",conv10.shape)
        model = Model(input = inputs, output = conv10)

        model.compile(optimizer = Adam(lr = 1e-5), loss = dice_coef_loss, metrics = [dice_coef])

        return model
####################################################################################################################
####################################################################################################################
####################################################################################################################
from tensorflow.keras.models import Model
import matplotlib.pyplot as plt
import cv2
import numpy as np
from tensorflow.keras.layers import Conv3D, MaxPooling3D, Dropout, concatenate, UpSampling3D
import tensorflow as tf
from scipy.spatial.distance import directed_hausdorff
from import_data import import_data, load_hdf5

def u_net_3d(inputs):
    x = inputs
    conv1 = Conv3D(8, 3, activation='relu', padding='same', data_format="channels_last")(x)
    conv1 = Conv3D(8, 3, activation='relu', padding='same')(conv1)
    pool1 = MaxPooling3D(pool_size=(2, 2, 2))(conv1)
    conv2 = Conv3D(16, 3, activation='relu', padding='same')(pool1)
    conv2 = Conv3D(16, 3, activation='relu', padding='same')(conv2)
    pool2 = MaxPooling3D(pool_size=(2, 2, 2))(conv2)
    conv3 = Conv3D(32, 3, activation='relu', padding='same')(pool2)
    conv3 = Conv3D(32, 3, activation='relu', padding='same')(conv3)
    pool3 = MaxPooling3D(pool_size=(2, 2, 2))(conv3)
    conv4 = Conv3D(64, 3, activation='relu', padding='same')(pool3)
    conv4 = Conv3D(64, 3, activation='relu', padding='same')(conv4)
    drop4 = Dropout(0.5)(conv4)
    pool4 = MaxPooling3D(pool_size=(2, 2, 2))(drop4)

    conv5 = Conv3D(128, 3, activation='relu', padding='same')(pool4)
    conv5 = Conv3D(128, 3, activation='relu', padding='same')(conv5)
    drop5 = Dropout(0.5)(conv5)

    up6 = Conv3D(64, 2, activation='relu', padding='same')(UpSampling3D(size=(2, 2, 2))(drop5))
    merge6 = concatenate([drop4, up6], axis=-1)
    conv6 = Conv3D(64, 3, activation='relu', padding='same')(merge6)
    conv6 = Conv3D(64, 3, activation='relu', padding='same')(conv6)

    up7 = Conv3D(32, 2, activation='relu', padding='same')(UpSampling3D(size=(2, 2, 2))(conv6))
    merge7 = concatenate([conv3, up7], axis=-1)
    conv7 = Conv3D(32, 3, activation='relu', padding='same')(merge7)
    conv7 = Conv3D(32, 3, activation='relu', padding='same')(conv7)

    up8 = Conv3D(16, 2, activation='relu', padding='same')(UpSampling3D(size=(2, 2, 2))(conv7))
    merge8 = concatenate([conv2, up8], axis=-1)
    conv8 = Conv3D(16, 3, activation='relu', padding='same')(merge8)
    conv8 = Conv3D(16, 3, activation='relu', padding='same')(conv8)

    up9 = Conv3D(8, 2, activation='relu', padding='same')(UpSampling3D(size=(2, 2, 2))(conv8))
    merge9 = concatenate([conv1, up9], axis=-1)
    conv9 = Conv3D(8, 3, activation='relu', padding='same')(merge9)
    conv9 = Conv3D(8, 3, activation='relu', padding='same')(conv9)
    conv10 = Conv3D(1, 1, activation='sigmoid')(conv9)
    model = Model(inputs=inputs, outputs=conv10)
    return model
####################################################################################################################
####################################################################################################################
####################################################################################################################
import tensorflow as tf
from tensorflow.keras.models import Model


def conv_layer_3D(x, num_filters, kernel_size, padding='same'):
    x = tf.keras.layers.Conv3D(num_filters,
                               kernel_size=kernel_size,
                               padding=padding)(x)
    x = tf.keras.layers.BatchNormalization()(x)

    x = tf.keras.layers.ReLU()(x)

    return x


def unet_3D():
    inputs = tf.keras.Input(shape=(128, 224, 224, 1))
    x = inputs
    conv1 = conv_layer_3D(x, num_filters=4, kernel_size=3)
    conv1 = conv_layer_3D(conv1, num_filters=4, kernel_size=3)
    pool1 = tf.keras.layers.MaxPool3D()(conv1)

    conv2 = conv_layer_3D(pool1, num_filters=8, kernel_size=3)
    conv2 = conv_layer_3D(conv2, num_filters=8, kernel_size=3)
    pool2 = tf.keras.layers.MaxPool3D()(conv2)

    conv3 = conv_layer_3D(pool2, num_filters=16, kernel_size=3)
    conv3 = conv_layer_3D(conv3, num_filters=16, kernel_size=3)
    pool3 = tf.keras.layers.MaxPool3D()(conv3)

    conv4 = conv_layer_3D(pool3, num_filters=32, kernel_size=3)
    conv4 = conv_layer_3D(conv4, num_filters=32, kernel_size=3)

    concat1 = tf.keras.layers.concatenate(
        [tf.keras.layers.Conv3DTranspose(16, 2, strides=2, padding="same")(conv4), conv3])

    conv5 = conv_layer_3D(concat1, num_filters=16, kernel_size=3)
    conv5 = conv_layer_3D(conv5, num_filters=16, kernel_size=3)

    concat2 = tf.keras.layers.concatenate(
        [tf.keras.layers.Conv3DTranspose(8, 2, strides=2, padding="same")(conv5), conv2])

    conv6 = conv_layer_3D(concat2, num_filters=8, kernel_size=3)
    conv6 = conv_layer_3D(conv6, num_filters=8, kernel_size=3)

    concat3 = tf.keras.layers.concatenate(
        [tf.keras.layers.Conv3DTranspose(4, 2, strides=2, padding="same")(conv6), conv1])

    conv7 = conv_layer_3D(concat3, num_filters=4, kernel_size=3)
    conv7 = conv_layer_3D(conv7, num_filters=4, kernel_size=3)

    output = tf.keras.layers.Conv3D(filters=1, kernel_size=(1, 1, 1), activation="sigmoid")(conv7)

    unet_model_3D = tf.keras.Model(inputs, output, name='U-Net_model_3D')

    return unet_model_3D

####################################################################################################################
####################################################################################################################
####################################################################################################################



####################################################################################################################
####################################################################################################################
####################################################################################################################



####################################################################################################################
####################################################################################################################
####################################################################################################################



####################################################################################################################
####################################################################################################################
####################################################################################################################




