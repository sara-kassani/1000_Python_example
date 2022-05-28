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
