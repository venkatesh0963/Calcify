import os
import re
from bs4 import BeautifulSoup

def main():
    target_dir = r"c:\Users\Venkatesh\OneDrive\Desktop\VENKATESH PJS\2) PLAYMOTIONS\calcify"
    html_path = os.path.join(target_dir, "calcify.html")
    
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
        
    soup = BeautifulSoup(html_content, "html.parser")
    
    # 1. Extract CSS
    style_tag = soup.find("style")
    css_content = style_tag.string if style_tag else ""
    
    # Add some CSS for the standalone calculator pages
    css_content += """
    /* Standalone Calculator Page Styles */
    .calc-page-body { background: #f8fafc; min-height: 100vh; display: flex; flex-direction: column; margin: 0; }
    .calc-main-container { flex: 1; display: flex; align-items: center; justify-content: center; padding: 2rem; }
    .calculator-box {
        background: white; border-radius: 24px; padding: 2.5rem;
        width: 100%; max-width: 450px;
        box-shadow: 0 25px 50px -12px rgba(0,0,0,0.1);
        border: 1px solid var(--border-color);
    }
    .back-link { display: flex; align-items: center; gap: 0.5rem; color: var(--text-color); text-decoration: none; font-weight: 600; }
    .back-link:hover { color: var(--primary-color); }
    """
    
    with open(os.path.join(target_dir, "style.css"), "w", encoding="utf-8") as f:
        f.write(css_content)
        
    if style_tag:
        style_tag.decompose()
        
    # 2. Extract JS
    script_tags = soup.find_all("script")
    js_content = ""
    lucide_src = ""
    for script in script_tags:
        if script.get("src") and "lucide" in script.get("src"):
            lucide_src = str(script)
            continue
        if script.string:
            js_content += script.string + "\n"
        script.decompose()
        
    with open(os.path.join(target_dir, "script.js"), "w", encoding="utf-8") as f:
        f.write(js_content)
        
    # Add links back to calcify.html
    head = soup.find("head")
    new_link = soup.new_tag("link", rel="stylesheet", href="style.css")
    head.append(new_link)
    if lucide_src:
        head.append(BeautifulSoup(lucide_src, "html.parser"))
        
    body = soup.find("body")
    new_script = soup.new_tag("script", src="script.js")
    body.append(new_script)
    
    # 3. Extract Calculators and Create HTML Files
    modals = soup.find_all("div", class_="modal")
    calculators = []
    
    for modal in modals:
        modal_id = modal.get("id") # e.g. modal-numerical
        calc_name = modal_id.replace("modal-", "")
        
        # Get header title
        header = modal.find("div", class_="modal-header")
        title = header.find("h3").text.strip() if header and header.find("h3") else calc_name.capitalize()
        
        # We need the inner HTML of the modal (excluding the header which we might redesign or keep)
        # Let's keep the modal's inner html exactly as is, it's already styled!
        modal_inner = "".join([str(child) for child in modal.contents])
        
        calc_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Calcify</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="calc-page-body">
    <header>
        <div class="nav-container">
            <a href="calcify.html" class="logo">Calcify.</a>
            <a href="calcify.html" class="back-link"><i data-lucide="arrow-left"></i> Back to Hub</a>
        </div>
    </header>
    <main class="calc-main-container">
        <div class="calculator-box">
            {modal_inner}
        </div>
    </main>
    <script src="script.js"></script>
</body>
</html>"""
        with open(os.path.join(target_dir, f"{calc_name}.html"), "w", encoding="utf-8") as f:
            f.write(calc_html)
            
        modal.decompose() # Remove from main file
        calculators.append(calc_name)
        
    # Remove overlay
    overlay = soup.find("div", id="modal-overlay")
    if overlay:
        overlay.decompose()
        
    # 4. Update Bento Cards in calcify.html
    bento_buttons = soup.find_all("button", class_="btn-use")
    for btn in bento_buttons:
        onclick = btn.get("onclick", "")
        if "openModal" in onclick:
            match = re.search(r"openModal\('modal-(.+?)'\)", onclick)
            if match:
                calc_name = match.group(1)
                new_a = soup.new_tag("a", href=f"{calc_name}.html")
                new_a["class"] = "btn-use"
                new_a.string = btn.string
                btn.replace_with(new_a)
                
    with open(os.path.join(target_dir, "style.css"), "a", encoding="utf-8") as f:
        f.write("\\n.btn-use { display: block; text-align: center; text-decoration: none; box-sizing: border-box; }\\n")
        
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
        
    print(f"Successfully generated {len(calculators)} calculator files and extracted CSS/JS!")

if __name__ == "__main__":
    main()
