import re
import os
import sys
from bs4 import BeautifulSoup, Tag

path = sys.argv[1]
save_path = sys.argv[2]
with open(path,'r') as f:
	data = f.read()
data = re.sub('Out\[\d+\]:','',data)
soup = BeautifulSoup(data, features="lxml")
# Change title
soup.title.string = "CS328 Writing Assignment"

# Insert link to style.css in head
style_link_tag = Tag(builder = soup.builder, name = "link", attrs={'rel': 'stylesheet', 'href': "style.css"})
soup.head.append(style_link_tag)

with open(save_path,'w') as f:
        f.write(str(soup.prettify()))