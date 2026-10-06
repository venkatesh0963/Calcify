import os
import glob
from bs4 import BeautifulSoup
import re

base = r'c:\Users\Venkatesh\OneDrive\Desktop\VENKATESH PJS\2) PLAYMOTIONS\calcify'

related_map = {
    'numerical': ['finance', 'discount', 'gst'],
    'currency': ['finance', 'discount', 'gst'],
    'length': ['area', 'volume', 'mass'],
    'mass': ['volume', 'length', 'bmi'],
    'area': ['length', 'volume', 'speed'],
    'volume': ['area', 'mass', 'length'],
    'time': ['speed', 'date', 'numerical'],
    'data': ['numerical', 'speed', 'time'],
    'speed': ['time', 'length', 'numerical'],
    'temperature': ['mass', 'length', 'volume'],
    'finance': ['discount', 'gst', 'numerical'],
    'discount': ['gst', 'finance', 'numerical'],
    'gst': ['discount', 'finance', 'currency'],
    'date': ['time', 'numerical', 'finance'],
    'bmi': ['mass', 'length', 'volume']
}

icon_map = {
    'numerical': 'calculator', 'currency': 'coins', 'length': 'ruler',
    'mass': 'scale', 'area': 'maximize', 'volume': 'beaker',
    'time': 'timer', 'data': 'hard-drive', 'speed': 'gauge',
    'temperature': 'thermometer', 'finance': 'landmark',
    'discount': 'tag', 'gst': 'receipt', 'date': 'calendar', 'bmi': 'activity'
}

title_map = {
    'numerical': 'Numerical', 'currency': 'Currency', 'length': 'Length',
    'mass': 'Mass', 'area': 'Area', 'volume': 'Volume',
    'time': 'Time', 'data': 'Data Storage', 'speed': 'Speed',
    'temperature': 'Temperature', 'finance': 'Finance',
    'discount': 'Discount', 'gst': 'GST Calculator', 'date': 'Date', 'bmi': 'BMI'
}

# 1. Update HTML Files
files = glob.glob(os.path.join(base, '*.html'))
for file in files:
    filename = os.path.basename(file)
    name = filename.replace('.html', '')
    
    if name not in related_map:
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    # Inject History UI
    calc_box = soup.find('div', class_='calculator-box')
    if calc_box and not calc_box.find('div', class_='calc-history'):
        hist_html = '''
        <div class="calc-history" style="margin-top: 2rem; padding-top: 1.5rem; border-top: 2px dashed var(--border-color);">
            <h4 style="font-size: 1rem; color: var(--text-muted); margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between;">
                <span><i data-lucide="history" style="width: 16px; height: 16px; margin-right: 4px; vertical-align: text-bottom;"></i> Recent History</span>
                <button onclick="clearHistory()" style="background:none; border:none; color: #ef4444; cursor: pointer; font-size: 0.85rem;">Clear</button>
            </h4>
            <ul id="hist-list" style="list-style: none; padding: 0; margin: 0;"></ul>
        </div>
        '''
        calc_box.append(BeautifulSoup(hist_html, 'html.parser'))

    # Inject Related Cards
    main = soup.find('main', class_='calc-main-container')
    if main and not main.find('div', class_='related-section'):
        cards_html = ""
        for r_name in related_map[name]:
            r_title = title_map[r_name]
            r_icon = icon_map[r_name]
            cards_html += f'''
            <a href="{r_name}.html" class="bento-card" style="text-decoration: none; max-width: 250px; background: white;">
                <div class="card-icon" style="background: #f1f5f9; color: var(--primary-color);"><i data-lucide="{r_icon}"></i></div>
                <div class="card-content">
                    <h3 style="font-size: 1.1rem; color: var(--text-color); margin-bottom: 0.5rem;">{r_title}</h3>
                    <p style="font-size: 0.9rem; color: var(--text-muted);">Try this related calculator</p>
                </div>
            </a>
            '''
            
        related_wrapper = f'''
        <div class="related-section" style="width: 100%; max-width: 800px; margin-top: 1rem;">
            <h3 style="margin-bottom: 1.5rem; color: var(--text-color); font-size: 1.5rem;">Related Calculators</h3>
            <div style="display: flex; gap: 1.5rem; flex-wrap: wrap;">
                {cards_html}
            </div>
        </div>
        '''
        main.append(BeautifulSoup(related_wrapper, 'html.parser'))
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(str(soup))

