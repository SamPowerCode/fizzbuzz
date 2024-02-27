def fizzbuzz(num):
    output = ""
    if num % 3 == 0:
        output += "Three"
    if num % 5 == 0:
        output += "Five"
    if output == "":
        # this could also be 'output += str(num)' here to keep the variable as a string if required
        output = num
    return output

if __name__ == "__main__":
    for num in range(1, 101):
        print(fizzbuzz(num))
