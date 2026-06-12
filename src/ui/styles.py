import streamlit as st

def load_css():
    st.markdown("""
    <style>
    /* ============================================
       FONT & BASE IMPORTS
    ============================================ */
    @import url('https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,500;14..32,600;14..32,700;14..32,800&display=swap');

    /* ============================================
       RESET & GLOBAL STYLES
    ============================================ */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* Hide Streamlit default elements */
    #MainMenu, footer, header, .stDeployButton {
        visibility: hidden !important;
        display: none !important;
    }

    /* Main app background */
    .stApp {
        background: linear-gradient(135deg, #0a0c10 0%, #0f1117 100%) !important;
    }

    /* Main container padding */
    .block-container {
        padding: 2rem 2rem 3rem 2rem !important;
        max-width: 1400px !important;
        margin: 0 auto !important;
    }
/* ============================================
   SIDEBAR STYLES - ALWAYS VISIBLE & EXPANDED
    ============================================ */

    /* EXTRA FIX - Remove ALL possible top spaces */
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }
    
    /* Remove any invisible blocking elements */
    [data-testid="stSidebar"] .st-emotion-cache-1v0mbdj,
    [data-testid="stSidebar"] .st-emotion-cache-18ni7ap,
    [data-testid="stSidebar"] .st-emotion-cache-16idsys,
    [data-testid="stSidebar"] header {
        display: none !important;
        height: 0 !important;
        min-height: 0 !important;
        max-height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        visibility: hidden !important;
    }
    
    /* Force the sidebar content to start from top */
    [data-testid="stSidebar"] > div:first-child {
        display: flex !important;
        flex-direction: column !important;
        justify-content: flex-start !important;
    }

    /* Hide the collapse button completely */
    [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }

    /* Remove default sidebar header space */
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 0 !important;
    }

    /* Remove any default header elements */
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"]:first-child {
        margin-top: 0 !important;
    }

    /* Hide any default app title/text in sidebar */
    [data-testid="stSidebar"] .st-emotion-cache-1v0mbdj,
    .css-1v0mbdj {
        display: none !important;
        padding-top: 0 !important;
    }

    /* Hide default navigation menu */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }

    /* Hide any default page links in sidebar */
    .st-emotion-cache-1cypcdb {
        display: none !important;
    }

    /* Sidebar background - ALWAYS EXPANDED */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0c10 0%, #0d0f14 100%) !important;
        border-right: 1px solid rgba(99, 102, 241, 0.15) !important;
        min-width: 280px !important;
        width: 280px !important;
    }

    /* Prevent sidebar from being collapsed */
    [data-testid="stSidebar"][aria-expanded="false"] {
        min-width: 280px !important;
        width: 280px !important;
        transform: none !important;
    }

    /* Make sidebar brand the absolute first element */
    .sidebar-brand {
        margin-top: 0 !important;
        padding: 1rem 1.5rem 1.5rem 1.5rem !important;
        margin-bottom: 0.5rem;
        border-bottom: 2px solid rgba(99, 102, 241, 0.15);
        text-align: left;
    }

    /* ============================================
       SIDEBAR BRANDING
    ============================================ */

    .sidebar-brand-icon {
        font-size: 2.2rem;
        margin-bottom: 0.5rem;
        display: block;
    }

    .sidebar-brand-name {
        font-size: 1.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #818CF8 0%, #C7D2FE 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.3px;
        margin-bottom: 0.25rem;
    }

    .sidebar-brand-sub {
        font-size: 0.7rem;
        color: #6b7280;
        margin-top: 0.25rem;
    }

    /* ============================================
       SIDEBAR NAVIGATION
    ============================================ */

    .nav-group-label {
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #6b7280;
        padding: 1.5rem 1.5rem 0.75rem 1.5rem;
    }

    /* Sidebar buttons styling */
    [data-testid="stSidebar"] .stButton button {
        background: transparent !important;
        border: none !important;
        color: #9ca3af !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        text-align: left !important;
        padding: 0.6rem 1.2rem !important;
        margin: 0.2rem 0 !important;
        border-radius: 8px !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
    }

    [data-testid="stSidebar"] .stButton button:hover {
        background: rgba(99, 102, 241, 0.1) !important;
        color: #f3f4f6 !important;
        transform: translateX(5px) !important;
    }

    /* ============================================
       SIDEBAR FOOTER
    ============================================ */

    .sidebar-footer {
        position: absolute;
        bottom: 1rem;
        left: 0;
        right: 0;
        padding: 1rem;
        border-top: 1px solid rgba(99, 102, 241, 0.1);
        text-align: center;
        color: #6b7280;
        font-size: 0.7rem;
    }

    .footer-icon {
        font-size: 1rem;
        margin-right: 0.3rem;
    }

    /* ============================================
       SIDEBAR SCROLLBAR
    ============================================ */

    [data-testid="stSidebar"] ::-webkit-scrollbar {
        width: 3px;
    }

    [data-testid="stSidebar"] ::-webkit-scrollbar-track {
        background: rgba(99, 102, 241, 0.05);
    }

    [data-testid="stSidebar"] ::-webkit-scrollbar-thumb {
        background: rgba(99, 102, 241, 0.3);
        border-radius: 3px;
    }

    /* ============================================
       RESPONSIVE SIDEBAR
    ============================================ */

    @media (max-width: 768px) {
        [data-testid="stSidebar"] {
            min-width: 260px !important;
            width: 260px !important;
        }
        
        .sidebar-brand-icon {
            font-size: 1.8rem;
        }
        
        .sidebar-brand-name {
            font-size: 1rem;
        }
        
        .sidebar-brand-sub {
            font-size: 0.6rem;
        }
    }
    /* ============================================
       END SIDEBAR STYLES
    ============================================ */
    /* ============================================
       CARD COMPONENTS
    ============================================ */
    /* Base card styling */
    .card {
        background: rgba(17, 19, 24, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(99, 102, 241, 0.15);
        border-radius: 1rem;
        padding: 1.25rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }

    .card:hover {
        transform: translateY(-2px);
        border-color: rgba(99, 102, 241, 0.3);
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.2), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
    }

    /* KPI Cards - Professional Dashboard Style */
    .kpi-card {
        background: linear-gradient(135deg, rgba(17, 19, 24, 0.95) 0%, rgba(22, 24, 30, 0.95) 100%);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 1rem;
        padding: 1.25rem;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        height: 100%;
    }

    .kpi-card:hover {
        transform: translateY(-3px);
        border-color: #6366F1;
        box-shadow: 0 8px 20px rgba(99, 102, 241, 0.15);
    }

    .kpi-top {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.75rem;
    }

    .kpi-label {
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        color: #9CA3AF;
    }

    .kpi-icon {
        font-size: 1.5rem;
        opacity: 0.8;
    }

    .kpi-value {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FFFFFF 0%, #D1D5DB 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2;
        margin: 0.5rem 0;
    }

    .kpi-sub {
        font-size: 0.7rem;
        color: #6B7280;
        font-weight: 400;
    }

    /* ============================================
       HEADER SECTION
    ============================================ */
    .header-card {
        background: linear-gradient(135deg, rgba(17, 19, 24, 0.9) 0%, rgba(25, 28, 36, 0.9) 100%);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 1rem;
        padding: 1.5rem 2rem;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

    .header-title {
        font-size: 1.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FFFFFF 0%, #A5B4FC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.5px;
    }

    .header-subtitle {
        font-size: 0.8rem;
        color: #9CA3AF;
        margin-top: 0.25rem;
    }

    .header-date {
        font-size: 0.9rem;
        font-weight: 600;
        color: #F3F4F6;
        text-align: right;
    }

    .header-year {
        font-size: 0.7rem;
        color: #6B7280;
        text-align: right;
        margin-top: 0.25rem;
    }

    /* ============================================
       FORM ELEMENTS - Clean & Modern
    ============================================ */
    /* Labels */
    label, .stSelectbox label, .stNumberInput label, .stSlider label {
        font-size: 0.75rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.05em !important;
        text-transform: uppercase !important;
        color: #9CA3AF !important;
        margin-bottom: 0.5rem !important;
    }

    /* Number Input */
    .stNumberInput > div > div > input {
        background: rgba(30, 34, 44, 0.9) !important;
        border: 1px solid rgba(99, 102, 241, 0.2) !important;
        border-radius: 0.5rem !important;
        color: #F3F4F6 !important;
        font-size: 0.9rem !important;
        padding: 0.6rem 0.8rem !important;
        transition: all 0.2s ease !important;
    }

    .stNumberInput > div > div > input:focus {
        border-color: #6366F1 !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
        outline: none !important;
    }

    /* Selectbox */
    .stSelectbox > div > div {
        background: rgba(30, 34, 44, 0.9) !important;
        border: 1px solid rgba(99, 102, 241, 0.2) !important;
        border-radius: 0.5rem !important;
        color: #F3F4F6 !important;
    }

    .stSelectbox > div > div:hover {
        border-color: rgba(99, 102, 241, 0.4) !important;
    }

    /* Slider */
    [data-testid="stSlider"] > div > div > div {
        background: rgba(99, 102, 241, 0.2) !important;
    }

    [data-testid="stSlider"] div[role="slider"] {
        background: #6366F1 !important;
        border-color: #818CF8 !important;
        width: 1rem !important;
        height: 1rem !important;
    }

    /* Button - Primary Action */
    .stButton > button {
        background: linear-gradient(135deg, #4F46E5 0%, #6366F1 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 0.75rem !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        padding: 0.75rem 1.5rem !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        letter-spacing: 0.02em !important;
    }

    .stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 10px 20px -5px rgba(79, 70, 229, 0.4) !important;
        background: linear-gradient(135deg, #4338CA 0%, #4F46E5 100%) !important;
    }

    .stButton > button:active {
        transform: translateY(0px) !important;
    }

    /* ============================================
       RESULT DISPLAY CARDS
    ============================================ */
    .score-card {
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.1) 0%, rgba(99, 102, 241, 0.05) 100%);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 1rem;
        padding: 1.5rem;
        height: 100%;
        text-align: center;
    }

    .score-number {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FFFFFF 0%, #A5B4FC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
    }

    .score-label {
        font-size: 0.75rem;
        color: #9CA3AF;
        margin-top: 0.5rem;
    }

    .risk-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        border-radius: 2rem;
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 1rem;
    }

    .risk-high {
        background: rgba(239, 68, 68, 0.15);
        color: #F87171;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }

    .risk-medium {
        background: rgba(251, 191, 36, 0.15);
        color: #FBBF24;
        border: 1px solid rgba(251, 191, 36, 0.3);
    }

    .risk-low {
        background: rgba(52, 211, 153, 0.15);
        color: #34D399;
        border: 1px solid rgba(52, 211, 153, 0.3);
    }

    /* ============================================
       INSIGHTS SECTION
    ============================================ */
    .insights-card {
        background: rgba(17, 19, 24, 0.6);
        border: 1px solid rgba(99, 102, 241, 0.15);
        border-radius: 1rem;
        padding: 1.5rem;
        margin-top: 1rem;
    }

    .insight-item {
        display: flex;
        align-items: center;
        gap: 1rem;
        padding: 1rem 0;
        border-bottom: 1px solid rgba(99, 102, 241, 0.1);
    }

    .insight-item:last-child {
        border-bottom: none;
    }

    .insight-icon {
        width: 2.5rem;
        height: 2.5rem;
        background: rgba(99, 102, 241, 0.15);
        border-radius: 0.75rem;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.25rem;
    }

    .insight-content {
        flex: 1;
    }

    .insight-title {
        font-weight: 600;
        color: #F3F4F6;
        margin-bottom: 0.25rem;
    }

    .insight-description {
        font-size: 0.8rem;
        color: #9CA3AF;
    }

    /* ============================================
       PROGRESS BARS & METRICS
    ============================================ */
    .progress-bar {
        width: 100%;
        height: 0.5rem;
        background: rgba(99, 102, 241, 0.1);
        border-radius: 1rem;
        overflow: hidden;
        margin: 0.75rem 0;
    }

    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, #4F46E5 0%, #818CF8 100%);
        border-radius: 1rem;
        transition: width 0.6s ease;
    }

    /* ============================================
       UTILITY CLASSES
    ============================================ */
    .text-gradient {
        background: linear-gradient(135deg, #FFFFFF 0%, #A5B4FC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.3), transparent);
        margin: 1rem 0;
    }

    /* ============================================
       RESPONSIVE ADJUSTMENTS
    ============================================ */
    @media (max-width: 768px) {
        .block-container {
            padding: 1rem !important;
        }
        
        .kpi-value {
            font-size: 1.5rem !important;
        }
        
        .score-number {
            font-size: 2.5rem !important;
        }
    }

    /* ============================================
       STREAMLIT SPECIFIC OVERRIDES
    ============================================ */
    /* Fix column gaps */
    [data-testid="column"] {
        padding: 0 0.5rem !important;
    }

    /* Improve metric container */
    [data-testid="stMetricValue"] {
        font-size: 1.75rem !important;
        font-weight 700 !important;
        color: #F3F4F6 !important;
    }

    /* Remove default Streamlit borders */
    .stAlert, .stException, .stMarkdown {
        background: transparent !important;
    }

    /* Smooth scrolling */
    html {
        scroll-behavior: smooth;
    }

    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    ::-webkit-scrollbar-track {
        background: rgba(17, 19, 24, 0.8);
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb {
        background: rgba(99, 102, 241, 0.4);
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: rgba(99, 102, 241, 0.6);
    }
     /* ============================================
       MINIMAL RECOMMENDATIONS STYLE
    ============================================ */
    .rec-minimal-card {
        background: rgba(17, 19, 24, 0.6);
        border: 1px solid rgba(99, 102, 241, 0.15);
        border-radius: 12px;
        margin-top: 1rem;
        overflow: hidden;
    }
    
    .rec-minimal-header {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 1rem 1.25rem;
        border-bottom: 1px solid rgba(99, 102, 241, 0.1);
    }
    
    .rec-minimal-icon {
        font-size: 1rem;
        opacity: 0.8;
    }
    
    .rec-minimal-title {
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #9CA3AF;
    }
    
    .rec-minimal-list {
        padding: 0.5rem 1.25rem 1rem 1.25rem;
    }
    
    .rec-minimal-item {
        display: flex;
        align-items: flex-start;
        gap: 10px;
        padding: 0.6rem 0;
        border-bottom: 1px solid rgba(99, 102, 241, 0.05);
    }
    
    .rec-minimal-item:last-child {
        border-bottom: none;
    }
    
    .rec-minimal-check {
        color: #6366F1;
        font-size: 0.9rem;
        font-weight: 500;
        flex-shrink: 0;
    }
    
    .rec-minimal-text {
        color: #D1D5DB;
        font-size: 0.85rem;
        line-height: 1.5;
    }
    
    /* ============================================
       MINIMAL INSIGHTS STYLE
    ============================================ */
    .insight-minimal-card {
        background: rgba(17, 19, 24, 0.6);
        border: 1px solid rgba(99, 102, 241, 0.15);
        border-radius: 12px;
        margin-top: 1rem;
        overflow: hidden;
    }
    
    .insight-minimal-header {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 1rem 1.25rem;
        border-bottom: 1px solid rgba(99, 102, 241, 0.1);
        flex-wrap: wrap;
    }
    
    .insight-minimal-icon-header {
        font-size: 1rem;
        opacity: 0.8;
    }
    
    .insight-minimal-title {
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #9CA3AF;
        flex: 1;
    }
    
    .insight-minimal-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #818CF8;
        background: rgba(99, 102, 241, 0.1);
        padding: 0.2rem 0.5rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .insight-minimal-list {
        padding: 0.25rem 1.25rem 0.75rem 1.25rem;
    }
    
    .insight-minimal-item {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 0.8rem 0;
        border-bottom: 1px solid rgba(99, 102, 241, 0.05);
    }
    
    .insight-minimal-item:last-child {
        border-bottom: none;
    }
    
    .insight-minimal-icon {
        font-size: 1.2rem;
        flex-shrink: 0;
        width: 28px;
        text-align: center;
    }
    
    .insight-minimal-content {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        flex-wrap: wrap;
    }
    
    .insight-minimal-text {
        color: #E5E7EB;
        font-size: 0.85rem;
        line-height: 1.4;
        flex: 1;
    }
    
    .insight-minimal-meta {
        display: flex;
        align-items: center;
        gap: 4px;
        flex-shrink: 0;
    }
    
    .insight-minimal-score {
        font-size: 0.75rem;
        font-weight: 600;
    }
    
    .insight-minimal-impact {
        font-size: 0.65rem;
        color: #6B7280;
    }
    
    /* Hover effects */
    .rec-minimal-item:hover .rec-minimal-text,
    .insight-minimal-item:hover .insight-minimal-text {
        color: #F3F4F6;
    }
    
    .rec-minimal-item:hover,
    .insight-minimal-item:hover {
        background: rgba(99, 102, 241, 0.03);
        margin: 0 -0.5rem;
        padding: 0.6rem 0.5rem;
        border-radius: 8px;
    }
    
    .rec-minimal-item:hover .rec-minimal-check {
        transform: translateX(2px);
        transition: transform 0.2s ease;
    }
    
    /* Responsive */
    @media (max-width: 640px) {
        .insight-minimal-content {
            flex-direction: column;
            align-items: flex-start;
            gap: 0.4rem;
        }
        
        .rec-minimal-header,
        .insight-minimal-header {
            padding: 0.8rem 1rem;
        }
        
        .rec-minimal-list,
        .insight-minimal-list {
            padding: 0.25rem 1rem 0.75rem 1rem;
        }
    }
    
    /* ============================================
       END MINIMAL STYLES
    ============================================ */   
       /* ============================================
       MINIMAL RISK GAUGE STYLE
    ============================================ */
    .gauge-minimal-card {
        background: rgba(17, 19, 24, 0.6);
        border: 1px solid rgba(99, 102, 241, 0.15);
        border-radius: 12px;
        margin-top: 1rem;
        overflow: hidden;
    }
    
    .gauge-minimal-header {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 1rem 1.25rem;
        border-bottom: 1px solid rgba(99, 102, 241, 0.1);
    }
    
    .gauge-minimal-icon {
        font-size: 1rem;
        opacity: 0.8;
    }
    
    .gauge-minimal-title {
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #9CA3AF;
        flex: 1;
    }
    
    .gauge-minimal-badge {
        font-size: 0.65rem;
        font-weight: 600;
        padding: 0.25rem 0.6rem;
        border-radius: 20px;
        letter-spacing: 0.03em;
    }
    
    .gauge-minimal-container {
        padding: 0.5rem 1rem 0rem 1rem;
    }
    
    /* Plotly chart container adjustments */
    .gauge-minimal-container .plotly-container {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    .gauge-minimal-footer {
        padding: 0rem 1.25rem 1.25rem 1.25rem;
        text-align: center;
    }
    
    .gauge-confidence {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        padding: 0.5rem 0rem 0.25rem 0rem;
        border-top: 1px solid rgba(99, 102, 241, 0.08);
    }
    
    .confidence-label {
        font-size: 0.7rem;
        font-weight: 500;
        color: #6B7280;
        letter-spacing: 0.02em;
    }
    
    .confidence-value {
        font-size: 0.85rem;
        font-weight: 700;
    }
    
    /* Hover effect */
    .gauge-minimal-card:hover {
        border-color: rgba(99, 102, 241, 0.25);
        transition: all 0.2s ease;
    }
    
    /* Responsive */
    @media (max-width: 640px) {
        .gauge-minimal-header {
            padding: 0.8rem 1rem;
        }
        
        .gauge-minimal-container {
            padding: 0.25rem 0.75rem 0rem 0.75rem;
        }
        
        .gauge-minimal-footer {
            padding: 0rem 1rem 1rem 1rem;
        }
        
        .gauge-confidence {
            padding: 0.4rem 0rem 0.15rem 0rem;
        }
    }
    
    /* ============================================
       END RISK GAUGE STYLES
    ============================================ */  
      /* ============================================
       MINIMAL STUDENT PROFILE STYLE
    ============================================ */
    .profile-minimal-card {
        background: rgba(17, 19, 24, 0.6);
        border: 1px solid rgba(99, 102, 241, 0.15);
        border-radius: 12px;
        margin-bottom: 1rem;
        overflow: hidden;
    }
    
    .profile-minimal-header {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 1rem 1.25rem;
        border-bottom: 1px solid rgba(99, 102, 241, 0.1);
    }
    
    .profile-minimal-icon {
        font-size: 1rem;
        opacity: 0.8;
    }
    
    .profile-minimal-title {
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #9CA3AF;
        flex: 1;
    }
    
    .profile-minimal-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #818CF8;
        background: rgba(99, 102, 241, 0.1);
        padding: 0.2rem 0.5rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .profile-minimal-container {
        padding: 1.25rem;
    }
    
    /* Form field spacing */
    .profile-minimal-container .stNumberInput,
    .profile-minimal-container .stSelectbox,
    .profile-minimal-container .stToggle {
        margin-bottom: 0.5rem;
    }
    
    /* Style form labels to match minimal design */
    .profile-minimal-container label {
        font-size: 0.7rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.03em !important;
        text-transform: uppercase !important;
        color: #9CA3AF !important;
        margin-bottom: 0.4rem !important;
    }
    
    /* Style inputs to match card theme */
    .profile-minimal-container .stNumberInput input,
    .profile-minimal-container .stSelectbox select {
        background: rgba(30, 34, 44, 0.6) !important;
        border: 1px solid rgba(99, 102, 241, 0.15) !important;
        border-radius: 8px !important;
        color: #F3F4F6 !important;
        font-size: 0.85rem !important;
        padding: 0.5rem 0.75rem !important;
    }
    
    .profile-minimal-container .stNumberInput input:focus,
    .profile-minimal-container .stSelectbox select:focus {
        border-color: rgba(99, 102, 241, 0.4) !important;
        box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.1) !important;
    }
    
    /* Toggle styling */
    .profile-minimal-container .stToggle {
        background: rgba(30, 34, 44, 0.4);
        border: 1px solid rgba(99, 102, 241, 0.1);
        border-radius: 8px;
        padding: 0.6rem 1rem !important;
        margin: 0.5rem 0;
    }
    
    .profile-minimal-container .stToggle:hover {
        background: rgba(30, 34, 44, 0.6);
        border-color: rgba(99, 102, 241, 0.2);
    }
    
    /* Selectbox dropdown styling */
    .profile-minimal-container .stSelectbox > div > div {
        background: rgba(30, 34, 44, 0.6) !important;
        border: 1px solid rgba(99, 102, 241, 0.15) !important;
        border-radius: 8px !important;
    }
    
    /* Number input buttons */
    .profile-minimal-container .stNumberInput button {
        background: rgba(99, 102, 241, 0.1) !important;
        border: none !important;
        color: #9CA3AF !important;
    }
    
    .profile-minimal-container .stNumberInput button:hover {
        background: rgba(99, 102, 241, 0.2) !important;
        color: #F3F4F6 !important;
    }
    
    /* Hover effect for the whole card */
    .profile-minimal-card:hover {
        border-color: rgba(99, 102, 241, 0.25);
        transition: all 0.2s ease;
    }
    
    /* Responsive */
    @media (max-width: 640px) {
        .profile-minimal-header {
            padding: 0.8rem 1rem;
        }
        
        .profile-minimal-container {
            padding: 1rem;
        }
        
        .profile-minimal-title {
            font-size: 0.75rem;
        }
    }
    
    /* ============================================
       END STUDENT PROFILE STYLES
    ============================================ */            
      /* ============================================
       MINIMAL ACADEMIC HISTORY STYLE
    ============================================ */
    .academic-minimal-card {
        background: rgba(17, 19, 24, 0.6);
        border: 1px solid rgba(99, 102, 241, 0.15);
        border-radius: 12px;
        margin-bottom: 1rem;
        overflow: hidden;
    }
    
    .academic-minimal-header {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 1rem 1.25rem;
        border-bottom: 1px solid rgba(99, 102, 241, 0.1);
    }
    
    .academic-minimal-icon {
        font-size: 1rem;
        opacity: 0.8;
    }
    
    .academic-minimal-title {
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #9CA3AF;
        flex: 1;
    }
    
    .academic-minimal-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #818CF8;
        background: rgba(99, 102, 241, 0.1);
        padding: 0.2rem 0.5rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .academic-minimal-container {
        padding: 1.25rem;
    }
    
    /* Form field spacing */
    .academic-minimal-container .stNumberInput {
        margin-bottom: 0.5rem;
    }
    
    /* Style form labels to match minimal design */
    .academic-minimal-container label {
        font-size: 0.7rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.03em !important;
        text-transform: uppercase !important;
        color: #9CA3AF !important;
        margin-bottom: 0.4rem !important;
    }
    
    /* Number input styling */
    .academic-minimal-container .stNumberInput input {
        background: rgba(30, 34, 44, 0.6) !important;
        border: 1px solid rgba(99, 102, 241, 0.15) !important;
        border-radius: 8px !important;
        color: #F3F4F6 !important;
        font-size: 0.85rem !important;
        padding: 0.5rem 0.75rem !important;
        width: 100% !important;
    }
    
    .academic-minimal-container .stNumberInput input:focus {
        border-color: rgba(99, 102, 241, 0.4) !important;
        box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.1) !important;
        outline: none !important;
    }
    
    /* Number input buttons */
    .academic-minimal-container .stNumberInput button {
        background: rgba(99, 102, 241, 0.1) !important;
        border: none !important;
        color: #9CA3AF !important;
        transition: all 0.2s ease !important;
    }
    
    .academic-minimal-container .stNumberInput button:hover {
        background: rgba(99, 102, 241, 0.2) !important;
        color: #F3F4F6 !important;
    }
    
    /* Column spacing */
    .academic-minimal-container [data-testid="column"] {
        gap: 1rem !important;
    }
    
    /* Card hover effect */
    .academic-minimal-card:hover {
        border-color: rgba(99, 102, 241, 0.25);
        transition: all 0.2s ease;
    }
    
    /* Responsive */
    @media (max-width: 640px) {
        .academic-minimal-header {
            padding: 0.8rem 1rem;
        }
        
        .academic-minimal-container {
            padding: 1rem;
        }
        
        .academic-minimal-title {
            font-size: 0.75rem;
        }
        
        .academic-minimal-container .stNumberInput input {
            font-size: 0.8rem !important;
            padding: 0.4rem 0.6rem !important;
        }
        
        .academic-minimal-container [data-testid="column"] {
            gap: 0.75rem !important;
        }
    }
    
    /* Optional: Add visual indicator for required fields */
    .academic-minimal-container .stNumberInput label:after {
        content: " *";
        color: #818CF8;
        font-size: 0.65rem;
    }
    
    /* ============================================
       END ACADEMIC HISTORY STYLES
    ============================================ */
     /* ============================================
       MINIMAL ACTIVE ENGAGEMENT STYLE
    ============================================ */
    .engagement-minimal-card {
        background: rgba(17, 19, 24, 0.6);
        border: 1px solid rgba(99, 102, 241, 0.15);
        border-radius: 12px;
        margin-bottom: 1rem;
        overflow: hidden;
    }
    
    .engagement-minimal-header {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 1rem 1.25rem;
        border-bottom: 1px solid rgba(99, 102, 241, 0.1);
    }
    
    .engagement-minimal-icon {
        font-size: 1rem;
        opacity: 0.8;
    }
    
    .engagement-minimal-title {
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #9CA3AF;
        flex: 1;
    }
    
    .engagement-minimal-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #818CF8;
        background: rgba(99, 102, 241, 0.1);
        padding: 0.2rem 0.5rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .engagement-minimal-container {
        padding: 1.25rem;
    }
    
    /* Form field spacing */
    .engagement-minimal-container .stSlider,
    .engagement-minimal-container .stNumberInput,
    .engagement-minimal-container .stSelectbox {
        margin-bottom: 0.75rem;
    }
    
    /* Style form labels to match minimal design */
    .engagement-minimal-container label {
        font-size: 0.7rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.03em !important;
        text-transform: uppercase !important;
        color: #9CA3AF !important;
        margin-bottom: 0.4rem !important;
    }
    
    /* Slider styling */
    .engagement-minimal-container [data-testid="stSlider"] {
        margin: 0.5rem 0 1rem 0;
    }
    
    .engagement-minimal-container [data-testid="stSlider"] > div > div > div {
        background: rgba(99, 102, 241, 0.15) !important;
    }
    
    .engagement-minimal-container [data-testid="stSlider"] div[role="slider"] {
        background: #6366F1 !important;
        border-color: #818CF8 !important;
        width: 0.9rem !important;
        height: 0.9rem !important;
    }
    
    .engagement-minimal-container [data-testid="stSlider"] div[role="slider"]:hover {
        transform: scale(1.1) !important;
        background: #818CF8 !important;
    }
    
    /* Value display for slider */
    .engagement-minimal-container [data-testid="stSlider"] output {
        color: #F3F4F6 !important;
        font-size: 0.8rem !important;
        font-weight: 600 !important;
    }
    
    /* Number input styling */
    .engagement-minimal-container .stNumberInput input {
        background: rgba(30, 34, 44, 0.6) !important;
        border: 1px solid rgba(99, 102, 241, 0.15) !important;
        border-radius: 8px !important;
        color: #F3F4F6 !important;
        font-size: 0.85rem !important;
        padding: 0.5rem 0.75rem !important;
    }
    
    .engagement-minimal-container .stNumberInput input:focus {
        border-color: rgba(99, 102, 241, 0.4) !important;
        box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.1) !important;
    }
    
    /* Number input buttons */
    .engagement-minimal-container .stNumberInput button {
        background: rgba(99, 102, 241, 0.1) !important;
        border: none !important;
        color: #9CA3AF !important;
    }
    
    .engagement-minimal-container .stNumberInput button:hover {
        background: rgba(99, 102, 241, 0.2) !important;
        color: #F3F4F6 !important;
    }
    
    /* Selectbox styling */
    .engagement-minimal-container .stSelectbox > div > div {
        background: rgba(30, 34, 44, 0.6) !important;
        border: 1px solid rgba(99, 102, 241, 0.15) !important;
        border-radius: 8px !important;
        color: #F3F4F6 !important;
    }
    
    .engagement-minimal-container .stSelectbox > div > div:hover {
        border-color: rgba(99, 102, 241, 0.3) !important;
    }
    
    .engagement-minimal-container .stSelectbox > div > div:focus-within {
        border-color: rgba(99, 102, 241, 0.4) !important;
        box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.1) !important;
    }
    
    /* Dropdown menu styling */
    .engagement-minimal-container .stSelectbox div[data-baseweb="popover"] {
        background: rgba(30, 34, 44, 0.95) !important;
        border: 1px solid rgba(99, 102, 241, 0.2) !important;
        border-radius: 8px !important;
    }
    
    /* Column spacing */
    .engagement-minimal-container [data-testid="column"] {
        gap: 0.75rem !important;
    }
    
    /* Card hover effect */
    .engagement-minimal-card:hover {
        border-color: rgba(99, 102, 241, 0.25);
        transition: all 0.2s ease;
    }
    
    /* Responsive */
    @media (max-width: 640px) {
        .engagement-minimal-header {
            padding: 0.8rem 1rem;
        }
        
        .engagement-minimal-container {
            padding: 1rem;
        }
        
        .engagement-minimal-title {
            font-size: 0.75rem;
        }
        
        .engagement-minimal-container .stNumberInput input {
            font-size: 0.8rem !important;
            padding: 0.4rem 0.6rem !important;
        }
    }
    
    /* ============================================
       END ACTIVE ENGAGEMENT STYLES
    ============================================ */     
    /* ============================================
       ANALYTICS DASHBOARD STYLES
    ============================================ */
    
    /* Header Card */
    .analytics-header-card {
        background: linear-gradient(135deg, #111318 0%, #1a1d24 100%);
        border: 1px solid #2a2f3d;
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .analytics-header-left {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .analytics-header-icon {
        font-size: 2rem;
        opacity: 0.9;
    }
    
    .analytics-header-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: -0.3px;
        margin-bottom: 0.25rem;
    }
    
    .analytics-header-subtitle {
        font-size: 0.8rem;
        color: #9ca3af;
    }
    
    .analytics-header-right {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .analytics-header-badge {
        font-size: 0.7rem;
        font-weight: 600;
        color: #10b981;
        background: rgba(16, 185, 129, 0.1);
        padding: 0.3rem 1rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }
    
    /* Divider */
    .analytics-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #2a2f3d, transparent);
        margin: 1.5rem 0;
    }
    
    /* Chart Cards */
    .chart-minimal-card {
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 1rem;
        transition: all 0.2s ease;
    }
    
    .chart-minimal-card:hover {
        border-color: #3a4050;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    
    .chart-minimal-header {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 1rem 1.25rem;
        background: rgba(99, 102, 241, 0.05);
        border-bottom: 1px solid #2a2f3d;
    }
    
    .chart-minimal-icon {
        font-size: 1.1rem;
        opacity: 0.8;
    }
    
    .chart-minimal-title {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #d1d5db;
        flex: 1;
    }
    
    .chart-minimal-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #818cf8;
        background: rgba(99, 102, 241, 0.15);
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .chart-minimal-container {
        padding: 0.75rem;
    }
    
    /* Table Card */
    .table-minimal-card {
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        overflow: hidden;
        margin-top: 0.5rem;
        transition: all 0.2s ease;
    }
    
    .table-minimal-card:hover {
        border-color: #3a4050;
    }
    
    .table-minimal-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 1.25rem;
        background: rgba(99, 102, 241, 0.05);
        border-bottom: 1px solid #2a2f3d;
    }
    
    .table-minimal-header-left {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .table-minimal-icon {
        font-size: 1.1rem;
        opacity: 0.8;
    }
    
    .table-minimal-title {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #d1d5db;
    }
    
    .table-minimal-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #818cf8;
        background: rgba(99, 102, 241, 0.15);
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .table-minimal-container {
        padding: 1rem;
    }
    
    /* DataFrame Styling */
    .stDataFrame {
        background: transparent !important;
        border: none !important;
    }
    
    .stDataFrame [data-testid="stElementDataFrame"] {
        border-radius: 8px !important;
        overflow: hidden !important;
    }
    
    /* Empty state */
    .analytics-empty-state {
        text-align: center;
        padding: 3rem 2rem;
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        margin: 2rem 0;
    }
    
    .empty-state-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        opacity: 0.5;
    }
    
    .empty-state-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #f3f4f6;
        margin-bottom: 0.5rem;
    }
    
    .empty-state-text {
        font-size: 0.85rem;
        color: #9ca3af;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .analytics-header-card {
            flex-direction: column;
            text-align: center;
            gap: 1rem;
            padding: 1rem;
        }
        
        .analytics-header-left {
            flex-direction: column;
            text-align: center;
        }
        
        .analytics-header-title {
            font-size: 1.1rem;
        }
        
        .analytics-header-subtitle {
            font-size: 0.7rem;
        }
        
        .chart-minimal-header,
        .table-minimal-header {
            padding: 0.75rem 1rem;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        
        .chart-minimal-title,
        .table-minimal-title {
            font-size: 0.7rem;
        }
        
        .chart-minimal-container {
            padding: 0.5rem;
        }
        
        .table-minimal-container {
            padding: 0.75rem;
            overflow-x: auto;
        }
    }
    
    /* Print styles */
    @media print {
        .analytics-header-card,
        .chart-minimal-card,
        .table-minimal-card {
            break-inside: avoid;
            border: 1px solid #ddd;
        }
        
        .analytics-header-badge {
            color: #000;
            border-color: #ddd;
        }
    }
    
    /* ============================================
       END ANALYTICS DASHBOARD STYLES
    ============================================ */
      /* ============================================
       FACULTY INTERVENTION STYLES
    ============================================ */
    
    /* Header Card */
    .intervention-header-card {
        background: linear-gradient(135deg, #111318 0%, #1a1d24 100%);
        border: 1px solid #2a2f3d;
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .intervention-header-left {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .intervention-header-icon {
        font-size: 2rem;
        opacity: 0.9;
    }
    
    .intervention-header-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: -0.3px;
        margin-bottom: 0.25rem;
    }
    
    .intervention-header-subtitle {
        font-size: 0.8rem;
        color: #9ca3af;
    }
    
    .intervention-header-right {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .intervention-header-badge {
        font-size: 0.7rem;
        font-weight: 600;
        color: #ef4444;
        background: rgba(239, 68, 68, 0.1);
        padding: 0.3rem 1rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
        border: 1px solid rgba(239, 68, 68, 0.3);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.7;
        }
    }
    
    /* Metric Cards */
    .intervention-metric-card {
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        padding: 1.25rem;
        text-align: center;
        transition: all 0.2s ease;
    }
    
    .intervention-metric-card:hover {
        border-color: #3a4050;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    
    .metric-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #f3f4f6;
        letter-spacing: -0.5px;
        margin-bottom: 0.25rem;
    }
    
    .metric-label {
        font-size: 0.75rem;
        font-weight: 500;
        color: #9ca3af;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Divider */
    .intervention-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #2a2f3d, transparent);
        margin: 1.5rem 0;
    }
    
    /* Table Card */
    .intervention-table-card {
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .intervention-table-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 1.25rem;
        background: rgba(99, 102, 241, 0.05);
        border-bottom: 1px solid #2a2f3d;
    }
    
    .intervention-table-header-left {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .intervention-table-icon {
        font-size: 1.1rem;
        opacity: 0.8;
    }
    
    .intervention-table-title {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #d1d5db;
    }
    
    .intervention-table-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #ef4444;
        background: rgba(239, 68, 68, 0.15);
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .intervention-table-container {
        padding: 1rem;
    }
    
    /* Form Card */
    .intervention-form-card {
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .intervention-form-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 1.25rem;
        background: rgba(99, 102, 241, 0.05);
        border-bottom: 1px solid #2a2f3d;
    }
    
    .intervention-form-header-left {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .intervention-form-icon {
        font-size: 1.1rem;
        opacity: 0.8;
    }
    
    .intervention-form-title {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #d1d5db;
    }
    
    .intervention-form-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #818cf8;
        background: rgba(99, 102, 241, 0.15);
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .intervention-form-container {
        padding: 1.25rem;
    }
    
    /* Form element spacing */
    .intervention-form-container .stSelectbox,
    .intervention-form-container .stTextInput {
        margin-bottom: 1rem;
    }
    
    /* Empty State */
    .intervention-empty-state {
        text-align: center;
        padding: 3rem 2rem;
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        margin: 2rem 0;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .intervention-header-card {
            flex-direction: column;
            text-align: center;
            gap: 1rem;
            padding: 1rem;
        }
        
        .intervention-header-left {
            flex-direction: column;
        }
        
        .intervention-header-title {
            font-size: 1.1rem;
        }
        
        .intervention-header-subtitle {
            font-size: 0.7rem;
        }
        
        .metric-value {
            font-size: 1.5rem;
        }
        
        .metric-icon {
            font-size: 1.5rem;
        }
        
        .intervention-table-header,
        .intervention-form-header {
            padding: 0.75rem 1rem;
        }
        
        .intervention-table-title,
        .intervention-form-title {
            font-size: 0.7rem;
        }
        
        .intervention-table-container,
        .intervention-form-container {
            padding: 0.75rem;
        }
    }
    
    /* ============================================
       END FACULTY INTERVENTION STYLES
    ============================================ */   

      /* ============================================
       MODEL PERFORMANCE STYLES
    ============================================ */
    
    /* Header Card */
    .performance-header-card {
        background: linear-gradient(135deg, #111318 0%, #1a1d24 100%);
        border: 1px solid #2a2f3d;
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .performance-header-left {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .performance-header-icon {
        font-size: 2rem;
        opacity: 0.9;
    }
    
    .performance-header-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: -0.3px;
        margin-bottom: 0.25rem;
    }
    
    .performance-header-subtitle {
        font-size: 0.8rem;
        color: #9ca3af;
    }
    
    .performance-header-right {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .performance-header-badge {
        font-size: 0.7rem;
        font-weight: 600;
        color: #10b981;
        background: rgba(16, 185, 129, 0.1);
        padding: 0.3rem 1rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }
    
    /* Section Header */
    .performance-section-header {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1.5rem;
        padding: 1rem;
        background: rgba(99, 102, 241, 0.05);
        border-radius: 12px;
        border-left: 4px solid #6366F1;
    }
    
    .section-header-icon {
        font-size: 2rem;
    }
    
    .section-header-content {
        flex: 1;
    }
    
    .section-header-title {
        font-size: 0.75rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #9ca3af;
    }
    
    .section-header-subtitle {
        font-size: 1.1rem;
        font-weight: 700;
        color: #f3f4f6;
        margin-top: 0.25rem;
    }
    
    /* Metric Cards */
    .performance-metric-card {
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        padding: 1.25rem;
        text-align: center;
        transition: all 0.2s ease;
    }
    
    .performance-metric-card:hover {
        border-color: #3a4050;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    
    /* Divider */
    .performance-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #2a2f3d, transparent);
        margin: 1.5rem 0;
    }
    
    /* Table Card */
    .performance-table-card {
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .performance-table-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 1.25rem;
        background: rgba(99, 102, 241, 0.05);
        border-bottom: 1px solid #2a2f3d;
    }
    
    .performance-table-header-left {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .performance-table-icon {
        font-size: 1.1rem;
        opacity: 0.8;
    }
    
    .performance-table-title {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #d1d5db;
    }
    
    .performance-table-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #818cf8;
        background: rgba(99, 102, 241, 0.15);
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .performance-table-container {
        padding: 1rem;
    }
    
    /* Chart Card */
    .performance-chart-card {
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .performance-chart-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 1.25rem;
        background: rgba(99, 102, 241, 0.05);
        border-bottom: 1px solid #2a2f3d;
    }
    
    .performance-chart-header-left {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .performance-chart-icon {
        font-size: 1.1rem;
        opacity: 0.8;
    }
    
    .performance-chart-title {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #d1d5db;
    }
    
    .performance-chart-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #818cf8;
        background: rgba(99, 102, 241, 0.15);
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .performance-chart-container {
        padding: 1rem;
    }
    
    /* Image Card */
    .performance-image-card {
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        overflow: hidden;
        margin: 0.5rem 0;
        height: 100%;
    }
    
    .performance-image-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 1.25rem;
        background: rgba(99, 102, 241, 0.05);
        border-bottom: 1px solid #2a2f3d;
    }
    
    .performance-image-header-left {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .performance-image-icon {
        font-size: 1.1rem;
        opacity: 0.8;
    }
    
    .performance-image-title {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #d1d5db;
    }
    
    .performance-image-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #818cf8;
        background: rgba(99, 102, 241, 0.15);
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .performance-image-container {
        padding: 1rem;
    }
    
    /* Insights Card */
    .performance-insights-card {
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .performance-insights-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 1.25rem;
        background: rgba(99, 102, 241, 0.05);
        border-bottom: 1px solid #2a2f3d;
    }
    
    .performance-insights-header-left {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .performance-insights-icon {
        font-size: 1.1rem;
        opacity: 0.8;
    }
    
    .performance-insights-title {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #d1d5db;
    }
    
    .performance-insights-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #10b981;
        background: rgba(16, 185, 129, 0.15);
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .performance-insights-container {
        padding: 1.25rem;
    }
    
    .insight-item {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        padding: 0.75rem 0;
        border-bottom: 1px solid rgba(99, 102, 241, 0.1);
    }
    
    .insight-item:last-child {
        border-bottom: none;
    }
    
    .insight-icon {
        font-size: 1.1rem;
        flex-shrink: 0;
    }
    
    .insight-text {
        font-size: 0.85rem;
        color: #d1d5db;
        line-height: 1.5;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .performance-header-card {
            flex-direction: column;
            text-align: center;
            gap: 1rem;
            padding: 1rem;
        }
        
        .performance-header-left {
            flex-direction: column;
        }
        
        .performance-header-title {
            font-size: 1.1rem;
        }
        
        .performance-metric-card .metric-value {
            font-size: 1.5rem;
        }
        
        .performance-table-container,
        .performance-chart-container,
        .performance-image-container,
        .performance-insights-container {
            padding: 0.75rem;
            overflow-x: auto;
        }
        
        .insight-text {
            font-size: 0.75rem;
        }
    }
    
    /* ============================================
       END MODEL PERFORMANCE STYLES
    ============================================ */      

     /* ============================================
       STUDENT RISK HISTORY STYLES
    ============================================ */
    
    /* Header Card */
    .history-header-card {
        background: linear-gradient(135deg, #111318 0%, #1a1d24 100%);
        border: 1px solid #2a2f3d;
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .history-header-left {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .history-header-icon {
        font-size: 2rem;
        opacity: 0.9;
    }
    
    .history-header-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: -0.3px;
        margin-bottom: 0.25rem;
    }
    
    .history-header-subtitle {
        font-size: 0.8rem;
        color: #9ca3af;
    }
    
    .history-header-right {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .history-header-badge {
        font-size: 0.7rem;
        font-weight: 600;
        color: #818cf8;
        background: rgba(99, 102, 241, 0.1);
        padding: 0.3rem 1rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
        border: 1px solid rgba(99, 102, 241, 0.3);
    }
    
    /* Filters Card */
    .history-filters-card {
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .history-filters-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 1.25rem;
        background: rgba(99, 102, 241, 0.05);
        border-bottom: 1px solid #2a2f3d;
    }
    
    .history-filters-header-left {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .history-filters-icon {
        font-size: 1.1rem;
        opacity: 0.8;
    }
    
    .history-filters-title {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #d1d5db;
    }
    
    .history-filters-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #818cf8;
        background: rgba(99, 102, 241, 0.15);
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .history-filters-container {
        padding: 1.25rem;
    }
    
    /* Form elements within filters */
    .history-filters-container .stSelectbox,
    .history-filters-container .stSlider {
        margin-bottom: 0.5rem;
    }
    
    /* Stats Card */
    .history-stats-card {
        background: rgba(99, 102, 241, 0.05);
        border: 1px solid rgba(99, 102, 241, 0.15);
        border-radius: 12px;
        padding: 1rem;
        margin: 1rem 0;
        text-align: center;
    }
    
    .history-stats-content {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.75rem;
    }
    
    .stats-icon {
        font-size: 1.5rem;
        opacity: 0.8;
    }
    
    .stats-text {
        display: flex;
        align-items: baseline;
        gap: 0.5rem;
        flex-wrap: wrap;
        justify-content: center;
    }
    
    .stats-count {
        font-size: 1.5rem;
        font-weight: 700;
        color: #f3f4f6;
    }
    
    .stats-label {
        font-size: 0.85rem;
        color: #9ca3af;
    }
    
    /* Divider */
    .history-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #2a2f3d, transparent);
        margin: 1.5rem 0;
    }
    
    /* Table Card */
    .history-table-card {
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .history-table-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 1.25rem;
        background: rgba(99, 102, 241, 0.05);
        border-bottom: 1px solid #2a2f3d;
    }
    
    .history-table-header-left {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .history-table-icon {
        font-size: 1.1rem;
        opacity: 0.8;
    }
    
    .history-table-title {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #d1d5db;
    }
    
    .history-table-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #818cf8;
        background: rgba(99, 102, 241, 0.15);
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .history-table-container {
        padding: 1rem;
    }
    
    /* Export Card */
    .history-export-card {
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .history-export-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 1.25rem;
        background: rgba(99, 102, 241, 0.05);
        border-bottom: 1px solid #2a2f3d;
    }
    
    .history-export-header-left {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .history-export-icon {
        font-size: 1.1rem;
        opacity: 0.8;
    }
    
    .history-export-title {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #d1d5db;
    }
    
    .history-export-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #10b981;
        background: rgba(16, 185, 129, 0.15);
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .history-export-container {
        padding: 1.25rem;
    }
    
    /* Empty State */
    .history-empty-state {
        text-align: center;
        padding: 3rem 2rem;
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        margin: 2rem 0;
    }
    
    /* Dataframe Styling */
    .stDataFrame {
        background: transparent !important;
        border: none !important;
    }
    
    .stDataFrame [data-testid="stElementDataFrame"] {
        border-radius: 8px !important;
        overflow: hidden !important;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .history-header-card {
            flex-direction: column;
            text-align: center;
            gap: 1rem;
            padding: 1rem;
        }
        
        .history-header-left {
            flex-direction: column;
        }
        
        .history-header-title {
            font-size: 1.1rem;
        }
        
        .history-header-subtitle {
            font-size: 0.7rem;
        }
        
        .history-filters-container,
        .history-table-container,
        .history-export-container {
            padding: 0.75rem;
        }
        
        .stats-count {
            font-size: 1.25rem;
        }
        
        .stats-icon {
            font-size: 1.25rem;
        }
        
        .history-table-header,
        .history-filters-header,
        .history-export-header {
            padding: 0.75rem 1rem;
        }
        
        .history-table-title,
        .history-filters-title,
        .history-export-title {
            font-size: 0.7rem;
        }
    }
    
    /* ============================================
       END STUDENT RISK HISTORY STYLES
    ============================================ */     

     /* ============================================
       STUDENT SEGMENTATION STYLES
    ============================================ */
    
    /* Header Card */
    .segmentation-header-card {
        background: linear-gradient(135deg, #111318 0%, #1a1d24 100%);
        border: 1px solid #2a2f3d;
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .segmentation-header-left {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .segmentation-header-icon {
        font-size: 2rem;
        opacity: 0.9;
    }
    
    .segmentation-header-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: -0.3px;
        margin-bottom: 0.25rem;
    }
    
    .segmentation-header-subtitle {
        font-size: 0.8rem;
        color: #9ca3af;
    }
    
    .segmentation-header-right {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .segmentation-header-badge {
        font-size: 0.7rem;
        font-weight: 600;
        color: #818cf8;
        background: rgba(99, 102, 241, 0.1);
        padding: 0.3rem 1rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
        border: 1px solid rgba(99, 102, 241, 0.3);
    }
    
    /* Chart Cards */
    .segmentation-chart-card {
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        overflow: hidden;
        margin: 1rem 0;
    }
    
    .segmentation-chart-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 1.25rem;
        background: rgba(99, 102, 241, 0.05);
        border-bottom: 1px solid #2a2f3d;
    }
    
    .segmentation-chart-header-left {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .segmentation-chart-icon {
        font-size: 1.1rem;
        opacity: 0.8;
    }
    
    .segmentation-chart-title {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #d1d5db;
    }
    
    .segmentation-chart-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #818cf8;
        background: rgba(99, 102, 241, 0.15);
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .segmentation-chart-container {
        padding: 1rem;
    }
    
    /* Table Card */
    .segmentation-table-card {
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        overflow: hidden;
        margin: 1rem 0;
    }
    
    .segmentation-table-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 1.25rem;
        background: rgba(99, 102, 241, 0.05);
        border-bottom: 1px solid #2a2f3d;
    }
    
    .segmentation-table-header-left {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .segmentation-table-icon {
        font-size: 1.1rem;
        opacity: 0.8;
    }
    
    .segmentation-table-title {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #d1d5db;
    }
    
    .segmentation-table-badge {
        font-size: 0.65rem;
        font-weight: 500;
        color: #ef4444;
        background: rgba(239, 68, 68, 0.15);
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        letter-spacing: 0.02em;
    }
    
    .segmentation-table-container {
        padding: 1rem;
    }
    
    /* Divider */
    .segmentation-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #2a2f3d, transparent);
        margin: 1rem 0;
    }
    
    /* Empty State */
    .segmentation-empty-state {
        text-align: center;
        padding: 3rem 2rem;
        background: #111318;
        border: 1px solid #2a2f3d;
        border-radius: 12px;
        margin: 2rem 0;
    }
    
    .empty-state-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        opacity: 0.5;
    }
    
    .empty-state-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #f3f4f6;
        margin-bottom: 0.5rem;
    }
    
    .empty-state-text {
        font-size: 0.85rem;
        color: #9ca3af;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .segmentation-header-card {
            flex-direction: column;
            text-align: center;
            gap: 1rem;
            padding: 1rem;
        }
        
        .segmentation-header-left {
            flex-direction: column;
        }
        
        .segmentation-header-title {
            font-size: 1.1rem;
        }
        
        .segmentation-header-subtitle {
            font-size: 0.7rem;
        }
        
        .segmentation-chart-header,
        .segmentation-table-header {
            padding: 0.75rem 1rem;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        
        .segmentation-chart-title,
        .segmentation-table-title {
            font-size: 0.7rem;
        }
        
        .segmentation-chart-container,
        .segmentation-table-container {
            padding: 0.75rem;
            overflow-x: auto;
        }
    }
    
    /* ============================================
       END STUDENT SEGMENTATION STYLES
    ============================================ */                                          
                       
    </style>
    """, unsafe_allow_html=True)