# 2. Update script.js for History Logic
with open(os.path.join(base, 'script.js'), 'r', encoding='utf-8') as f:
    js = f.read()
    
history_js = """
// --- History System ---
function getCalcName() {
    let h3 = document.querySelector('.modal-header h3');
    if(!h3) return 'Unknown';
    let text = h3.innerText.trim();
    // For unit converters, their title gets dynamically set (e.g. "Currency", "Length").
    // We just return whatever text is in the header.
    return text;
}

function saveHistory(expr, result) {
    let calcName = getCalcName();
    let hist = JSON.parse(localStorage.getItem('calcify_history_' + calcName) || '[]');
    hist.unshift({ expr: expr, res: result });
    if(hist.length > 5) hist.pop();
    localStorage.setItem('calcify_history_' + calcName, JSON.stringify(hist));
    renderHistory();
}

function renderHistory() {
    const histList = document.getElementById('hist-list');
    if(!histList) return;
    let calcName = getCalcName();
    let hist = JSON.parse(localStorage.getItem('calcify_history_' + calcName) || '[]');
    if(hist.length === 0) {
        histList.innerHTML = '<li style="color: var(--text-muted); font-size: 0.9rem;">No history yet.</li>';
        return;
    }
    histList.innerHTML = hist.map(h => `<li style="display:flex; justify-content:space-between; border-bottom:1px solid var(--border-color); padding: 0.75rem 0; font-size: 0.95rem;">
        <span style="color: var(--text-muted); max-width: 60%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${h.expr}</span>
        <strong style="color: var(--primary-color)">${h.res}</strong>
    </li>`).join('');
}

function clearHistory() {
    let calcName = getCalcName();
    localStorage.removeItem('calcify_history_' + calcName);
    renderHistory();
}

document.addEventListener('DOMContentLoaded', () => {
    setTimeout(renderHistory, 100);
});
"""

if "function saveHistory" not in js:
    js = history_js + js

# Inject into functions safely
# stdEq
js = re.sub(r'(updateStd\(\);\s*})', r'\1\n                saveHistory(oldExp, result);', js)
js = js.replace('let result = eval(stdExp.replace(/%/g, \'/100\'));', 'let oldExp = stdExp;\n                let result = eval(stdExp.replace(/%/g, \'/100\'));')

# runConversion
js = re.sub(r'(res\.innerText = out;\s*})', r'\1\n            let unitF = document.getElementById("conv-from").options[document.getElementById("conv-from").selectedIndex].text;\n            let unitT = document.getElementById("conv-to").options[document.getElementById("conv-to").selectedIndex].text;\n            saveHistory(val + " " + unitF, out + " " + unitT);', js)

# Finance
js = re.sub(r'(document\.getElementById\(\'fin-res\'\)\.innerHTML = `[^`]+`;)', r'\1\n                saveHistory("P:$"+p+", R:"+r+"%, T:"+t+"y", "$"+(p+i).toFixed(2));', js)

# Discount
js = re.sub(r'(document\.getElementById\(\'disc-res\'\)\.innerHTML = `[^`]+`;)', r'\1\n                saveHistory("$"+p+" (-"+d+"%)", "Final: $"+fp);', js)

# GST
js = re.sub(r'(document\.getElementById\(\'gst-res\'\)\.innerHTML = `[^`]+`;)', r'\1\n                let op = m==="add"?"+":"-";\n                saveHistory("$"+a+" " + op + g+"%", "Final: $"+res);', js)

# Date
js = re.sub(r'(document\.getElementById\(\'date-res\'\)\.innerHTML = `.*?`;)', r'\1\n                saveHistory(d1.toLocaleDateString() + " → " + d2.toLocaleDateString(), diffDays + " Days");', js)

# BMI
js = re.sub(r'(document\.getElementById\(\'bmi-res\'\)\.innerHTML = `.*?`;)', r'\1\n                saveHistory(w + "kg / " + h + "cm", "BMI: " + bmi);', js)

# Temp
js = re.sub(r'(document\.getElementById\(\'temp-res\'\)\.innerHTML = `.*?`;)', r'\1\n            saveHistory(val + "°" + from.toUpperCase(), res + "°" + to.toUpperCase());', js)

with open(os.path.join(base, 'script.js'), 'w', encoding='utf-8') as f:
    f.write(js)
    
print("Added history and related cards!")
