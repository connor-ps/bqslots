def box_print(msg, indent=1, width=None, title=None):
    """
    Need I say more?
    :param msg:
    :param indent:
    :param width:
    :param title:
    :return:
    """
    lines = msg.split("\n")
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f"║{space}{title:<{width}}{space}║\n"  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += "".join([f"║{space}{line:<{width}}{space}║\n" for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)