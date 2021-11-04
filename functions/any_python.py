import json
from typing import Mapping, Dict

from pydantic import ValidationError
from pydantic.error_wrappers import display_errors

from functions._models import EventModelBodyParameters, PostAppEventBody

numbers = [1, 2, 3, 4, 5]
print(any(numbers))

mix_data_a = [0, False, 5]  # True since 5 is true
print(any(mix_data_a))


def create_app_environment(event: Mapping[str, object]) -> Dict[str, object]:
    parsed_event = EventModelBodyParameters.parse_obj(event)
    if "appName" not in parsed_event.pathParameters:
        raise Exception(f"There is not a appName field")

    appName = parsed_event.pathParameters["appName"].lower()
    user_email = parsed_event.requestContext.authorizer.user_email
    print(f"appName: {appName} and user_email: {user_email}")

    body_string = "{}" if parsed_event.body is None or parsed_event.body == "" else parsed_event.body
    try:
        body = json.loads(body_string)
        validate_input_data = PostAppEventBody.parse_obj(body)
        app_environment_name = validate_input_data.environment
        print(f"App Environment Name: {app_environment_name}")
    except ValidationError as e:
        msg = display_errors(e.errors())
        return {"statusCode": 400, "body": json.dumps({"msg": msg})}


if __name__ == '__main__':
    event = {
        "body": json.dumps(
            {
                "branchName": "main",
                "environment": "dev",
                "envVariables": {"username": "userName", "password": "1234"},
                "logSharingAwsAccountIds": ["12345567"],
                "resourceConfiguration": {"memoryMB": 2000, "cpuMillicores": 1000},
            }
        ),
        "pathParameters": {"appName": "davor-test"},
        "requestContext": {
            "authorizer": {
                "user_email": "test@test.com"
            }
        },
    }
    response = create_app_environment(event=event)
    print(response)
