strategy = tf.distribute.MirroredStrategy(devices=["/gpu:0", "/gpu:1"], 
                                           cross_device_ops=tf.distribute.HierarchicalCopyAllReduce())
print('Number of devices: {}'.format(strategy.num_replicas_in_sync))

with strategy.scope():
  # model construction & `compile()`.
    model1 = sm.Unet('densenet121', input_shape=input_shape, encoder_weights=encoder_weights, activation= activation)
#     model1.summary()     # Trainable params: 26,555,121 with densenet121 (26M)
    model1.compile(optimizer = optimizer, loss = dice_loss, metrics = metrics)

# ##########################################################################################################################



# original documentation - from keras.io
# Create a MirroredStrategy.
strategy = tf.distribute.MirroredStrategy()
print('Number of devices: {}'.format(strategy.num_replicas_in_sync))

# Open a strategy scope.
with strategy.scope():
  # Everything that creates variables should be under the strategy scope.
  # In general this is only model construction & `compile()`.
  model = Model(...)
  model.compile(...)

# Train the model on all available devices.
model.fit(train_dataset, validation_data=val_dataset, ...)

# Test the model on all available devices.
model.evaluate(test_dataset)
