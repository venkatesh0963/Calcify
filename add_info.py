import os
import glob
from bs4 import BeautifulSoup

base = r'c:\Users\Venkatesh\OneDrive\Desktop\VENKATESH PJS\2) PLAYMOTIONS\calcify'

info_data = {
    'numerical': """
        <h2>About the Numerical Calculator</h2>
        <p>This is a standard calculator designed for everyday arithmetic. It follows the standard order of operations and handles floating-point math with precision, ensuring accurate results for shopping, homework, and quick financial tallies.</p>
        <h3>Calculation Rules</h3>
        <p>The calculator adheres to standard mathematical rules:</p>
        <ul>
            <li><strong>Addition (+)</strong>: Combines numbers.</li>
            <li><strong>Subtraction (−)</strong>: Finds the difference between values.</li>
            <li><strong>Multiplication (×)</strong>: Scales a value.</li>
            <li><strong>Division (÷)</strong>: Splits a value into equal parts (division by zero is undefined).</li>
            <li><strong>Percentages (%)</strong>: Calculates a fraction out of 100. (e.g., <code>50 %</code> converts to <code>0.5</code>).</li>
        </ul>
        <h3>Examples</h3>
        <p>To calculate a 15% tip on a $40 bill: Type <code>40 * 15 %</code> to get 6, then add it to 40 for a total of 46.</p>
    """,
    'currency': """
        <h2>Live Currency Converter</h2>
        <p>Our Currency Converter provides simulated live exchange rates to help you translate money values instantly. Whether you are traveling abroad, buying products internationally, or trading forex, knowing the exact conversion is vital.</p>
        <h3>How it works</h3>
        <p>The converter uses a base fiat value and applies a conversion multiplier:</p>
        <ul>
            <li><code>Result = Amount × (Target Rate / Source Rate)</code></li>
        </ul>
        <p>For example, if the USD base rate is 1.0, and the EUR rate is 0.92, converting 100 USD to EUR involves <code>100 × (0.92 / 1.0) = 92 EUR</code>.</p>
        <h3>Common Currency Codes</h3>
        <ul>
            <li><strong>USD</strong>: United States Dollar</li>
            <li><strong>EUR</strong>: Euro</li>
            <li><strong>GBP</strong>: British Pound Sterling</li>
            <li><strong>JPY</strong>: Japanese Yen</li>
            <li><strong>INR</strong>: Indian Rupee</li>
        </ul>
    """,
    'length': """
        <h2>Length & Distance Converter</h2>
        <p>Convert linear measurements seamlessly between metric and imperial units. This is incredibly useful for engineering, architecture, sports, and daily life.</p>
        <h3>Conversion Formulas</h3>
        <p>All length conversions are standardized against the base unit of 1 Meter (m):</p>
        <ul>
            <li><strong>Kilometer (km)</strong>: <code>1 m = 0.001 km</code></li>
            <li><strong>Centimeter (cm)</strong>: <code>1 m = 100 cm</code></li>
            <li><strong>Millimeter (mm)</strong>: <code>1 m = 1000 mm</code></li>
            <li><strong>Mile (mi)</strong>: <code>1 m ≈ 0.000621371 mi</code> (1 mile = 1.60934 km)</li>
            <li><strong>Yard (yd)</strong>: <code>1 m ≈ 1.09361 yd</code></li>
            <li><strong>Foot (ft)</strong>: <code>1 m ≈ 3.28084 ft</code></li>
            <li><strong>Inch (in)</strong>: <code>1 m ≈ 39.3701 in</code> (1 inch = 2.54 cm)</li>
        </ul>
        <h3>Fun Fact</h3>
        <p>The meter was originally defined in 1793 as one ten-millionth of the distance from the equator to the North Pole. Today, it is defined by the speed of light in a vacuum!</p>
    """,
    'mass': """
        <h2>Weight & Mass Converter</h2>
        <p>Translate weight and mass measurements between the metric (SI) and imperial systems. Essential for cooking, shipping, and scientific equations.</p>
        <h3>Conversion Formulas</h3>
        <p>Conversions are calculated against the base unit of 1 Kilogram (kg):</p>
        <ul>
            <li><strong>Gram (g)</strong>: <code>1 kg = 1000 g</code></li>
            <li><strong>Milligram (mg)</strong>: <code>1 kg = 1,000,000 mg</code></li>
            <li><strong>Metric Ton (t)</strong>: <code>1 kg = 0.001 t</code></li>
            <li><strong>Pound (lb)</strong>: <code>1 kg ≈ 2.20462 lbs</code> (1 lb = 0.453592 kg)</li>
            <li><strong>Ounce (oz)</strong>: <code>1 kg ≈ 35.274 oz</code> (1 lb = 16 oz)</li>
        </ul>
        <p>Note: While "mass" refers to the amount of matter in an object, "weight" refers to the force of gravity on that object. On Earth, they are commonly used interchangeably.</p>
    """,
    'area': """
        <h2>Area Converter</h2>
        <p>Calculate two-dimensional space. Perfect for real estate, farming, interior design, and geometry.</p>
        <h3>Conversion Formulas</h3>
        <p>Conversions are standard against 1 Square Meter (m²):</p>
        <ul>
            <li><strong>Square Kilometer (km²)</strong>: <code>1 m² = 0.000001 km²</code></li>
            <li><strong>Hectare (ha)</strong>: <code>1 m² = 0.0001 ha</code> (1 ha = 10,000 m²)</li>
            <li><strong>Acre (ac)</strong>: <code>1 m² ≈ 0.000247105 ac</code></li>
            <li><strong>Square Mile (mi²)</strong>: <code>1 m² ≈ 3.861e-7 mi²</code></li>
            <li><strong>Square Foot (ft²)</strong>: <code>1 m² ≈ 10.7639 ft²</code></li>
        </ul>
    """,
    'volume': """
        <h2>Volume & Liquid Converter</h2>
        <p>Measure three-dimensional space or liquid capacity. This calculator bridges the gap between metric volumes and US/Imperial fluid measurements.</p>
        <h3>Conversion Formulas</h3>
        <p>Conversions use 1 Liter (L) as the base unit:</p>
        <ul>
            <li><strong>Milliliter (mL)</strong>: <code>1 L = 1000 mL</code> (Equivalent to 1 cubic centimeter or cc)</li>
            <li><strong>Cubic Meter (m³)</strong>: <code>1 L = 0.001 m³</code></li>
            <li><strong>US Gallon (gal)</strong>: <code>1 L ≈ 0.264172 gal</code></li>
            <li><strong>US Quart (qt)</strong>: <code>1 L ≈ 1.05669 qt</code></li>
            <li><strong>US Fluid Ounce (fl oz)</strong>: <code>1 L ≈ 33.814 fl oz</code></li>
        </ul>
    """,
    'time': """
        <h2>Time Converter</h2>
        <p>Convert units of time dynamically. This is useful for project management, physics, and calculating durations.</p>
        <h3>Conversion Formulas</h3>
        <p>Based on 1 Second (s):</p>
        <ul>
            <li><strong>Minute (min)</strong>: <code>1 min = 60 seconds</code></li>
            <li><strong>Hour (hr)</strong>: <code>1 hr = 60 minutes = 3,600 seconds</code></li>
            <li><strong>Day (d)</strong>: <code>1 day = 24 hours = 86,400 seconds</code></li>
            <li><strong>Week (wk)</strong>: <code>1 week = 7 days = 604,800 seconds</code></li>
            <li><strong>Year (yr)</strong>: <code>1 year = 365 days = 31,536,000 seconds</code></li>
        </ul>
    """,
    'data': """
        <h2>Data Storage Converter</h2>
        <p>Translate digital storage sizes. Understand exactly how much space your files, games, or hard drives are consuming.</p>
        <h3>Conversion Formulas (Decimal Standard)</h3>
        <p>Modern storage manufacturers use the decimal (base 10) system, where calculations are relative to 1 Byte (B):</p>
        <ul>
            <li><strong>Kilobyte (KB)</strong>: <code>1 KB = 1000 Bytes</code></li>
            <li><strong>Megabyte (MB)</strong>: <code>1 MB = 1000 KB = 1,000,000 Bytes</code></li>
            <li><strong>Gigabyte (GB)</strong>: <code>1 GB = 1000 MB = 1,000,000,000 Bytes</code></li>
            <li><strong>Terabyte (TB)</strong>: <code>1 TB = 1000 GB = 1,000,000,000,000 Bytes</code></li>
        </ul>
        <p><em>Note: Operating systems like Windows often calculate using binary (base 2) units like Mebibytes (MiB, 1024 KiB), which is why a 1TB hard drive shows as ~931 GB in Windows!</em></p>
    """,
    'speed': """
        <h2>Speed Converter</h2>
        <p>Convert velocity rates between metric, imperial, and nautical systems. Perfect for physics problems, travel, and aviation.</p>
        <h3>Conversion Formulas</h3>
        <p>Conversions are based against 1 Meter per Second (m/s):</p>
        <ul>
            <li><strong>Kilometers per Hour (km/h)</strong>: <code>1 m/s = 3.6 km/h</code></li>
            <li><strong>Miles per Hour (mph)</strong>: <code>1 m/s ≈ 2.23694 mph</code></li>
            <li><strong>Knot (kn)</strong>: <code>1 m/s ≈ 1.94384 knots</code> (1 knot = 1 nautical mile per hour)</li>
        </ul>
    """,
    'temperature': """
        <h2>Temperature Converter</h2>
        <p>Convert heat and temperature scales. Because temperature scales have different starting points (zeroes), they require specific formulas rather than simple multiplication.</p>
        <h3>Calculation Formulas</h3>
        <ul>
            <li><strong>Celsius to Fahrenheit</strong>: <code>°F = (°C × 9/5) + 32</code></li>
            <li><strong>Fahrenheit to Celsius</strong>: <code>°C = (°F - 32) × 5/9</code></li>
            <li><strong>Celsius to Kelvin</strong>: <code>K = °C + 273.15</code></li>
            <li><strong>Kelvin to Celsius</strong>: <code>°C = K - 273.15</code></li>
        </ul>
        <h3>Absolute Zero</h3>
        <p>0 Kelvin (0 K) is Absolute Zero, the lowest theoretical temperature where all molecular movement stops. This is equal to -273.15 °C or -459.67 °F.</p>
    """,
    'finance': """
        <h2>Simple Interest Finance Calculator</h2>
        <p>Estimate the growth of your investments or the total cost of a loan over time using the simple interest model.</p>
        <h3>Calculation Formula</h3>
        <p>Simple interest is calculated only on the principal amount, unlike compound interest which calculates on accumulated interest.</p>
        <ul>
            <li><code>I = P × R × T</code></li>
        </ul>
        <p>Where:</p>
        <ul>
            <li><strong>P</strong> = Principal amount (initial investment or loan)</li>
            <li><strong>R</strong> = Annual interest rate (in decimal form, e.g., 5% = 0.05)</li>
            <li><strong>T</strong> = Time (in years)</li>
            <li><strong>Total Amount</strong> = <code>P + I</code></li>
        </ul>
        <p><strong>Example</strong>: $10,000 at 5% interest for 3 years generates $1,500 in interest, for a total of $11,500.</p>
    """,
    'discount': """
        <h2>Discount & Sale Price Calculator</h2>
        <p>Quickly determine how much you will save and the final price you'll pay during a sale.</p>
        <h3>Calculation Formula</h3>
        <p>The math behind a discount is straightforward:</p>
        <ul>
            <li><strong>Discount Amount</strong> = <code>Original Price × (Discount % / 100)</code></li>
            <li><strong>Final Price</strong> = <code>Original Price - Discount Amount</code></li>
        </ul>
        <p><strong>Example</strong>: A $150 jacket is 20% off.</p>
        <p>Discount = 150 × 0.20 = $30. Final Price = 150 - 30 = <strong>$120</strong>.</p>
    """,
    'gst': """
        <h2>GST & Sales Tax Calculator</h2>
        <p>Easily calculate the final price inclusive of tax, or extract the base amount before tax was applied. Useful for invoicing, accounting, and budgeting.</p>
        <h3>Calculation Formulas</h3>
        <p><strong>To Add Tax (Exclusive to Inclusive):</strong></p>
        <ul>
            <li><code>Final Price = Base Amount × (1 + (Tax % / 100))</code></li>
            <li>Example: $100 + 10% Tax = <code>100 × 1.10 = $110</code></li>
        </ul>
        <p><strong>To Remove Tax (Inclusive to Exclusive):</strong></p>
        <ul>
            <li><code>Base Amount = Total Price / (1 + (Tax % / 100))</code></li>
            <li>Example: $110 including 10% tax = <code>110 / 1.10 = $100</code></li>
        </ul>
        <p>Note: Removing tax is NOT the same as subtracting the tax percentage from the total!</p>
    """,
    'date': """
        <h2>Date Calculator</h2>
        <p>Find the exact duration between two dates. Useful for counting down to events, tracking project deadlines, or finding out exactly how old something is.</p>
        <h3>How it's calculated</h3>
        <p>The calculator takes the two calendar dates, converts them into digital timestamps (milliseconds since January 1, 1970, known as the Unix Epoch), and subtracts them.</p>
        <ul>
            <li><code>Difference in Milliseconds = Date 2 - Date 1</code></li>
            <li><code>Days = Milliseconds / (1000 × 60 × 60 × 24)</code></li>
        </ul>
        <p>This method automatically accounts for leap years and varying month lengths.</p>
    """,
    'bmi': """
        <h2>Body Mass Index (BMI) Calculator</h2>
        <p>BMI is a standardized metric used by medical professionals worldwide to categorize body weight relative to height. It acts as a general screening tool to identify potential weight problems for adults.</p>
        <h3>Calculation Formula</h3>
        <ul>
            <li><strong>Metric</strong>: <code>BMI = Weight(kg) / (Height(m))²</code></li>
            <li><strong>Imperial</strong>: <code>BMI = 703 × Weight(lbs) / (Height(in))²</code></li>
        </ul>
        <h3>Standard BMI Categories (WHO)</h3>
        <ul>
            <li><strong>Underweight</strong>: Less than 18.5</li>
            <li><strong>Normal weight</strong>: 18.5 – 24.9</li>
            <li><strong>Overweight</strong>: 25 – 29.9</li>
            <li><strong>Obese</strong>: 30 or greater</li>
        </ul>
        <p><em>Disclaimer: BMI does not measure body fat directly and does not account for muscle mass, bone density, or age. Athletes often have a high BMI due to muscle.</em></p>
    """
}

files = glob.glob(os.path.join(base, '*.html'))

for file in files:
    filename = os.path.basename(file)
    name = filename.replace('.html', '')
    
    if name not in info_data:
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    main = soup.find('main')
    
    if not main:
        continue
        
    # Check if info already exists
    if soup.find('div', class_='calc-info'):
        soup.find('div', class_='calc-info').decompose()
        
    info_div = BeautifulSoup(f'<div class="calc-info">{info_data[name]}</div>', 'html.parser')
    main.append(info_div)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print("Injected rich info into all 15 calculators!")
