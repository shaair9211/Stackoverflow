import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui

webbrowser.open('https://web.whatsapp.com/')
sleep(15)

workbook = openpyxl.load_workbook(r'C:\Users\shaai\PycharmProjects\pythonProject\Density_data_a.xlsx')
sheet = workbook['Sheet1']

for row in sheet.iter_rows(min_row=2):
    name = row[0].value
    phone = row[1].value
    message = row[2].value

    whatsapp_link = f'https://web.whatsapp.com/send?phone={phone}&text={quote(message)}'
    print(f'Opening link: {whatsapp_link}')
    webbrowser.open(whatsapp_link)
    sleep(20)


    try:
        arrow = pyautogui.locateCenterOnScreen('/home/cauademartin/PycharmProjects/controle/Scripts/seta.png', confidence=0.7)
        if arrow:
            print(f'Arrow located at: {arrow}')
            sleep(10)
            pyautogui.click(arrow[0], arrow[1])
            sleep(5)
        else:
            print('Arrow not found.')

    except Exception as e:
        print(f'Error locating or clicking on the arrow: {e}')

    input('Press Enter after sending the message...')