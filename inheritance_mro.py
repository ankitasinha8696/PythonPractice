class A:
    def show(self):
        print("Method from A")

class B(A):
    def show(self):
        super().show()  # Calls A's show()
        print("Method from B")

class C(A):
    def show(self):
        super().show()  # Calls A's show()
        print("Method from C")

class D(B, C):
    def show(self):
        super().show()  # Calls the next method in MRO
        print("Method from D")



def main():
    # Creating an object of D
    obj = D()
    obj.show()

if __name__ == "__main__":
    main()