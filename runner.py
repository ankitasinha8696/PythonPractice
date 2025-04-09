import os

project_path = 'C:/Users/z004w44s/Documents/GitHub/PythonPractice'

# Loop through all files in that directory
for root, dirs, files in os.walk(project_path):
    for file in files:
        if file.endswith('.py') and file != 'runner.py':
            filepath = os.path.join(root, file)
            print(f"\nRunning {filepath}...")
            exit_code = os.system(f'python "{filepath}"')
            print(f"Execution completed with exit code: {exit_code}")