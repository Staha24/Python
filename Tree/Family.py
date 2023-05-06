class Family():
    x,y = 0,0

    def __init__(self,surname,live):
        self.surname = surname
        self.live = live



obj = Family("Член семьи Востриковых","Живет в Испании")
print(obj.surname, obj.live)
