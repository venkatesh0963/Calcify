import os
import glob
from bs4 import BeautifulSoup

base = r'c:\Users\Venkatesh\OneDrive\Desktop\VENKATESH PJS\2) PLAYMOTIONS\calcify'

# SEO Data mapping
seo_data = {
    'calcify': {
        'title': 'Calcify | 15 Free Powerful Online Calculators in One Hub',
        'desc': 'Calcify is your ultimate free online calculation hub. Access 15 powerful tools including BMI, Currency, GST, Scientific, and Conversion calculators in one beautiful interface.',
        'keys': 'online calculators, free calculator, currency converter, bmi calculator, gst calculator, math tools'
    },
    'numerical': {
        'title': 'Free Standard & Scientific Calculator | Calcify',
        'desc': 'Perform everyday arithmetic or complex scientific calculations instantly with our free online numerical calculator.',
        'keys': 'scientific calculator, online calculator, math calculator, basic calculator, free calculator'
    },
    'currency': {
        'title': 'Live Currency Converter & Exchange Rates | Calcify',
        'desc': 'Convert USD, EUR, GBP, JPY, and other global currencies instantly with our free live currency converter.',
        'keys': 'currency converter, exchange rates, usd to eur, money converter, fx rates'
    },
    'length': {
        'title': 'Length & Distance Converter | Calcify',
        'desc': 'Convert between meters, kilometers, miles, inches, and feet instantly with our free length conversion tool.',
        'keys': 'length converter, distance converter, miles to km, inches to cm, measurement converter'
    },
    'mass': {
        'title': 'Weight & Mass Converter | Calcify',
        'desc': 'Easily convert between kilograms, pounds, ounces, and grams with our free online weight calculator.',
        'keys': 'weight converter, mass converter, kg to lbs, pounds to kilograms, weight calculator'
    },
    'area': {
        'title': 'Area Converter | Acres, Hectares, Sq Meters | Calcify',
        'desc': 'Convert area measurements instantly. Switch between acres, hectares, square meters, and square feet.',
        'keys': 'area converter, acres to hectares, square meters to square feet, land measurement'
    },
    'volume': {
        'title': 'Volume & Liquid Converter | Calcify',
        'desc': 'Convert between liters, gallons, milliliters, and cubic meters with our free volume conversion calculator.',
        'keys': 'volume converter, liters to gallons, liquid volume, ml to oz'
    },
    'time': {
        'title': 'Time Converter | Seconds, Minutes, Hours, Days | Calcify',
        'desc': 'Convert time units instantly. Calculate the exact conversion between seconds, minutes, hours, days, and years.',
        'keys': 'time converter, hours to minutes, days to hours, seconds to hours'
    },
    'data': {
        'title': 'Data Storage Converter | MB, GB, TB, PB | Calcify',
        'desc': 'Convert digital data storage units. Translate between Bytes, Kilobytes (KB), Megabytes (MB), Gigabytes (GB), and Terabytes (TB).',
        'keys': 'data converter, gb to tb, mb to kb, byte converter, digital storage'
    },
    'speed': {
        'title': 'Speed Converter | mph, km/h, m/s | Calcify',
        'desc': 'Convert velocity and speed measurements instantly. Switch between miles per hour, kilometers per hour, and meters per second.',
        'keys': 'speed converter, mph to kmh, meters per second, velocity calculator'
    },
    'temperature': {
        'title': 'Temperature Converter | Celsius, Fahrenheit, Kelvin | Calcify',
        'desc': 'Convert temperatures instantly between Celsius (°C), Fahrenheit (°F), and Kelvin (K) with our free tool.',
        'keys': 'temperature converter, celsius to fahrenheit, f to c, kelvin converter'
    },
    'finance': {
        'title': 'Simple Interest & Finance Calculator | Calcify',
        'desc': 'Calculate simple interest, principal amounts, and loan projections over time with our free finance tool.',
        'keys': 'interest calculator, simple interest, finance calculator, loan calculator'
    },
    'discount': {
        'title': 'Discount & Sale Price Calculator | Calcify',
        'desc': 'Find the final price after sales tax and discounts. Calculate exactly how much you will save instantly.',
        'keys': 'discount calculator, sale price, percent off calculator, shopping calculator'
    },
    'gst': {
        'title': 'GST & Tax Calculator | Add or Remove Tax | Calcify',
        'desc': 'Easily add or remove Goods and Services Tax (GST) or Sales Tax from any amount with our free online calculator.',
        'keys': 'gst calculator, tax calculator, add tax, remove tax, sales tax'
    },
    'date': {
        'title': 'Date Calculator | Days Between Dates | Calcify',
        'desc': 'Calculate the exact number of days between two dates. Find out how much time has passed or is remaining.',
        'keys': 'date calculator, days between dates, time duration, date difference'
    },
    'bmi': {
        'title': 'BMI Calculator | Body Mass Index Checker | Calcify',
        'desc': 'Check your Body Mass Index (BMI) instantly. Understand your health metrics based on your height and weight.',
        'keys': 'bmi calculator, body mass index, health calculator, ideal weight'
    }
}

files = glob.glob(os.path.join(base, '*.html'))

for file in files:
    filename = os.path.basename(file)
    name = filename.replace('.html', '')
    
    if name not in seo_data:
        continue
        
    data = seo_data[name]
    
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    head = soup.find('head')
    if not head:
        continue
        
    # Remove old title
    if head.find('title'):
        head.find('title').decompose()
        
    # Remove old meta descriptions/keywords/og if they exist to avoid duplicates
    for meta in head.find_all('meta'):
        if meta.get('name') in ['description', 'keywords']:
            meta.decompose()
        if meta.get('property') and meta.get('property').startswith('og:'):
            meta.decompose()
            
    # Inject new SEO tags
    new_tags = f"""
    <title>{data['title']}</title>
    <meta name="description" content="{data['desc']}">
    <meta name="keywords" content="{data['keys']}">
    <meta property="og:title" content="{data['title']}">
    <meta property="og:description" content="{data['desc']}">
    <meta property="og:type" content="website">
    <meta name="robots" content="index, follow">
    """
    
    new_soup = BeautifulSoup(new_tags, 'html.parser')
    head.append(new_soup)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print('SEO tags injected into all 16 pages!')
