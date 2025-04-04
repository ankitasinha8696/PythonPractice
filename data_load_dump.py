import json

data = {
    "name": "Alice",
    "age": 30,
    "is_active": True
}

# Serialize to JSON string
json_str = json.dumps(data)
print(json_str)

json_data = '{"name": "Alice", "age": 30, "is_active": true}'

# Deserialize JSON string
python_data = json.loads(json_data)
print(python_data)
print(python_data['name'])  # Access like a dict

