# AWS Smile Detection AI Pipeline

A cloud-based computer vision pipeline that detects smiles and facial emotions using **Amazon Rekognition**, **Amazon S3**, and **Amazon SageMaker**.

This project demonstrates how to build a simple AI workflow using AWS services and Python.

---

# Project Overview

This project captures a webcam image locally using Python and OpenCV, uploads it to **Amazon S3**, and analyzes it using **Amazon Rekognition** to detect:

- Faces
- Smiles
- Emotions
- Facial bounding boxes

The results are visualized using **Python, Pillow, and Matplotlib** inside a **SageMaker Notebook**.

---

# Architecture

The system follows this pipeline:
Local Machine
│
▼
Python + OpenCV
Capture Webcam Image
│
▼
Amazon S3
Secure Image Storage
│
▼
Amazon SageMaker Notebook
Data Processing
│
▼
Amazon Rekognition
Face & Smile Detection
│
▼
Annotated Image Output


---

# Technologies Used

| Technology | Purpose |
|-----------|--------|
| Python | Core programming language |
| OpenCV | Capture webcam image |
| boto3 | AWS SDK for Python |
| Amazon S3 | Image storage |
| Amazon SageMaker | Notebook environment |
| Amazon Rekognition | Face and smile detection |
| Pillow | Image processing |
| Matplotlib | Visualization |

---

# Project Structure


aws-smile-detection-pipeline
│
├── scripts
│ └── upload_image_to_s3.py
│
├── notebooks
│ └── smile_detection_lab.ipynb
│
├── images
│ └── (project screenshots)
│
├── docs
│
├── requirements.txt
│
└── README.md


---

# Setup Instructions

## 1 Install Dependencies


pip install boto3 opencv-python pillow matplotlib


---

## 2 Configure AWS CLI


aws configure


Enter:


AWS Access Key
AWS Secret Key
Region: us-east-1


Never commit credentials to GitHub.

---

## 3 Create S3 Bucket

Create an S3 bucket:


smile-detection-lab-yourname


Region:


us-east-1


---

## 4 Run Webcam Capture Script


python scripts/upload_image_to_s3.py


Press **SPACE** to capture an image.

The image will automatically upload to **Amazon S3**.

---

## 5 Launch SageMaker Notebook

Create a notebook instance:


Instance type: ml.t2.medium


Open **JupyterLab** and run the notebook:


notebooks/smile_detection_lab.ipynb


---

# Example Output

The system detects faces and determines whether the person is smiling.

Output includes:

- Face bounding boxes
- Smile confidence score
- Emotion probabilities

Example result:


Face 1:
Smile: True (Confidence: 98.4%)
HAPPY: 97.2%
CALM: 1.8%


---

# Cost Estimate

This project uses mostly **AWS Free Tier services**.

Typical cost for a short test run:

| Service | Estimated Cost |
|-------|------|
| Amazon S3 | negligible |
| SageMaker Notebook (ml.t2.medium) | ~ $0.05–$0.07/hour |
| Amazon Rekognition | a few cents per 1000 images |

Always stop the SageMaker notebook after use to avoid charges.

---

# Security Best Practices

This project follows AWS security best practices:

- Use **IAM roles instead of access keys**
- Apply **least privilege permissions**
- Never store credentials in code
- Use **AWS CLI configuration**
- Store images securely in **S3**

---

# Cleanup

To avoid charges:

1. Stop or delete the SageMaker notebook
2. Delete the S3 bucket
3. Remove unused IAM resources

---

# Key Learning Outcomes

This project demonstrates:

- AWS AI service integration
- Python automation with boto3
- Computer vision pipelines
- Cloud-based machine learning workflows
- Image visualization and annotation

---

# Future Improvements

Possible extensions:

- Real-time smile detection
- Video stream processing
- Serverless pipeline with AWS Lambda
- Web application interface

---

# Author

GitHub: https://github.com/MAKOMERE111
