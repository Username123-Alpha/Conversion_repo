def number_to_words(n):
    """
    Convert a number into words.
    Args:
        n (int): The number to convert.
    Returns:
        str: The number in words.
    """
    if n == 0:
        return "zero"
    def ones_and_tens(num):
        ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                 "nineteen"]
        tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        if 1 <= num < 10:
            return ones[num]
        elif 11 <= num <= 19:
            return teens[num - 10]
        elif 10 <= num < 100:
            return tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else "")
        else:
            return ""
    def convert_chunk(num):
        """Convert a number less than 1000 into words."""
        ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        if num < 100:
            return ones_and_tens(num)
        else:
            return ones[num // 100] + " hundred" + (" and " + ones_and_tens(num % 100) if num % 100 != 0 else "")
    chunks = []
    chunk_names = ["", "thousand", "million", "billion", "trillion"]
    num = abs(n)
    i = 0
    while num > 0:
        chunk = num % 1000
        if chunk > 0:
            chunks.append((convert_chunk(chunk), chunk_names[i]))
        num //= 1000
        i += 1
    words = []
    for chunk, name in reversed(chunks):
        words.append(chunk + (" " + name if name else ""))
    result = " ".join(words)
    if n < 0:
        result = "negative " + result
    return result
# Input from user
number = int(input("Enter a number: "))
print(f" {number_to_words(number)}")