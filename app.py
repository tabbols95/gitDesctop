import shutil
import os

print('Commander secret files')
# err[0] - ошибка ввода команд
# err[1] - отсутсвие дирректория
err = ['>> Ошибка ввода команд', '>> Выбранная Вами дирректория отсутствует']
while True:
    level = -1
    command = input('>> ')
    commandDetail = command.split(' ')
    gitResult = []
    complete = ''
    for x in commandDetail:
        level += 1
        # command
        if (x == 'git') and (level == 0) and (len(command) == 3):
            print('>> Hi, my name`s git')
            continue
        if (x == 'git') and (level == 0) and (complete == ''):
            complete = 'git'
            continue
        elif (x == 'log') and (level == 1) and (complete == 'git'):
            file = open(r'.secretFiles/controle.log', 'r', encoding='utf-8')
            reader = file.read().split('\n')
            for readerRead in reader:
                if readerRead != '':
                    gitResult.append('- ' + readerRead)
            file.close()
            complete = 'log'
            continue
        elif (x == 'help') and (level == 0) and (len(command) == 4) and (complete == ''):
            gitResult.append('- [git] // поприветствовать систему git')
            gitResult.append('- [git log] // показать файлы логов')
            gitResult.append('- [git copy Folder] // скопировать папку из секретной папки')
            gitResult.append('- [close] // выход из приложения')
        elif (x == 'copy') and (level == 1) and (complete == 'git') and ((len(commandDetail) - level) > 1):
            complete = 'copy'
            continue
        elif (x == 'close') and (level == 0) and (len(command) == 5) and (complete == ''):
            exit()

        # files
        elif (x != '') and (level == 2) and (complete == 'copy'):
            try:
                shutil.copytree(r'.secretFiles/{0}'.format(x), r'.{0}'.format(x))
                listsDirrectiry = os.listdir(r'.secretFiles/{}'.format(x))
                gitResult.append('Скопированные файлы:')
                for listsDirrectiryRead in listsDirrectiry:
                    gitResult.append('- ' + listsDirrectiryRead)
            except FileNotFoundError:
                gitResult.append(err[1])

        # errors
        else:
            print(err[0])
            gitResult = []
            break
    for readResult in gitResult:
        print(readResult)
