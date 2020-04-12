from qutils import terminal
from q1.editor import Editor

WELCOME_MESSAGE = """Welcome to GenericEditor!
Commands:
# Erase last character | #l Erase a line | #l:{number} Erase multiple lines
@ Erase all | q! Exit | wq:{filename} Save and exit
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=--=-=-"""
error_message = ""

def editorTicks(editor: Editor):
    global error_message
    terminated = False
    terminal_text = editor.numeratedLines
    changed = False
    while not terminated:
        terminal.clear()
        if changed:
            terminal_text = editor.numeratedLines

        print(WELCOME_MESSAGE, error_message, sep='\n')
        print()
        if terminal_text:
            print(terminal_text)

        stdin = input(': ')

        if stdin:
            error_message = ""
            changed = True
            if stdin == '#':
                editor.pull()

            elif stdin.startswith('#l'):
                lines = 1
                line = stdin.split(':')
                if len(line) > 1 and line[1].isdigit():
                    lines = int(line[1])
                editor.removeLines(lines)

            elif stdin.startswith('wq:'):
                filename = stdin.split(':')[1]
                if filename:
                    try:
                        editor.save(filename)
                        terminated = True
                    except:
                        error_message = f"Nome de arquivo inválido: {filename}"
                else:
                    error_message = f"Você precisa colocar um nome para o arquivo!"

            elif stdin == '@':
                editor.remove()

            elif stdin == 'q!':
                terminated = True
                
            else:
                editor.read('\n' + stdin)
        
def main(args):
    filename = ''
    text = ''
    if args:
        filename = args[0]
        try:
            fp = open(filename, 'r')
            text = fp.read()
            fp.close()
        except:
            print(f'O nome de arquivo {filename} é inválido!')
            return
    editor = Editor(text)
    editorTicks(editor)