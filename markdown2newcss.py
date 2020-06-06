import mistune
import fire
 

tmpl_begin = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="https://fonts.xz.style/serve/inter.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@exampledev/new.css@1/new.min.css">
</head>
<body>
"""

tmpl_end = """
</body>
</html>
"""


def ul_to_nav(txt):
    """
    Convert the following HTML
        <ul>
        <li><a href="http://google.com">google</a></li>
        <li><a href="https://github.com/">github</li>
        </ul>
    to
        <nav>
        <a href="http://google.com">google</a> /
        <a href="https://github.com/">github</a>
        </nav>
    """    
    out = txt.replace('<ul>', '<nav>')
    out = out.replace('</ul>', '</nav>')
    out = out.replace('<li>', '')
    n = out.count('</li>')
    out = out.replace('</li>', ' /', n-1)
    out = out.replace('</li>', '')
    return out



def run(body="body.md", nav="nav.md", out="index.html", title="index"):
    """
    Convert the markdown to html.
    
    Args:
        body (str): A path to the markdown file of body
        nav (str): A path to the markdown file of navigation
        out (str): A path to the output html file
        title (str): A title of the website
    """

    html = tmpl_begin.format(title=title)

    with open(nav, "rt") as f:
        html += '<header>\n'
        html += ul_to_nav(mistune.html(f.read()))
        html += '</header>\n'

    with open(body, "rt") as f:
        html += mistune.html(f.read())

    html += tmpl_end

    with open(out, "wt") as f:
        f.write(html)


if __name__ == "__main__":
    fire.Fire(run)