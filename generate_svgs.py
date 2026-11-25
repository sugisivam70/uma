import os

out_dir = r'C:/Users/Asus/Downloads/uma/UMA-Enterprises/assets/generated-images'
os.makedirs(out_dir, exist_ok=True)

def make_svg(filename, title, subtitle, diagram_markup, dark=False):
    bg = '#091322' if dark else '#F4F6F9'
    fg = '#FFFFFF' if dark else '#141B24'
    grid = 'rgba(255,255,255,0.06)' if dark else 'rgba(11,102,152,0.08)'
    sub = '#9AA7B8' if dark else '#526071'
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 560" fill="none">
  <rect width="800" height="560" fill="{bg}"/>
  <defs>
    <pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{grid}" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="800" height="560" fill="url(#g)"/>
  <rect x="24" y="24" width="752" height="512" rx="14" stroke="{grid}" stroke-width="1.5"/>
  {diagram_markup}
  <rect x="44" y="454" width="712" height="62" rx="8" fill="{'#101E33' if dark else '#FFFFFF'}" stroke="{grid}"/>
  <circle cx="68" cy="485" r="6" fill="#E86A17"/>
  <text x="86" y="481" fill="{fg}" font-family="sans-serif" font-size="16" font-weight="700">{title}</text>
  <text x="86" y="502" fill="{sub}" font-family="monospace" font-size="12">{subtitle} · ILLUSTRATIVE ENGINEERING GRAPHIC</text>
</svg>'''
    with open(os.path.join(out_dir, filename), 'w', encoding='utf-8') as f:
        f.write(svg)

# 1. Hero Composite Laminate & Fairing
make_svg('hero-composite.svg', 'GFRP & CFRP Composite Architecture', 'MULTI-LAYER LAMINATE · PRECISION MOULDING', '''
  <path d="M120 340 C220 170, 520 140, 680 260 L640 360 C480 280, 260 300, 120 340 Z" fill="#0B6698" fill-opacity="0.18" stroke="#0B6698" stroke-width="2.5"/>
  <path d="M150 315 C245 190, 500 170, 645 268" stroke="#E86A17" stroke-width="2.5" stroke-dasharray="8 6"/>
  <path d="M180 295 C270 210, 485 195, 615 275" stroke="#0B6698" stroke-width="1.5"/>
  <line x1="400" y1="90" x2="400" y2="410" stroke="#E86A17" stroke-width="1" stroke-dasharray="4 4"/>
  <circle cx="400" cy="205" r="8" fill="#E86A17"/>
  <circle cx="400" cy="205" r="20" stroke="#E86A17" stroke-width="1.2"/>
''', dark=False)

# 2. Fiberglass Layup & Laminate Stack
make_svg('fiberglass-layup.svg', 'Woven Roving & Hand Layup Stack', 'SURFACE GELCOAT · WOVEN GLASS · STRUCTURAL RESIN', '''
  <rect x="140" y="130" width="520" height="36" rx="4" fill="#E86A17" fill-opacity="0.22" stroke="#E86A17" stroke-width="2"/>
  <rect x="140" y="182" width="520" height="44" rx="4" fill="#0B6698" fill-opacity="0.2" stroke="#0B6698" stroke-width="2"/>
  <rect x="140" y="242" width="520" height="58" rx="4" fill="#0B6698" fill-opacity="0.12" stroke="#0B6698" stroke-width="2" stroke-dasharray="6 4"/>
  <rect x="140" y="316" width="520" height="56" rx="4" fill="#141B24" fill-opacity="0.08" stroke="#526071" stroke-width="2"/>
  <text x="160" y="153" fill="#141B24" font-family="monospace" font-size="13">01 / GELCOAT &amp; SURFACE VEIL</text>
  <text x="160" y="209" fill="#141B24" font-family="monospace" font-size="13">02 / E-GLASS WOVEN ROVING PLIES</text>
  <text x="160" y="276" fill="#141B24" font-family="monospace" font-size="13">03 / PUF OR HONEYCOMB CORE (SANDWICH)</text>
  <text x="160" y="349" fill="#141B24" font-family="monospace" font-size="13">04 / INNER STRUCTURAL SKIN &amp; MOULD TOOL</text>
''', dark=False)

# 3. Vacuum Bagging & Moulding
make_svg('vacuum-moulding.svg', 'Vacuum & Pressure Bag Consolidation', 'ED 15 HIVAC · CONTROLLED FIBER-TO-RESIN RATIO', '''
  <path d="M120 350 Q400 220 680 350 L680 385 L120 385 Z" fill="#0B6698" fill-opacity="0.22" stroke="#0B6698" stroke-width="2.5"/>
  <path d="M140 330 Q400 200 660 330" stroke="#E86A17" stroke-width="3"/>
  <path d="M135 312 Q400 182 665 312" stroke="#FFFFFF" stroke-width="1.5" stroke-dasharray="6 5"/>
  <rect x="355" y="120" width="90" height="44" rx="6" stroke="#E86A17" stroke-width="2" fill="#101E33"/>
  <line x1="400" y1="164" x2="400" y2="235" stroke="#E86A17" stroke-width="2"/>
  <text x="369" y="147" fill="#FFFFFF" font-family="monospace" font-size="12">VACUUM</text>
''', dark=True)

# 4. Wind Tunnel Aerodynamic Model
make_svg('wind-tunnel-model.svg', 'Wind & Water Tunnel Test Model', 'SCALED AIRCRAFT GEOMETRY · PRESSURE TAPPINGS', '''
  <line x1="90" y1="180" x2="710" y2="180" stroke="#0B6698" stroke-width="1.5" stroke-dasharray="10 6"/>
  <line x1="90" y1="260" x2="710" y2="260" stroke="#0B6698" stroke-width="1.5" stroke-dasharray="10 6"/>
  <line x1="90" y1="340" x2="710" y2="340" stroke="#0B6698" stroke-width="1.5" stroke-dasharray="10 6"/>
  <path d="M190 265 C280 230, 440 225, 610 260 C460 285, 290 290, 190 265 Z" fill="#0B6698" fill-opacity="0.25" stroke="#0B6698" stroke-width="2.5"/>
  <path d="M350 235 L420 135 L465 135 L425 235 Z" fill="#E86A17" fill-opacity="0.25" stroke="#E86A17" stroke-width="2"/>
  <circle cx="290" cy="252" r="4" fill="#E86A17"/><circle cx="360" cy="248" r="4" fill="#E86A17"/><circle cx="430" cy="250" r="4" fill="#E86A17"/>
''', dark=False)

# 5. Cockpit Simulator Shell
make_svg('cockpit-simulator.svg', '1:1 Scale Cockpit Simulator Shell', 'ERGONOMIC ENCLOSURE · CONSOLE MOUNTINGS', '''
  <path d="M180 370 L240 210 L420 155 L580 210 L620 370 Z" fill="#0B6698" fill-opacity="0.2" stroke="#0B6698" stroke-width="2.5"/>
  <path d="M250 225 L415 172 L530 225 L500 285 L270 285 Z" fill="#FFFFFF" fill-opacity="0.08" stroke="#E86A17" stroke-width="2"/>
  <rect x="290" y="305" width="220" height="45" rx="4" stroke="#9AA7B8" stroke-width="1.5"/>
''', dark=True)

# 6. Composite Radome & Parabolic Reflector
make_svg('radome-reflector.svg', 'GFRP Radomes & CFRP Reflectors', 'RF TRANSPARENCY · PARABOLIC SURFACE ACCURACY', '''
  <path d="M180 350 A220 220 0 0 1 620 350" stroke="#0B6698" stroke-width="3" fill="#0B6698" fill-opacity="0.12"/>
  <path d="M230 350 A170 170 0 0 1 570 350" stroke="#E86A17" stroke-width="2" stroke-dasharray="6 4"/>
  <line x1="400" y1="110" x2="400" y2="375" stroke="#526071" stroke-width="1.5" stroke-dasharray="4 4"/>
  <circle cx="400" cy="255" r="10" fill="#E86A17"/>
''', dark=False)

# 7. Automotive & HVAC Housings
make_svg('automotive-hvac.svg', 'Automotive & Rooftop HVAC Housings', 'UV-STABILIZED GFRP · IMPACT-RESISTANT MOULDING', '''
  <rect x="170" y="175" width="460" height="175" rx="26" fill="#0B6698" fill-opacity="0.16" stroke="#0B6698" stroke-width="2.5"/>
  <rect x="210" y="210" width="160" height="105" rx="10" stroke="#E86A17" stroke-width="2"/>
  <rect x="405" y="210" width="185" height="105" rx="10" stroke="#0B6698" stroke-width="1.5"/>
  <circle cx="290" cy="262" r="34" stroke="#E86A17" stroke-width="2" stroke-dasharray="6 4"/>
''', dark=False)

# 8. Industrial Enclosures & Tooling
make_svg('industrial-enclosure.svg', 'Industrial Machine Enclosures', 'CORROSION-PROOF GFRP · METAL INTEGRATION', '''
  <rect x="190" y="130" width="420" height="260" rx="12" fill="#101E33" stroke="#0B6698" stroke-width="2.5"/>
  <rect x="225" y="165" width="220" height="190" rx="6" stroke="#9AA7B8" stroke-width="1.5"/>
  <rect x="465" y="165" width="110" height="90" rx="6" stroke="#E86A17" stroke-width="2"/>
  <circle cx="520" cy="310" r="24" stroke="#E86A17" stroke-width="2"/>
''', dark=True)

# 9. Infrastructure & Quality Inspection
make_svg('quality-inspection.svg', '8,000 sq. ft. Facility & Quality Control', 'ISO 9001:2015 ALIGNED · DIMENSIONAL VERIFICATION', '''
  <rect x="140" y="140" width="520" height="240" rx="10" stroke="#0B6698" stroke-width="2" fill="#FFFFFF"/>
  <line x1="140" y1="220" x2="660" y2="220" stroke="#0B6698" stroke-opacity="0.25"/>
  <line x1="140" y1="300" x2="660" y2="300" stroke="#0B6698" stroke-opacity="0.25"/>
  <line x1="313" y1="140" x2="313" y2="380" stroke="#0B6698" stroke-opacity="0.25"/>
  <line x1="486" y1="140" x2="486" y2="380" stroke="#0B6698" stroke-opacity="0.25"/>
  <path d="M210 280 L280 250 L360 265 L450 200 L580 185" stroke="#E86A17" stroke-width="3" fill="none"/>
  <circle cx="450" cy="200" r="6" fill="#E86A17"/>
  <circle cx="580" cy="185" r="6" fill="#0B6698"/>
''', dark=False)

# 10. Custom Engineered Composites
make_svg('custom-composites.svg', 'Custom-Engineered Composite Solutions', 'TOOLING · PATTERN MAKING · FINISHING', '''
  <polygon points="400,110 610,210 610,330 400,410 190,330 190,210" fill="#0B6698" fill-opacity="0.18" stroke="#0B6698" stroke-width="2.5"/>
  <polyline points="190,210 400,285 610,210" stroke="#E86A17" stroke-width="2"/>
  <line x1="400" y1="285" x2="400" y2="410" stroke="#E86A17" stroke-width="2"/>
''', dark=True)

print("Generated 10 illustrative technical SVG assets.")
