import streamlit as st

def render_analytics_cards(summary):
    # Add CSS styling for the cards
    st.markdown("""
        <style>
        .kpi-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            padding: 15px;
            margin: 10px 5px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .kpi-card:hover {
            transform: translateY(-5px);
        }
        .kpi-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .kpi-label {
            color: rgba(255,255,255,0.9);
            font-size: 14px;
            font-weight: 500;
            letter-spacing: 0.5px;
        }
        .kpi-icon {
            font-size: 24px;
        }
        .kpi-value {
            color: white;
            font-size: 32px;
            font-weight: bold;
            margin: 10px 0;
        }
        .kpi-sub {
            color: rgba(255,255,255,0.7);
            font-size: 12px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Ensure summary has all required keys with default values
    summary = {
        "total_predictions": summary.get("total_predictions", 0),
        "high_risk": summary.get("high_risk", 0),
        "medium_risk": summary.get("medium_risk", 0),
        "low_risk": summary.get("low_risk", 0),
        "average_risk": summary.get("average_risk", 0)
    }

    col1, col2, col3, col4, col5 = st.columns(5)

    cards = [
        {
            "title": "Total Predictions",
            "value": summary["total_predictions"],
            "sub": "Records",
            "icon": "📊"
        },
        {
            "title": "High Risk",
            "value": summary["high_risk"],
            "sub": "Students",
            "icon": "🔴"
        },
        {
            "title": "Medium Risk",
            "value": summary["medium_risk"],
            "sub": "Students",
            "icon": "🟡"
        },
        {
            "title": "Low Risk",
            "value": summary["low_risk"],
            "sub": "Students",
            "icon": "🟢"
        },
        {
            "title": "Average Risk",
            "value": f"{summary['average_risk']}%",
            "sub": "Overall",
            "icon": "📈"
        }
    ]

    for col, card in zip([col1, col2, col3, col4, col5], cards):
        with col:
            st.markdown(
                f"""
                <div class="kpi-card">
                    <div class="kpi-top">
                        <div class="kpi-label">{card['title']}</div>
                        <div class="kpi-icon">{card['icon']}</div>
                    </div>
                    <div class="kpi-value">{card['value']}</div>
                    <div class="kpi-sub">{card['sub']}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

