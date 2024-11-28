import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image1.jpg','Ratan Tata'),
      ('image2.jpg','Ratan Tata'),
      ('image3.jpg','Mukesh Ambani'),
      ('image4.jpg','Mukesh Ambani'),
      ('image5.jpg','Sundar Pichai'),
      ('image6.jpg','Sundar Pichai')
      ]

# Iterate through list to upload objects to S3 Bucket  
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('famouspersons1','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
