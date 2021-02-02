import markdown

foot = '\n        </div>\n    </body>\n</html>'

for i in range (1, 5):
    markdown.markdownFromFile(
    input='0' + str(i) + 'BDL.md',
    output= 'stage.html',
    encoding='utf8',
    )
    with open('stage.html', 'r') as original: data = original.read()
    with open('template.html', 'r') as template: head = template.read()
    with open('0' + str(i) + 'BDL.html', "w") as modified: modified.write(head + data + foot)