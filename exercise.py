class Bottles(object):
    def verse(self, line):
        if line == 0:
            return ("No more bottles of beer on the wall, no more bottles of beer.\n"
                    "Go to the store and buy some more, 99 bottles of beer on the wall.")

        if line == 1:
            return ("1 bottle of beer on the wall, 1 bottle of beer.\n"
                    "Take it down and pass it around, no more bottles of beer on the wall.")

        if line == 2:
            return ("2 bottles of beer on the wall, 2 bottles of beer.\n"
                    "Take one down and pass it around, 1 bottle of beer on the wall.")


        return ("%s bottles of beer on the wall, %s bottles of beer.\n"
                "Take one down and pass it around, %s bottles of beer on the wall.") % (line, line, line - 1)

    def verses(self, *lines):
        start, end = lines

        required_lines = range(end, start + 1)
        reversed_required_lines = reversed(required_lines)

        verses = [self.verse(line) for line in reversed_required_lines]

        return '\n\n'.join(verses)

    def song(self):
        return self.verses(99,0)
