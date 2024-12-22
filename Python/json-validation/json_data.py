data = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {"lat": "-37.3159", "lng": "81.1496"},
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets",
        },
    },
    {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "Shanna@melissa.tv",
        "address": {
            # "street": "Victor Plains",
            "street": 234,
            "suite": "Suite 879",
            "city": "Wisokyburgh",
            "zipcode": "90566-7771",
            "geo": {"lat": "-43.9509", "lng": "-34.4618"},
        },
        "phone": "010-692-6593 x09125",
        "website": "anastasia.net",
        "company": {
            "name": "Deckow-Crist",
            "catchPhrase": "Proactive didactic contingency",
            "bs": "synergize scalable supply-chains",
        },
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
            "address": {
                "type": "object",
                "properties": {
                    "street": {"type": "string"},
                    "suite": {"type": "string"},
                    "city": {"type": "string"},
                    "zipcode": {"type": "string"},
                    "geo": {
                        "type": "object",
                        "properties": {
                            "lat": {"type": "string"},
                            "lng": {"type": "string"},
                        },
                        "required": ["lat", "lng"],
                    },
                },
                "required": ["street", "suite", "city", "zipcode", "geo"],
            },
            "phone": {"type": "string"},
            "website": {"type": "string"},
            "company": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "catchPhrase": {"type": "string"},
                    "bs": {"type": "string"},
                },
                "required": ["name", "catchPhrase", "bs"],
            },
        },
        "required": [
            "id",
            "name",
            "username",
            "email",
            "address",
            "phone",
            "website",
            "company",
        ],
    },
}


def validate_json_data(data, schema):
    errors = []

    def validate_item(item, schema_item):
        for field in schema_item.get("required", []):
            if field not in item:
                errors.append(
                    {"field": field, "error": f"Field '{field}' is required."}
                )

        for field, rules in schema_item["properties"].items():
            if field in item:
                expected_type = rules["type"]
                actual_value = item[field]

                if expected_type == "integer" and not isinstance(actual_value, int):
                    errors.append(
                        {
                            "field": field,
                            "error": f"Invalid type for field '{field}'. Expected {expected_type}, but got {type(actual_value).__name__}.",
                        }
                    )
                elif expected_type == "string" and not isinstance(actual_value, str):
                    errors.append(
                        {
                            "field": field,
                            "error": f"Invalid type for field '{field}'. Expected {expected_type}, but got {type(actual_value).__name__}.",
                        }
                    )

                if isinstance(actual_value, dict):
                    validate_item(actual_value, rules)

    for item in data:
        validate_item(item, schema["items"])

    if errors:
        for item in data:
            item["error"] = errors
        return data

    return data


result = validate_json_data(data, schema)
print(result)
