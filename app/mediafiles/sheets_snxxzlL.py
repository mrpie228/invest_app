import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

DATE_COL_NUMBER = 2
MONTH = {1: 'январь', 2: 'февраль', 3: 'март',
         4: 'апрель', 5: 'май', 6: 'июнь',
         7: 'июль', 8: 'август', 9: 'сентябрь',
         10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}

today_day = datetime.today()
now_month = today_day.month

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("login.json", scope)
client = gspread.authorize(creds)

spreadsheet = client.open('Копия бюджетик 2020-2021')
sheet = spreadsheet.worksheet('расходы, сентябрь')
cols = sheet.col_values(DATE_COL_NUMBER)


def what_next_line(cols):
    next_line = len(cols) + 1
    return next_line


def get_last_comsumption():
    col_number = str(what_next_line(cols) - 1)


def create_consumption(date, price, desc, category):
    col_number = str(what_next_line(cols))
    sheet.update('B' + col_number, date)
    sheet.update('C' + col_number, price)
    sheet.update('D' + col_number, desc)
    sheet.update('E' + col_number, category)


