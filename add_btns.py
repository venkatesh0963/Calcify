import os
import glob
import re

base = r'c:\Users\Venkatesh\OneDrive\Desktop\VENKATESH PJS\2) PLAYMOTIONS\calcify'
files = glob.glob(os.path.join(base, '*.html'))

btn_html = '<button class="btn-use" style="width:100%; margin: 1.5rem 0; font-size: 1.1rem; border:none; cursor:pointer;" onclick="{fn}">Calculate</button>'

fn_map = {
    'finance': 'calcFin()',
    'discount': 'calcDisc()',
    'gst': 'calcGst()',
    'date': 'calcDateDiff()',
    'bmi': 'calcBmi()',
    'currency': 'runConversion()',
    'length': 'runConversion()',
    'mass': 'runConversion()',
    'area': 'runConversion()',
    'volume': 'runConversion()',
    'time': 'runConversion()',
    'data': 'runConversion()',
    'speed': 'runConversion()'
}

for file in files:
    name = os.path.basename(file).replace('.html', '')
    
    if name not in fn_map:
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Remove oninput and onchange
    html = re.sub(r'\s*oninput=\"[^\"]+\"', '', html)
    html = re.sub(r'\s*onchange=\"[^\"]+\"', '', html)
    
    if '>Calculate</button>' in html:
        continue
        
    fn = fn_map[name]
    button = btn_html.format(fn=fn)
    
    html = html.replace('<div class="calc-result"', button + '\n<div class="calc-result"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
        
print('Added calculate buttons to all forms!')
