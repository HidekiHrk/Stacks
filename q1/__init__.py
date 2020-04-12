from qutils import terminal
from q1.editor import Editor

WELCOME_MESSAGE = """Welcome to GenericEditor!
Commands:
# Erase last character | #l Erase a line | #l:{number} | @ Erase all | q! Exit
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=--=-=-
"""

def editorTicks(editor: Editor):
    terminated = False
    terminal_text = "1|"
    changed = False
    while not terminated:
        terminal.clear()
        if changed:
            terminal_text = editor.numeratedLines

        print(WELCOME_MESSAGE)
        if terminal_text:
            print(terminal_text)

        stdin = input()

        if stdin:
            changed = True
            if stdin == '#':
                editor.pull()
            elif stdin.startswith('#l'):
                lines = 1
                line = stdin.split(':')
                if len(line) > 1 and line[1].isdigit():
                    lines = int(line[1])
                for x in range(lines):
                    editor.remove('\n')
            elif stdin == '@':
                editor.remove()
            elif stdin == 'q!':
                terminated = True
            else:
                editor.read('\n' + stdin)
        
def main():
    editor = Editor()
    editorTicks(editor)