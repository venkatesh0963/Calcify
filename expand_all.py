import os
import glob
from bs4 import BeautifulSoup

base = r'c:\Users\Venkatesh\OneDrive\Desktop\VENKATESH PJS\2) PLAYMOTIONS\calcify\calculators'

expanded_data = {
    'numerical': '''
        <h2>Comprehensive Numerical Calculator</h2>
        <p>The standard numerical calculator is the foundation of digital mathematics. Whether you are balancing a checkbook, completing algebra homework, or estimating grocery costs, our online calculator is designed to provide immediate, high-precision results without the need for physical hardware.</p>
        
        <h3>The Order of Operations (PEMDAS / BODMAS)</h3>
        <p>Unlike basic pocket calculators that execute math sequentially as you type it (where <code>2 + 3 × 4</code> equals 20), our calculator uses standard algebraic logic. It strictly follows the order of operations, ensuring that mathematical formulas are calculated correctly (where <code>2 + 3 × 4</code> correctly equals 14).</p>
        <ul>
            <li><strong>P / B:</strong> Parentheses / Brackets</li>
            <li><strong>E / O:</strong> Exponents / Orders</li>
            <li><strong>M & D:</strong> Multiplication & Division (left to right)</li>
            <li><strong>A & S:</strong> Addition & Subtraction (left to right)</li>
        </ul>
        
        <h3>Advanced Features & Edge Cases</h3>
        <p>Our numerical engine handles floating-point arithmetic with built-in precision correctors. In standard JavaScript, calculating <code>0.1 + 0.2</code> often returns a bizarre <code>0.30000000000000004</code> due to binary floating-point limitations. Our engine intercepts these edge cases and rounds them to the mathematically correct human-readable output.</p>
        
        <h3>Frequently Asked Questions</h3>
        <p><strong>Why do I get an error when dividing by zero?</strong><br>In standard arithmetic, division by zero is undefined. It is impossible to split an object into zero parts, so the calculator throws a protective Error rather than crashing.</p>
        <p><strong>How does the percentage (%) button work?</strong><br>The percentage button converts the preceding number into its decimal fraction equivalent. For example, typing <code>50 %</code> converts the value to <code>0.5</code>, which can then be multiplied by a base number.</p>
    ''',
    
    'finance': '''
        <h2>Simple Interest & Loan Finance Calculator</h2>
        <p>Understanding how interest works is the cornerstone of personal finance. Whether you are taking out a car loan, securing a mortgage, or depositing money into a high-yield savings account, knowing the exact cost of borrowing (or the reward for saving) is critical. Our Simple Interest Calculator gives you an immediate projection of your financial future.</p>
        
        <h3>The Simple Interest Formula</h3>
        <p>Simple interest is calculated exclusively on the original principal amount. It does not account for interest compounding over time. The formula is universal in accounting:</p>
        <ul>
            <li><code>Interest = Principal × Rate × Time (I = P × R × T)</code></li>
            <li><strong>Principal (P):</strong> The initial amount of money borrowed or invested.</li>
            <li><strong>Rate (R):</strong> The annual interest rate, converted to a decimal (e.g., 5% becomes 0.05).</li>
            <li><strong>Time (T):</strong> The duration the money is borrowed or invested, measured in years.</li>
        </ul>
        <p><em>Example:</em> You invest $10,000 at a 5% annual rate for 3 years. The interest generated is <code>10000 × 0.05 × 3 = $1,500</code>. Your total amount is $11,500.</p>
        
        <h3>Simple vs. Compound Interest</h3>
        <p>It is vital to understand the difference between simple and compound interest. <strong>Simple interest</strong> grows in a straight, linear line. <strong>Compound interest</strong> (which is used by most modern banks for savings accounts and credit cards) calculates interest on the principal <em>and</em> the accumulated interest, causing exponential growth.</p>
        
        <h3>Frequently Asked Questions</h3>
        <p><strong>Can I use this for my credit card debt?</strong><br>Generally, no. Credit cards use daily compound interest. Using a simple interest calculator will significantly underestimate how much credit card debt will cost you over time.</p>
        <p><strong>What if my time period is in months?</strong><br>You must convert months into a fraction of a year before inputting it. For 6 months, enter <code>0.5</code> years.</p>
    ''',

    'currency': '''
        <h2>Live Global Currency Converter</h2>
        <p>In an increasingly globalized economy, understanding foreign exchange (Forex) rates is essential. Whether you are an e-commerce business selling internationally, a tourist planning a vacation to Europe, or a day trader analyzing macroeconomics, our currency converter provides the accurate exchange ratios you need.</p>
        
        <h3>How Currency Exchange Rates Work</h3>
        <p>Currencies are always traded and priced in pairs (e.g., USD/EUR). The first currency is the <strong>Base</strong>, and the second is the <strong>Quote</strong>. If the USD/EUR rate is 0.92, it means 1 US Dollar can purchase 0.92 Euros.</p>
        <p>Conversion Formula: <code>Target Amount = Source Amount × (Target Rate / Source Rate)</code></p>
        
        <h3>Why Do Exchange Rates Fluctuate?</h3>
        <p>Fiat currency values are not static; they float freely on the open market and change every millisecond based on:</p>
        <ul>
            <li><strong>Interest Rates:</strong> Central banks (like the US Federal Reserve) raise rates to combat inflation. Higher rates attract foreign investment, increasing demand and value for that currency.</li>
            <li><strong>Economic Performance:</strong> High GDP growth, low unemployment, and stable trade balances strengthen a currency.</li>
            <li><strong>Geopolitics:</strong> Political instability or war can cause investors to flee a local currency for "safe haven" currencies like the US Dollar or Swiss Franc.</li>
        </ul>
        
        <h3>Frequently Asked Questions</h3>
        <p><strong>Are these rates exactly what my bank will charge?</strong><br>No. Our calculator provides the "mid-market" rate (the true rate banks use to trade with each other). Your personal bank or credit card will usually add a 1% to 3% markup or spread on top of this rate as their profit margin.</p>
    ''',

    'length': '''
        <h2>Length & Distance Conversion Tool</h2>
        <p>The world is split between two primary systems of measurement: the Metric System (used by 95% of the world) and the Imperial System (used primarily by the United States, Liberia, and Myanmar). Our length converter flawlessly translates distances between these two systems.</p>
        
        <h3>The History of Measurement Systems</h3>
        <p>The <strong>Metric System (SI)</strong> was developed during the French Revolution in the 1790s to replace a confusing web of local measurements. It is based entirely on powers of 10, making calculations incredibly simple (1 Kilometer = 1,000 Meters = 100,000 Centimeters).</p>
        <p>The <strong>Imperial System</strong> evolved from ancient Roman and British traditions, often based on the human body (a "foot" was literally the length of a king's foot). Conversions require memorization (1 Mile = 1,760 Yards = 5,280 Feet = 63,360 Inches).</p>
        
        <h3>Common Conversion Reference Table</h3>
        <ul>
            <li><strong>1 Inch</strong> = exactly 2.54 Centimeters</li>
            <li><strong>1 Foot</strong> = exactly 0.3048 Meters</li>
            <li><strong>1 Mile</strong> ≈ 1.609 Kilometers</li>
            <li><strong>1 Kilometer</strong> ≈ 0.621 Miles</li>
        </ul>
        
        <h3>Frequently Asked Questions</h3>
        <p><strong>Why is an inch exactly 2.54 cm?</strong><br>In 1959, the United States and Commonwealth nations signed the International Yard and Pound Agreement, mathematically redefining the inch to be exactly 25.4 millimeters to ensure industrial parts fit together globally.</p>
    ''',

    'mass': '''
        <h2>Weight & Mass Conversion Tool</h2>
        <p>Whether you are baking a recipe from a European cookbook, calculating shipping freight across the Atlantic, or configuring your weightlifting goals, converting between metric (Kilograms, Grams) and imperial (Pounds, Ounces) mass units is a daily necessity.</p>
        
        <h3>Mass vs. Weight: The Physics Difference</h3>
        <p>In everyday language, "mass" and "weight" are used interchangeably, but in physics, they are vastly different concepts:</p>
        <ul>
            <li><strong>Mass</strong> is the absolute amount of matter in an object. It never changes, regardless of where you are in the universe. It is measured in Kilograms.</li>
            <li><strong>Weight</strong> is the force exerted on an object by gravity (<code>Weight = Mass × Gravity</code>). It is technically measured in Newtons. An object with a mass of 10 kg will weigh much less on the Moon than on Earth, but its mass remains 10 kg.</li>
        </ul>
        
        <h3>Common Conversion Reference Table</h3>
        <ul>
            <li><strong>1 Kilogram (kg)</strong> ≈ 2.20462 Pounds (lbs)</li>
            <li><strong>1 Pound (lb)</strong> = exactly 453.592 Grams (g)</li>
            <li><strong>1 Ounce (oz)</strong> ≈ 28.3495 Grams (g)</li>
            <li><strong>1 Metric Ton (t)</strong> = 1,000 Kilograms</li>
        </ul>
        
        <h3>Frequently Asked Questions</h3>
        <p><strong>What is a "Stone"?</strong><br>A stone is a unit of weight used almost exclusively in the UK and Ireland for measuring human body weight. 1 Stone is exactly equal to 14 Pounds (approx. 6.35 kg).</p>
    ''',

    'area': '''
        <h2>Area & Land Measurement Converter</h2>
        <p>Calculating two-dimensional space is essential in real estate, architecture, farming, and interior design. Because area is squared (two-dimensional), conversions are exponential compared to standard length conversions, making mental math extremely difficult without a calculator.</p>
        
        <h3>How Area is Calculated</h3>
        <p>The area of a standard rectangle or square is found by multiplying its Length by its Width (<code>Area = L × W</code>). However, because you are multiplying the units together, the resulting unit is squared. This means that while there are 3 feet in a yard, there are <strong>9 square feet</strong> (3×3) in a square yard.</p>
        
        <h3>Common Area Units Explained</h3>
        <ul>
            <li><strong>Acre:</strong> Primarily used in the US and UK for land tracts. Originally defined in the Middle Ages as the amount of land a yoke of oxen could plow in one day. (1 Acre = 43,560 sq ft).</li>
            <li><strong>Hectare (ha):</strong> The metric standard for large land masses. (1 Hectare = 10,000 square meters, or approx. 2.47 Acres).</li>
            <li><strong>Square Meter (m²):</strong> The standard SI unit for everyday area measurement, such as room sizes or flooring.</li>
        </ul>
        
        <h3>Frequently Asked Questions</h3>
        <p><strong>Why are real estate sizes so confusing?</strong><br>Real estate spans different eras of measurement. A US property might list the lot size in Acres, but the house interior in Square Feet, requiring two different conversion paradigms.</p>
    ''',

    'volume': '''
        <h2>Volume & Liquid Capacity Converter</h2>
        <p>Volume measures three-dimensional space or liquid capacity. Converting volumes is notoriously complex because the Imperial system actually has different definitions for liquid vs. dry volume, and the US gallon is different from the UK gallon!</p>
        
        <h3>The Metric System (Liters & Cubic Meters)</h3>
        <p>The metric volume system is beautifully tied to its length system. One cubic centimeter (1 cm³) of water is exactly equal to 1 Milliliter (1 mL). A cube that is 10cm x 10cm x 10cm holds exactly 1 Liter. This flawless mathematical linking makes scientific calculations trivial.</p>
        
        <h3>The Gallon Problem (US vs Imperial)</h3>
        <p>If you are converting gallons, you must be careful:</p>
        <ul>
            <li><strong>US Liquid Gallon:</strong> Officially defined as 231 cubic inches (approx. 3.785 Liters).</li>
            <li><strong>UK/Imperial Gallon:</strong> Defined as the volume of 10 pounds of water at 62°F (approx. 4.546 Liters).</li>
        </ul>
        <p>Our calculator uses the globally dominant <strong>US Liquid Gallon</strong> standard by default.</p>
        
        <h3>Common Conversion Reference Table</h3>
        <ul>
            <li><strong>1 Liter</strong> = 1,000 Milliliters (mL)</li>
            <li><strong>1 US Gallon</strong> = 4 Quarts = 8 Pints = 128 US Fluid Ounces</li>
            <li><strong>1 US Fluid Ounce</strong> ≈ 29.57 Milliliters</li>
        </ul>
    ''',

    'time': '''
        <h2>Time & Duration Converter</h2>
        <p>Time is the only measurement system that successfully resisted decimalization. Rooted in ancient Babylonian base-60 mathematics, converting time requires jumping between base-60 (minutes/seconds), base-24 (hours), and base-365 (years), making a calculator indispensable for logistics, astronomy, and computing.</p>
        
        <h3>The Math of Time</h3>
        <ul>
            <li><strong>Minute:</strong> 60 Seconds</li>
            <li><strong>Hour:</strong> 60 Minutes (3,600 Seconds)</li>
            <li><strong>Day:</strong> 24 Hours (86,400 Seconds)</li>
            <li><strong>Year:</strong> 365 Days (31,536,000 Seconds)</li>
        </ul>
        
        <h3>What is Unix Epoch Time?</h3>
        <p>If you are a programmer, you deal with Unix Time. Instead of tracking months and years, computers simply count the total number of seconds that have elapsed since January 1, 1970, at 00:00:00 UTC. This single massive number (currently over 1.7 billion) allows computers to effortlessly calculate time differences without worrying about time zones or leap years.</p>
        
        <h3>Frequently Asked Questions</h3>
        <p><strong>Does this account for Leap Years?</strong><br>Standard time converters assume a flat 365-day year for generic conversions. If you need precise calendar math that accounts for leap years, use our dedicated "Date Difference" calculator instead.</p>
    ''',

    'speed': '''
        <h2>Speed & Velocity Converter</h2>
        <p>Speed measures how much distance an object covers over a specific duration of time (<code>Speed = Distance / Time</code>). Whether you are analyzing a car's speedometer, tracking a hurricane, or studying physics, our converter instantly translates velocity across land, sea, and scientific units.</p>
        
        <h3>Common Speed Measurements</h3>
        <ul>
            <li><strong>Miles Per Hour (mph):</strong> The standard road speed limit unit in the US, UK, and a few Caribbean nations.</li>
            <li><strong>Kilometers Per Hour (km/h):</strong> The global standard for automotive speed limits. (100 km/h ≈ 62 mph).</li>
            <li><strong>Meters Per Second (m/s):</strong> The standard SI unit used in physics and engineering.</li>
            <li><strong>Knots (kn):</strong> Used exclusively in aviation and maritime navigation. One knot equals one nautical mile per hour (approx. 1.15 mph). A nautical mile is based on the circumference of the Earth.</li>
        </ul>
        
        <h3>Fun Fact: Terminal Velocity</h3>
        <p>Terminal velocity is the maximum speed a falling object can reach before air resistance perfectly balances the force of gravity. For a human skydiver in a belly-to-earth freefall, terminal velocity is roughly 120 mph (193 km/h or 54 m/s).</p>
    ''',

    'data': '''
        <h2>Digital Data & Storage Size Converter</h2>
        <p>In the digital age, understanding file sizes and hard drive capacity is crucial. However, the data storage industry is notorious for a massive mathematical discrepancy that confuses millions of consumers regarding how much space their devices actually have.</p>
        
        <h3>The Base-10 vs. Base-2 Discrepancy</h3>
        <p>Data is stored in binary (Base-2), meaning computers count in powers of 2 (2, 4, 8, 16, 32... 1024). However, humans count in decimals (Base-10). This creates two conflicting systems:</p>
        <ul>
            <li><strong>Hard Drive Manufacturers (Decimal):</strong> Sell drives using Base-10. To them, 1 Kilobyte (KB) is exactly 1,000 Bytes. Therefore, a 1 Terabyte (TB) hard drive contains exactly 1,000,000,000,000 bytes.</li>
            <li><strong>Windows Operating Systems (Binary):</strong> Read drives using Base-2. To Windows, 1 Kilobyte (technically a Kibibyte or KiB) is 1,024 Bytes. Because 1024 is larger than 1000, the total number of "Gigabytes" Windows reports is smaller than what is on the box!</li>
        </ul>
        <p><strong>The Result:</strong> When you buy a 1 TB hard drive and plug it into a Windows PC, the PC divides the 1,000,000,000,000 bytes by 1024 three times, reporting the drive capacity as only <strong>931 GB</strong>!</p>
        
        <h3>Bits vs. Bytes</h3>
        <p>Internet speeds are sold in <strong>Megabits</strong> per second (Mbps), while files are measured in <strong>Megabytes</strong> (MB). There are 8 bits in a byte. If you have a 100 Mbps internet connection, your maximum download speed is actually 12.5 Megabytes per second!</p>
    ''',

    'temperature': '''
        <h2>Temperature Scale Converter</h2>
        <p>Converting temperatures is mathematically unique. Unlike converting length (where 0 meters equals 0 feet), temperature scales have different starting points (zeroes). This means you cannot simply multiply to convert them; you must use specific algebraic formulas to account for the offset.</p>
        
        <h3>The Three Primary Scales</h3>
        <ul>
            <li><strong>Fahrenheit (°F):</strong> Used primarily in the US. Water freezes at 32°F and boils at 212°F.</li>
            <li><strong>Celsius (°C):</strong> The global standard. It is perfectly tethered to water: it freezes at 0°C and boils at 100°C.</li>
            <li><strong>Kelvin (K):</strong> Used entirely by scientists. It uses the exact same degree increments as Celsius, but it moves the zero point down to "Absolute Zero".</li>
        </ul>
        
        <h3>What is Absolute Zero?</h3>
        <p>Absolute Zero (0 Kelvin) is the lowest theoretical temperature possible in the universe. At this temperature, all atomic and molecular movement completely halts. It is physically impossible to get colder. 0 Kelvin translates to -273.15 °C or -459.67 °F.</p>
        
        <h3>Frequently Asked Questions</h3>
        <p><strong>Is there a temperature where Celsius and Fahrenheit are exactly the same?</strong><br>Yes! Due to the way their formulas intersect, <strong>-40 °C is exactly equal to -40 °F</strong>.</p>
    ''',

    'discount': '''
        <h2>Discount & Retail Markdown Calculator</h2>
        <p>During massive sales events like Black Friday or Cyber Monday, calculating exactly how much you are saving (and what the final hit to your wallet will be) is essential for budgeting. Our discount calculator instantly handles the retail math for you.</p>
        
        <h3>How to Calculate a Discount Manually</h3>
        <p>If you don't have our calculator handy, the fastest way to calculate a discount mentally is to multiply the price by the remaining percentage you <em>have</em> to pay.</p>
        <p>If an $80 jacket is 20% off, that means you have to pay 80% of the price. Simply multiply <code>80 × 0.8 = 64</code>. The final price is $64.</p>
        
        <h3>The "Stacking Discounts" Illusion</h3>
        <p>Retailers often use manipulative marketing tactics by advertising "Take an extra 20% off already reduced 30% clearance items!". Human intuition assumes this means 50% off (30 + 20). <strong>This is mathematically false.</strong></p>
        <p>Discounts stack multiplicatively, not additively. The second discount only applies to the remaining balance of the first.</p>
        <ul>
            <li>Original Price: $100</li>
            <li>First 30% Off: Price drops to $70.</li>
            <li>Extra 20% Off: Applies to the $70, taking off $14.</li>
            <li>Final Price: $56.</li>
        </ul>
        <p>You received a total actual discount of 44%, not 50%!</p>
    ''',

    'date': '''
        <h2>Date Difference & Duration Calculator</h2>
        <p>Calculating the exact number of days between two calendar dates is incredibly tedious to do manually due to the varying lengths of months and the erratic injection of leap years. Our Date Calculator perfectly handles Gregorian calendar math to give you the exact duration.</p>
        
        <h3>The Gregorian Calendar & Leap Years</h3>
        <p>Introduced by Pope Gregory XIII in 1582, our current calendar is designed to keep us aligned with the Earth's revolutions around the Sun (which takes approximately 365.2425 days). To account for that decimal, we add an extra day (Feb 29) every 4 years.</p>
        <p>However, to prevent over-correcting, a year that is exactly divisible by 100 is <strong>not</strong> a leap year, <em>unless</em> it is also divisible by 400. (This is why the year 2000 was a leap year, but 1900 was not!). Our javascript calculator automatically factors in all of these centuries-old rules when computing your dates.</p>
        
        <h3>Common Uses for this Calculator</h3>
        <ul>
            <li><strong>Project Management:</strong> Finding the exact number of days remaining until a software launch or construction deadline.</li>
            <li><strong>Finance & Legal:</strong> Calculating interest maturation dates or the expiration of a 90-day contract clause.</li>
            <li><strong>Personal Milestones:</strong> Figuring out exactly how many days old you are, or counting down to a wedding or vacation.</li>
        </ul>
    '''
}

for calc, html_content in expanded_data.items():
    file_path = os.path.join(base, f'{calc}.html')
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    info = soup.find('div', class_='calc-info')
    if info:
        info.clear()
        info.append(BeautifulSoup(html_content, 'html.parser'))
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print("Expanded all 15 calculators!")
