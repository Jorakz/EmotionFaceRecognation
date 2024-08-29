import os
from PIL import Image

input_folder = "emotion recognation 224X224"
output_folder = "emotion recognation 48X48"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for emotion in ['angry','disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']:
    input_path = os.path.join(input_folder, emotion)
    output_path = os.path.join(output_folder, emotion)

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for filename in os.listdir(input_path):
        if filename.endswith(".png"):
            input_file = os.path.join(input_path, filename)
            output_file = os.path.join(output_path, filename)

            with Image.open(input_file) as img:
                img = img.convert("L")
                img = img.resize((48, 48), Image.NEAREST)
                img.save(output_file, "PNG")

            print(f"Resized {input_file} to {output_file}")