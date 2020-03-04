num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

def number(num_to_word):
    if num_to_word > 1 and num_to_word <= 19:
        print(num2words1[num_to_word])
    else:
        print("Number Out Of Range")
        main()

def main():
    num = int(input("Please enter a number between 0 and 20: "))
    number(num)

main()