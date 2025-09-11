data = [
    {
        "name": "Ravi",
        "age": 45,
        "location": "Delhi"
    },
    {
        "name": "Ravi",
        "age": 45,
        "location": "Delhi"
    },
    {
        "name": "Ravi",
        "age": 45,
        "location": "Delhi"
    }
]

# Write to file in single line format
with open("output.txt", "w") as f:
    for element in data:
        for key, value in element.items():
            f.write(f"{key}:{value}\n")
        f.write("\n")
