#подключаем нами записанные функции###########################
from Def_Parser import download,parser_HTML,input_vallues,collumn_and_line,current_directory
#xlrd библиотека для работы с Excel файлами################
import xlrd

#Функция для скачки нашего файла########################3
download()

#открываем наш файл с рассписанием и даем ее имя excel_da*####################
excel_data_file=xlrd.open_workbook(current_directory+'/schedule.xlsx')
#открываем первую страницу для нащего файла
worksheet = excel_data_file.sheet_by_index(0)

#Ввод группы####################################
print("Введите вашу группу")
gpoup=input_vallues()
fale,size_group=collumn_and_line(gpoup)

#Ввод для недели########################
print("Введите день недели")
week=input_vallues()
size_week,fale=collumn_and_line(week)

#функиця для выяснения номера недели#################3
fale,number_of_week=parser_HTML()

#Четность недели########################
parity=number_of_week%2
schedule=[]
if parity!=0 :
    size_week=size_week
elif parity==0 :
    size_week=size_week+1
######################################

#через цикл добавляем в список все нужные нам элементы попутно удаляя ненужные символы и знаки###########
for size_week in range(size_week,size_week+12,2):

    name_cells = worksheet.cell(size_week, size_group)
    schedule.append(str(name_cells).replace("empty:", "").replace("text:", "").replace(":", " ").replace("'", ""))



#Вывод самого рассписания с привоением номеру списка элемент списка
for i, value_list in enumerate(schedule, 1):
    if i==1 :
        print(str(i)+" пара(9:00-10:30) :", value_list)
    elif i==2 :
        print(str(i) + " пара(10:40-12:10):", value_list)
    elif i==3 :
        print(str(i) + " пара(13:00-14:30):", value_list)
    elif i==4 :
        print(str(i) + " пара(14:40-16:10):", value_list)
    elif i==5 :
        print(str(i) + " пара(16:20-17:50):", value_list)
    elif i==6 :
        print(str(i) + " пара(18:00-19:30):", value_list)
