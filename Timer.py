class Timer:
    def __init__(self, hour, minutes, seconds):
        self.__hour = hour
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return stringFormatter(self.__hour) + ":" + stringFormatter(self.__minutes) + ":" + stringFormatter(self.__seconds)

    def next_second(self):
        self.__seconds += 1
        minutes = self.__seconds // 60
        self.__minutes += minutes
        hour = self.__minutes // 60
        self.__hour += hour
        self.__hour %= 24
        self.__minutes %= 60
        self.__seconds %= 60


    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0 :
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0 :
                self.__minutes = 59
                self.__hour -= 1
                if self.__hour < 0 :
                    self.__hour = 23

def stringFormatter(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)