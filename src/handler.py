import json

print('Loading function')

def lambda_handler(event, context):
    print("i'm running")

    data = {}
    data["message"] = "this is a message"
    data["message2"] = "this is another good message"

    #reponse = {}
    #reponse["statusCode"] = 200
    #reponse["body"] = json.dumps(data)

    return {
        "statusCode" : 200,
        "body" : json.dumps(data)
    }

output = lambda_handler("", "")
print(output)
