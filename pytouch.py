import sys
import os 

try:
    if (sys.argv[1:][0] == '--set' or sys.argv[1:][0] == '-s'):
        print('\nData-input,['+'\033[91m'+'overwriting'+'\033[0m'+']')

        print('\nEnter the module name and alias only [ex- numpy as np,pandas as pd ...] [comma-separated]')
        MODS = input().split(',')
        print(MODS)
        # Write mods in import.logs

        with open('/usr/local/bin/headers.log', 'w') as f:
            for module in MODS:
                f.write('import ' + module + '\n')

            f.close()

        print('header-setting'+'\033[92m'+ 'completed.'+'\033[0m')


    elif (sys.argv[1:][0] == '--truncate' or sys.argv[1:][0] == '-t'):
        print('\nErasing data in logs')
        
        with open('/usr/local/bin/headers.log', 'w') as f:
            f.truncate(0)
            print('\033[96m'+'headers.log..'+'\033[0m'+',\ndata_status=['+'\033[91m'+'truncated'+'\033[0m'+']')
    
            f.close()
        print()



    elif (sys.argv[1:][0] == '--add' or sys.argv[1:][0] == '-a'):

        print('\nEnter the module name and alias only [ex- numpy as np,pandas as pd ...] [comma-separated]')
        MODS = input().split(',')
        with open('/usr/local/bin/headers.log', 'a') as f:
            for module in MODS:
                f.write('import ' + module + '\n')

            f.close()

        print('Module '+'\033[92m'+'added '+'\033[0m' +'to logs.')


    elif (sys.argv[1:][0] == '--display' or sys.argv[1:][0] == '-d'):
        print('\033[92m'+'\nDisplaying logs..'+'\033[0m')

        with open('/usr/local/bin/headers.log', 'r') as f:

            content = f.readlines()

            f.close()

        for i,line in enumerate(content,1):
            print('\n' +str(i)+". "+ line.strip())

        print('\n')

    elif (sys.argv[1:][0] == '--edit' or sys.argv[1:][0] == '-e'):
        print('\033[92m'+'\nEditing logs..'+'\033[0m')

        with open('/usr/local/bin/headers.log', 'r') as f:

            content = f.readlines()

        print('\n')

        for i, line in enumerate(content, 1):
            print(str(i) + "." + line.strip())

        print('\n')

        content = list(map(lambda x: x.strip(), content))

        while True:

            editline = int(input('Enter the line number to --edit | `9` to exit : '))

            if (editline == 9):
                print('\033[91m'+'exiting..'+'\033[0m')
                break
                exit(0)

            elif editline in list(range(1, len(content) + 1)):
                print(content[editline - 1])
                print('Editing line ' + str(editline))
                replace = input(
                    '\nEnter the module name and alias only [ex- numpy as np,pandas as pd ...] [comma-separated]\n')
                content[editline - 1] = 'import ' + replace
                print(content)
                with open('/usr/local/bin/headers.log', 'w') as f:

                    for module in content:
                        f.write(module + '\n')

                    f.close()

                print('headers.log ['+'\033[92m'+'updated'+'\033[0m'+'].')

                break

            else:
                continue

    elif (sys.argv[1]=='--file' or sys.argv[1] == '-f'):
        filenames = sys.argv[2:]
        with open('/usr/local/bin/headers.log','r') as hf:
            content = hf.readlines()
        hf.close()
        for file in filenames:
            with open(file,'w') as wf:
                for importline in content:
                    wf.write(importline)
                print('\033[92m' + 'imports set in : ' + '\033[0m' + '[' + file + ']')
                wf.close()



    else:
        pass


except KeyboardInterrupt:
    print("\n"+"\033[91m"+"\033[1m"+"Command interrupted "+"\033[0m")




   
        




        

        
    
       

     

