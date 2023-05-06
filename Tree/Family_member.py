class Family_member():

    class_name = "Это член семьи"


class Father(Family_member):
    name = "Петр"
    age = 45
    height = 180
    hair_colour = "цвет волос русый"
    yes_colour = "цвет глаз голубой"


father = Father()
print(father.class_name,father.name,father.age,father.height,father.hair_colour,father.yes_colour)


class Mather(Family_member):
    name1 = "Мария"
    age1 = 45
    height1 = 165
    hair_colour1 = "цвет волос коричневый"
    eyes_colour1 = "цвет глаз зеленый"


mather = Mather()
print(mather.class_name,mather.name1,mather.age1,mather.height1,mather.hair_colour1,mather.eyes_colour1)


class Children(Mather,Father):
    def __init__(self, name, gender, relationDegree):
        self.name = name
        self.gender = gender
        self.relationDegree = relationDegree


    def getName(self):

        return self.name

    def getGender(self):
        return self.gender

    def getRelationDegree(self):
        return self.relationDegree



son = Children("Николай", "мальчик", "сын")
print(son.getName(),son.getGender(), son.getRelationDegree(), son.hair_colour, son.eyes_colour1)
daughter = Children("Татьяна", "девочка", "дочь")
print(daughter.getName(), daughter.getGender(), daughter.getRelationDegree(), daughter.hair_colour1, daughter.yes_colour)



