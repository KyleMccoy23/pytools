from tools import newProject
from tools import emailCleaner

while True:
    choise = input("""
<Menu>
|
|_ 0 - New Project
|          
|_ 1 - Email Cleaner
|                 
|_ 2 - Python Lab
|
|_ 3 - Download Cleaner - WIP
|
|_ Q - Quit
                   
> """).lower()
    
    match(choise):
        case '0':
            newProject.main()
            break
        case '1':
            emailCleaner.main()
            break
        case '2':
            newProject.labProject()
            break
        case '3':
            print("curently a work in progress")
            break
        case 'q':
            break
