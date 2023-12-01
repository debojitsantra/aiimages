import os
import json

image_folder = "Generated"
json_file = "images.json"

image_paths = [f"{image_folder}/{image}" for image in os.listdir(image_folder) if image.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

data = {"images": image_paths}

with open(json_file, "w") as json_file:
    json.dump(data, json_file, indent=2)

print(f"JSON file '{json_file}' generated successfully.")
