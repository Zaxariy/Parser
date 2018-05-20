import requests , bs4,xlrd,os
import shutil

#опрделяем рабочую дерикторию
current_directory=os.getcwd()

def download() :
    print("Идет скачивание файла")
    #открываем или создаем файл для записи содержимого и присваиваем ему нужное нам имя
    f = open('schedule.xlsx', 'wb')
    #ссылка на нужный файл
    ufr = requests.get("https://www.mirea.ru/upload/medialibrary/401/IK-1k-17_18-vesna.xlsx")
    #запись и закрытие файла
    f.write(ufr.content)
    f.close()
    print("Скачивание файла завершено")

def parser_HTML() :
    #Парсинг сайта МИРЭА с целью узнать четность недели
    s = requests.get('https://www.mirea.ru/')

    b = bs4.BeautifulSoup(s.text, "html.parser")
    data = b.select('.date_text')
    data_real = data[0].getText()


    data_real = str(data_real)
    #выделяем цифры и заносим их в список
    l = len(data_real)
    integ = []
    i = 0
    while i < l:
        data_real_int = ''
        a = data_real[i]
        while '0' <= a <= '9':
            data_real_int += a
            i += 1
            if i < l:
                a = data_real[i]
            else:
                break
        i += 1
        if data_real_int != '':
            integ.append(int(data_real_int))

    return integ

def input_vallues() :#Функия ввода значений и присвоение им нужного вида
    vallues=input("Введите ваше значение:")
    vallues=vallues.upper()
    vallues=vallues.strip()
    vallues="text:"+"'"+str(vallues)+"'"
    return vallues

def collumn_and_line(vallues) :#Поиск значений по xlsx файлу
    excel_data_file = xlrd.open_workbook(str(current_directory)+'/schedule.xlsx')
    worksheet = excel_data_file.sheet_by_index(0)
    for collumn in range(92):
        for line in range(153):
            name_cells=worksheet.cell(collumn,line)
            name_cells=str(name_cells)
            if name_cells==vallues:
                return collumn, line
                break
