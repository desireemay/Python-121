#Printers
class InkPrinter:
    def print_document(self):
        return "Printing using ink..."

class LaserPrinter:
    def print_document(self):
        return "Printing using laser..."

printers = [InkPrinter(), LaserPrinter()]
for p in printers:
    print(p.print_document())


#Duck Typing
def make_it_speak(obj):
    obj.speak()

class Bird:
    def speak(self):
        print("Tweettt tweet!")

class Robot:
    def speak(self):
        print("Beepppp!")

make_it_speak(Bird())
make_it_speak(Robot())
