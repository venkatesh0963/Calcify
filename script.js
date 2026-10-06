// --- History System ---
function getCalcName() {
    let h3 = document.querySelector('.modal-header h3');
    if(!h3) return 'Unknown';
    let text = h3.innerText.trim();
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

// Universal Converter Configuration
const convConfig = {
    currency: { title: 'Currency', units: { usd: 'USD ($)', eur: 'EUR (€)', gbp: 'GBP (£)', inr: 'INR (₹)', jpy: 'JPY (¥)' }, rates: { usd: 1, eur: 0.92, gbp: 0.79, inr: 83.5, jpy: 154.2 } },
    length: { title: 'Length', units: { m: 'Meters', km: 'Kilometers', cm: 'Centimeters', mm: 'Millimeters', inch: 'Inches', foot: 'Feet', yard: 'Yards', mile: 'Miles' }, rates: { m: 1, km: 1000, cm: 0.01, mm: 0.001, inch: 0.0254, foot: 0.3048, yard: 0.9144, mile: 1609.34 } },
    mass: { title: 'Mass', units: { kg: 'Kilograms', g: 'Grams', mg: 'Milligrams', lb: 'Pounds', oz: 'Ounces' }, rates: { kg: 1, g: 0.001, mg: 0.000001, lb: 0.453592, oz: 0.0283495 } },
    area: { title: 'Area', units: { sqm: 'Square Meters', sqkm: 'Sq Kilometers', sqfoot: 'Square Feet', acre: 'Acres', hectare: 'Hectares' }, rates: { sqm: 1, sqkm: 1000000, sqfoot: 0.092903, acre: 4046.86, hectare: 10000 } },
    volume: { title: 'Volume', units: { l: 'Liters', ml: 'Milliliters', gal: 'Gallons (US)', cubicm: 'Cubic Meters' }, rates: { l: 1, ml: 0.001, gal: 3.78541, cubicm: 1000 } },
    time: { title: 'Time', units: { sec: 'Seconds', min: 'Minutes', hr: 'Hours', day: 'Days' }, rates: { sec: 1, min: 60, hr: 3600, day: 86400 } },
    speed: { title: 'Speed', units: { ms: 'Meters/Sec', kmh: 'Km/Hour', mph: 'Miles/Hour', knot: 'Knots' }, rates: { ms: 1, kmh: 0.277778, mph: 0.44704, knot: 0.514444 } },
    data: { title: 'Data Storage', units: { b: 'Bytes', kb: 'Kilobytes', mb: 'Megabytes', gb: 'Gigabytes', tb: 'Terabytes' }, rates: { b: 1, kb: 1024, mb: 1048576, gb: 1073741824, tb: 1099511627776 } }
};

function setupConverter(type) {
    const config = convConfig[type];
    document.getElementById('conv-type').value = type;
    
    const fromSelect = document.getElementById('conv-from');
    const toSelect = document.getElementById('conv-to');
    fromSelect.innerHTML = ''; toSelect.innerHTML = '';
    
    for (let [key, name] of Object.entries(config.units)) {
        fromSelect.innerHTML += `<option value="${key}">${name}</option>`;
        toSelect.innerHTML += `<option value="${key}">${name}</option>`;
    }
    
    if(toSelect.options.length > 1) toSelect.selectedIndex = 1;
    document.getElementById('conv-val').value = '';
    document.getElementById('conv-res').innerText = '--';
}

function runConversion() {
    const type = document.getElementById('conv-type').value;
    const val = parseFloat(document.getElementById('conv-val').value);
    const from = document.getElementById('conv-from').value;
    const to = document.getElementById('conv-to').value;
    const res = document.getElementById('conv-res');
    
    if(isNaN(val)) { res.innerText = '--'; return; }
    
    const rates = convConfig[type].rates;
    const baseVal = val * rates[from];
    const finalVal = baseVal / rates[to];
    
    let out = finalVal.toPrecision(6);
    if(out.includes('.')) out = out.replace(/\.?0+$/, '');
    if(out.includes('e')) out = finalVal.toExponential(4);
    
    res.innerText = out;
    
    let unitF = document.getElementById("conv-from").options[document.getElementById("conv-from").selectedIndex].text;
    let unitT = document.getElementById("conv-to").options[document.getElementById("conv-to").selectedIndex].text;
    saveHistory(val + " " + unitF, out + " " + unitT);
}

// 1. Numerical (Standard Calc) Logic
let stdExp = '';
const stdDisplay = document.getElementById('std-display');
function stdNum(n) { stdExp += n; updateStd(); }
function stdOp(o) { 
    if(stdExp === '' && o !== '-') return;
    const last = stdExp.slice(-1);
    if(['+','-','*','/','%'].includes(last)) stdExp = stdExp.slice(0, -1) + o;
    else stdExp += o; 
    updateStd(); 
}
function stdClear() { stdExp = ''; updateStd(); }
function stdDel() { stdExp = stdExp.slice(0, -1); updateStd(); }
function stdEq() {
    try {
        let oldExp = stdExp;
        let result = eval(stdExp.replace(/%/g, '/100'));
        result = Math.round(result * 100000000) / 100000000;
        stdExp = result.toString();
        updateStd();
        saveHistory(oldExp, result);
    } catch (e) {
        stdDisplay.innerText = 'Error';
        stdExp = '';
    }
}
function updateStd() { if(stdDisplay) stdDisplay.innerText = stdExp || '0'; }

// Finance
function calcFin() {
    const p = parseFloat(document.getElementById('fin-p').value);
    const r = parseFloat(document.getElementById('fin-r').value);
    const t = parseFloat(document.getElementById('fin-t').value);
    if(p>0 && r>=0 && t>0) {
        const int = (p * r * t) / 100;
        document.getElementById('fin-res').innerText = '$' + int.toFixed(2) + ' Interest';
        document.getElementById('fin-tot').innerText = 'Total Amount: $' + (p + int).toFixed(2);
        saveHistory("P:$"+p+", R:"+r+"%, T:"+t+"y", "$"+(p+int).toFixed(2));
    } else {
        document.getElementById('fin-res').innerText = '--';
        document.getElementById('fin-tot').innerText = 'Total Amount: --';
    }
}

// Discount
function calcDisc() {
    const p = parseFloat(document.getElementById('disc-price').value);
    const d = parseFloat(document.getElementById('disc-perc').value);
    if(p>0 && d>=0) {
        const saved = p * (d/100);
        document.getElementById('disc-res').innerText = '$' + (p - saved).toFixed(2);
        document.getElementById('disc-saved').innerText = 'Saved: $' + saved.toFixed(2);
        saveHistory("$"+p+" (-"+d+"%)", "Final: $"+(p-saved).toFixed(2));
    } else {
        document.getElementById('disc-res').innerText = '--';
        document.getElementById('disc-saved').innerText = 'Saved: --';
    }
}

// GST
function calcGst() {
    const a = parseFloat(document.getElementById('gst-amt').value);
    const r = parseFloat(document.getElementById('gst-rate').value);
    if(a>0 && r>=0) {
        const add = a + (a * (r/100));
        const sub = a - (a - (a / (1 + (r/100))));
        document.getElementById('gst-add').innerText = '$' + add.toFixed(2);
        document.getElementById('gst-sub').innerText = '$' + sub.toFixed(2);
        saveHistory("$"+a+" +"+r+"%", "Add: $"+add.toFixed(2)+" | Sub: $"+sub.toFixed(2));
    } else {
        document.getElementById('gst-add').innerText = '--';
        document.getElementById('gst-sub').innerText = '--';
    }
}

// Date
function calcDateDiff() {
    const d1 = new Date(document.getElementById('date-1').value);
    const d2 = new Date(document.getElementById('date-2').value);
    if(!isNaN(d1) && !isNaN(d2)) {
        const diff = Math.abs(d2 - d1);
        const days = Math.ceil(diff / (1000 * 60 * 60 * 24));
        document.getElementById('date-res').innerText = days + ' Days';
        saveHistory(d1.toLocaleDateString() + " → " + d2.toLocaleDateString(), days + " Days");
    } else {
        document.getElementById('date-res').innerText = '-- Days';
    }
}

// BMI
function calcBmi() {
    const w = parseFloat(document.getElementById('bmi-w').value);
    const h = parseFloat(document.getElementById('bmi-h').value) / 100;
    const res = document.getElementById('bmi-res');
    const cat = document.getElementById('bmi-cat');
    
    if (w > 0 && h > 0) {
        const bmi = (w / (h * h)).toFixed(1);
        res.innerText = bmi;
        if (bmi < 18.5) { cat.innerText = 'Underweight'; cat.style.color = '#3b82f6'; }
        else if (bmi < 25) { cat.innerText = 'Normal weight'; cat.style.color = '#10b981'; }
        else if (bmi < 30) { cat.innerText = 'Overweight'; cat.style.color = '#f59e0b'; }
        else { cat.innerText = 'Obese'; cat.style.color = '#ef4444'; }
        saveHistory(w + "kg / " + (h*100) + "cm", "BMI: " + bmi);
    } else {
        res.innerText = '--';
        cat.innerText = 'Enter values';
        cat.style.color = 'var(--text-muted)';
    }
}

// Temperature
function convTemp(type) {
    const c = document.getElementById('temp-c');
    const f = document.getElementById('temp-f');
    const k = document.getElementById('temp-k');
    
    let cVal;
    if (type === 'C' && c.value !== '') {
        cVal = parseFloat(c.value);
        f.value = ((cVal * 9/5) + 32).toFixed(2);
        k.value = (cVal + 273.15).toFixed(2);
        saveHistory(cVal + "°C", f.value + "°F | " + k.value + "K");
    } else if (type === 'F' && f.value !== '') {
        const fVal = parseFloat(f.value);
        cVal = (fVal - 32) * 5/9;
        c.value = cVal.toFixed(2);
        k.value = (cVal + 273.15).toFixed(2);
        saveHistory(fVal + "°F", c.value + "°C | " + k.value + "K");
    } else if (type === 'K' && k.value !== '') {
        const kVal = parseFloat(k.value);
        cVal = kVal - 273.15;
        c.value = cVal.toFixed(2);
        f.value = ((cVal * 9/5) + 32).toFixed(2);
        saveHistory(kVal + "K", c.value + "°C | " + f.value + "°F");
    } else {
        c.value = ''; f.value = ''; k.value = '';
    }
}

// Initialize Lucide Icons
if (typeof lucide !== 'undefined') {
    lucide.createIcons();
}

// --- Keyboard Support ---
document.addEventListener('keydown', (e) => {
    let calcName = getCalcName();
    
    if(calcName === 'Numerical') {
        if(e.key >= '0' && e.key <= '9') { stdNum(e.key); e.preventDefault(); }
        else if(e.key === '.') { stdNum('.'); e.preventDefault(); }
        else if(e.key === '+' || e.key === '-') { stdOp(e.key); e.preventDefault(); }
        else if(e.key === '*') { stdOp('*'); e.preventDefault(); }
        else if(e.key === '/') { stdOp('/'); e.preventDefault(); }
        else if(e.key === '%') { stdOp('%'); e.preventDefault(); }
        else if(e.key === 'Enter' || e.key === '=') { stdEq(); e.preventDefault(); }
        else if(e.key === 'Backspace') { stdDel(); e.preventDefault(); }
        else if(e.key === 'Escape') { stdClear(); e.preventDefault(); }
    } 
    else if(e.key === 'Enter') {
        const calcBtn = document.querySelector('.calculator-box button[onclick]');
        if(calcBtn) {
            calcBtn.click();
            e.preventDefault();
        }
    }
});
