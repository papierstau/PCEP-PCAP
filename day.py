class WeekDayError(Exception):
    pass
	

class Weeker:
    __days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        try:
            self.__dayIndex = Weeker.__days.index(day)
        except ValueError:
            raise WeekDayError
        except ImportError:
            raise WeekDayError
        except:
            raise WeekDayError
            
    def __str__(self):
        return Weeker.__days[self.__dayIndex]

    def add_days(self, n):
        self.__dayIndex = (n + self.__dayIndex) % 7
        

    def subtract_days(self, n):
        self.__dayIndex = (self.__dayIndex - n) % 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")