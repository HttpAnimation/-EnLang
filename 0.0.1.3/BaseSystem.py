import subprocess
import webbrowser
import sys
import random
import string
import json
import os
import importlib.util

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
            "random.value": self.random_value,
            "pip": self.install_package,
            "pysnip": self.execute_python_snippet
        }

    def interpret(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip().startswith('//'):
                    continue
                tokens = line.strip().split(' ')
                if tokens[0] == "get":
                    if len(tokens) >= 2:
                        self.imported_commands.add(tokens[1])
                    else:
                        print("Invalid get statement:")
                else:
                    command = tokens.pop(0)
                    if command in self.imported_commands:
                        if command in self.commands:
                            # Check if the command contains a variable and substitute its value
                            command_with_vars = ' '.join(tokens)
                            for var, val in self.variables.items():
                                command_with_vars = command_with_vars.replace('+' + var, val)
                            self.commands[command](command_with_vars)
                        else:
                            print(f"Unknown command: {command}")
                    else:
                        print(f"Command not installed: {command}")

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
            print(f"Error running Python script make sure you have the python path: {e}")

    def ask_question(self, question):
        response = input(question + " ")
        self.variables['response'] = response

    def set_variable(self, assignment):
        variable, value = assignment.split("=")
        self.variables[variable.strip()] = value.strip()

    def random_value(self, length):
        value = ''.join(random.choices(string.ascii_letters + string.digits, k=int(length)))
        self.variables['random_value'] = value

    def install_package(self, package):
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', package], check=True)
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package}: {e}")

    def execute_python_snippet(self, snippet):
        script = """
// Python code here
{}
//""".format(snippet)
        try:
            exec(script, globals())
        except Exception as e:
            print(f"Error executing Python snippet: {e}")

if __name__ == "__main__":
    interpreter = EKGInterpreter()
    ekg_file = os.path.join("public", "main.ekg")
    about_file = "About.json"

    # Read data from About.json
    try:
        with open(about_file, 'r') as about_file:
            about_data = json.load(about_file)
            project_name = about_data[0]['Name']
            project_version = about_data[0]['Version']
    except Exception as e:
        print(f"Error reading About.json: {e}")
        sys.exit()

    print(f"Running {project_name} running with version {project_version}")

    # Interpret the EKG file
    interpreter.interpret(ekg_file)
