import pandas as pd

data = {'имя': ['Анна', 'Борис', 'Вера'],
        'возраст': [25, 30, 28],
        'город': ['Мосева', 'Анапа', 'Казань']}

df = pd.DataFrame(data)
print(df)

data = {'дата': ['21-02-2024', '21-02-2024', '22-02-2024', '22-02-2024', '23-02-2024'],
'продукт': ['яблоки', 'груши', 'яблоки', 'бананы', 'груши'],
'количество': [5, 3, 4, 2, 4],
'цена': [100, 120, 100, 80, 120]}

df = pd.DataFrame(data)

сводная = pd.pivot_table(df, values='количество', index=['дата'], columns=['продукт'], aggfunc='sum', fill_value=0)

print(сводная)


df = pd.DataFrame({
    'имя': ['Анна', 'Борис', 'Вера'],
    'возраст': [25, 30, 28]})
def классификация_возраста(возраст):
    if возраст < 30:
        return 'молодой'
    else:
        return 'взрослый'

df['категория'] = df['возраст'].apply(классификация_возраста)
print(df)




import requests

responce = requests.get('https://api.github.com')
print(responce.status_code)
print(responce.json())


data = {'key': 'value'}
responce = requests.post('https://httpbin.org/post', data=data)
print(responce.status_code)
print(responce.json())


responce = requests.get('https://api.github.com')
if responce.status_code == 200:
    data = responce.json()
    print(data)
else:
    print(f'Ошибка: {responce.status_code}')




from PIL import Image
img = Image.open("Default_capybara_0.jpg")
print(img)


rotated_img = img.rotate(90)
print(rotated_img)


new_img = img.resize((800, 600))
new_img.save("новое_изображение.jpg")
print(new_img)








