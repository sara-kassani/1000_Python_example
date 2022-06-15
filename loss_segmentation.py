# https://www.kaggle.com/code/bigironsphere/loss-function-library-keras-pytorch/notebook

"""
Loss functions define how neural network models calculate the overall error from their residuals for each training batch. This in turn affects how they adjust their internal weights when performing backpropagation, so the choice of loss function has a direct influence on model performance.

The default choice of loss function for segmentation and other classification tasks is Binary Cross-Entropy (BCE). In situations where a particular metric, like the Dice Coefficient or Intersection over Union (IoU), is being used to judge model performance, competitors will sometimes experiment with loss functions that derive from these metrics - typically in the form 1 - f(x) where f(x) is the metric in question.

These functions cannot simply be written in NumPy, as they must operate on tensors that also have gradient parameters which need to be calculated throughout the model during backpropagation. Accordingly, loss functions must be written using backend functions from the respective model library. This is less complicated than it sounds! For example in Keras, you would simply use the same familiar mathematical functions, albeit using the Keras backend imported as K, i.e K.sum(). Gradient calculation is handled automatically by the model libraries, although (at least in PyTorch) you can define this manually if you are confident in your mathematical ability and wish to make alterations of your own.
"""
"""

Dice Loss: The Dice coefficient, or Dice-Sørensen coefficient, is a common metric for pixel segmentation that can also be modified to act as a loss function
"""
import numpy as np
import keras
import keras.backend as K


def DiceLoss(targets, inputs, smooth=1e-6):
    
    #flatten label and prediction tensors
    inputs = K.flatten(inputs)
    targets = K.flatten(targets)
    
    intersection = K.sum(K.dot(targets, inputs))
    dice = (2*intersection + smooth) / (K.sum(targets) + K.sum(inputs) + smooth)
    return 1 - dice


"""
BCE-Dice Loss

This loss combines Dice loss with the standard binary cross-entropy (BCE) loss that is generally the default for segmentation models. Combining the two methods allows for some diversity in the loss, while benefitting from the stability of BCE. The equation for multi-class BCE by itself will be familiar to anyone who has studied logistic regression
"""

#Keras
def DiceBCELoss(targets, inputs, smooth=1e-6):    
       
    #flatten label and prediction tensors
    inputs = K.flatten(inputs)
    targets = K.flatten(targets)
    
    BCE =  binary_crossentropy(targets, inputs)
    intersection = K.sum(K.dot(targets, inputs))    
    dice_loss = 1 - (2*intersection + smooth) / (K.sum(targets) + K.sum(inputs) + smooth)
    Dice_BCE = BCE + dice_loss
    
    return Dice_BCE


"""
Jaccard/Intersection over Union (IoU) Loss
The IoU metric, or Jaccard Index, is similar to the Dice metric and is calculated as the ratio between the overlap of the positive instances between two sets, and their mutual combined values:
Like the Dice metric, it is a common means of evaluating the performance of pixel segmentation models.
"""

def IoULoss(targets, inputs, smooth=1e-6):
    
    #flatten label and prediction tensors
    inputs = K.flatten(inputs)
    targets = K.flatten(targets)
    
    intersection = K.sum(K.dot(targets, inputs))
    total = K.sum(targets) + K.sum(inputs)
    union = total - intersection
    
    IoU = (intersection + smooth) / (union + smooth)
    return 1 - IoU



"""
Focal Loss

Focal Loss was introduced by Lin et al of Facebook AI Research in 2017 as a means of combatting extremely imbalanced datasets where positive cases were relatively rare. Their paper "Focal Loss for Dense Object Detection" is retrievable here: https://arxiv.org/abs/1708.02002. 
"""

ALPHA = 0.8
GAMMA = 2

def FocalLoss(targets, inputs, alpha=ALPHA, gamma=GAMMA):    
    
    inputs = K.flatten(inputs)
    targets = K.flatten(targets)
    
    BCE = K.binary_crossentropy(targets, inputs)
    BCE_EXP = K.exp(-BCE)
    focal_loss = K.mean(alpha * K.pow((1-BCE_EXP), gamma) * BCE)
    
    return focal_loss


"""

Tversky Loss

This loss was introduced in "Tversky loss function for image segmentationusing 3D fully convolutional deep networks", retrievable here: https://arxiv.org/abs/1706.05721. It was designed to optimise segmentation on imbalanced medical datasets by utilising constants that can adjust how harshly different types of error are penalised in the loss function. From the paper:

    ... in the case of α=β=0.5 the Tversky index simplifies to be the same as the Dice coefficient, which is also equal to the F1 score. With α=β=1, Equation 2 produces Tanimoto coefficient, and setting α+β=1 produces the set of Fβ scores. Larger βs weigh recall higher than precision (by placing more emphasis on false negatives).

To summarise, this loss function is weighted by the constants 'alpha' and 'beta' that penalise false positives and false negatives respectively to a higher degree in the loss function as their value is increased. The beta constant in particular has applications in situations where models can obtain misleadingly positive performance via highly conservative prediction. You may want to experiment with different values to find the optimum. With alpha==beta==0.5, this loss becomes equivalent to Dice Loss.

"""

