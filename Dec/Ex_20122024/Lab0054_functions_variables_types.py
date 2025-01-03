public_toilet="PB"

def home():
    private_toilet="PT"
    print(public_toilet)

def stranger():
    print(public_toilet)
    # print(private_toilet) not able to use private variable in another function

print(public_toilet)
# print(private_toilet) not able to use outside also


