def no_return():
    # return 23
    pass;

def find_sum(a, b=10):
    return a+b;

var = no_return();

print(var);

print(find_sum(10.2, 23));
print(find_sum(10.2));
print(find_sum(a=10.2));



# dict ==> HashMap

my_dict = {
    "name": "gurpreet",
    "age":  19,
    "class": "asdgasd"
}

print(my_dict["class"])

# tuple ==> (immutable list)

my_tup = (10,20,30)

my_tup[0] = 20

