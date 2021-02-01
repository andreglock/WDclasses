# BDL - Day 3

## More commands

Friends of cat

$ tail output.log # display the last lines of text in a file
$ tail -n 5 output.log  # display the last 5 lines of text in a file

Have a peek at a file

$ head # display the first lines of text in a file

## MarkdownMarkdown syntax Documentation: [Markdown Guide](https://www.markdownguide.org/basic-syntax)Super simple.
Is rendered.
Can be converted into HTML easily by renderers.
Halfway between visual and code.![Les Horribles Cernettes](./Les_Horribles_Cernettes_in_1992.jpeg "Les Horribles Cernettes say hello")Syntax examples- Images are done using this syntax: `![Image Text Version](relative/path/to/image.jpg "What the image is")`
- List
	- Sublist 1
		- SubSublist 1
		- SubSublist 2
	- Sublist 2
- Text effect: **Bold** text
- Text effect: __Bold__ text
- Text effect: *Italic* text
- Text effect: _Italic_ text
- Text effects combo: **_Both_ effects**
- Text effect: `Inline code blocks` like so!
- Linking to an address: `[Link Text Here](address here)`
- Headings
	- `# Level 1`
	- `## Level 2`
	- `### Level 3 ... up until level 6`
- Indented code blocks / preformatted text
- Block quotes
- Numbered lists:
	1. Example Banana
	1. Example Beet
	1. Example Cherry
	1. Example Potato
	1. Example CurryExample of a Code Block:	$ mkdir projects/newproject
	$ cd projects/newproject
	$ something_else_amazing> Albert Einstein once said,> "HTML Rocks"> Something

## Installing softwareMAC/OSX -- brew, cask (macports program)A few commands$ df -h # check how much space do I have lefts 
$ whoami
$ groups
$ sudo # do something as the "super user" or "root"Root has all permissions, can do anything to the system.
Avoid using sudo or the root user as much as possible. Use only when necessary.Package management systems: apt, snap, npm, brew, cask, yum, gem, emerge$ sudo apt update	# updates the list of things that I can install
$ sudo apt install	# actually installs something
$ sudo apt remove	# uninstall something
$ sudo apt search google chrome	# search for something to install
$ sudo apt autoremove # remove left over files from updating and installing$ sudo snap search opera
$ sudo snap install opera
$ sudo snap remove$ npm install -g "something" # node package manager installation
$ npm uninstall -g "something" $ which  # show information about a program
$ whereis # show program location## Browser BasicsBig browsers: Google Chrome, Safari, Internet Explorer, Edge, Mozilla Firefox
Small browsers: Opera, Brave, Vivaldi, eLinks, DuckDuck, Midori....Target browsers: Support latest version of chrome and EdgeBrowser = Browser Engine + JavaScript engine + other stuff too, such as plugins and tools
Browser Engine = HTML to visual rendering
JavaSript Engine = Runs JavascriptIf your site works with one Browser using the Blink engine, most likely other Blink engine Browsers will work too.
If your JS works with one browser that uses the V8 engine, it will most likely work with all of them.Shortcuts^T -- opens new tab
^N -- opens new window
^W -- closes a tab
^Shift-T -- reopens a closed tab
^Shift-N -- reopens a closed window
F11 -- view full screen
F12 -- open developer console -- the web developers best friend and toolkit