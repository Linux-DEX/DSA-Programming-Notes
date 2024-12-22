data = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": "Kulas Light",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": "Romaguera-Crona",
    },
    {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "Shanna@melissa.tv",
        # "address": "some value",
        "suite": "Suite 879",
        # "city": "Wisokyburgh",
        "zipcode": "90566-7771",
        "phone": "010-692-6593 x09125",
        "website": "anastasia.net",
        "company": "Deckow-Crist",
    },
    {
        "id": 3,
        "name": "Linux-Dex",
        "username": "linuxdex",
        "email": "linux@example.com",
        "address": "Bangalore",
        "suite": "Suite 879",
        "city": "Wisokyburgh",
        "zipcode": "90566-7771",
        "phone": "010-692-6593 x09125",
        "website": "anastasia.net",
        "company": "Deckow-Crist",
    },
]

schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "username": {"type": "string"},
            "email": {"type": "string"},
            "address": {"type": "string"},
            "suite": {"type": "string"},
            "city": {"type": "string"},
            "zipcode": {"type": "string"},
            "phone": {"type": "string"},
            "website": {"type": "string"},
            "company": {"type": "string"},
        },
        "required": [
            "id",
            "name",
            "username",
            "email",
            "address",
            "city",
            "zipcode",
            "phone",
            "website",
            "company",
        ],
    },
}


# def validate_json_data(data, schema):
#     errors = []
#
#     for item in data:
#         for field, rules in schema["items"]["properties"].items():
#             if field in schema["items"]["required"] and field not in item:
#                 errors.append(
#                     {"field": field, "error": f"Field '{field}' is required."}
#                 )
#
#             if field in item:
#                 expected_type = rules["type"]
#                 actual_type = type(item[field]).__name__
#
#                 if expected_type == "integer" and actual_type != "int":
#                     errors.append(
#                         {
#                             "field": field,
#                             "error": f"Invalid type for field '{field}'. Expected {expected_type}, but got {actual_type}.",
#                         }
#                     )
#                 elif expected_type == "string" and actual_type != "str":
#                     errors.append(
#                         {
#                             "field": field,
#                             "error": f"Invalid type for field '{field}'. Expected {expected_type}, but got {actual_type}.",
#                         }
#                     )
#
#     if errors:
#         item["errors"] = errors
#     else:
#         item["errors"] = errors
#
#     return data


def validate_json_data(data, schema):
    for item in data:
        errors = []

        for field, rules in schema["items"]["properties"].items():
            if field in schema["items"]["required"] and field not in item:
                errors.append(
                    {"field": field, "error": f"Field '{field}' is required."}
                )

            if field in item:
                expected_type = rules["type"]
                actual_type = type(item[field]).__name__

                if expected_type == "integer" and actual_type != "int":
                    errors.append(
                        {
                            "field": field,
                            "error": f"Invalid type for field '{field}'. Expected {expected_type}, but got {actual_type}.",
                        }
                    )
                elif expected_type == "string" and actual_type != "str":
                    errors.append(
                        {
                            "field": field,
                            "error": f"Invalid type for field '{field}'. Expected {expected_type}, but got {actual_type}.",
                        }
                    )

        if errors:
            item["errors"] = errors

    return data


result = validate_json_data(data, schema)

print(result)
