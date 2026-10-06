import os
import glob
base = r'c:\Users\Venkatesh\OneDrive\Desktop\VENKATESH PJS\2) PLAYMOTIONS\calcify\calculators'
files = glob.glob(os.path.join(base, '*.html'))
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace('href="../calcify.html#about"', 'href="../about.html"')
    content = content.replace('href="../calcify.html#contact"', 'href="../contact.html"')
    
    content = content.replace('<a href="../calcify.html">Privacy Policy</a>', '<a href="../privacy-policy.html">Privacy Policy</a>')
    content = content.replace('<a href="../calcify.html">Terms of Service</a>', '<a href="../terms-of-service.html">Terms of Service</a>')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Fixed footer links in calculators')
