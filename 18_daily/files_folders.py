
for dirname, subdirlist, filelist in os.walk(path):
    print(dirname)
# /kaggle/input/cynch-corrected64/
# /kaggle/input/cynch-corrected64/images
# /kaggle/input/cynch-corrected64/human_corrected_without_vessel_removal
# /kaggle/input/cynch-corrected64/human_corrected_with_vessel_removal
# ***********************************************************************************
for dirname, subdirlist, filelist in os.walk(path):
    print(subdirlist)
# ['images', 'human_corrected_without_vessel_removal', 'human_corrected_with_vessel_removal']
# []
# []
# []
# ***********************************************************************************
for dirname, subdirlist, filelist in os.walk(path):
    print(filelist)
# []
# ['c_1509.nii', 'c_4381.nii', 'c_5593.nii', 'c_9125.nii', 'c_5553.nii', 'c_8733.nii', 'c_5545.nii', 'c_5413.nii', 'c_5435.nii', 'c_3307.nii', 'c_1370.nii', 'c_5524.nii', 'c_5541.nii', 'c_1512.nii', 'c_4323.nii', 'c_4372.nii', 'c_1464.nii', 'c_5437.nii', 'c_5518.nii', 'c_5536.nii', 'c_9143.nii', 'c_5426.nii', 'c_1453.nii', 'c_4218.nii', 'c_9142.nii', 'c_5304.nii', 'c_1326.nii', 'c_3361.nii', 'c_5427.nii', 'c_2356.nii', 'c_1309.nii', 'c_4382.nii', 'c_3358.nii', 'c_5522.nii', 'c_3312.nii', 'c_7353.nii', 'c_5542.nii', 'c_9132.nii', 'c_5538.nii', 'c_1481.nii', 'c_5589.nii', 'c_5586.nii', 'c_5258.nii', 'c_5548.nii', 'c_5127.nii', 'c_5430.nii', 'c_2354.nii', 'c_3310.nii', 'c_1493.nii', 'c_5434.nii', 'c_4379.nii', 'c_1501.nii', 'c_8740.nii', 'c_1445.nii', 'c_4325.nii', 'c_5431.nii', 'c_5511.nii', 'c_9121.nii', 'c_2355.nii', 'c_9124.nii', 'c_9110.nii', 'c_5535.nii', 'c_3311.nii', 'c_9137.nii', 'c_5519.nii', 'c_3316.nii', 'c_4408.nii', 'c_5423.nii', 'c_5540.nii', 'c_5546.nii', 'c_5555.nii', 'c_4322.nii', 'c_5421.nii', 'c_1514.nii', 'c_4409.nii', 'c_9135.nii', 'c_5585.nii', 'c_5424.nii', 'c_5543.nii', 'c_2288.nii', 'c_1513.nii', 'c_5348.nii', 'c_5587.nii', 'c_2351.nii', 'c_1459.nii', 'c_5517.nii', 'c_9131.nii', 'c_5438.nii', 'c_3313.nii', 'c_4385.nii', 'c_5554.nii', 'c_8728.nii', 'c_5513.nii', 'c_5512.nii', 'c_5440.nii', 'c_4398.nii', 'c_9119.nii', 'c_5533.nii', 'c_5525.nii', 'c_5429.nii', 'c_5544.nii', 'c_5425.nii', 'c_5378.nii', 'c_5528.nii', 'c_3357.nii', 'c_5311.nii', 'c_5428.nii', 'c_9122.nii', 'c_2281.nii', 'c_6080.nii', 'c_5514.nii']
# ['c_1509.nii', 'c_4381.nii', 'c_5593.nii', 'c_9125.nii', 'c_5553.nii', 'c_8733.nii', 'c_5545.nii', 'c_5413.nii', 'c_5435.nii', 'c_3307.nii', 'c_1370.nii', 'c_5524.nii', 'c_5541.nii', 'c_1512.nii', 'c_4323.nii', 'c_4372.nii', 'c_1464.nii', 'c_5437.nii', 'c_5518.nii', 'c_5536.nii', 'c_9143.nii', 'c_5426.nii', 'c_1453.nii', 'c_4218.nii', 'c_9142.nii', 'c_5304.nii', 'c_1326.nii', 'c_3361.nii', 'c_5427.nii', 'c_2356.nii', 'c_1309.nii', 'c_4382.nii', 'c_3358.nii', 'c_5522.nii', 'c_3312.nii', 'c_7353.nii', 'c_5542.nii', 'c_9132.nii', 'c_5538.nii', 'c_1481.nii', 'c_5589.nii', 'c_5586.nii', 'c_5258.nii', 'c_5548.nii', 'c_5127.nii', 'c_5430.nii', 'c_2354.nii', 'c_3310.nii', 'c_1493.nii', 'c_5434.nii', 'c_4379.nii', 'c_1501.nii', 'c_8740.nii', 'c_1445.nii', 'c_4325.nii', 'c_5431.nii', 'c_5511.nii', 'c_9121.nii', 'c_2355.nii', 'c_9124.nii', 'c_9110.nii', 'c_5535.nii', 'c_3311.nii', 'c_9137.nii', 'c_5519.nii', 'c_3316.nii', 'c_4408.nii', 'c_5423.nii', 'c_5540.nii', 'c_5546.nii', 'c_5555.nii', 'c_4322.nii', 'c_5421.nii', 'c_1514.nii', 'c_4409.nii', 'c_9135.nii', 'c_5585.nii', 'c_5424.nii', 'c_5543.nii', 'c_2288.nii', 'c_1513.nii', 'c_5348.nii', 'c_5587.nii', 'c_2351.nii', 'c_1459.nii', 'c_5517.nii', 'c_9131.nii', 'c_5438.nii', 'c_3313.nii', 'c_4385.nii', 'c_5554.nii', 'c_8728.nii', 'c_5513.nii', 'c_5512.nii', 'c_5440.nii', 'c_4398.nii', 'c_9119.nii', 'c_5533.nii', 'c_5525.nii', 'c_5429.nii', 'c_5544.nii', 'c_5425.nii', 'c_5378.nii', 'c_5528.nii', 'c_3357.nii', 'c_5311.nii', 'c_5428.nii', 'c_9122.nii', 'c_2281.nii', 'c_6080.nii', 'c_5514.nii']
# ['c_1509.nii', 'c_4381.nii', 'c_5593.nii', 'c_9125.nii', 'c_5553.nii', 'c_8733.nii', 'c_5545.nii', 'c_5413.nii', 'c_5435.nii', 'c_3307.nii', 'c_1370.nii', 'c_5524.nii', 'c_5541.nii', 'c_1512.nii', 'c_4323.nii', 'c_4372.nii', 'c_1464.nii', 'c_5437.nii', 'c_5518.nii', 'c_5536.nii', 'c_9143.nii', 'c_5426.nii', 'c_1453.nii', 'c_4218.nii', 'c_9142.nii', 'c_5304.nii', 'c_1326.nii', 'c_3361.nii', 'c_5427.nii', 'c_2356.nii', 'c_1309.nii', 'c_4382.nii', 'c_3358.nii', 'c_5522.nii', 'c_3312.nii', 'c_7353.nii', 'c_5542.nii', 'c_9132.nii', 'c_5538.nii', 'c_1481.nii', 'c_5589.nii', 'c_5586.nii', 'c_5258.nii', 'c_5548.nii', 'c_5127.nii', 'c_5430.nii', 'c_2354.nii', 'c_3310.nii', 'c_1493.nii', 'c_5434.nii', 'c_4379.nii', 'c_1501.nii', 'c_8740.nii', 'c_1445.nii', 'c_4325.nii', 'c_5431.nii', 'c_5511.nii', 'c_9121.nii', 'c_2355.nii', 'c_9124.nii', 'c_9110.nii', 'c_5535.nii', 'c_3311.nii', 'c_9137.nii', 'c_5519.nii', 'c_3316.nii', 'c_4408.nii', 'c_5423.nii', 'c_5540.nii', 'c_5546.nii', 'c_5555.nii', 'c_4322.nii', 'c_5421.nii', 'c_1514.nii', 'c_4409.nii', 'c_9135.nii', 'c_5585.nii', 'c_5424.nii', 'c_5543.nii', 'c_2288.nii', 'c_1513.nii', 'c_5348.nii', 'c_5587.nii', 'c_2351.nii', 'c_1459.nii', 'c_5517.nii', 'c_9131.nii', 'c_5438.nii', 'c_3313.nii', 'c_4385.nii', 'c_5554.nii', 'c_8728.nii', 'c_5513.nii', 'c_5512.nii', 'c_5440.nii', 'c_4398.nii', 'c_9119.nii', 'c_5533.nii', 'c_5525.nii', 'c_5429.nii', 'c_5544.nii', 'c_5425.nii', 'c_5378.nii', 'c_5528.nii', 'c_3357.nii', 'c_5311.nii', 'c_5428.nii', 'c_9122.nii', 'c_2281.nii', 'c_6080.nii', 'c_5514.nii']
# ***********************************************************************************
## split the extension from file path:
image_list = sorted(glob.glob(os.path.join(input_dir, 'images/') + '*.nii'))
for i, image_name in enumerate(image_list):
    print(image_name.split('.'))

# ['/kaggle/input/cynch-corrected64/images/c_1309', 'nii']
# ['/kaggle/input/cynch-corrected64/images/c_1326', 'nii']
# ['/kaggle/input/cynch-corrected64/images/c_1370', 'nii']

for i, image_name in enumerate(image_list):
    print(image_name.split('.')[1]) # or -1 ----> split by (.) --> 0(.)1
# nii
# nii
# nii

for i, image_name in enumerate(image_list):
    print(image_name.split('.')[0])
# /kaggle/input/cynch-corrected64/images/c_1309
# /kaggle/input/cynch-corrected64/images/c_1326
# /kaggle/input/cynch-corrected64/images/c_1370
# ***********************************************************************************
# extract only filename from glob.glob path
image_list = sorted(glob.glob(os.path.join(input_dir, 'images/') + '*.nii'))
for i, image_name in enumerate(image_list):
    print(os.path.basename(image_name))
# c_1309.nii
# c_1326.nii
# c_1370.nii
# c_1445.nii
# c_1453.nii
# c_1459.nii
# ***********************************************************************************

