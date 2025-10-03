import os

def ls():
    print("Available files:")
    for f in os.listdir('files'):
        print(f)

def cat(filename):
    try:
        with open(os.path.join('files', filename), 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def whoami():
    import getpass
    print(f"Current user: {getpass.getuser()}")

def help_cmd():
    print('''Available commands:
  ls
  cat <filename>
  whoami
  clear
  help
  submit
  slack
  exit / quit''')

def main():
    while True:
        cmd = input('you@hackclub ~ % ')
        if cmd == 'ls':
            ls()
        elif cmd.startswith('cat '):
            cat(cmd.split(' ', 1)[1])
        elif cmd == 'whoami':
            whoami()
        elif cmd == 'clear':
            os.system('clear')
        elif cmd == 'help':
            help_cmd()
        elif cmd == 'submit':
            print('Opening submission form...')
        elif cmd == 'slack':
            print('Opening #terminal-craft channel...')
        elif cmd in ('exit','quit'):
            break
        else:
            print('Unknown command. Type help.')

if __name__ == '__main__':
    main()
