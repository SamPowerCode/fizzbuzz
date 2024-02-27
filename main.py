def fizzbuzz():
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output += "Three"
        if i % 5 == 0:
            output += "Five"
        if output == "":
            # this could also be 'output += str(i)' here to keep the variable as a string if required
            output = i
        print(output)

if __name__ == "__main__":
    fizzbuzz()
