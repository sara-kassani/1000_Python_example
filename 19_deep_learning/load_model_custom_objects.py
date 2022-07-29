

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
