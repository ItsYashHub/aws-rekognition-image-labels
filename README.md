# AWS Rekognition Image Label Detection (Python)

This repository contains a Python application that demonstrates the use of **AWS Rekognition** to detect labels in images stored in **Amazon S3**. The project retrieves detected objects along with confidence scores and visualizes bounding boxes on the image.

---

## Overview

The objective of this project is to implement an end-to-end image analysis workflow using AWS AI services. The application interacts with AWS Rekognition via the **boto3 SDK**, processes images stored in S3, and displays the detection results using Python visualization libraries.

This project is designed for:
- Learning AWS Rekognition
- Understanding cloud-based computer vision
- Demonstrating practical AWS SDK usage
- Portfolio and interview preparation

---

## Architecture Flow

1. An image is uploaded to an Amazon S3 bucket  
2. The Python script sends the image reference to AWS Rekognition  
3. Rekognition analyzes the image and detects labels  
4. The service returns confidence scores and bounding box data  
5. The results are displayed and visualized locally  

---

## Technology Stack

- Python 3.9+
- AWS Rekognition
- Amazon S3
- boto3 (AWS SDK for Python)
- Matplotlib
- Pillow (PIL)

---

## Project Structure

