import os

path = 'D:/JenkinsProjects/python-practice'

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            print(f'Running: {filepath}')
            exit_code = os.system(f'python "{filepath}"')
            print(f'Exit code: {exit_code}')