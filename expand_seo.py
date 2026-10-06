import os
import glob
from bs4 import BeautifulSoup

base = r'c:\Users\Venkatesh\OneDrive\Desktop\VENKATESH PJS\2) PLAYMOTIONS\calcify'
calc_dir = os.path.join(base, 'calculators')

expanded_data = {
    'bmi': '''
        <h2>Body Mass Index (BMI) Calculator</h2>
        <p>The Body Mass Index (BMI) is a highly utilized, standardized metric adopted by medical professionals, health researchers, and fitness experts worldwide to categorize human body weight relative to their height. It acts as a primary general screening tool to identify potential weight problems for adults and serves as a fundamental benchmark in personal health tracking.</p>
        
        <h3>How BMI is Calculated (The Formula)</h3>
        <p>The math behind the BMI is straightforward, relying entirely on your height and weight. Our calculator handles both the Metric and Imperial systems automatically.</p>
        <ul>
            <li><strong>Metric Formula</strong>: <code>BMI = Weight in Kilograms / (Height in Meters)²</code></li>
            <li><strong>Imperial Formula</strong>: <code>BMI = 703 × Weight in Pounds / (Height in Inches)²</code></li>
        </ul>
        <p>For example, if you weigh 70 kg and are 1.75 meters tall, your BMI is calculated as <code>70 / (1.75 × 1.75) = 22.86</code>.</p>
        
        <h3>Standard BMI Categories (WHO Guidelines)</h3>
        <p>The World Health Organization (WHO) provides the following internationally recognized classifications:</p>
        <ul>
            <li><strong>Underweight (Below 18.5):</strong> Indicates a potential nutritional deficiency or underlying health issue. Consulting a nutritionist is advised.</li>
            <li><strong>Normal weight (18.5 – 24.9):</strong> The optimal weight range associated with the lowest risk of cardiovascular diseases.</li>
            <li><strong>Overweight (25.0 – 29.9):</strong> Indicates excess body weight. Lifestyle changes such as diet modification and exercise are typically recommended.</li>
            <li><strong>Obese (30.0 and above):</strong> Indicates a significant excess of body fat, which highly correlates with increased risks of diabetes, heart disease, and hypertension.</li>
        </ul>
        
        <h3>Limitations of the BMI</h3>
        <p>While BMI is a fantastic population-level screening tool, it has notable limitations on an individual basis. BMI <strong>does not measure body fat directly</strong>. It cannot distinguish between muscle mass, bone density, and fat. For example, professional bodybuilders often score in the "Obese" category because muscle is significantly denser and heavier than fat. Additionally, it does not account for age, gender, or fat distribution (e.g., visceral vs. subcutaneous fat).</p>
        
        <h3>Frequently Asked Questions</h3>
        <p><strong>Is BMI accurate for children?</strong><br>No. Children and teens use a different percentile-based BMI chart that compares their numbers against other children of the same age and sex.</p>
        <p><strong>Should I solely rely on my BMI?</strong><br>No. BMI should be viewed as one piece of the puzzle. You should also consider body fat percentage, waist circumference, blood pressure, and cholesterol levels for a complete health picture.</p>
    ''',
    
    'gst': '''
        <h2>Comprehensive GST & Sales Tax Calculator</h2>
        <p>Whether you are a small business owner issuing invoices, an accountant balancing the books, or a consumer trying to figure out the true cost of an item, our GST (Goods and Services Tax) calculator is the ultimate tool. It allows you to seamlessly add tax to a base amount or extract the hidden tax from a final inclusive price.</p>
        
        <h3>How Sales Tax & GST is Calculated (The Formulas)</h3>
        <p>Many people make the mathematical error of simply subtracting the tax percentage from the final price to find the base price. <strong>This is mathematically incorrect.</strong> Here are the proper formulas used by accountants:</p>
        
        <p><strong>To Add Tax (Exclusive to Inclusive):</strong></p>
        <p>When you have a base price and need to add the tax on top of it:</p>
        <ul>
            <li><code>Tax Amount = Base Price × (Tax Percentage / 100)</code></li>
            <li><code>Final Price = Base Price + Tax Amount</code></li>
            <li><em>Example:</em> A $200 item with 10% GST. <code>200 × 0.10 = $20</code>. The Final Price is <strong>$220</strong>.</li>
        </ul>
        
        <p><strong>To Remove Tax (Inclusive to Exclusive):</strong></p>
        <p>When you have the final receipt price and need to find out what the item cost before tax (reverse calculating):</p>
        <ul>
            <li><code>Base Price = Final Price / (1 + (Tax Percentage / 100))</code></li>
            <li><code>Tax Amount = Final Price - Base Price</code></li>
            <li><em>Example:</em> You paid $220 total, which includes 10% GST. <code>220 / 1.10 = $200</code>. The Base Price is <strong>$200</strong>, and the tax was $20.</li>
        </ul>
        
        <h3>Global Tax Systems Reference</h3>
        <ul>
            <li><strong>Australia/New Zealand:</strong> 10% to 15% standard GST applied to most goods and services.</li>
            <li><strong>Canada:</strong> Uses a mix of federal GST (5%) and provincial PST, sometimes combined into an HST (Harmonized Sales Tax) up to 15%.</li>
            <li><strong>Europe (VAT):</strong> Value Added Tax varies wildly by country, often ranging from 17% to 25%.</li>
            <li><strong>United States:</strong> Uses state and local Sales Tax (not a federal VAT/GST), ranging from 0% (e.g., Oregon) up to nearly 10% in some municipalities.</li>
        </ul>
        
        <h3>Frequently Asked Questions</h3>
        <p><strong>Why can't I just subtract 10% from the total to find the base price?</strong><br>Because the 10% tax was calculated based on the <em>smaller</em> base number, not the larger final number! 10% of 220 is 22, meaning 220 - 22 = 198 (which is incorrect, the base was 200).</p>
    '''
}

# Apply expansions to calculators in the new directory
files = glob.glob(os.path.join(calc_dir, '*.html'))

for file in files:
    name = os.path.basename(file).replace('.html', '')
    
    if name not in expanded_data:
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    info = soup.find('div', class_='calc-info')
    if info:
        info.clear()
        info.append(BeautifulSoup(expanded_data[name], 'html.parser'))
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(str(soup))

print('Expanded SEO text on core calculators!')
