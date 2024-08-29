import os
import pandas as pd
import numpy as np
from PIL import Image

# Define the directories
train_dir = 'FER-2013/train'
test_dir = 'FER-2013/test'
valid_dir = 'FER-2013/valid'
import matplotlib.pyplot as plt

# Данные для каждой диаграммы
emotions = ["Anger", "Disgust", "Fear", "Happy", "Sadness", "Surprise", "Neutral"]

train_values = [3995, 436, 4097, 7215, 4830, 3171, 4965]
valid_values = [491, 55, 528, 879, 594, 416, 626]
test_values = [467, 56, 496, 895, 653, 415 , 607]

# Создаем 3 диаграммы в одном графике
fig, axs = plt.subplots(1, 3, figsize=(22, 6), sharey=True)

# Первая диаграмма для Train
axs[0].bar(emotions, train_values)
axs[0].set_title("Train")
axs[0].set_xlabel("Тип емоцій")
axs[0].set_ylabel("Кількість зображень")
# Добавляем числовые метки над столбцами
for i, value in enumerate(train_values):
    axs[0].text(i, value + 30, str(value), ha='center')

# Вторая диаграмма для Valid
axs[1].bar(emotions, valid_values)
axs[1].set_title("Valid")
axs[1].set_xlabel("Тип емоцій")
for i, value in enumerate(valid_values):
    axs[1].text(i, value + 30, str(value), ha='center')

# Третья диаграмма для Test
axs[2].bar(emotions, test_values)
axs[2].set_title("Test")
axs[2].set_xlabel("Тип емоцій")
for i, value in enumerate(test_values):
    axs[2].text(i, value + 30, str(value), ha='center')

# Показ графика
plt.show()
emotions = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

# Initialize the CSV data
csv_data = {'emotion': [], ' Usage': [], ' pixels': []}

def data_editing(dir, emotion,usage_type):
    for filename in os.listdir(os.path.join(dir, emotion)):
        # Open the image file
        image_path = os.path.join(os.path.join(dir, emotion), filename)
        image = Image.open(image_path)

        # Convert the image to a numpy array
        pixels = np.array(image)
        pixels_str = ' '.join(map(str, pixels.flatten()))
        # Add the emotion and pixels to the CSV data
        csv_data['emotion'].append(emotions.index(emotion))
        csv_data[' Usage'].append(usage_type)
        csv_data[' pixels'].append(pixels_str)

# Loop through each emotion
for emotion in emotions:
    # Define the emotion directory
    #emotion_dir = os.path.join(train_dir, emotion)

    data_editing(train_dir, emotion, 'Training')
    data_editing(test_dir, emotion, 'Testing')
    data_editing(valid_dir, emotion, 'Validation')

# Convert the CSV data to a Pandas DataFrame
df = pd.DataFrame(csv_data)
print(df)
# Shuffle the DataFrame rows while maintaining the order of 'emotion' and 'usage'
df_shuffled = df.groupby([' Usage']).apply(lambda x: x.sample(frac=1)).reset_index(drop=True)


# Save the DataFrame to a CSV file

print(df_shuffled)
df_shuffled.to_csv('FER-2013_7_emotion.csv', index=False)