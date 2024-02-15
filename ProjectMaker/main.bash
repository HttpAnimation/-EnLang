#!/bin/bash

# Create project directory and navigate into it
mkdir -p Project
cd Project

# Download About.json
wget https://raw.githubusercontent.com/HttpAnimation/-EnLang/main/ProjectMaker/About.json

# Create public directory and navigate into it
mkdir -p public
cd public

# Download main.ekg
wget https://raw.githubusercontent.com/HttpAnimation/-EnLang/main/ProjectMaker/main.ekg

# Navigate back to the Project directory
cd ..

# Download BaseSystem.py
wget https://github.com/HttpAnimation/-EnLang/releases/download/0.0.0.9/BaseSystem.py

# Navigate back to the initial directory
cd ..

# Display completion message
echo "Done. You can rename the project by renaming the 'Project' folder and changing the name in About.json."
