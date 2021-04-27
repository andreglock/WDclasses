import markdown
import os

foot = '        </div>\n    </div>\n\n        <!-- jQuery CDN - Slim version (=without AJAX) -->\n        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>\n        <!-- Popper.JS -->\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js" integrity="sha384-cs/chFZiN24E4KMATLdqdvsezGxaGsi4hLGOzlXwp5UZB1LY//20VyM2taTB4QvJ" crossorigin="anonymous"></script>\n        <!-- Bootstrap JS -->\n        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js" integrity="sha384-uefMccjFJAIv6A+rW+L4AHf99KvxDjWSu1z9VI8SKNVmz4sk7buKt/6v9KI65qnm" crossorigin="anonymous"></script>\n\n        <script type="text/javascript">\n            $(document).ready(function () {\n                $("#sidebarCollapse").on("click", function () {\n                    $("#sidebar").toggleClass("active");\n                    $(this).toggleClass("active");\n                });\n            });\n        </script>\n    </body>\n    </html>'

for i in range (36, 49):
    print(str('%02d' % (i)) + 'PB.md is input', end='    ')
    markdown.markdownFromFile(
    input = str('%02d' % (i)) + 'PB.md',
    output = 'stage.html',
    encoding = 'utf8',
    )
    with open('stage.html', 'r') as original: data = original.read()
    with open('templatePB.html', 'r') as template: head = template.read()
    with open(str("%02d" % (i)) + 'PB.html', 'w') as modified: modified.write(head + data + foot)
    print(str("%02d" % (i)) + 'PB.html' + ' made')

os.remove('stage.html')
print('stage.html removed')