# samlambda
Example AWS SAM application with API gateway and a Python3 Lambda function


Package, which uploads a zip of the code to the S3 bucket+prefix with a randomly-generated name, and creates a new CloudFormation template with the path to the zipped code

    $ aws cloudformation package --template-file samlambda.yaml --s3-bucket rob78596 —s3-prefix myfunction --output-template-file samlambda.packaged.yaml

Deploy. Multiple deploys will overwrite old versions of the CF stack and the components it presents

    $ aws cloudformation deploy --template-file samlambda.packaged.yaml --stack-name samlambda --capabilities CAPABILITY_IAM
