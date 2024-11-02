"""
Languages
Estimate: 30 minutes
Start Time: 1255
Actual: 32 minutes
Finish Time: 1327
"""

from programming_language import ProgrammingLanguage

# Sample instances for testing
def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)
    print(ruby)
    print(visual_basic)

    languages = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

main()
