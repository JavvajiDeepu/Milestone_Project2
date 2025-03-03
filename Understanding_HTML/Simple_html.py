from bs4 import BeautifulSoup
SIMPLE_HTML ='''<html>
<head></head>
<body>
<h1> This is a title </h1>
<p> class="subtitle"> lorem ipsum dolor sit amet. consectetur adipiscing elit. </p>
<p>Here's another p with out a class</p>
<u1>
    <li>max</li>
    <li>john</li>   
    <li>jose</li>
</u1>
</body>
</html>
'''
simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)
def find_list_items():
    list_items = simple_soup.find_all('li')
    list_contents = [item.string for item in list_items]
    print(list_contents)

def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph)

def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p.string for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragraph)


find_title()
find_list_items()
find_subtitle()
find_other_paragraph()