#Keras
ALPHA = 0.5
BETA = 0.5

def TverskyLoss(targets, inputs, alpha=ALPHA, beta=BETA, smooth=1e-6):
        
        #flatten label and prediction tensors
        inputs = K.flatten(inputs)
        targets = K.flatten(targets)
        
        #True Positives, False Positives & False Negatives
        TP = K.sum((inputs * targets))
        FP = K.sum(((1-targets) * inputs))
        FN = K.sum((targets * (1-inputs)))
       
        Tversky = (TP + smooth) / (TP + alpha*FP + beta*FN + smooth)  
        
        return 1 - Tversky




"""

Focal Tversky Loss

A variant on the Tversky loss that also includes the gamma modifier from Focal Loss.

"""

#Keras
ALPHA = 0.5
BETA = 0.5
GAMMA = 1

def FocalTverskyLoss(targets, inputs, alpha=ALPHA, beta=BETA, gamma=GAMMA, smooth=1e-6):
    
        #flatten label and prediction tensors
        inputs = K.flatten(inputs)
        targets = K.flatten(targets)
        
        #True Positives, False Positives & False Negatives
        TP = K.sum((inputs * targets))
        FP = K.sum(((1-targets) * inputs))
        FN = K.sum((targets * (1-inputs)))
               
        Tversky = (TP + smooth) / (TP + alpha*FP + beta*FN + smooth)  
        FocalTversky = K.pow((1 - Tversky), gamma)
        
        return FocalTversky


"""

Lovasz Hinge Loss

This complex loss function was introduced by Berman, Triki and Blaschko in their paper "The Lovasz-Softmax loss: A tractable surrogate for the optimization of the intersection-over-union measure in neural networks", retrievable here: https://arxiv.org/abs/1705.08790. It is designed to optimise the Intersection over Union score for semantic segmentation, particularly for multi-class instances. Specifically, it sorts predictions by their error before calculating cumulatively how each error affects the IoU score. This gradient vector is then multiplied with the initial error vector to penalise most strongly the predictions that decreased the IoU score the most. This procedure is detailed by jeandebleu in his excellent summary here.

This code is taken directly from the author's github repo here: https://github.com/bermanmaxim/LovaszSoftmax and all credit is to them.

In this kernel I have implemented the flat variant that uses reshaped rank-1 tensors as inputs for PyTorch. You can modify it accordingly with the dimensions and class number of your data as needed. This code takes raw logits so ensure your model does not contain an activation layer prior to the loss calculation.

I have hidden the researchers' own code below for brevity; simply load it into your kernel for the losses to function. In the case of their tensorflow implementation, I am still working to make it compatible with Keras. There are differences between the Tensorflow and Keras function libraries that complicate this.

"""

#Keras
# not working yet



"""
Combo Loss

This loss was introduced by Taghanaki et al in their paper "Combo loss: Handling input and output imbalance in multi-organ segmentation", retrievable here: https://arxiv.org/abs/1805.02798. Combo loss is a combination of Dice Loss and a modified Cross-Entropy function that, like Tversky loss, has additional constants which penalise either false positives or false negatives more respectively.
"""
#Keras
ALPHA = 0.5 # < 0.5 penalises FP more, > 0.5 penalises FN more
CE_RATIO = 0.5 #weighted contribution of modified CE loss compared to Dice loss

def Combo_loss(targets, inputs, eps=1e-9):
    targets = K.flatten(targets)
    inputs = K.flatten(inputs)
    
    intersection = K.sum(targets * inputs)
    dice = (2. * intersection + smooth) / (K.sum(targets) + K.sum(inputs) + smooth)
    inputs = K.clip(inputs, eps, 1.0 - eps)
    out = - (ALPHA * ((targets * K.log(inputs)) + ((1 - ALPHA) * (1.0 - targets) * K.log(1.0 - inputs))))
    weighted_ce = K.mean(out, axis=-1)
    combo = (CE_RATIO * weighted_ce) - ((1 - CE_RATIO) * dice)
    
    return combo


"""
Usage Tips

In my experience testing and debugging these losses, I have some observations that may be useful to beginners experimenting with different loss functions. These are not rules that are set in stone; they are simply my findings and your results may vary.

    Tversky and Focal-Tversky loss benefit from very low learning rates, of the order 5e-5 to 1e-4. They would not see much improvement in my kernels until around 7-10 epochs, upon which performance would improve significantly.

    In general, if a loss function does not appear to be working well (or at all), experiment with modifying the learning rate before moving on to other options.

    You can easily create your own loss functions by combining any of the above with Binary Cross-Entropy or any combination of other losses. Bear in mind that loss is calculated for every batch, so more complex losses will increase runtime.

"""













