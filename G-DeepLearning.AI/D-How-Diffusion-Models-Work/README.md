# Notes

These notes are from the DeepLearning.ai course on [How Diffusion Models Work](https://www.deeplearning.ai/short-courses/how-diffusion-models-work/)

The topics covered in the lectures are as follows:
- Introduction 
- Intuition (4)
- Sampling (7)
- Neural Network (3)
- Training (6)
- Controlling (5) 
- Speeding Up (4)
- Summary (2)

## 1. Introduction 

- Midjourney, Stable Diffusion, DALL-E, and others are able to generate the image by just giving a prompt. 
- These models have learnt to subtract noise to generate an image.
- Concrete implementation of image generation using a diffusion model.
- Current state and capabilities of diffusion models 
- Understand the sampling process and then refine it to build a nice looking image 
- Learn the necessary programming skills to learn to train a diffusion model effectively. 
- Build a neural network that can prevent noise in an image 
- You can add context to the model so that you can control what you want to generate. 
- By implementing advanced algorithms, you will learn how to accelerate the sampling process by 10X

Running example:
    - generating 16X16 stripes
    - 8 bit characters in video games

Application of Diffusion Models: 
- generating molecules for drug discovery

## 2. Intuition
