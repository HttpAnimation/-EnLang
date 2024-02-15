import subprocess
import webbrowser
import sys
import random
import string

class EKGInterpreter:
    def __init__(self):
        self.imported_commands = set()
        self.variables = {}
        self.commands = {
            "say": self.say,
            "run.sys.command": self.run_sys_command,
            "open.browser": self.open_browser,
            "run.py.script": self.run_python_script,
            "ask.question": self.ask_question,
            "set.variable": self.set_variable,
            "random.value": self.random_value
        }

    def interpret(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                tokens = line.strip().split(' ')
                if tokens[0] == "get":
                    if len(tokens) >= 2:
                        self.imported_commands.add(tokens[1])
                    else:
                        print("Invalid import statement")
                else:
                    command = tokens.pop(0)
                    if command in self.imported_commands:
                        if command in self.commands:
                            self.commands[command](' '.join(tokens))
                        else:
                            print(f"Unknown command: {command}")
                    else:
                        print(f"Command not imported: {command}")

    def say(self, message):
        print(message)

    def run_sys_command(self, command):
        subprocess.run(command, shell=True)

    def open_browser(self, url):
        webbrowser.open(url)

    def run_python_script(self, script_name):
        try:
            exec(open(script_name).read(), globals())
        except Exception as e:
            print(f"Error running Python script: {e}")

    def ask_question(self, question):
        response = input(question + " ")
        self.variables['response'] = response

    def set_variable(self, assignment):
        variable, value = assignment.split("=")
        self.variables[variable.strip()] = value.strip()

    def random_value(self, length):
        value = ''.join(random.choices(string.ascii_letters + string.digits, k=int(length)))
        self.variables['random_value'] = value

if __name__ == "__main__":
    interpreter = EKGInterpreter()
    filename = input("Enter the filename to interpret: ")
    interpreter.interpret(filename)
