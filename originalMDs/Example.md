# Tasks 01 BDL Day 4 Maxie

## Commands used so far (not complete)

      $ cat # print text in text files
      $ ls # list files and folders
      $ ls -lha # list with more info on the        files, all hidden files, and with human        readable files sizes
      $ ls -R # list files and folders, also        subfolders (recursively)
      $ history # all commands used in that         bash window in order
      $ cd # change folder 
      $ cd Documents/ # go to folder Documents      (relative path)
      $ touch newfile.md # create empty .md         file called newfile in current directory
      $ nano newfile.md # open newfile.md with      in-built text editor in Terminal
      $ mdir test # create folder called test
      $ mkdir -p test2/test 3 # create parent       folder test2 and child folder test 3
      $ mkdir Documents/test4/test5 # create        folder test5 in location given as      relative path
      $ cp deletme deleteme # create a copy of      deletme in the same directory and name it        deleteme
      $ mv deletme /tmp/deleteme # move folder      deletme from current directory and move      it to the folder tmp in root and rename      it deleteme
      $ rm emptyfile # delete emptyfile from        current directory
      $ rm -r deletme # delete folder deletme       and everything in it from current         directory
      $ code --help # get instructions for the      code command

## General tips for using terminal

- [Commands cheat sheet](https://cheatography.com/davechild/cheat-sheets/linux-command-line/)
- use `Tab` key to autocomplete
- be very careful with any `$ rm -r` or especially `$ rm -rf`!!
- use `^C`to quit processes
- `M-U` means `Alt` key and `U` key are pressed
- `$ brew` is the command to do installing with the terminal on Mac (program **Homebrew**)
- use `up arrow` key to display last command and navigate through command history
  - ~ short for home
  - / short for root
  - . current directory
  - .. directory one level up

## Whole history of commands used in that one window of my bash 

  $ ls #comment for history
  $ history
  $ cd Documents/
  $ ls
  $ mkdir test
  $ ls
  $ mkdir -p test2/test3
  $ ls
  $ cd
  $ mkdir /Documents/test4/test5
  $ cd Documents/
  $ ls
  $ cd
  $ ls
  $ code --help
  $ slack
  $ cd Do
  $ cd Do
  $ cd Doc
  $ cd Documents/
  $ ls
  $ rmdir test
  $ ls
  $ rmdir test2