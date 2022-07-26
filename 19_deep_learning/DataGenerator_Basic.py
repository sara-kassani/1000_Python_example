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
