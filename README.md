# Dog/Cat Image Classifier 

This project is an end-to-end machine learning pipeline for classifying images of dogs and cats, built using a VGG16 pre-trained model. The application is developed with Flask for the backend and a web-based frontend to provide an intuitive user interface for uploading images and displaying classification results.

# Introduction
This project aims to provide a simple yet comprehensive example of how to build and deploy a machine learning model for image classification. Users can upload images of dogs and cats, and the application will classify them accordingly using a pre-trained VGG16 model.

# Features
->Upload images from your computer.  
->View the uploaded image in the browser.  
->Get real-time predictions (Dog or Cat) for the uploaded image.  
->Visually appealing interface with a responsive design.  

# Architecture
The project consists of the following components:

->Frontend: Built using HTML, CSS, JavaScript, and Bootstrap for responsive design.  
->Backend: Flask server to handle image uploads, processing, and serving the trained machine learning model.  
->Machine Learning Model: A pre-trained model for dog/cat classification, using TensorFlow/PyTorch.  

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/viyas52/End-to-End-Image-Classification-Project.git
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n ETEIC python=3.8 -y
```

```bash
conda activate ETEIC
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03- run the application
open the terminal and type the following command to run the application

```bash
python app.py
```

### STEP 03- run the application
Open your browser and go to:
```arduino
http://127.0.0.1:8080/
```
![readme for image classification proj](https://github.com/user-attachments/assets/5484cb37-2bac-4e19-bda3-7653f22db1a5)

# Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

