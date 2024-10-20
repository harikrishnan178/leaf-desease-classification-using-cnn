# Leaf Disease Classification using CNN
This repository contains a deep learning project for classifying leaf diseases using a Convolutional Neural Network (CNN).


# Introduction
Leaf diseases can have a significant impact on crop yield and quality. This project aims to classify different types of leaf diseases using a CNN model. By leveraging deep learning techniques, this system can help in the early detection of plant diseases, assisting farmers and agricultural experts in taking timely preventive actions.

# Dataset
The dataset used for this project contains images of healthy and diseased plant leaves. Each image is labeled with the type of disease or whether the leaf is healthy.

Number of Classes: X (e.g., healthy, powdery mildew, rust, etc.)
Total Images: X
Source: Kaggle/Custom Dataset
# Model Architecture
The model is based on a Convolutional Neural Network (CNN) that consists of multiple layers of convolutions, pooling, and fully connected layers to extract features from leaf images and classify them into different disease categories.

Input Layer: XxX pixels
Conv Layers: X (e.g., 3 conv layers with ReLU activations)
Pooling: Max Pooling
Fully Connected Layers: X (e.g., 2 dense layers with softmax for classification)
Loss Function: Categorical Crossentropy
Optimizer: Adam
# Dependencies
To run this project, you need to install the following dependencies:

Python 3.x
TensorFlow / Keras
NumPy
Matplotlib
OpenCV
Scikit-learn
You can install these dependencies using:

bash
Copy code
pip install tensorflow numpy matplotlib opencv-python scikit-learn
Usage
# Clone this repository:

bash
Copy code
git clone https://github.com/harikrishnan178/leaf-desease-classification-using-cnn
cd leaf-disease-classification-using-cnn
Download the dataset and place it in the data/ folder.

# Run the training script:

bash
Copy code
python train.py
To test the model on new images:

bash
Copy code
python predict.py --image path_to_image.jpg
# Results
The model achieved an accuracy of X% on the validation set. Below is an example of predictions made by the model:

# Image	Prediction	Confidence
Leaf 1	Rust	95%
Leaf 2	Healthy	98%
# Future Work
Experiment with different CNN architectures for better accuracy.
Implement transfer learning using pre-trained models such as VGG16 or ResNet.
Create a mobile application to deploy the trained model for real-time disease detection.
# License
This project is licensed under the MIT License - see the LICENSE file for details.
