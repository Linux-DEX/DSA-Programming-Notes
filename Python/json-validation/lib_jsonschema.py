import jsonschema
from jsonschema import ValidationError, validate


def validate_json_data(data, schema):
    errors = []

    def custom_error_handler(err):
        field = err.path[0] if err.path else "Unknown"
        message = f"Invalid type for field '{field}'. Expected {err.schema['type']}, but got {type(data.get(field)).__name__}."
        errors.append({"field": field, "error": message})

    try:
        validate(instance=data, schema=schema)
    except ValidationError as err:
        custom_error_handler(err)

    if errors:
        data["errors"] = errors

    return data


# JSON schema
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "email": {"type": "string"},
    },
    "required": ["name", "age"],
}

# JSON data
data = {
    "name": "Linux-DEX",
    "age": "23",  # This will cause an error since it should be an integer
    "email": "linux@example.com",
}

# Validate the data
result = validate_json_data(data, schema)

print(result)
