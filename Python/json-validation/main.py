import json


def validate_json_data(data, schema):
    errors = []

    for field, rules in schema["properties"].items():
        if field in schema["required"] and field not in data:
            errors.append({"field": field, "error": f"Field '{field}' is required."})

        if field in data:
            expected_type = rules["type"]
            actual_type = type(data[field]).__name__

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
        data["errors"] = errors

    return data


schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "email": {"type": "string"},
    },
    "required": ["name", "age"],
}

data = {
    "name": "Linux-DEX",
    "age": "25",
    "email": "linux@example.com",
}

result = validate_json_data(data, schema)

print(result)
