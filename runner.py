import os

path = 'C:/Users/z004w44s/Documents/GitHub/PythonPractice'

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            print(f'Running: {filepath}')
            os.system(f'python "{filepath}"')