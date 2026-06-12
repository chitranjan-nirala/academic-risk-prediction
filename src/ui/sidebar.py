# src/ui/sidebar.py
import streamlit as st

def render_sidebar():
    """Render the sidebar with branding and navigation"""
    
    # Hide default Streamlit navigation
    st.markdown("""
    <style>
    /* Hide default Streamlit sidebar navigation */
    [data-testid="stSidebarNav"] {
        display: none !important;
    }
    
    /* Hide the default page navigation menu */
    .st-emotion-cache-16idsys p {
        display: none !important;
    }
    
    /* Adjust sidebar padding after hiding default nav */
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Use st.sidebar context manager
    with st.sidebar:
        # Brand header
        st.markdown("""
        <div class="sidebar-brand">
            <div class="sidebar-brand-icon">🎓</div>
            <div class="sidebar-brand-name">Academic Risk</div>
            <div class="sidebar-brand-sub">Prediction System</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="nav-group-label">Main Navigation</div>', unsafe_allow_html=True)
        
        # Navigation buttons
        if st.button("🏠 Dashboard", key="nav_dashboard", use_container_width=True):
            st.switch_page("app.py")
        
        if st.button("📈 Analytics", key="nav_analytics", use_container_width=True):
            st.switch_page("pages/Analytics.py")
        
        if st.button("🎯 Segmentation", key="nav_segmentation", use_container_width=True):
            st.switch_page("pages/Student_Segmentation.py")
        
        if st.button("🚨 Intervention", key="nav_intervention", use_container_width=True):
            st.switch_page("pages/Faculty_Intervention.py")
        
        if st.button("🕒 Risk History", key="nav_history", use_container_width=True):
            st.switch_page("pages/Student_Risk_History.py")
        
        if st.button("📈 Model Performance", key="nav_performance", use_container_width=True):
            st.switch_page("pages/Model_Performance.py")
        
