import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

pdf_path = r"D:\Deepfake_detection_\PRESENTATION_SCRIPT_AND_QA_GUIDE.pdf"
qr_showcase = r"D:\Deepfake_detection_\qr_showcase_vercel.png"
qr_demo = r"D:\Deepfake_detection_\qr_live_demo_ngrok.png"

# Letter size: 8.5 x 11 inches. Printable height: 11 - (0.35 * 2) = 10.3 inches = ~740 pt
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    rightMargin=36,
    leftMargin=36,
    topMargin=26,
    bottomMargin=26
)

styles = getSampleStyleSheet()

# Typography Styles: High contrast, large readable text
banner_html_style = ParagraphStyle(
    'BannerHTML',
    alignment=1,
    leading=14
)

h1_section_style = ParagraphStyle(
    'H1_Section',
    fontName='Helvetica-Bold',
    fontSize=13,
    leading=16,
    textColor=colors.HexColor('#0a192f'),
    spaceBefore=4,
    spaceAfter=3
)

cue_style = ParagraphStyle(
    'StageCue',
    fontName='Helvetica-Bold',
    fontSize=9.5,
    leading=13,
    textColor=colors.HexColor('#0284c7'),
    spaceBefore=2,
    spaceAfter=2
)

# Big, readable spoken speech (11pt / 16pt leading) in soft blue card
spoken_text_style = ParagraphStyle(
    'SpokenText',
    fontName='Helvetica',
    fontSize=10.5,
    leading=15,
    textColor=colors.HexColor('#0a192f'),
    backColor=colors.HexColor('#f0f7ff'),
    borderColor=colors.HexColor('#0077ff'),
    borderWidth=1.2,
    borderPadding=7,
    spaceAfter=6
)

# Q&A Styles (Large & Readable)
qa_q_style = ParagraphStyle(
    'QA_Q',
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=15,
    textColor=colors.HexColor('#0a192f'),
    spaceBefore=6,
    spaceAfter=2
)

qa_a_style = ParagraphStyle(
    'QA_A',
    fontName='Helvetica',
    fontSize=10,
    leading=14.5,
    textColor=colors.HexColor('#1e293b'),
    backColor=colors.HexColor('#f8fafc'),
    borderColor=colors.HexColor('#94a3b8'),
    borderWidth=0.8,
    borderPadding=6,
    spaceAfter=5
)

story = []

# =========================================================================
# PAGE 1: TITLE BANNER, DUAL QR CARDS, TIMELINE & STAGE RULES
# =========================================================================

# Top Executive Navy Banner
banner_html = Paragraph(
    '<font size="14" color="#ffffff"><b>DEEPFAKE DETECTION USING ARTIFICIAL INTELLIGENCE</b></font><br/>'
    '<font size="10" color="#00d4ff"><b>Spatio-Temporal Hybrid Deep Learning Framework (ResNeXt50 + LSTM)</b></font><br/>'
    '<font size="8" color="#cbd5e1">K. D. Polytechnic, Patan | Department of Computer Engineering | Diploma Poster Competition</font>',
    banner_html_style
)
banner_table = Table([[banner_html]], colWidths=[7.5*inch])
banner_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0a192f')),
    ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ('TOPPADDING', (0,0), (-1,-1), 7),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BOX', (0,0), (-1,-1), 2, colors.HexColor('#00d4ff')),
]))
story.append(banner_table)
story.append(Spacer(1, 8))

# DUAL QR CODES CARDS (SHOWCASE & LIVE AI NGROK)
qr_img1 = Image(qr_showcase, width=1.3*inch, height=1.3*inch)
qr_img2 = Image(qr_demo, width=1.3*inch, height=1.3*inch)

card1_desc = Paragraph(
    '<font size="10.5" color="#0a192f"><b>1. SHOWCASE PORTAL (VERCEL)</b></font><br/>'
    '<font size="8.5" color="#0077ff"><b><u>https://deepfakedetection-cyan.vercel.app/</u></b></font><br/><br/>'
    '<font size="8" color="#334155">'
    '<b>Live 24x7 Hosted on Vercel:</b><br/>'
    'Judges can scan with any phone to view the interactive System Architecture, 8K Forensics, and Benchmark results.'
    '</font>',
    ParagraphStyle('QR1Desc', leading=11.5)
)

card2_desc = Paragraph(
    '<font size="10.5" color="#0a192f"><b>2. LIVE AI ENGINE (NGROK)</b></font><br/>'
    '<font size="8.5" color="#0077ff"><b><u>https://petite-discover-precut.ngrok-free.dev/</u></b></font><br/><br/>'
    '<font size="8" color="#334155">'
    '<b>Live PyTorch Detection Engine:</b><br/>'
    'Scan to upload video right in front of judges and see instant real-time REAL/FAKE prediction &amp; 68 facial landmarks.'
    '</font>',
    ParagraphStyle('QR2Desc', leading=11.5)
)

