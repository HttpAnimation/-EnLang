# Running system command
This part will go over how you can run a system command for the os you are coding for.

## Command
To run a commnad on the system you are gonna use the block *run.sys.command*.

## Importing
The way you can import the **run.sys.command** command is by making a new line and having a starting block for **run.sys.command** witch is the following **get** system command.

```ekg
get run.sys.command
```

## Sending data
To send the data over to the system you will use the commnad **run.sys.command** followed by the command you wanna send.

This expmale command just updates the system on Fedora based systems.
```ekg
get run.sys.command
run.sys.command sudo dnf update
```