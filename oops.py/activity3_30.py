#all about countries
class india():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is the most widely spoken language of India")
    def type(self):
        print("India is a developing country")

class russia():
    def capital(self):
        print("Moscow is the capital of Russia")
    def language(self):
        print("Russian is the most widely spoken language of Russia")
    def type(self):
        print("Russia is a developing country")

obj1= india()
obj2= russia()

for country in (obj1, obj2):
    country.capital()
    country.language()
    country.type()