
import shutil
import os

def main():
    _path = "C:\\Users\\kylem\\OneDrive\\Documents\\ProgrammingProjects"

    while True:
        try:
            projectName = input("What is the name: ")
            projectPath = os.path.join(_path, projectName)
            os.makedirs(projectPath)
            break
        except:
            print("There is already a project with that name")

    shutil.copy(f'{_path}\\Scripts\\pytools\\Templates\\main.py', f'{projectPath}\\main.py')

    os.system(f"code {projectPath}")
    SystemExit()

def labProject():
    _path = "C:\\Users\\kylem\\OneDrive\\Documents\\ProgrammingProjects\\Labs"

    while True:
        try:
            projectName = input("What is the name: ")
            projectPath = os.path.join(_path, projectName)
            os.makedirs(projectPath)
            break
        except:
            print("There is already a project with that name")

    with open(f'{projectPath}\\{projectName}.py', 'w') as f:
        f.write("print('Hello World')")

    os.system(f"code {projectPath}")
    SystemExit()
    
main()