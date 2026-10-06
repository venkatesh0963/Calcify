import os
import glob
import shutil

base = r'c:\Users\Venkatesh\OneDrive\Desktop\VENKATESH PJS\2) PLAYMOTIONS\calcify'
calc_dir = os.path.join(base, 'calculators')
os.makedirs(calc_dir, exist_ok=True)

calcs = ['numerical', 'finance', 'currency', 'length', 'mass', 'area', 'volume', 'time', 'speed', 'data', 'temperature', 'discount', 'gst', 'date', 'bmi']

for calc in calcs:
    old_path = os.path.join(base, f'{calc}.html')
    new_path = os.path.join(calc_dir, f'{calc}.html')
    
    if not os.path.exists(old_path):
        continue
        
    with open(old_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    html = html.replace('href="style.css"', 'href="../style.css"')
    html = html.replace('src="script.js"', 'src="../script.js"')
    html = html.replace('href="calcify.html', 'href="../calcify.html')
    
    with open(new_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    os.remove(old_path)

# Update calcify.html
hub_path = os.path.join(base, 'calcify.html')
with open(hub_path, 'r', encoding='utf-8') as f:
    hub = f.read()

for calc in calcs:
    hub = hub.replace(f'href="{calc}.html"', f'href="calculators/{calc}.html"')

with open(hub_path, 'w', encoding='utf-8') as f:
    f.write(hub)

print('Moved to calculators folder!')
