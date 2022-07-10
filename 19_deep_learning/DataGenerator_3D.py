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
