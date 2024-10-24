def main(input: str):

    num_and_operation = input.split()


    if len(num_and_operation) != 3:
        return "throws Exception"


    try:

        a = int(num_and_operation[0])
        b = int(num_and_operation[2])



        if num_and_operation[1] == "+":
            result = a + b
        elif num_and_operation[1] == "-":
            result = a - b
        elif num_and_operation[1] == "*":
            result = a * b
        elif num_and_operation[1] == "/":
            result = a // b

        for a, b in num_and_operation:
            try:
                num = int(a, b)
                if not (1 <= num <= 10):
                    raise ValueError
            except ValueError:
                print("throws Exception")


        return str(result)
    except ValueError:
        return "throws Exception"
    except ZeroDivisionError:
        return "throws Exception"



while True:
    user_input = input("")
    result = main(user_input)


    print(result)
