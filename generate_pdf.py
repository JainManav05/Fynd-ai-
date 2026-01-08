"""
Convert PROJECT_REPORT.md to PDF
"""
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import re

def create_pdf_report():
    # Read markdown file
    with open('PROJECT_REPORT.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create PDF
    pdf_file = "Fynd_AI_Assessment_Report_Manav_Jain.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading1_style = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=10,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=12
    )
    
    code_style = ParagraphStyle(
        'Code',
        parent=styles['Code'],
        fontSize=9,
        leftIndent=20,
        fontName='Courier'
    )
    
    # Title
    elements.append(Paragraph("Fynd AI Intern Assessment 2.0", title_style))
    elements.append(Paragraph("Project Report", title_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Metadata
    elements.append(Paragraph("<b>Submitted by:</b> Manav Jain", body_style))
    elements.append(Paragraph("<b>GitHub:</b> https://github.com/JainManav05/Fynd-ai-.git", body_style))
    elements.append(Paragraph("<b>Date:</b> January 8, 2026", body_style))
    elements.append(Spacer(1, 0.3*inch))
    
    # Parse and add content
    lines = content.split('\n')
    skip_until_toc = True
    
    for line in lines:
        line = line.strip()
        
        # Skip title and metadata (already added)
        if skip_until_toc and '## Table of Contents' not in line:
            continue
        skip_until_toc = False
        
        if not line:
            continue
            
        # Headers
        if line.startswith('# ') and not line.startswith('##'):
            text = line[2:].replace('{#', '').replace('}', '')
            elements.append(PageBreak())
            elements.append(Paragraph(text, heading1_style))
        elif line.startswith('## '):
            text = line[3:].replace('{#', '').replace('}', '')
            elements.append(Spacer(1, 0.2*inch))
            elements.append(Paragraph(text, heading1_style))
        elif line.startswith('### '):
            text = line[4:]
            elements.append(Paragraph(text, heading2_style))
        elif line.startswith('**') and line.endswith('**'):
            elements.append(Paragraph(line, body_style))
        elif line.startswith('- ✅') or line.startswith('- ❌'):
            elements.append(Paragraph(line, body_style))
        elif line.startswith('---'):
            elements.append(Spacer(1, 0.1*inch))
        elif line.startswith('```'):
            continue  # Skip code block markers
        elif line.startswith('|'):
            continue  # Skip table markers for now
        else:
            # Regular paragraph
            if line and not line.startswith('#'):
                elements.append(Paragraph(line, body_style))
    
    # Build PDF
    doc.build(elements)
    print(f"PDF created successfully: {pdf_file}")

if __name__ == "__main__":
    create_pdf_report()
