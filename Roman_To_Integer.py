
roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


class App():
    def __init__(self):
        self.total = 0

    def romanToInt(self, input: str) -> int:
        inputstring = list(input)
        inputstring.reverse()
        count = 0
        for str in inputstring:
            if (count > 0):
                if roman[inputstring[count - 1]] > roman[str]:
                    self.total -= roman[str]
                else:
                    self.total += roman[str]
            else:
                self.total += roman[str]

            count += 1

        return self.total


if __name__ == '__main__':
    app = App()
    app.romanToInt('MCMXCIV')
    print(app.total)
