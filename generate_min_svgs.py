import os

out_dir = r'C:/Users/Asus/Downloads/uma/UMA-Enterprises/assets/generated-images'
os.makedirs(out_dir, exist_ok=True)

def make_min_svg(filename, title, subtitle, markup, dark=False):
    bg = '#091322' if dark else '#F4F6F9'
    fg = '#FFFFFF' if dark else '#141B24'
    sub = '#9AA7B8' if dark else '#526071'
    line = 'rgba(255,255,255,0.08)' if dark else 'rgba(11,102,152,0.1)'
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" fill="none">
  <rect width="800" height="500" fill="{bg}"/>
  <rect x="28" y="28" width="744" height="444" rx="12" stroke="{line}" stroke-width="1.2"/>
  {markup}
  <text x="52" y="425" fill="{fg}" font-family="sans-serif" font-size="16" font-weight="700">{title}</text>
  <text x="52" y="448" fill="{sub}" font-family="monospace" font-size="11">{subtitle} · MINIMALIST ILLUSTRATIVE VISUAL</text>
</svg>'''
    with open(os.path.join(out_dir, filename), 'w', encoding='utf-8') as f:
        f.write(svg)

# Minimalist section-specific visuals
make_min_svg('about-philosophy.svg', 'Engineering Coordination & Quality', 'DESIGN · TOOLING · INSPECTION', '''
  <circle cx="240" cy="215" r="78" stroke="#0B6698" stroke-width="2"/>
  <circle cx="400" cy="215" r="78" stroke="#E86A17" stroke-width="2"/>
  <circle cx="560" cy="215" r="78" stroke="#0B6698" stroke-width="2"/>
  <line x1="140" y1="215" x2="660" y2="215" stroke="#526071" stroke-width="1" stroke-dasharray="4 4"/>
''', dark=False)

make_min_svg('about-timeline.svg', 'Two Decades of Composite Growth', '2001 — PRESENT · CONTINUOUS CAPABILITY EXPANSION', '''
  <line x1="120" y1="230" x2="680" y2="230" stroke="#0B6698" stroke-width="2"/>
  <circle cx="160" cy="230" r="9" fill="#E86A17"/>
  <circle cx="320" cy="230" r="9" fill="#0B6698"/>
  <circle cx="480" cy="230" r="9" fill="#0B6698"/>
  <circle cx="640" cy="230" r="11" fill="#E86A17"/>
  <text x="142" y="200" fill="#526071" font-family="monospace" font-size="12">2001</text>
  <text x="302" y="200" fill="#526071" font-family="monospace" font-size="12">2008</text>
  <text x="462" y="200" fill="#526071" font-family="monospace" font-size="12">2015</text>
  <text x="620" y="200" fill="#141B24" font-family="monospace" font-size="12" font-weight="700">2026</text>
''', dark=False)

make_min_svg('infra-facility.svg', '8,000 sq. ft. Production Layout', 'PATTERN · MOULDING · FINISHING · INSPECTION', '''
  <rect x="110" y="105" width="270" height="120" rx="6" stroke="#0B6698" stroke-width="1.8"/>
  <rect x="410" y="105" width="280" height="120" rx="6" stroke="#0B6698" stroke-width="1.8"/>
  <rect x="110" y="245" width="270" height="115" rx="6" stroke="#E86A17" stroke-width="1.8"/>
  <rect x="410" y="245" width="280" height="115" rx="6" stroke="#0B6698" stroke-width="1.8"/>
  <text x="135" y="170" fill="#141B24" font-family="monospace" font-size="12">01 / PATTERN &amp; MOULDING</text>
  <text x="435" y="170" fill="#141B24" font-family="monospace" font-size="12">02 / LAYUP &amp; VACUUM BAY</text>
  <text x="135" y="308" fill="#141B24" font-family="monospace" font-size="12">03 / TRIMMING &amp; FINISHING</text>
  <text x="435" y="308" fill="#141B24" font-family="monospace" font-size="12">04 / QC &amp; DISPATCH</text>
''', dark=False)

make_min_svg('contact-enquiry.svg', 'Technical Enquiry &amp; Feasibility Review', 'DRAWING REVIEW · MATERIAL SELECTION · QUOTATION', '''
  <rect x="170" y="115" width="460" height="230" rx="10" stroke="#0B6698" stroke-width="1.8"/>
  <line x1="210" y1="165" x2="590" y2="165" stroke="#0B6698" stroke-opacity="0.35" stroke-width="2"/>
  <line x1="210" y1="210" x2="510" y2="210" stroke="#0B6698" stroke-opacity="0.35" stroke-width="2"/>
  <line x1="210" y1="255" x2="450" y2="255" stroke="#E86A17" stroke-width="2.5"/>
  <circle cx="565" cy="285" r="24" stroke="#E86A17" stroke-width="2"/>
''', dark=False)

print("Generated 4 additional minimalist section SVGs.")
