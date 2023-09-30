# CaptchaAI

<p align="justify">
Capturing and labeling captcha images from a website automatically using javascript. The goal here is to make a dataset of captcha images and finally use the dataset to make an AI model which predicts the text in a captcha image. The other goal is to make a GAN model which can generate captcha images.
</p>

This project is now divided into 3 parts:

## 1. Captcha Text Prediction
<p align="justify">
In this part, the main focus is on creating a dataset of annotated captcha images. After putting together a large enough dataset, the goal will be to make an AI model which can use the dataset to predict text in a given captcha image.
</p>

## 2. Captcha Generation
<p align="justify">
In this part, the main focus is on generating new captcha images via a Generative Adversarial Network (GAN). We don't need annotated data for this part so putting together a dataset is not that difficult. However, we do need a large amount of data! The model is implemented in CaptchaGAN.ipynb.
</p>

## 3. Captcha Clustering
<p align="justify">
There are different kinds of captcha images. This variety will stop the GAN from finding any particular pattern in the images, making the GAN unable to produce any proper captcha image. So, before feeding the whole dataset to the GAN we have to preprocess the dataset in a way that same kind of captcha images are grouped together. For automatic grouping of images, AutoEncoder and K-Means are used. AutoEncoder is used for getting the latent variables and K-Means is used for clustering.
</p>