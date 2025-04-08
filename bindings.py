from tkinter import Text


def OnKey(textBox: Text, postfix: str) -> str:
    current = textBox.index('insert')
    if textBox.compare(current, "<", postfix):
        return "break"


def OnBack(textBox: Text, postfix: str) -> str:
    current = textBox.index('insert')
    if textBox.compare(current, "<=", postfix):
        return "break"


def OnReturn(textBox: Text, prefix: str, extra: str = "") -> str:
    textBox.insert("end", extra + prefix)
    return textBox.index("insert")
