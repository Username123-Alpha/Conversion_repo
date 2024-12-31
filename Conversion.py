#List holding the datas of numbers
Figure = {"0": "zero","1": "One","2": "Two","3": "Three","4": "four","5": "five","6": "six","7": "seven","8": "eight","9": "nine","10": "ten",
          "11": "eleven", "12": "twelve", "13": "thirteen","14": "fourteen","15": "fifteen","16": "sixteen","17": "seventeen","18": "eighteen",
          "19": "nineteen","20": "twenty",
          "Tens":{"1":"Ten","2":"Twenty","3":"Thirty","4":"Forty","5":"Fifty","6":"Sixty","7":"Seventy","8":"Eighty","9":"Ninety"},
          "Hundred":{"1":"One Hundred","2":"Two hundred","3":"Three hundred","4":"Four hundred","5":"Five hundred","6":"Six hundred",
                     "7":"Seven hundred","8":"Eight hundred","9":"Nine hundred"},
          "Thousand":{"1":"One thousand","2":"Two thousand", "3":"Three thousand","4":"Four thousand", "5":"Five thousand","6":"Six thousand",
                      "7":"Seven thousand", "8":"Eight thousand", "9":"Nine thousand"}
          }
# To take in the figures from the user
num = str(input("Enter the figure: \n"))
string_num = int(num)
Digit = len(num)
#Condition to handle unit. e.g. 1
if Digit == 1:
    print(Figure[f"{string_num}"])
#Condition to handle tens. e.g. 20
elif Digit == 2:
    first_tens = num[0]
    second_tens = num[1]
    if first_tens in Figure["Tens"]:
        print(Figure["Tens"][f"{first_tens}"] + "-" + Figure[f"{second_tens}"])
    else:
        print(Figure[f"{num}"])
#Condition to handle hundreds. e.g. 100
elif Digit == 3:
    first_tens = num[0]
    second_tens = num[1]
    third_tens = num[2]
    if second_tens == "0" and third_tens == "0":
        print(Figure["Hundred"][f"{first_tens}"])
    elif third_tens == "0":
        print(Figure["Hundred"][f"{first_tens}"] + " " "and" " " + Figure["Tens"][f"{second_tens}"])
    elif second_tens == "0":
        print(Figure["Hundred"][f"{first_tens}"] + " " "and" " " + Figure[f"{third_tens}"])
    else:
        print(Figure["Hundred"][f"{first_tens}"] + " " "and" " " + Figure["Tens"][f"{second_tens}"] + "-" + Figure[f"{third_tens}"])
#Condition to handle Thousands. e.g. 2000 (This can only handle up to nine thousand, nine hundred and ninety-nine)
elif Digit == 4:
        first_tens = num[0]
        second_tens = num[1]
        third_tens = num[2]
        fourth_tens = num[3]
        if second_tens == "0" and third_tens == "0" and fourth_tens == "0":
            print(Figure["Thousand"][f"{first_tens}"])
        elif third_tens == "0" and fourth_tens == "0":
            print(Figure["Thousand"][f"{first_tens}"] + " " + Figure["Hundred"][f"{second_tens}"])
        elif second_tens == "0" and third_tens == "0":
            print(Figure["Thousand"][f"{first_tens}"] + " " "and" " " + Figure[f"{fourth_tens}"])
        elif second_tens == "0":
            print(Figure["Thousand"][f"{first_tens}"] + " " "and" " " + Figure["Tens"][f"{third_tens}"] + "-" + Figure[f"{fourth_tens}"])
        elif fourth_tens == "0":
            print(Figure["Thousand"][f"{first_tens}"] + " " + Figure["Hundred"][f"{second_tens}"] + " " "and" " " + Figure["Tens"][f"{third_tens}"])
        else:
            print(Figure["Thousand"][f"{first_tens}"] + " "+ Figure["Hundred"][f"{second_tens}"] + " " "and" " " + Figure["Tens"][f"{third_tens}"] + "-" + Figure[f"{fourth_tens}"])