dual_qr_data = [
    [qr_img1, card1_desc, qr_img2, card2_desc]
]
dual_qr_table = Table(dual_qr_data, colWidths=[1.35*inch, 2.4*inch, 1.35*inch, 2.4*inch])
dual_qr_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
    ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#00d4ff')),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('ALIGN', (0,0), (0,0), 'CENTER'),
    ('ALIGN', (2,0), (2,0), 'CENTER'),
    ('LINEBEFORE', (2,0), (2,-1), 1, colors.HexColor('#cbd5e1')),
]))
story.append(dual_qr_table)
story.append(Spacer(1, 8))

# 5-Minute Speech Timeline Table
story.append(Paragraph('<b>5-MINUTE PRESENTATION TIMELINE &amp; POSTER STAGE CUES</b>', h1_section_style))
timeline_data = [
    ['Timing', 'Presentation Stage', 'What to Point on Poster', 'Key Target Message'],
    ['0:00 - 1:00', 'Stage 1: Opening & Problem', 'Poster Title & Section 1', 'The Deepfake Crisis: Seeing is no longer believing!'],
    ['1:00 - 2:15', 'Stage 2: ResNeXt50 + LSTM', 'Figure 1 (Split Forensics Face)', 'Why Spatio-Temporal beats single-frame CNNs.'],
    ['2:15 - 3:30', 'Stage 3: 4-Step Pipeline', 'Figure 2 (LSTM Frame Flow)', '20-frame sampling to 112x112 to Softmax verdict.'],
    ['3:30 - 4:30', 'Stage 4: Live Demo & QR', 'Showcase QR Code Card', 'Invite judges to scan on their smartphones.'],
    ['4:30 - 5:30', 'Stage 5: Results & Closing', 'Figure 3 (87% Matrix)', '87% accuracy across 23,186 videos & applications.']
]
timeline_table = Table(timeline_data, colWidths=[0.95*inch, 1.95*inch, 2.2*inch, 2.4*inch])
timeline_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0a192f')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#00d4ff')),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 8.5),
    ('BOTTOMPADDING', (0,0), (-1,0), 4),
    ('TOPPADDING', (0,0), (-1,0), 4),
    ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#ffffff')),
    ('TEXTCOLOR', (0,1), (-1,-1), colors.HexColor('#1e293b')),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,1), (-1,-1), 8),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#94a3b8')),
    ('TOPPADDING', (0,1), (-1,-1), 3),
    ('BOTTOMPADDING', (0,1), (-1,-1), 3),
]))
story.append(timeline_table)
story.append(Spacer(1, 8))

# Presenter Rules Card
rules_html = Paragraph(
    '<b>PRESENTER GOLDEN RULES FOR 1ST PRIZE:</b><br/>'
    '<b>1. Smile &amp; Confident Eye Contact:</b> Look at all judges with a warm smile. Never turn your back to the judges.<br/>'
    '<b>2. Point Clearly with Hand/Pen:</b> When saying "Figure 1", "Figure 2", or "Showcase QR", point clearly to the poster.<br/>'
    '<b>3. Natural GujEnglish Flow:</b> Speak naturally in conversational Gujarati and highlight English technical terms clearly.',
    ParagraphStyle('RulesCard', fontSize=8.5, leading=12, textColor=colors.HexColor('#0369a1'))
)
rules_table = Table([[rules_html]], colWidths=[7.5*inch])
rules_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f0f9ff')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#0ea5e9')),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
]))
story.append(rules_table)

# =========================================================================
# PAGE 2: 5-STAGE EASY-TO-READ SPOKEN SCRIPT (PART 1: STAGES 1, 2, 3)
# =========================================================================
story.append(PageBreak())

story.append(Paragraph('<b>STAGE 1: OPENING &amp; THE PROBLEM (0:00 - 1:00)</b>', h1_section_style))
story.append(Paragraph('<b>[ACTION: Judges samaksha smile karo ane Namaste karo]</b>', cue_style))
story.append(Paragraph(
    '"Respected Judges, Faculty Members, and my dear friends. A very good morning to all of you!<br/><br/>'
    'Aaj na digital era ma ek famous proverb badlai gayu che: <b>Seeing is no longer believing!</b><br/><br/>'
    'Aaje GANs ane modern AI tools etla advanced thai gaya che ke koi pan vyakti no face, voice, ane expressions duplicate kari ne ek realistic fake video banavi shakay che - jene apde <b>Deepfakes</b> kahiye chiye!<br/><br/>'
    'Deepfakes identity theft, financial fraud, ane fake news ma explosive speed thi vadhi rahya che. Human naked eye thi aa synthetic videos catch karva almost impossible che.<br/><br/>'
    'Aa national cyber security challenge ne solve karva mate, ame present kariye chiye amaru project: <b>Deepfake Detection Using Artificial Intelligence!</b>"',
    spoken_text_style
))

