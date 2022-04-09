import re
import os
import sys
from bs4 import BeautifulSoup, Tag

path = sys.argv[1]
save_path = sys.argv[2]
with open(path, "r") as f:
    data = f.read()
data = re.sub("Out\[\d+\]:", "", data)
soup = BeautifulSoup(data, features="lxml")

# Change title
soup.title.string = "CS328 Writing Assignment"

# Insert Bootstrap CSS in head
bootstrap_btn_link_tag = Tag(
    builder=soup.builder,
    name="link",
    attrs={
        "rel": "stylesheet",
        "href": "bootstrap_only_btn.css",
    },
)
soup.head.append(bootstrap_btn_link_tag)

# Insert jQuery
jquery_script_tag = Tag(
    builder=soup.builder,
    name="script",
    attrs={
        "src": "https://code.jquery.com/jquery-3.2.1.slim.min.js",
        "integrity": "sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN",
        "crossorigin": "anonymous",
    },
)
soup.head.append(jquery_script_tag)

# Insert link to style.css in head
style_link_tag = Tag(
    builder=soup.builder, name="link", attrs={"rel": "stylesheet", "href": "style.css"}
)
soup.head.append(style_link_tag)

# Insert our custom js script
script_src_tag = Tag(builder=soup.builder, name="script", attrs={"src": "script.js"})
soup.head.append(script_src_tag)

with open(save_path, "w") as f:
    f.write(str(soup.prettify()))
