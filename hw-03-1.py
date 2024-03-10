from datetime import datetime

input_date = input("Введіть дату (РРРР-ММ-ДД): ")

def from_then_to_now(input_date):
    try:
        date_datetime = datetime.strptime(input_date, "%Y-%m-%d")

        now = datetime.today()
    
        difference = now - date_datetime
        days_difference = difference.days
        return days_difference
    except ValueError:
        print("Неправильний формат дати")

result = from_then_to_now(input_date)
print(result)



