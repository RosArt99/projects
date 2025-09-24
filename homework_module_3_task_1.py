from datetime import datetime

def get_days_from_today(): #date was removed from function arguments. Incorporated in function instead.
    while True: #turning on loop
        try: 
            date = str(input("Enter the date in format \"YYYY-MM-DD\": ")) #\ to ignore "
            converted_time = datetime.strptime(date, "%Y-%m-%d").date() #place where ValueError occurs 
        except ValueError:
            print("Invalid time format, try again, please, use \"YYYY-MM-DD\" format.")
        else:
            today = datetime.today().date()
            days_ahead = (converted_time - today).days #days_ahead is timedelta object, .days is an attribute
            return days_ahead


print(get_days_from_today())

