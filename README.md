# samlambda
Example AWS SAM application with API gateway and a Python3 Lambda function


## Package
Uploads a zip of the application code to the specified S3 bucket with a randomly-generated file name. And then creates a new local version of the CloudFormation template with the correct path to the application code in S3

    $ aws cloudformation package --template-file samlambda.yaml --s3-bucket rob78596 —s3-prefix myfunction --output-template-file samlambda.packaged.yaml

## Deploy
Creates and deploys a CloudFormation stack. This creates an API Gateway, Lambda function and appropriate roles for the API GW to execute the Lambdas. Note that multiple CF deploys will overwrite old versions of the CF stack and the components it presents (which is probably what you want in dev)

    $ aws cloudformation deploy --template-file samlambda.packaged.yaml --stack-name samlambda --capabilities CAPABILITY_IAM
