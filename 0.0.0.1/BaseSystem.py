import subprocess
import webbrowser

class EKGInterpreter:
    def __init__(self):
        self.commands = {
            "say": self.say,
            "run.sys.command": self.run_sys_command,
            "open.browser": self.open_browser
        }

    def interpret(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                tokens = line.strip().split(' ')
                command = tokens.pop(0)
                if command in self.commands:
                    self.commands[command](' '.join(tokens))
                else:
                    print(f"Unknown command: {command}")

    def say(self, message):
        print(message)

    def run_sys_command(self, command):
        subprocess.run(command, shell=True)

    def open_browser(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    interpreter = EKGInterpreter()
    filename = input("Enter the filename to interpret: ")
    interpreter.interpret(filename)
