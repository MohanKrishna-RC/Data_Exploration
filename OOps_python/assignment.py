class Football:
  final_res = "lose"
  def __init__(self, name, score):
    self.name = name
    self.score = score
    self.final_res = "lose"
  def calc(self, winning_score):
    if self.score > winning_score:
      self.final_res = "win"
      print(self.final_res)

match = Football("Juventus", 3)
match.calc(2)
print(match)
print(Football.final_res, match.final_res)

class NewClass:
    print("Hello World")
NewClass()
A = NewClass()
B = NewClass()
NewClass()

class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 1
    def __eq__(self, other):
        return self.x * self.y == other.x * other.y
obj1 = A(9, 8)
obj2 = A(8, 9)
print(obj1 == obj2)

class Batman:
  fn = "Ben"
  ln = "Affleck"

  def instance_method(self):
    self.fn = "Christian"
    self.ln = "Bale"
    print(self.fn, self.ln, end = " | ")

  @classmethod
  def class_method(cls):
    print(cls.fn, cls.ln, end = " | ")
    cls.fn = "Robert"
    cls.ln = "Pattinson"

  @staticmethod
  def static_method():
    print(Batman.fn, Batman.ln)

batman = Batman()
batman.instance_method()
Batman.class_method()
Batman.static_method()


def timeconv(a,b,c,d):
    # YOUR CODE GOES HERE
    class time:
        def __init__(self,h,m):
            self.hours=h
            self.mins=m
        def displaytime(self):
            print("{} hours and {} min".format(self.hours,self.mins))
        
        @classmethod
        def addtime(cls,t1,t2):
            # print(t1,t2)
            hours = (t1.displayminute()+t2.displayminute())//60
            mins = (t1.displayminute()+t2.displayminute())%60
            return cls(hours,mins)

        def displayminute(self):
            # print("{} min".format(self.hours*60+self.mins))
            return self.hours*60+self.mins
        
    t1=time(a,b)
    t2=time(c,d)
    # print(t1.displayminute(),t2.displayminute())
    t3=time.addtime(t1,t2)
    t3.displaytime()

class Animal:
    def __init__(self):
        print("Animal is Here")

    def sound(self):
        print("Animal Sounds")
        
# Define class Dog
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
    def sound(self):
        print("Dog Barks")    




# Define class Cat
class Cat(Animal):
    def __init__(self):
        pass

    def sound(self):
        print("Cat Meows")

def main():
    an = Animal()
    an.sound()
    dg = Dog()
    dg.sound()
    ct = Cat()
    ct.sound()