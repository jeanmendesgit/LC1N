def header(title, spacing):
    print("=" * spacing)
    print("-" * spacing)
    print(" " * (((spacing - len(title)) // 2) - 1),title)
    print("-" * spacing)
    print(" ")
    return

def highlight(variable, spacing):
    print(" ")
    print("-" * spacing)
    print(f"{" " * ((spacing - len(variable)) // 2)}", variable)
    print("-" * spacing)
    return

def line(spacing):
    print(f"\n{"-" * spacing}\n")

def footer(spacing):
    print(" ")
    print("-" * spacing)
    print("=" * spacing)
    return " "