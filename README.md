# CaptchaAI

Capturing and labeling captcha images from a website automatically using javascript. The goal here is to make a dataset of captcha images and finally use the dataset to make an AI model which predicts the text in a captcha image. The other goal is to make a GAN model which can generate captcha images.

This project is now divided into 2 parts:

## 1. Captcha Text Prediction
In this part, the main focus is on creating a dataset of annotated captcha images. After putting together a large enough dataset, the goal will be to make an AI model which can use the dataset to predict text in a given captcha image.

## 2. Captcha Generation
In this part, the main focus is on generating new captcha images via a Generative Adversarial Network (GAN). We don't need annotated data for this part so putting together a dataset is not that difficult. However, we do need a large amount of data! The model is implemented in CaptchaGAN.ipynb.