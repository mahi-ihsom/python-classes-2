class dog:
    def __init__(self, region, size):
        self.region= region
        self.size= size

class husky:
    def __init__(dog):
        region= "Cold"
        size= "big"

class chihuahua:
    def __init__(dog):
        region= "Mexico"
        size= "tiny"

obj1= husky()
obj2= chihuahua()

print("Huskies are very {1} dogs. They are found in {2}".f)