# AWS Rekognition Image Label Generator

## Overview

This project demonstrates how to build an **image label detection system** using **Amazon Rekognition**.
Images are stored in **Amazon S3**, analyzed using Rekognition’s `DetectLabels` API, and the detected objects are displayed with **confidence scores and bounding boxes** using Python.

This project showcases practical usage of **AWS services**, **IAM security**, and **Python automation**, making it suitable for **cloud engineering and data engineering portfolios**.

---

## Architecture

1. User uploads images to **Amazon S3**
2. Python application accesses AWS using **IAM + AWS CLI**
3. **Amazon Rekognition** analyzes images from S3
4. Detected labels and confidence scores are returned
5. **Matplotlib** displays bounding boxes on the image

---

## Technologies Used

* **Amazon S3** – Image storage
* **Amazon Rekognition** – Image label detection
* **AWS IAM** – Authentication and authorization
* **AWS CLI** – Programmatic AWS access
* **Python (Boto3)** – AWS SDK
* **Matplotlib** – Visualization
* **Pillow (PIL)** – Image handling

---

## Prerequisites

* AWS Account (with billing enabled)
* Python 3.8 or above
* AWS CLI installed
* Basic knowledge of AWS and Python

---

## Setup and Installation

### 1. Create an S3 Bucket

* Create an S3 bucket in AWS
* Upload one or more images (e.g., `image1.jpg`)
* Note the **bucket name** and **region**

---

### 2. Create IAM User

* Go to **IAM → Users → Create User**
* Enable **Programmatic access**
* Attach policy: `AdministratorAccess` (for learning/demo)
* Save the **Access Key ID** and **Secret Access Key**

---

### 3. Configure AWS CLI

Run the following command in terminal:

```bash
aws configure
```

Enter:

* Access Key ID
* Secret Access Key
* Region (same as S3 bucket)
* Output format: `json` (optional)

---

### 4. Install Required Python Libraries

```bash
pip install boto3 matplotlib pillow
```

---

## Project Structure

```text
aws-rekognition-image-labels/
│
├── rekognition_image_labels.py
├── README.md
└── requirements.txt (optional)
```

---

## How to Run the Project

1. Open terminal in the project directory
2. Update the following variables in the Python file:

```python
photo = "your_image_name.jpg"
bucket = "your_bucket_name"
```

3. Run the script:

```bash
python rekognition_image_labels.py
```

---

## Output

* Terminal output shows:

  * Detected labels
  * Confidence scores
* A pop-up window displays:

  * Image with bounding boxes
  * Label names with confidence percentages

---

## Sample Detected Labels

* Car (97%)
* Person (99%)
* Traffic Light (88%)
* Road
* Urban
* Walking

---

## Use Cases

* Image content analysis
* Smart surveillance systems
* Traffic and crowd analysis
* Retail product recognition
* AI-powered image moderation

---

## Clean-Up (Important)

After testing:

* Delete the S3 bucket
* Remove IAM user and access keys
* Verify no unused AWS resources remain

---

## Future Enhancements

* Video label detection
* Real-time webcam detection
* Facial expression analysis
* Serverless integration with AWS Lambda
* Web UI using Flask or Streamlit

---

## One-Line Project Description

A Python-based AWS project that detects objects in S3 images using Amazon Rekognition and visualizes results with confidence scores and bounding boxes.

---

## Author

**Yash Sunil Jadhav**
Computer Engineering Graduate
AWS & Data Engineering Enthusiast


