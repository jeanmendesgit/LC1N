def header(title, spacing):
    print("=" * spacing)
    print("-" * spacing)
    print(" " * (((spacing - len(title)) // 2) - 1),title)
    print("-" * spacing)
    print(" ")
    return

def footer(spacing):
    print(" ")
    print("-" * spacing)
    print("=" * spacing)
    return " "