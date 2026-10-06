import os
import re

base = r'c:\Users\Venkatesh\OneDrive\Desktop\VENKATESH PJS\2) PLAYMOTIONS\calcify\calculators'

# Fix GST
with open(os.path.join(base, 'gst.html'), 'r', encoding='utf-8') as f:
    gst = f.read()
if '>Calculate</button>' not in gst:
    gst = gst.replace('oninput="calcGst()"', '')
    btn = '<button class="btn-use" onclick="calcGst()" style="width:100%; margin: 1.5rem 0; font-size: 1.1rem; border:none; cursor:pointer;">Calculate</button>\n<div style="display:flex; gap:10px; margin-top:1.5rem;">'
    gst = gst.replace('<div style="display:flex; gap:10px; margin-top:1.5rem;">', btn)
    with open(os.path.join(base, 'gst.html'), 'w', encoding='utf-8') as f:
        f.write(gst)

# Fix Temperature
with open(os.path.join(base, 'temperature.html'), 'r', encoding='utf-8') as f:
    temp = f.read()
if '>Calculate</button>' not in temp:
    temp = temp.replace('oninput="convTemp(\'C\')"', 'oninput="window.lastTemp=\'C\'"')
    temp = temp.replace('oninput="convTemp(\'F\')"', 'oninput="window.lastTemp=\'F\'"')
    temp = temp.replace('oninput="convTemp(\'K\')"', 'oninput="window.lastTemp=\'K\'"')
    
    btn = '<button class="btn-use" onclick="if(window.lastTemp) convTemp(window.lastTemp); else convTemp(\'C\');" style="width:100%; margin: 1.5rem 0; font-size: 1.1rem; border:none; cursor:pointer;">Calculate</button>\n</div>\n<div class="calc-history"'
    temp = temp.replace('</div>\n<div class="calc-history"', btn)
    with open(os.path.join(base, 'temperature.html'), 'w', encoding='utf-8') as f:
        f.write(temp)

print('Added missing buttons to GST and Temperature!')