story.append(Paragraph('<b>STAGE 2: CORE NOVELTY - RESNEXT50 + LSTM (1:00 - 2:15)</b>', h1_section_style))
story.append(Paragraph('<b>[ACTION: Poster na Section 2 ma Figure 1 taraf point karo]</b>', cue_style))
story.append(Paragraph(
    '"Judges, normal models khali ek single frame (photo) check kare che. Pan deepfake creators single frame ma high blending kari de che!<br/><br/>'
    'Pan video ma <b>Temporal Continuity</b> (frame-to-frame flow) - jem ke eye blink rate, facial muscle movement, ane light jitter - preserve nathi kari shakta!<br/><br/>'
    'Aetle amari core innovation che: <b>Hybrid Spatio-Temporal Modeling!</b><br/>'
    '&bull; <b>1. ResNeXt-50 (Spatial Backbone):</b> Frame mathi subtle face texture ane boundary artifacts extract kare che.<br/>'
    '&bull; <b>2. LSTM (Temporal Network):</b> 20 continuous frames ni series ma unnatural flickering ane temporal drift catch kare che!<br/><br/>'
    'Poster na <b>Figure 1</b> ma tame joi shako cho: Real face ma landmarks coherent che, jyare Fake face ma <b>Grad-CAM Heatmap</b> manipulation boundary clear red color ma batavi de che!"',
    spoken_text_style
))

story.append(Paragraph('<b>STAGE 3: END-TO-END 4-STEP PIPELINE (2:15 - 3:30)</b>', h1_section_style))
story.append(Paragraph('<b>[ACTION: Poster na Section 4 &amp; 5 na Flowchart taraf point karo]</b>', cue_style))
story.append(Paragraph(
    '"Amari system nu execution pipeline simple 4 steps ma execute thay che:<br/>'
    '&bull; <b>Step 1 (Upload):</b> User Django web portal par video upload kare che.<br/>'
    '&bull; <b>Step 2 (20-Frames Sampling):</b> OpenCV engine video mathi uniformly <b>20 frames</b> extract kare che.<br/>'
    '&bull; <b>Step 3 (Face Crop):</b> Dlib 68 landmarks localize kari ne face 112x112 resolution ma normalize kare che.<br/>'
    '&bull; <b>Step 4 (Hybrid Classification):</b> ResNeXt-50 spatial features generate kare che, LSTM temporal series evaluate kare che, ane final verdict display kare che: <b>REAL ke FAKE + Confidence % + CAM Heatmap!</b>"',
    spoken_text_style
))

# =========================================================================
# PAGE 3: 5-STAGE EASY-TO-READ SPOKEN SCRIPT (PART 2: STAGES 4, 5) & DEMO
# =========================================================================
story.append(PageBreak())

story.append(Paragraph('<b>STAGE 4: LIVE DEMO &amp; SHOWCASE QR CODES (3:30 - 4:30)</b>', h1_section_style))
story.append(Paragraph('<b>[ACTION: Poster na Section 8 ma rahela Showcase QR Code taraf point karo]</b>', cue_style))
story.append(Paragraph(
    '"Judges, amaro project theoretical nathi, production-ready live deploy karelo che!<br/><br/>'
    'Poster na Section 8 ma <b>amari Showcase Website no official QR Code</b> che (Hosted 24x7 on Vercel). Tame potana mobile thi scan kari ne interactive architecture, 8K forensics heatmaps, ane test results live verify kari shako cho!<br/><br/>'
    'Furthermore, amari web app ma client-side <b>real-time 68 facial landmark tracking</b> pan chale che, je video playback sathe live render thay che!"',
    spoken_text_style
))

