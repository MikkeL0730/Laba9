#12. выполняет проверку на ровно одну нечетную цифру на четной позиции и палиндромичность числа, выводит числа, удовлетворяющие обоим условиям
class NumberChecker:
    def __init__(self, num):
        self.num = num

    def has_one_odd_digit_at_even_position(self):
        num_str = str(self.num)
        count_odd = 0
        for i in range(1, len(num_str), 2):
            if int(num_str[i]) % 2 != 0:
                count_odd += 1
        return count_odd == 1

    def is_palindrome(self):
        num_str = str(self.num)
        return num_str == num_str[::-1]

    def print_numbers_with_one_odd_digit_and_palindrome(n):
        for num in range(1, n + 1):
            checker = NumberChecker(num)
            if checker.has_one_odd_digit_at_even_position() and checker.is_palindrome():
                print(num)


n = int(input("Введите число n: "))
NumberChecker.print_numbers_with_one_odd_digit_and_palindrome(n)