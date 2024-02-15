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
release_url="https://github.com/HttpAnimation/-EnLang/releases"
download_url=$(curl -s $release_url | grep -o -m 1 "https://github.com/HttpAnimation/-EnLang/releases/download/.*/BaseSystem.py")
wget $download_url

# Navigate back to the initial directory
cd ..

# Display completion message
echo "Done. You can rename the project by renaming the 'Project' folder and changing the name in About.json."
