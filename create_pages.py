import os
from bs4 import BeautifulSoup

base = r'c:\Users\Venkatesh\OneDrive\Desktop\VENKATESH PJS\2) PLAYMOTIONS\calcify'
hub_path = os.path.join(base, 'calcify.html')

with open(hub_path, 'r', encoding='utf-8') as f:
    hub = BeautifulSoup(f.read(), 'html.parser')

header_str = str(hub.find('header'))
footer_str = str(hub.find('footer'))

# Pages Content
pages = {
    'privacy-policy': {
        'title': 'Privacy Policy | Calcify',
        'h1': 'Privacy Policy',
        'content': '''
        <p>At Calcify, we take your privacy very seriously. This Privacy Policy explains how we collect, use, and protect your information when you use our calculators.</p>
        
        <h3>1. Data Collection and Usage</h3>
        <p><strong>Zero Server-Side Storage:</strong> Calcify is designed as a client-side web application. All calculations you perform (whether financial, health-related, or mathematical) are processed locally within your own browser. We do <strong>not</strong> transmit, collect, or store any of your inputted numbers, dates, or personal metrics on our servers.</p>
        
        <h3>2. Local Storage (Cookies & Cache)</h3>
        <p>We use your browser's native Local Storage feature to save your "Recent History" (the last 5 calculations made on a specific tool). This data never leaves your device and is used strictly to enhance your user experience. You can clear this history at any time using the "Clear" button provided on each calculator.</p>
        
        <h3>3. Third-Party Analytics and Advertising</h3>
        <p>To keep Calcify free, we may use standard third-party analytics (like Google Analytics) to understand aggregated traffic patterns (e.g., which calculators are most popular) and automated ad networks (like Google AdSense). These third-party vendors may use cookies to serve ads based on your prior visits to this website or other websites.</p>
        
        <h3>4. Changes to This Policy</h3>
        <p>We may update this Privacy Policy from time to time. Any changes will be posted directly on this page.</p>
        '''
    },
    'terms-of-service': {
        'title': 'Terms of Service & Disclaimer | Calcify',
        'h1': 'Terms of Service',
        'content': '''
        <p>By accessing and using Calcify, you accept and agree to be bound by the terms and provisions of this agreement.</p>
        
        <h3>1. Accuracy of Information (Disclaimer)</h3>
        <p>Calcify provides mathematical, financial, and health-related calculation tools for <strong>informational and educational purposes only</strong>.</p>
        <ul>
            <li><strong>Financial Calculators:</strong> Tools such as the Finance, GST, and Discount calculators provide estimates based on the exact numbers you input. They do not constitute certified financial or tax advice. Always consult a certified accountant or financial advisor for official tax filing or investment planning.</li>
            <li><strong>Health Calculators:</strong> The BMI (Body Mass Index) calculator is based on standard World Health Organization (WHO) formulas. It is a general screening tool and does not diagnose body fatness or the health of an individual. Do not use this tool as a substitute for professional medical advice, diagnosis, or treatment.</li>
            <li><strong>Currency Converter:</strong> Currency exchange rates fluctuate constantly. The rates provided by our tool may be simulated or delayed and should not be relied upon for actual trading or international financial transactions.</li>
        </ul>
        
        <h3>2. Limitation of Liability</h3>
        <p>In no event shall Calcify or its developers be liable for any direct, indirect, incidental, consequential, or special damages arising out of or in any way connected with the use of our calculators or the information they provide.</p>
        
        <h3>3. Intellectual Property</h3>
        <p>All content, designs, grids, and original code on this website are the property of Calcify and may not be reproduced without permission.</p>
        '''
    },
    'about': {
        'title': 'About Us | Calcify',
        'h1': 'About Calcify',
        'content': '''
        <p>Calcify was born out of a simple frustration: everyday math shouldn't require jumping between ten different messy apps or ad-filled websites.</p>
        
        <h3>Our Mission</h3>
        <p>Our mission is to provide a single, unified hub where you can perform any calculation you need—whether you are figuring out a 20% discount at a store, projecting a 5-year loan, or checking your BMI.</p>
        <p>We believe that utility software should be lightning-fast, respect your privacy, and look absolutely beautiful. That's why we designed Calcify using a clean "Bento-grid" interface, premium typography, and client-side processing that ensures your numbers stay on your device.</p>
        
        <h3>Why Choose Us?</h3>
        <ul>
            <li><strong>All-in-One:</strong> 15 powerful calculators seamlessly integrated into one platform.</li>
            <li><strong>Privacy First:</strong> No databases. No accounts. All math happens locally.</li>
            <li><strong>Modern Design:</strong> A gorgeous, ad-optimized interface that works flawlessly on desktop and mobile.</li>
        </ul>
        '''
    },
    'contact': {
        'title': 'Contact Us | Calcify',
        'h1': 'Get in Touch',
        'content': '''
        <p>Have a question, feedback, or a suggestion for a new calculator? We'd love to hear from you!</p>
        
        <div style="background: white; padding: 2rem; border-radius: 20px; border: 1px solid var(--border-color); margin-top: 2rem; max-width: 600px;">
            <form action="https://formspree.io/f/your_form_endpoint" method="POST" style="display: flex; flex-direction: column; gap: 1.5rem;">
                <div class="form-group" style="margin:0;">
                    <label style="display:block; margin-bottom:0.5rem; font-weight:600;">Your Name</label>
                    <input type="text" name="name" required style="width:100%; padding: 0.8rem; border-radius: 8px; border: 1px solid #cbd5e1; outline:none;" placeholder="John Doe">
                </div>
                <div class="form-group" style="margin:0;">
                    <label style="display:block; margin-bottom:0.5rem; font-weight:600;">Email Address</label>
                    <input type="email" name="_replyto" required style="width:100%; padding: 0.8rem; border-radius: 8px; border: 1px solid #cbd5e1; outline:none;" placeholder="you@example.com">
                </div>
                <div class="form-group" style="margin:0;">
                    <label style="display:block; margin-bottom:0.5rem; font-weight:600;">Message</label>
                    <textarea name="message" required style="width:100%; padding: 0.8rem; border-radius: 8px; border: 1px solid #cbd5e1; outline:none; min-height: 150px; font-family: inherit; resize: vertical;" placeholder="How can we help?"></textarea>
                </div>
                <button type="submit" class="btn-use" style="background: var(--primary-color); color: white; padding: 1rem; border-radius: 8px; font-weight: 600; cursor: pointer; border: none; font-size: 1.1rem;">Send Message</button>
            </form>
            <p style="margin-top: 1rem; font-size: 0.9rem; color: var(--text-muted); text-align: center;">Powered by Formspree. We usually respond within 24-48 hours.</p>
        </div>
        '''
    }
}

