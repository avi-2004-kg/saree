from flask import Flask, render_template, request, jsonify, send_file
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/catalogue')
def catalogue():
    return render_template('catalogue.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/contact', methods=['POST'])
def contact_api():
    data = request.get_json()
    # In a real application, you would process the contact form data here
    # For now, we'll just return a success message
    return jsonify({'message': 'Thank you for your message! We will get back to you soon.'})

@app.route('/download-catalogue')
def download_catalogue():
    """Generate and download a digital catalogue PDF"""
    try:
        # Create PDF in memory
        pdf_buffer = BytesIO()
        doc = SimpleDocTemplate(pdf_buffer, pagesize=A4, topMargin=0.5*inch, bottomMargin=0.5*inch)
        
        # Get styles
        styles = getSampleStyleSheet()
        
        # Create custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=28,
            textColor=colors.HexColor('#8b5e3c'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#8b5e3c'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        )
        
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['BodyText'],
            fontSize=11,
            textColor=colors.HexColor('#5a4535'),
            alignment=TA_JUSTIFY,
            spaceAfter=10
        )
        
        # Content list
        content = []
        
        # Title Page
        content.append(Spacer(1, 1*inch))
        content.append(Paragraph("✨ Kumudhini Silks ✨", title_style))
        content.append(Spacer(1, 0.3*inch))
        content.append(Paragraph("Digital Catalogue 2025", ParagraphStyle(
            'Subtitle',
            parent=styles['Normal'],
            fontSize=18,
            textColor=colors.HexColor('#d4af37'),
            alignment=TA_CENTER,
            spaceAfter=20
        )))
        content.append(Spacer(1, 0.2*inch))
        content.append(Paragraph("Woven by Heritage. Carried by Heart.", body_style))
        content.append(Paragraph("35 Years of Authentic Silk Sarees", body_style))
        content.append(Spacer(1, 0.5*inch))
        content.append(Paragraph("For over three decades, Kumudhini Silks has been a destination for women who seek beauty woven with meaning.", body_style))
        
        content.append(PageBreak())
        
        # Collections Section
        collections = [
            {
                'title': '👑 Kancheepuram Silk Sarees',
                'description': 'Pure, regal, and handwoven with rich zari borders, these sarees are a timeless reflection of South India\'s weaving heritage. Every Kancheepuram silk is crafted on traditional looms, with temple-inspired motifs and contrasting hues that radiate grandeur.',
                'features': ['100% pure silk', 'Handwoven with traditional techniques', 'Rich zari work', 'Temple-inspired motifs'],
                'price': 'From ₹12,000'
            },
            {
                'title': '🎨 Banarasi Silk Sarees',
                'description': 'From the ghats of Varanasi come our Banarasi silks - opulent, intricate, and woven with real zari threads. These sarees are a symbol of royalty, perfect for festive and ceremonial occasions.',
                'features': ['Authentic Banarasi weaves', 'Real zari threads', 'Intricate brocade work', 'Royal appearance'],
                'price': 'From ₹18,000'
            },
            {
                'title': '✨ Tissue and Designer Silks',
                'description': 'Where innovation meets tradition. Lightweight, luminous, and fashion-forward, these sarees are perfect for women who love subtle glamour with a cultural touch.',
                'features': ['Lightweight and comfortable', 'Modern designs with traditional elements', 'Luminous finish', 'Fashion-forward patterns'],
                'price': 'From ₹8,000'
            },
            {
                'title': '💍 Bridal Silks',
                'description': 'A bride\'s truest adornment. Our bridal collection is handcrafted to embody grace, devotion, and celebration - because every bride deserves to feel like tradition herself.',
                'features': ['Exclusive bridal designs', 'Premium quality silk', 'Elaborate embroidery and embellishments', 'Perfect for wedding ceremonies'],
                'price': 'From ₹25,000'
            }
        ]
        
        for i, collection in enumerate(collections):
            content.append(Paragraph(collection['title'], heading_style))
            content.append(Paragraph(collection['description'], body_style))
            content.append(Paragraph(f"<b>Price: {collection['price']}</b>", body_style))
            content.append(Paragraph("<b>Features:</b>", body_style))
            
            features_text = '<br/>'.join([f"• {feature}" for feature in collection['features']])
            content.append(Paragraph(features_text, body_style))
            
            if i < len(collections) - 1:
                content.append(Spacer(1, 0.3*inch))
                content.append(PageBreak())
        
        content.append(PageBreak())
        
        # Quality Assurance Section
        content.append(Paragraph("🔍 Our Quality Assurance 🔍", heading_style))
        content.append(Paragraph("Each creation is inspected for its weave, zari purity, and craftsmanship - ensuring that only the finest silks find their way to you.", body_style))
        content.append(Spacer(1, 0.2*inch))
        
        assurance_items = [
            ('✓ Weave Inspection', 'Every saree is checked for perfect weaving patterns'),
            ('✓ Zari Purity', 'Verified authentic zari work in every design'),
            ('✓ Craftsmanship', 'Quality assessment by expert artisans'),
            ('✓ Material Authenticity', '100% genuine silk guaranteed')
        ]
        
        for item_title, item_desc in assurance_items:
            content.append(Paragraph(f"<b>{item_title}:</b> {item_desc}", body_style))
        
        content.append(Spacer(1, 0.3*inch))
        
        # Contact Section
        content.append(Paragraph("📞 Contact Information 📞", heading_style))
        contact_text = """
        <b>Kumudhini Silks</b><br/>
        #197/7, Maruthi Mansion, Canara Bank Building<br/>
        Cunningham Road, Bengaluru - 560052<br/>
        <br/>
        Phone: 080 2226 2354<br/>
        Mobile: +91 95352 86772<br/>
        Email: kumudhinisilks7686@gmail.com<br/>
        <br/>
        Store Hours: 10:00 AM - 8:00 PM (Mon-Sat)<br/>
        11:00 AM - 7:00 PM (Sunday)<br/>
        <br/>
        Instagram: @kumudhinisilks
        """
        content.append(Paragraph(contact_text, body_style))
        
        # Build PDF
        doc.build(content)
        
        # Reset buffer position
        pdf_buffer.seek(0)
        
        return send_file(
            pdf_buffer,
            mimetype='application/pdf',
            as_attachment=True,
            download_name='Kumudhini_Silks_Catalogue_2025.pdf'
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)