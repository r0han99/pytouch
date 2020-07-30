# The pytouch utility


![pytouch](https://user-images.githubusercontent.com/45916202/85221930-65782500-b3d5-11ea-9c67-5376a5d702d3.gif)


## Description
    This utility when executed will automatically fill the import statements required for a python file for your work, I wrote this scrip only because I was annoyed of writting the same import lines for multiple python files.This kind of scenario of creating multiple python files with same imports may come across during the learning curve of a particular ascpect of python. 

## Usage

```bash
    # pre-setting the imports in log file (like a local db)
    pytouch --set
```
##### Creating Python files with import statements

```bash
    
    pytouch --file greyscalefigure.py image+processing.py # Example files 
```
##### Creating Bashscripts with an Interpreter Preset.

```bash
    
    pytouch --bash bashscript0.sh bashscript1.sh 
```

## Installation 
##### Linux + MacOS

```bash
    cd Linux+Mac/
    bash setup.sh
```

##### Windows : use pytinstaller to convert the script into Binary/exe.

