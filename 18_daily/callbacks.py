checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath='best_weights.h5',
                                                monitor='val_loss',
                                                verbose=1,
                                                save_best_only=True,
                                                save_weights_only=False,
                                                mode='auto')
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss',
                                                  patience=10,
                                                  verbose=1,
                                                  mode='min')

reduce_plateau = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=2, min_lr=0.000001, verbose=1)
# #################################################################################################
 callbacks= [checkpoint, early_stopping]
# or
callbacks= [ModelCheckpoint(file_path, verbose=1, save_best_only=True, save_weights_only=False)]

model.fit(..., callbacks = callbacks)
