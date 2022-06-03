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



###########################################################################



###########################################################################
