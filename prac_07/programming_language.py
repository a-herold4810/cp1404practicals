"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
                f", Pointer Arithmetic={self.pointer_arithmetic}")

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def has_pointer_arithmetic(self):
        """ Determine if language supports pointer arithmetic """
        return self.pointer_arithmetic


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage(name="Ruby", typing="Dynamic", reflection=True, year=1995, pointer_arithmetic=False)
    python = ProgrammingLanguage(name="Python", typing="Dynamic", reflection=True, year=1991, pointer_arithmetic=False)
    visual_basic = ProgrammingLanguage(name="Visual Basic", typing="Static", reflection=False, year=1991,
                                       pointer_arithmetic=False)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