story.append(Paragraph('<b>STAGE 5: BENCHMARK RESULTS &amp; CONCLUSION (4:30 - 5:30)</b>', h1_section_style))
story.append(Paragraph('<b>[ACTION: Section 6 na 87% Accuracy Box &amp; Figure 3 taraf point karo]</b>', cue_style))
story.append(Paragraph(
    '"Ame model ne 3 world-standard research datasets par train ane test karyu che: <b>DFDC (Meta AI), Celeb-DF v2, ane FaceForensics++</b> (over 23,000+ videos).<br/><br/>'
    'Amara hybrid model ae <b>87% overall accuracy</b> achieve kari che - je normal single-frame model karta <b>+8.6% better</b> che!<br/><br/>'
    '<b>Real-World Applications:</b> Social media par fake news filtering, Banking E-KYC video spoof protection, ane Cyber crime forensic investigation.<br/><br/>'
    'Thank you so much for your time and kind attention! We are now open for your valuable questions!"',
    spoken_text_style
))

story.append(Spacer(1, 4))
demo_checklist_html = Paragraph(
    '<b>STAGE LIVE DEMO ACTION CHECKLIST:</b><br/>'
    '&bull; <b>Video 1 (Real):</b> Upload <code>TESTING VIDEO/1_REAL_Male_Interview.mp4</code> &rarr; Show green verdict: <b>REAL (High Confidence)</b>.<br/>'
    '&bull; <b>Video 2 (Fake):</b> Upload <code>TESTING VIDEO/2_FAKE_Male_Deepfake.mp4</code> &rarr; Show red alert: <b>FAKE (Deepfake Detected)</b>.<br/>'
    '&bull; <b>Landmark Live Canvas:</b> Point out 68 neon cyan facial dots moving across frames on the browser screen in real time.',
    ParagraphStyle('DemoChecklist', fontSize=8.5, leading=12.5, textColor=colors.HexColor('#065f46'))
)
demo_table = Table([[demo_checklist_html]], colWidths=[7.5*inch])
demo_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ecfdf5')),
    ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#10b981')),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
]))
story.append(demo_table)

# =========================================================================
# PAGE 4: TOP 5 JUDGES Q&A ROUND CHEAT-SHEET (LARGE & READABLE)
# =========================================================================
story.append(PageBreak())

story.append(Paragraph('<b>TOP 5 JUDGES Q&amp;A CHEAT-SHEET (CONCISE 2-LINE WINNING ANSWERS)</b>', h1_section_style))
story.append(Paragraph('Judges aa questions maathi j prashno poochhse. Aa concise javabo bold ane confident aapo:', cue_style))
story.append(Spacer(1, 4))

qa_list = [
    ("Q1: ResNeXt50 kem pasand karyu? Regular ResNet kem nahi?",
     "Sir, ResNeXt50 ma <b>Cardinality (32 parallel convolution paths)</b> hoy che. Deepfake artifacts micro level na hoy che. ResNeXt50 boundary blending ane color contrast independent paths thi superior precision sathe catch kare che."),

    ("Q2: LSTM nu shu kaam che aa project ma?",
     "Sir, CNN khali 2D photo samje che, pan video temporal media che! Deepfakes ma ek frame thi biji frame vache eye blinking ane facial jitter ma discontinuity aave che. <b>LSTM 20 frames na sequence ma aa temporal inconsistency catch kare che.</b>"),

    ("Q3: Video mathi 20 frames j kem lidhi? Badhi 300 frames kem nahi?",
     "Sir, standard video ma 300 frames hoy che. Badhi process karva ma 15-20 seconds lage. <b>20 frames thi inference khali 1.8 seconds ma thai jaay che ane 87% accuracy male che.</b> Aa latency ane accuracy no optimal sweet spot che."),

    ("Q4: Input resolution 112x112 kem raakhyu? 224x224 kem nahi?",
     "Sir, background remove karya pachi face crop mate 112x112 resolution purti che. <b>224x224 karta 112x112 ma memory usage 75% ochhi thai jaay che</b>, jena lidhe amaro model lightweight ane fast bane che."),

    ("Q5: Jo video poor quality ke compressed hoy to shu thay?",
     "Sir, heavy compression ma pixel boundaries blur thai jaay che, jethi false negative rate vadhi shake. Aa current limitation che, ane future ma ame <b>frequency-domain Fourier transform (FFT)</b> add karvanu plan karyu che."),

    ("Bonus Q6: Client-side face-api.js ane Server-side dlib ma difference shu che?",
     "Sir, <b>face-api.js browser ma WebGL par client side</b> fast UI feedback mate chale che, jyare <b>server side dlib/face_recognition</b> 112x112 crops extract kari PyTorch model ne feed kare che.")
]

for q, a in qa_list:
    story.append(Paragraph(f"<b>{q}</b>", qa_q_style))
    story.append(Paragraph(f"{a}", qa_a_style))

doc.build(story)
print("SUCCESS! Master High-Readability 4-Page PDF Generated:", pdf_path)