template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="robots" content="index, follow">
    <link rel="stylesheet" href="style.css">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        .page-content {{ max-width: 800px; margin: 0 auto; padding: 10rem 2rem 5rem; line-height: 1.8; }}
        .page-content h1 {{ font-size: 3rem; margin-bottom: 2rem; background: linear-gradient(135deg, var(--primary-color), #ec4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .page-content h3 {{ margin-top: 2rem; margin-bottom: 1rem; color: #0f172a; font-size: 1.5rem; }}
        .page-content p {{ margin-bottom: 1.5rem; color: var(--text-muted); font-size: 1.1rem; }}
        .page-content ul {{ margin-left: 2rem; margin-bottom: 1.5rem; color: var(--text-muted); list-style-type: disc; }}
        .page-content ul li {{ margin-bottom: 0.5rem; }}
        .page-content strong {{ color: #0f172a; }}
    </style>
</head>
<body>
    {header}
    <main class="page-content">
        <h1>{h1}</h1>
        {content}
    </main>
    {footer}
    <script>lucide.createIcons();</script>
</body>
</html>
'''

for slug, data in pages.items():
    html = template.format(
        title=data['title'],
        h1=data['h1'],
        content=data['content'],
        header=header_str,
        footer=footer_str
    )
    with open(os.path.join(base, f'{slug}.html'), 'w', encoding='utf-8') as f:
        f.write(html)
        
# 3. Update calcify.html Footer and Header links to point to these new pages
hub_path = os.path.join(base, 'calcify.html')
with open(hub_path, 'r', encoding='utf-8') as f:
    hub_html = f.read()
    
hub_html = hub_html.replace('href="#about"', 'href="about.html"')
hub_html = hub_html.replace('href="#contact"', 'href="contact.html"')
hub_html = hub_html.replace('href="#"', 'href="privacy-policy.html"') # replaces the privacy/terms dummy links
hub_html = hub_html.replace('href="privacy-policy.html">Terms of Service', 'href="terms-of-service.html">Terms of Service')

with open(hub_path, 'w', encoding='utf-8') as f:
    f.write(hub_html)

# Also update the footer string in the template pages so they link to each other properly
# We just update them via a quick replace
for slug in pages.keys():
    path = os.path.join(base, f'{slug}.html')
    with open(path, 'r', encoding='utf-8') as f:
        h = f.read()
    h = h.replace('href="#about"', 'href="about.html"')
    h = h.replace('href="#contact"', 'href="contact.html"')
    h = h.replace('href="#"', 'href="privacy-policy.html"')
    h = h.replace('href="privacy-policy.html">Terms of Service', 'href="terms-of-service.html">Terms of Service')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(h)

print('Generated Legal/Info Pages!')
