import boto3
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from io import BytesIO


def detect_labels(photo, bucket):
    # Create Rekognition client
    client = boto3.client('rekognition', region_name='us-east-1')
    
    # Call Rekognition to detect labels
    response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': photo
            }
        },
        MaxLabels=10
    )

    print("Detected labels for " + photo)
    print()

    # Print label information
    for label in response['Labels']:
        print("Label:", label['Name'])
        print("Confidence:", label['Confidence'])
        print()

    # Load image from S3
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, photo)
    img_data = obj.get()['Body'].read()
    img = Image.open(BytesIO(img_data))

    # Display the image
    plt.imshow(img)
    ax = plt.gca()

    # Plot bounding boxes
    for label in response['Labels']:
        for instance in label.get('Instances', []):
            bbox = instance['BoundingBox']

            left = bbox['Left'] * img.width
            top = bbox['Top'] * img.height
            width = bbox['Width'] * img.width
            height = bbox['Height'] * img.height

            rect = patches.Rectangle(
                (left, top),
                width,
                height,
                linewidth=1,
                edgecolor='r',
                facecolor='none'
            )
            ax.add_patch(rect)

            label_text = (
                label['Name'] +
                " (" +
                str(round(label['Confidence'], 2)) +
                "%)"
            )

            plt.text(
                left,
                top - 2,
                label_text,
                color='r',
                fontsize=8,
                bbox=dict(facecolor='white', alpha=0.5)
            )

    plt.axis('off')
    plt.show()

    return len(response['Labels'])


# -------------------------
# Replace these values
# -------------------------
bucket_name = "aws-rekognition-label-images-22"
image_file_name = "pexels-leofallflat-1737957.jpg"

detect_labels(image_file_name, bucket_name)