# Example usage function for the KPI cards
def render_kpi_cards(summary):
    """Render professional KPI cards using the new styling"""
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    cards_data = [
        {"title": "Total Predictions", "value": summary.get("total_predictions", 0), 
         "sub": "Records", "icon": "📊", "color": "#6366F1"},
        {"title": "High Risk", "value": summary.get("high_risk", 0), 
         "sub": "Students", "icon": "🔴", "color": "#EF4444"},
        {"title": "Medium Risk", "value": summary.get("medium_risk", 0), 
         "sub": "Students", "icon": "🟡", "color": "#FBBF24"},
        {"title": "Low Risk", "value": summary.get("low_risk", 0), 
         "sub": "Students", "icon": "🟢", "color": "#34D399"},
        {"title": "Average Risk", "value": f"{summary.get('average_risk', 0)}%", 
         "sub": "Overall", "icon": "📈", "color": "#818CF8"}
    ]
    
    for col, card in zip([col1, col2, col3, col4, col5], cards_data):
        with col:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-top">
                    <span class="kpi-label">{card['title']}</span>
                    <span class="kpi-icon">{card['icon']}</span>
                </div>
                <div class="kpi-value">{card['value']}</div>
                <div class="kpi-sub">{card['sub']}</div>
            </div>
            """, unsafe_allow_html=True)

