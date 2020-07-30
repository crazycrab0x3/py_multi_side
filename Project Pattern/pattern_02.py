class Pattern_Two:
    '''Pattern two

        1 1 1 1 1 1 1
        1 1 1 1 1 1
        1 1 1 1 1
        1 1 1 1
        1 1 1
        1 1
        1

    '''

    def __init__(self, strings='1', steps=10):
        self.steps = steps

        if isinstance(strings, str):
            self.strings = strings

        else:  # If provided 'strings' is integer then converting it to string
            self.strings = str(strings)

    def method_one(self):
        print('\nMethod One')

        for step in range(self.steps, 0, -1):
            print(' '.join(self.strings * step))

    def method_two(self):
        print('\nMethod Two')

        steps = self.steps

        while steps > 0:
            print(' '.join(self.strings * steps))
            steps -= 1


if __name__ == '__main__':
    pattern_two = Pattern_Two()

    pattern_two.method_one()
    pattern_two.method_two()
