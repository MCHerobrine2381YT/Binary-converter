class Binary:
    def __init__(self, run):
        self.run = bin(run)
    
    def convert_binary(self):
        print("Binary code: {}".format(self.run))

code = Binary(int(input("Convert to binary: ")))
code.convert_binary()
