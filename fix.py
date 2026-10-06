import os

base = r'c:\Users\Venkatesh\OneDrive\Desktop\VENKATESH PJS\2) PLAYMOTIONS\calcify'
with open(os.path.join(base, 'converter.html'), 'r', encoding='utf-8') as f:
    template = f.read()

types = {
    'currency': ('Currency', 'coins'),
    'length': ('Length', 'ruler'),
    'mass': ('Mass', 'scale'),
    'area': ('Area', 'maximize'),
    'volume': ('Volume', 'beaker'),
    'time': ('Time', 'timer'),
    'data': ('Data Storage', 'hard-drive'),
    'speed': ('Speed', 'gauge')
}

for t, info in types.items():
    name, icon = info
    html = template.replace('<title>Converter - Calcify</title>', f'<title>{name} - Calcify</title>')
    init_script = f"""
    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            if(typeof setupConverter === 'function') setupConverter('{t}');
            let h3 = document.querySelector('.modal-header h3');
            if (h3) h3.innerHTML = '<i data-lucide="{icon}"></i> {name}';
            if(typeof lucide !== 'undefined') lucide.createIcons();
        }});
    </script>
    """
    html = html.replace('</body>', init_script + '</body>')
    with open(os.path.join(base, f'{t}.html'), 'w', encoding='utf-8') as f:
        f.write(html)

os.remove(os.path.join(base, 'converter.html'))
print('Fixed converters!')
