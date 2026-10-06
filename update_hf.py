import os
import glob
from bs4 import BeautifulSoup

base = r'c:\Users\Venkatesh\OneDrive\Desktop\VENKATESH PJS\2) PLAYMOTIONS\calcify'
with open(os.path.join(base, 'calcify.html'), 'r', encoding='utf-8') as f:
    hub_soup = BeautifulSoup(f.read(), 'html.parser')

header_tag = hub_soup.find('header')
footer_tag = hub_soup.find('footer')

# Make links absolute to calcify.html
for a in header_tag.find_all('a'):
    href = a.get('href', '')
    if href.startswith('#'):
        a['href'] = 'calcify.html' + href
    if href == '#':
        a['href'] = 'calcify.html'

# Add 'Back to Hub' to header
nav = header_tag.find('nav', class_='nav-links')
if nav:
    nav.insert(0, BeautifulSoup('<a href="calcify.html" style="color: var(--primary-color);"><i data-lucide="arrow-left" style="width: 16px; height: 16px; margin-right: 4px; vertical-align: text-bottom;"></i> Hub</a>', 'html.parser'))

for a in footer_tag.find_all('a'):
    href = a.get('href', '')
    if href.startswith('#'):
        a['href'] = 'calcify.html' + href
    if href == '#':
        a['href'] = 'calcify.html'

# Find all calculator html files
files = glob.glob(os.path.join(base, '*.html'))
for file in files:
    if 'calcify.html' in file:
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    old_header = soup.find('header')
    if old_header:
        old_header.replace_with(BeautifulSoup(str(header_tag), 'html.parser'))
        
    old_footer = soup.find('footer')
    if old_footer:
        old_footer.replace_with(BeautifulSoup(str(footer_tag), 'html.parser'))
    else:
        # insert before script or at end of body
        main = soup.find('main')
        if main:
            main.insert_after(BeautifulSoup(str(footer_tag), 'html.parser'))
            
    with open(file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print('Updated headers and footers!')
