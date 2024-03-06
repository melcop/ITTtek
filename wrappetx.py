import textwrap

text = "Python is useful, but C is powerful, maybe"

# Wrap teksten to en specifik bredde
wrapped_text = textwrap.wrap(text, width = 12)

# Print wrap tekst ud
for line in wrapped_text:
    print(line)