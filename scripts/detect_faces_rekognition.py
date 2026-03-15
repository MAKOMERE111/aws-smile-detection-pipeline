import boto3
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

BUCKET_NAME = 'smile-detection-lab-yourname'  # Replace with your S3 bucket
OBJECT_KEY = 'webcam_20260315_022647.jpg'     # Replace with your image key
LOCAL_IMAGE = 'webcam_20260315_022647.jpg'

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')

s3.download_file(BUCKET_NAME, OBJECT_KEY, LOCAL_IMAGE)
print(f"Downloaded {LOCAL_IMAGE} from S3")

with open(LOCAL_IMAGE, 'rb') as img_file:
    response = rekognition.detect_faces(Image={'Bytes': img_file.read()}, Attributes=['ALL'])

image = Image.open(LOCAL_IMAGE)
img_width, img_height = image.size
draw = ImageDraw.Draw(image)

for i, face in enumerate(response['FaceDetails'], start=1):
    smile = face['Smile']
    status = 'Smiling' if smile['Value'] else 'Not Smiling'
    confidence = smile['Confidence']

    box = face['BoundingBox']
    left = img_width * box['Left']
    top = img_height * box['Top']
    width = img_width * box['Width']
    height = img_height * box['Height']

    draw.rectangle([left, top, left + width, top + height], outline='red', width=3)
    draw.text((left, top + height + 5), f"{status} ({confidence:.1f}%)", fill='green')

    print(f"Face {i}: {status} ({confidence:.1f}%)")

plt.figure(figsize=(10, 6))
plt.imshow(image)
plt.axis('off')
plt.title("Smile Detection Output")
plt.show()