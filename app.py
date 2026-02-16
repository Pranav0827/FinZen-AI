

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import io


#  PAGE CONFIG

st.set_page_config(
    page_title="FinZen AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


#  CUSTOM CSS — Dark neon-green terminal aesthetic

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Mono:wght@400;500&family=Nunito:wght@400;500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }
.stApp { background: #07080f; color: #e2e4f0; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1.4rem 2.2rem 2rem; max-width: 1350px; }

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: #0c0d18 !important;
    border-right: 1px solid #1a1d2e !important;
}
section[data-testid="stSidebar"] * { color: #e2e4f0 !important; }
section[data-testid="stSidebar"] .stRadio label {
    padding: 9px 14px; border-radius: 10px;
    cursor: pointer; font-size: 13px; font-weight: 500;
    transition: all .15s;
}
section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(79,255,176,.07) !important;
    color: #4fffb0 !important;
}

/* ── Metric Cards ── */
[data-testid="metric-container"] {
    background: #0e101a !important;
    border: 1px solid #1e2235 !important;
    border-radius: 14px !important;
    padding: 16px 20px !important;
    transition: border-color .2s !important;
}
[data-testid="metric-container"]:hover { border-color: #4fffb040 !important; }
[data-testid="metric-container"] label {
    color: #6b7196 !important; font-size: 11px !important;
    text-transform: uppercase; letter-spacing: .07em;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    font-family: 'DM Mono', monospace !important;
    font-size: 21px !important; color: #e2e4f0 !important;
}
[data-testid="metric-container"] [data-testid="stMetricDelta"] { font-size: 11px !important; }

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: transparent;
    border-bottom: 1px solid #1e2235; gap: 0;
}
.stTabs [data-baseweb="tab"] {
    background: transparent; color: #6b7196;
    font-weight: 600; font-size: 13px; padding: 10px 22px;
    border-bottom: 2px solid transparent; border-radius: 0;
}
.stTabs [aria-selected="true"] {
    color: #4fffb0 !important;
    border-bottom: 2px solid #4fffb0 !important;
    background: rgba(79,255,176,.04) !important;
}
.stTabs [data-baseweb="tab-panel"] { padding-top: 22px; }

/* ── Buttons ── */
.stButton button {
    background: linear-gradient(135deg, #4fffb0, #6c63ff) !important;
    color: #07080f !important; font-weight: 700 !important;
    font-family: 'Syne', sans-serif !important;
    border: none !important; border-radius: 10px !important;
    transition: all .2s !important;
}
.stButton button:hover { transform: translateY(-2px) !important; box-shadow: 0 8px 24px rgba(79,255,176,.25) !important; }
.stButton button[kind="secondary"] {
    background: #151825 !important; color: #e2e4f0 !important;
    border: 1px solid #1e2235 !important;
}
.stButton button[kind="secondary"]:hover { border-color: #6c63ff !important; }

/* ── Inputs ── */
.stTextInput input, .stNumberInput input, .stSelectbox > div > div {
    background: #151825 !important; border: 1px solid #1e2235 !important;
    color: #e2e4f0 !important; border-radius: 10px !important;
    font-family: 'Nunito', sans-serif !important;
}
.stTextInput input:focus { border-color: #4fffb0 !important; }

/* ── Sliders ── */
.stSlider [data-baseweb="slider"] div[role="slider"] {
    background: #4fffb0 !important; border-color: #4fffb0 !important;
}
.stSlider [data-baseweb="slider"] div { background: #4fffb020 !important; }

/* ── DataFrames ── */
.stDataFrame { border-radius: 12px !important; overflow: hidden !important; }
.stDataFrame thead th {
    background: #0e101a !important; color: #6b7196 !important;
    font-size: 11px !important; text-transform: uppercase !important;
    letter-spacing: .05em !important;
}
.stDataFrame tbody tr { background: #0c0d18 !important; }
.stDataFrame tbody tr:hover { background: #151825 !important; }

/* ── Progress ── */
.stProgress > div > div > div { background: linear-gradient(90deg,#4fffb0,#6c63ff) !important; }

/* ── Divider ── */
hr { border-color: #1e2235 !important; }

/* ── Expander ── */
.streamlit-expanderHeader {
    background: #151825 !important; border: 1px solid #1e2235 !important;
    border-radius: 10px !important; color: #e2e4f0 !important;
}
.streamlit-expanderContent {
    background: #0e101a !important; border: 1px solid #1e2235 !important;
    border-top: none !important; border-radius: 0 0 10px 10px !important;
}

/* ── Custom cards ── */
.fz-card {
    background: #0e101a; border: 1px solid #1e2235;
    border-radius: 16px; padding: 20px 22px; margin-bottom: 14px;
}
.fz-card-title {
    font-family: 'Syne', sans-serif; font-size: 14px;
    font-weight: 700; color: #e2e4f0; margin-bottom: 14px;
}
.fz-hero {
    background: linear-gradient(135deg, #0e101a 60%, #0e1820);
    border: 1px solid #1e2235; border-radius: 20px; padding: 28px;
}
.fz-score-num {
    font-family: 'DM Mono', monospace; font-size: 56px;
    font-weight: 500; color: #4fffb0; line-height: 1;
}
.fz-tag-green  { background:rgba(79,255,176,.08); color:#4fffb0; border:1px solid rgba(79,255,176,.25); padding:3px 11px; border-radius:20px; font-size:11px; font-weight:700; }
.fz-tag-yellow { background:rgba(255,209,102,.08); color:#ffd166; border:1px solid rgba(255,209,102,.25); padding:3px 11px; border-radius:20px; font-size:11px; font-weight:700; }
.fz-tag-red    { background:rgba(255,95,126,.08); color:#ff5f7e; border:1px solid rgba(255,95,126,.25); padding:3px 11px; border-radius:20px; font-size:11px; font-weight:700; }
.fz-tag-purple { background:rgba(108,99,255,.08); color:#6c63ff; border:1px solid rgba(108,99,255,.25); padding:3px 11px; border-radius:20px; font-size:11px; font-weight:700; }
.rec-card { background:#151825; border:1px solid #1e2235; border-radius:13px; padding:16px 18px; margin-bottom:10px; }
.rec-title { font-weight:700; font-size:14px; margin-bottom:4px; }
.rec-body  { font-size:13px; color:#9ca3c0; line-height:1.55; }
.rec-amt   { font-family:'DM Mono',monospace; font-size:13px; color:#4fffb0; margin-top:6px; }
.chat-user { background:linear-gradient(135deg,#6c63ff,#4fffb0); color:#07080f; padding:12px 16px; border-radius:18px 18px 4px 18px; max-width:72%; margin-left:auto; margin-bottom:12px; font-size:14px; }
.chat-ai   { background:#0e101a; border:1px solid #1e2235; padding:14px 18px; border-radius:4px 18px 18px 18px; max-width:82%; margin-bottom:12px; font-size:14px; line-height:1.6; }
.chat-ai-lbl { font-size:10px; color:#4fffb0; font-weight:700; letter-spacing:.08em; margin-bottom:5px; }
.pg-title { font-family:'Syne',sans-serif; font-size:26px; font-weight:800; color:#e2e4f0; margin-bottom:2px; }
.pg-sub   { font-size:13px; color:#6b7196; margin-bottom:22px; }
</style>
""", unsafe_allow_html=True)


#  PLOTLY DARK THEME

PL = dict(
    paper_bgcolor="#0e101a", plot_bgcolor="#0e101a",
    font=dict(family="DM Mono, monospace", color="#9ca3c0", size=11),
    margin=dict(l=10, r=10, t=36, b=10),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(size=11)),
    xaxis=dict(gridcolor="#1e2235", linecolor="#1e2235", tickfont=dict(size=10)),
    yaxis=dict(gridcolor="#1e2235", linecolor="#1e2235", tickfont=dict(size=10)),
)
C = dict(
    green="#4fffb0", purple="#6c63ff", red="#ff5f7e", yellow="#ffd166",
    teal="#4ecdc4", pink="#f8a5c2", cyan="#67e8f9", orange="#fb923c",
    food="#4fffb0", rent="#6c63ff", travel="#ff5f7e", entertainment="#ffd166",
    investment="#4ecdc4", emi="#f8a5c2", utilities="#a8e6cf",
    healthcare="#ffa07a", shopping="#dda0dd", others="#87ceeb",
)


#  EMBEDDED DATASET  (no CSV file needed)

RAW_DATA = """user_id,month,year,income,food,rent,travel,entertainment,investment,emi,utilities,healthcare,shopping,others
user1,1,2024,55000,7200,15000,2500,3000,2000,5000,1200,800,4000,2100
user1,2,2024,55000,6800,15000,1800,2500,2000,5000,1100,0,3500,1900
user1,3,2024,58000,7500,15000,3200,4000,3000,5000,1300,1500,5000,2300
user1,4,2024,55000,6500,15000,1500,2000,2000,5000,1100,0,2800,1700
user1,5,2024,55000,8000,15000,2800,3500,2000,5000,1200,600,4500,2200
user1,6,2024,60000,7800,15000,4500,3000,3000,5000,1300,1000,5500,2400
user1,7,2024,55000,7200,15000,2200,2800,2000,5000,1150,0,3800,2000
user1,8,2024,55000,6900,15000,1900,2500,2000,5000,1100,500,3200,1800
user1,9,2024,62000,8500,15000,5000,4000,4000,5000,1400,1200,6000,2600
user1,10,2024,55000,7100,15000,2100,2700,2000,5000,1150,0,4000,1950
user1,11,2024,55000,7800,15000,3000,5000,2000,5000,1200,800,7000,2500
user1,12,2024,70000,9000,15000,6000,6000,5000,5000,1500,1500,8000,3200
user2,1,2024,80000,9000,22000,5000,4000,5000,8000,2000,1000,6000,3200
user2,2,2024,80000,8500,22000,3500,3500,5000,8000,1900,0,5000,2800
user2,3,2024,85000,10000,22000,6000,5000,6000,8000,2200,2000,7000,3500
user2,4,2024,80000,8800,22000,4000,4000,5000,8000,2000,500,5500,3000
user2,5,2024,80000,9200,22000,4500,4500,5000,8000,2100,800,6200,3100
user2,6,2024,90000,10500,22000,7000,5500,8000,8000,2300,1500,8000,3800
user2,7,2024,80000,9000,22000,4000,4200,5000,8000,2000,0,5800,3000
user2,8,2024,80000,8700,22000,3800,3800,5000,8000,1950,600,5300,2900
user2,9,2024,92000,11000,22000,8000,6000,8000,8000,2500,2000,9000,4200
user2,10,2024,80000,9100,22000,4200,4100,5000,8000,2050,0,6000,3050
user2,11,2024,80000,9500,22000,5000,6000,5000,8000,2100,1000,8000,3400
user2,12,2024,100000,12000,22000,9000,8000,10000,8000,2500,2000,11000,4800
user3,1,2024,35000,5000,10000,1500,2000,0,3000,800,500,2500,1500
user3,2,2024,35000,4800,10000,1200,1800,0,3000,750,0,2200,1300
user3,3,2024,37000,5200,10000,1800,2200,1000,3000,850,1000,3000,1600
user3,4,2024,35000,4900,10000,1000,1700,0,3000,780,0,2000,1200
user3,5,2024,35000,5500,10000,1600,2100,0,3000,820,400,2800,1500
user3,6,2024,38000,5800,10000,2500,2500,1500,3000,900,800,3500,1700
user3,7,2024,35000,5100,10000,1400,2000,0,3000,810,0,2300,1400
user3,8,2024,35000,4950,10000,1100,1900,0,3000,790,300,2100,1350
user3,9,2024,40000,6000,10000,3000,2800,2000,3000,950,1200,4000,1900
user3,10,2024,35000,5050,10000,1300,1950,0,3000,800,0,2400,1380
user3,11,2024,35000,5400,10000,1700,2900,0,3000,830,600,3800,1550
user3,12,2024,45000,6500,10000,3500,3500,3000,3000,1000,1000,5000,2200
user4,1,2024,50000,6500,12000,2200,2600,1800,4000,1000,700,3500,1800
user4,2,2024,50000,6200,12000,1600,2200,1800,4000,950,0,3000,1600
user4,3,2024,52000,6800,12000,2800,3500,2600,4000,1100,1300,4300,2000
user4,4,2024,50000,5900,12000,1300,1800,1800,4000,950,0,2400,1500
user4,5,2024,50000,7200,12000,2400,3000,1800,4000,1000,500,3800,1900
user4,6,2024,54000,7000,12000,3800,2600,2600,4000,1100,800,4700,2100
user4,7,2024,50000,6500,12000,1900,2400,1800,4000,980,0,3200,1700
user4,8,2024,50000,6200,12000,1600,2200,1800,4000,950,400,2700,1500
user4,9,2024,56000,7600,12000,4200,3500,3500,4000,1200,1000,5100,2300
user4,10,2024,50000,6400,12000,1800,2300,1800,4000,980,0,3400,1700
user4,11,2024,50000,7000,12000,2500,4200,1800,4000,1000,700,5900,2200
user4,12,2024,60000,8000,12000,5000,5000,4000,4000,1300,1300,6800,2800
user5,1,2024,80000,10400,24000,3600,4800,4000,12000,2400,1200,7200,3600
user5,2,2024,80000,9760,24000,2880,4400,4000,12000,2280,0,6600,3120
user5,3,2024,85000,11200,24000,4800,6000,6000,12000,2640,2400,8400,4200
user5,4,2024,80000,10080,24000,3600,4800,4000,12000,2400,600,6600,3600
user5,5,2024,80000,10560,24000,4050,5400,4000,12000,2520,960,7440,3720
user5,6,2024,90000,12150,24000,6300,6600,8000,12000,2760,1800,9600,4560
user5,7,2024,80000,10400,24000,3600,5040,4000,12000,2400,0,6960,3600
user5,8,2024,80000,10080,24000,3420,4560,4000,12000,2340,720,6360,3480
user5,9,2024,92000,12650,24000,7200,7200,8000,12000,3000,2400,10800,5040
user5,10,2024,80000,10480,24000,3780,4920,4000,12000,2460,0,7200,3660
user5,11,2024,80000,10900,24000,4500,7200,4000,12000,2520,1200,9600,4080
user5,12,2024,100000,13800,24000,8100,9600,10000,12000,3000,2400,13200,5760
user6,1,2024,40000,5200,12000,2000,2400,800,3000,800,400,3200,1400
user6,2,2024,40000,4960,12000,1440,2160,800,3000,720,0,2640,1240
user6,3,2024,41000,5460,12000,1800,2640,1000,3000,780,800,3600,1520
user6,4,2024,40000,4760,12000,1200,2040,800,3000,744,0,2400,1160
user6,5,2024,40000,5800,12000,1600,2520,800,3000,760,320,3360,1400
user6,6,2024,42000,6090,12000,2100,3000,1500,3000,840,640,4200,1610
user6,7,2024,40000,5080,12000,1400,2400,800,3000,768,0,2760,1320
user6,8,2024,40000,4920,12000,1320,2280,800,3000,756,240,2520,1284
user6,9,2024,44000,6600,12000,2640,3360,2000,3000,880,960,4800,1800
user6,10,2024,40000,5020,12000,1560,2340,800,3000,760,0,2880,1316
user6,11,2024,40000,5320,12000,1700,3480,800,3000,780,480,4560,1470
user6,12,2024,48000,6720,12000,3360,4200,2400,3000,960,960,6000,2112
user7,1,2024,60000,7800,18000,3000,3600,2400,6000,1440,720,4800,2160
user7,2,2024,60000,7440,18000,2160,3300,2400,6000,1380,0,3960,1872
user7,3,2024,63000,8400,18000,3600,4500,3600,6000,1620,1440,5040,2520
user7,4,2024,60000,7680,18000,2700,3600,2400,6000,1440,360,4140,2160
user7,5,2024,60000,7920,18000,3150,4050,2400,6000,1560,576,4680,2232
user7,6,2024,66000,9075,18000,4725,4950,4800,6000,1980,1080,7200,3456
user7,7,2024,60000,7800,18000,2700,3780,2400,6000,1440,0,5220,2160
user7,8,2024,60000,7680,18000,2568,3456,2400,6000,1404,432,4536,2088
user7,9,2024,69000,9450,18000,5400,5400,4800,6000,2100,1440,8100,3024
user7,10,2024,60000,7920,18000,2832,3696,2400,6000,1476,0,5400,2208
user7,11,2024,60000,8250,18000,3375,5400,2400,6000,1512,720,7200,2448
user7,12,2024,72000,10080,18000,5760,7200,6000,6000,2160,1440,9600,3456
user8,1,2024,55000,7150,16500,2750,3300,2200,5500,1320,660,4400,1980
user8,2,2024,55000,6820,16500,1980,3025,2200,5500,1265,0,3630,1716
user8,3,2024,57500,7700,16500,3300,4125,2750,5500,1485,1320,4620,2310
user8,4,2024,55000,7040,16500,2475,3300,2200,5500,1320,330,3795,1980
user8,5,2024,55000,7260,16500,2888,3713,2200,5500,1430,528,4290,2046
user8,6,2024,60500,8318,16500,4339,4536,2640,5500,1813,990,6600,3168
user8,7,2024,55000,7150,16500,2475,3465,2200,5500,1320,0,4793,1980
user8,8,2024,55000,7040,16500,2346,3168,2200,5500,1287,396,4158,1925
user8,9,2024,63250,8655,16500,4950,4950,3520,5500,1925,1320,7425,2772
user8,10,2024,55000,7260,16500,2597,3396,2200,5500,1365,0,4950,2028
user8,11,2024,55000,7563,16500,3094,4950,2200,5500,1386,660,6600,2246
user8,12,2024,66000,9240,16500,5280,6600,4400,5500,1980,1320,8800,3168
user9,1,2024,45000,5850,13500,2250,2700,1800,4500,1080,540,3600,1620
user9,2,2024,45000,5580,13500,1620,2475,1800,4500,1035,0,2970,1404
user9,3,2024,47250,6300,13500,2700,3375,2250,4500,1215,1080,3780,1890
user9,4,2024,45000,5760,13500,2025,2700,1800,4500,1080,270,3105,1620
user9,5,2024,45000,5940,13500,2363,3038,1800,4500,1170,432,3510,1676
user9,6,2024,49500,6799,13500,3539,3713,2160,4500,1484,810,5400,2592
user9,7,2024,45000,5850,13500,2025,2835,1800,4500,1080,0,3918,1620
user9,8,2024,45000,5760,13500,1926,2592,1800,4500,1053,324,3402,1575
user9,9,2024,51750,7088,13500,4050,4050,2880,4500,1575,1080,6075,2268
user9,10,2024,45000,5940,13500,2127,2787,1800,4500,1118,0,4050,1662
user9,11,2024,45000,6194,13500,2534,4050,1800,4500,1131,540,5400,1841
user9,12,2024,54000,7560,13500,4320,5400,3600,4500,1620,1080,7200,2592
user10,1,2024,70000,9100,21000,3500,4200,2800,7000,1680,840,5600,2520
user10,2,2024,70000,8680,21000,2520,3850,2800,7000,1610,0,4620,2178
user10,3,2024,73500,9800,21000,4200,5250,3500,7000,1890,1680,5880,2940
user10,4,2024,70000,8960,21000,3150,4200,2800,7000,1680,420,4830,2520
user10,5,2024,70000,9240,21000,3675,5145,2800,7000,1820,672,5880,2586
user10,6,2024,77000,10575,21000,5513,5775,3920,7000,2184,1176,8400,3924
user10,7,2024,70000,9100,21000,3150,4410,2800,7000,1680,0,6300,2520
user10,8,2024,70000,8960,21000,2992,4032,2800,7000,1638,504,5544,2520
user10,9,2024,80500,11015,21000,6300,6300,4480,7000,2265,1512,9240,3528
user10,10,2024,70000,9240,21000,3306,4326,2800,7000,1764,0,6300,2604
user10,11,2024,70000,9625,21000,3938,6300,2800,7000,1911,840,8400,3024
user10,12,2024,84000,11760,21000,6720,8400,5600,7000,2520,1680,11200,4032
user11,1,2024,50000,6500,15000,2500,3000,2000,5000,1200,800,4000,2100
user11,2,2024,50000,6200,15000,1800,2500,2000,5000,1150,0,3500,1900
user11,3,2024,52000,6760,15000,3200,4000,3000,5000,1300,1500,5000,2300
user11,4,2024,50000,5900,15000,1500,2000,2000,5000,1100,0,2800,1700
user11,5,2024,50000,7200,15000,2800,3500,2000,5000,1200,600,4500,2200
user11,6,2024,54000,7020,15000,4500,3000,3000,5000,1300,1000,5500,2400
user11,7,2024,50000,6500,15000,2200,2800,2000,5000,1150,0,3800,2000
user11,8,2024,50000,6200,15000,1900,2500,2000,5000,1100,500,3200,1800
user11,9,2024,56000,7680,15000,5000,4000,4000,5000,1400,1200,6000,2600
user11,10,2024,50000,6400,15000,2100,2700,2000,5000,1150,0,4000,1950
user11,11,2024,50000,7000,15000,3000,5000,2000,5000,1200,800,7000,2500
user11,12,2024,60000,7800,15000,6000,6000,5000,5000,1500,1500,8000,3200
user12,1,2024,65000,8450,19500,3250,3900,2600,6500,1560,780,5200,2340
user12,2,2024,65000,8060,19500,2340,3575,2600,6500,1495,0,4290,2016
user12,3,2024,68250,9100,19500,3900,4875,3250,6500,1755,1560,5460,2710
user12,4,2024,65000,8320,19500,2925,3900,2600,6500,1560,390,4465,2340
user12,5,2024,65000,8580,19500,3402,4361,2600,6500,1690,624,5070,2412
user12,6,2024,71500,9813,19500,5119,5355,3120,6500,2133,1170,7800,3726
user12,7,2024,65000,8450,19500,2925,4070,2600,6500,1560,0,5859,2340
user12,8,2024,65000,8320,19500,2792,3768,2600,6500,1523,468,4914,2270
user12,9,2024,74750,10238,19500,5850,5850,4160,6500,2123,1560,8638,3256
user12,10,2024,65000,8580,19500,3077,4017,2600,6500,1647,0,5850,2388
user12,11,2024,65000,8944,19500,3661,5850,2600,6500,1626,780,7800,2652
user12,12,2024,78000,10920,19500,6240,7800,5200,6500,2340,1560,10400,3744
user13,1,2024,35000,4550,10500,1750,2100,1400,3500,840,420,2800,1470
user13,2,2024,35000,4340,10500,1260,1575,1400,3500,805,0,2310,1078
user13,3,2024,36750,4900,10500,2100,2625,1750,3500,945,840,2940,1170
user13,4,2024,35000,4480,10500,1575,2100,1400,3500,840,210,2415,1260
user13,5,2024,35000,4620,10500,1838,2359,1400,3500,910,336,2730,1302
user13,6,2024,38500,5289,10500,2759,2889,1680,3500,1173,630,4200,2016
user13,7,2024,35000,4550,10500,1575,2205,1400,3500,840,0,3066,1260
user13,8,2024,35000,4480,10500,1512,2040,1400,3500,819,252,2664,1225
user13,9,2024,40250,5513,10500,3150,3150,2240,3500,1225,840,4725,1764
user13,10,2024,35000,4620,10500,1659,2173,1400,3500,874,0,3150,1296
user13,11,2024,35000,4904,10500,2009,3150,1400,3500,886,420,4200,1431
user13,12,2024,42000,5880,10500,3360,4200,2800,3500,1260,840,5600,2016
user14,1,2024,40000,5200,12000,2000,2400,1600,4000,960,480,3200,1680
user14,2,2024,40000,4960,12000,1440,2160,1600,4000,920,0,2640,1408
user14,3,2024,41000,5460,12000,1800,2640,2000,4000,860,1000,3600,1760
user14,4,2024,40000,4760,12000,1200,2040,1600,4000,880,0,2400,1320
user14,5,2024,40000,5800,12000,1600,2520,1600,4000,920,400,3360,1520
user14,6,2024,42000,6090,12000,2100,3000,2000,4000,900,800,4200,1840
user14,7,2024,40000,5080,12000,1400,2400,1600,4000,860,0,2760,1400
user14,8,2024,40000,4920,12000,1320,2280,1600,4000,850,300,2520,1360
user14,9,2024,44000,6600,12000,2640,3360,2400,4000,950,1200,4800,2040
user14,10,2024,40000,5020,12000,1560,2340,1600,4000,860,0,2880,1396
user14,11,2024,40000,5320,12000,1700,3480,1600,4000,880,600,4560,1650
user14,12,2024,48000,6720,12000,3360,4200,3200,4000,1020,1200,6000,2384
user15,1,2024,45000,5850,13500,2250,2700,1800,4500,1080,5040,36050,16200
user15,2,2024,45000,5580,13500,1620,2475,1800,4500,1035,521,29170,14804
user15,3,2024,47250,6300,13500,2700,3375,2250,4500,12125,10280,37580,18990
user15,4,2024,45000,5760,13500,2025,2700,1800,4500,10680,2270,3105,1620
user15,5,2024,45000,5940,13500,2363,3038,1800,4500,1170,4232,3510,1676
user15,6,2024,49500,6799,13500,3539,3713,2160,4500,1484,8160,5400,2592
user15,7,2024,45000,5850,13500,2025,2835,1800,4500,1080,200,3918,1620
user15,8,2024,45000,5760,13500,1926,2592,1800,4500,1053,3224,3402,1575
user15,9,2024,51750,7088,13500,4050,4050,2880,4500,15075,10800,6075,2268
user15,10,2024,45000,5940,13500,2127,2787,1800,46500,1118,2360,4050,16062
user15,11,2024,45000,6194,13500,2534,4050,1800,4500,1131,5406,5400,18041
user15,12,2024,54000,7560,13500,43020,5400,3600,4500,16020,1080,72000,25920"""

EXPENSE_COLS = ["food","rent","travel","entertainment","investment",
                "emi","utilities","healthcare","shopping","others"]
IDEAL_PCT    = {"food":15,"rent":30,"travel":5,"entertainment":5,
                "investment":15,"emi":20,"utilities":5,
                "healthcare":3,"shopping":8,"others":4}
MONTHS       = ["Jan","Feb","Mar","Apr","May","Jun",
                "Jul","Aug","Sep","Oct","Nov","Dec"]
USERS        = {
    "user1": {"name":"Arjun Sharma",     "emoji":"👨‍💻", "role":"Software Engineer", "city":"Pune",   "email":"arjun.sharma@email.com",     "password":"arjun123"},
    "user2": {"name":"Priya Desai",      "emoji":"👩‍💼", "role":"Product Manager",   "city":"Mumbai", "email":"priya.desai@email.com",      "password":"priya123"},
    "user3": {"name":"Sneha Kulkarni",   "emoji":"👩‍🎓", "role":"Junior Analyst",    "city":"Nagpur", "email":"sneha.kulkarni@email.com",   "password":"sneha123"},
    "user4": {"name":"Rahul Verma",      "emoji":"👨‍🎨", "role":"UX Designer",       "city":"Delhi",  "email":"rahul.verma@email.com",      "password":"rahul123"},
    "user5": {"name":"Ananya Singh",     "emoji":"👩‍⚕️", "role":"Doctor",            "city":"Bangalore","email":"ananya.singh@email.com",   "password":"ananya123"},
    "user6": {"name":"Vikram Patel",     "emoji":"👨‍🏫", "role":"Teacher",           "city":"Ahmedabad","email":"vikram.patel@email.com",   "password":"vikram123"},
    "user7": {"name":"Kavya Rao",        "emoji":"👩‍🔬", "role":"Researcher",        "city":"Hyderabad","email":"kavya.rao@email.com",      "password":"kavya123"},
    "user8": {"name":"Amit Kumar",       "emoji":"👨‍💼", "role":"Business Analyst",  "city":"Chennai","email":"amit.kumar@email.com",     "password":"amit123"},
    "user9": {"name":"Meera Joshi",      "emoji":"👩‍🎤", "role":"Content Creator",   "city":"Jaipur", "email":"meera.joshi@email.com",     "password":"meera123"},
    "user10":{"name":"Sandeep Gupta",    "emoji":"👨‍🚀", "role":"Data Scientist",   "city":"Kolkata","email":"sandeep.gupta@email.com",  "password":"sandeep123"},
    "user11":{"name":"Riya Agarwal",     "emoji":"👩‍💻", "role":"Frontend Developer","city":"Pune",   "email":"riya.agarwal@email.com",    "password":"riya123"},
    "user12":{"name":"Karan Mehta",      "emoji":"👨‍⚖️", "role":"Lawyer",            "city":"Surat",  "email":"karan.mehta@email.com",     "password":"karan123"},
    "user13":{"name":"Pooja Nair",       "emoji":"👩‍🍳", "role":"Chef",              "city":"Kochi",  "email":"pooja.nair@email.com",      "password":"pooja123"},
    "user14":{"name":"Sarthak Gavhane",     "emoji":"👨‍🎾", "role":"Sports Coach",      "city":"Indore", "email":"sarth.g@email.com",    "password":"sarthak123"},
    "user15":{"name":"Yuvraj Pawar",      "emoji":"👩‍🎨", "role":"Graphic Designer",  "city":"Pune","email":"yuvraj.pawar@email.com",     "password":"yuvraj123"},
}

@st.cache_data
def load_all_data():
    return pd.read_csv(io.StringIO(RAW_DATA))

def get_user_df(uid):
    df  = load_all_data()
    udf = df[df["user_id"] == uid].copy()
    udf["total_expense"] = udf[EXPENSE_COLS].sum(axis=1)
    udf["savings"]       = udf["income"] - udf["total_expense"]
    udf["savings_rate"]  = (udf["savings"] / udf["income"] * 100).round(2)
    return udf.sort_values("month").reset_index(drop=True)


#  ANALYTICS ENGINE  (replaces FastAPI backend)

def fmt(n):
    return f"₹{int(round(n)):,}"

def health_score(udf):
    inc  = float(udf["income"].mean())
    sav  = float(udf["savings"].mean())
    sr   = float(udf["savings_rate"].mean())
    inv  = float(udf["investment"].mean())
    ent  = float(udf["entertainment"].mean())
    shop = float(udf["shopping"].mean())
    cv   = float(udf["savings"].std()) / sav if sav > 0 else 1.0

    sr_pts   = min(40.0, sr   * 1.5)
    inv_pts  = min(25.0, (inv / inc * 100) * 1.5)
    ctrl_pts = max(0.0,  20.0 - (ent/inc*100 + shop/inc*100) * 0.8)
    cons_pts = max(0.0,  15.0 * (1.0 - cv))
    total    = min(100.0, round(sr_pts + inv_pts + ctrl_pts + cons_pts, 1))

    grade = ("Excellent 🌟" if total >= 75 else
             "Good 👍"      if total >= 55 else
             "Fair ⚠️"       if total >= 35 else
             "Needs Work 🔴")
    color = ("#4fffb0" if total >= 75 else
             "#4ecdc4" if total >= 55 else
             "#ffd166" if total >= 35 else "#ff5f7e")
    return {
        "score": total, "grade": grade, "color": color,
        "breakdown": [
            {"label":"Savings Rate",     "pts":round(sr_pts,1),   "max":40},
            {"label":"Investment Habit", "pts":round(inv_pts,1),  "max":25},
            {"label":"Expense Control",  "pts":round(ctrl_pts,1), "max":20},
            {"label":"Consistency",      "pts":round(cons_pts,1), "max":15},
        ]
    }

def credit_score(udf):
    inc  = float(udf["income"].mean())
    emi  = float(udf["emi"].mean())
    sav  = float(udf["savings"].mean())
    sr   = float(udf["savings_rate"].mean())
    inv  = float(udf["investment"].mean())
    cv_sav = float(udf["savings"].std()) / sav if sav > 0 else 1.0
    cv_emi = float(udf["emi"].std()) / emi if emi > 0 else 0.0

    # Payment history: consistent EMI payments (assume on-time if consistent)
    pay_hist = max(0, 35 - cv_emi * 100) if emi > 0 else 35

    # Credit utilization: EMI as % of income (lower is better)
    util_ratio = emi / inc * 100
    credit_util = max(0, 30 - util_ratio * 0.5)

    # Length of credit history: based on data consistency
    hist_len = 15 if cv_sav < 0.2 else 10 if cv_sav < 0.4 else 5

    # New credit: low variation in EMI
    new_credit = 10 if cv_emi < 0.1 else 5

    # Credit mix: having investments and savings
    mix = 10 if inv > inc * 0.1 and sr > 15 else 5

    total_score = 300 + pay_hist + credit_util + hist_len + new_credit + mix
    total_score = min(0, max(300, round(total_score)))

    grade = ("Excellent 🌟" if total_score >= 800 else
             "Very Good 👍" if total_score >= 700 else
             "Good ✅"      if total_score >= 550 else
             "Fair ⚠️"      if total_score >= 320 else
             "Poor 🔴")
    color = ("#4fffb0" if total_score >= 800 else
             "#4ecdc4" if total_score >= 700 else
             "#ffd166" if total_score >= 550 else
             "#ff9f43" if total_score >= 320 else "#ff5f7e")
    return {
        "score": total_score, "grade": grade, "color": color,
        "breakdown": [
            {"label":"Payment History", "pts":round(pay_hist), "max":35},
            {"label":"Credit Utilization", "pts":round(credit_util), "max":30},
            {"label":"Credit History", "pts":hist_len, "max":15},
            {"label":"New Credit", "pts":new_credit, "max":10},
            {"label":"Credit Mix", "pts":mix, "max":10},
        ]
    }

def predictions(udf):
    sav = udf["savings"].values.astype(float)
    n   = len(sav)
    x   = np.arange(n, dtype=float)
    slope, intercept = (np.polyfit(x, sav, 1) if n > 1 else (0.0, sav[0]))
    slope, intercept = float(slope), float(intercept)
    next_pred  = max(0.0, slope * n + intercept)
    avg_sav    = float(np.mean(sav))
    cv         = float(np.std(sav)) / avg_sav if avg_sav > 0 else 1.0

    cum, monthly_cum = 0.0, []
    for m in range(60):
        cum += next_pred * (1.05 ** (m / 12.0))
        monthly_cum.append(round(cum))

    f3y = sum(next_pred * (1.05 ** (m/12)) for m in range(36))
    f5y = sum(next_pred * (1.05 ** (m/12)) for m in range(60))

    risk = "Low 🟢" if cv < 0.15 else "Medium 🟡" if cv < 0.30 else "High 🔴"
    return {
        "next_pred":    round(next_pred),
        "avg_sav":      round(avg_sav),
        "slope":        round(slope, 2),
        "direction":    "📈 Improving" if slope >= 0 else "📉 Declining",
        "f3y":          round(f3y),
        "f5y":          round(f5y),
        "monthly_cum":  monthly_cum,
        "risk":         risk,
        "cv":           round(cv, 3),
    }

def recommendations(udf):
    inc  = float(udf["income"].mean())
    sav  = float(udf["savings"].mean())
    exp  = float(udf["total_expense"].mean())
    sr   = float(udf["savings_rate"].mean())
    recs = []

    ef_t = round(exp * 6); ef_m = round(ef_t / 12)
    recs.append({"icon":"🛡️","title":"Build Emergency Fund","priority":"HIGH",
                 "body":f"Target {fmt(ef_t)} (6-month buffer). Auto-save {fmt(ef_m)}/month to a liquid fund.",
                 "amount":fmt(ef_m)+"/month"})

    sip = max(500, round((sav - ef_m) * 0.6 / 500) * 500)
    sip5= round(sip * 12 * ((1.12**5 - 1) / 0.12))
    recs.append({"icon":"📈","title":"Start/Increase SIP","priority":"HIGH",
                 "body":f"Invest {fmt(sip)}/month in Flexi Cap MF. At 12% CAGR → {fmt(sip5)} in 5 years!",
                 "amount":fmt(sip)+"/month"})

    ent_pct = float(udf["entertainment"].mean()) / inc * 100
    if ent_pct > 8:
        sv = round(float(udf["entertainment"].mean()) - inc * 0.05)
        recs.append({"icon":"🎬","title":"Reduce Entertainment","priority":"MEDIUM",
                     "body":f"Entertainment is {ent_pct:.1f}% of income (ideal ≤5%). Cutting saves {fmt(sv)}/month.",
                     "amount":"Save "+fmt(sv)+"/month"})

    shop_pct = float(udf["shopping"].mean()) / inc * 100
    if shop_pct > 12:
        sv = round(float(udf["shopping"].mean()) - inc * 0.08)
        recs.append({"icon":"🛍️","title":"Optimise Shopping","priority":"MEDIUM",
                     "body":f"Shopping is {shop_pct:.1f}% of income (ideal ≤8%). Try the 24-hour rule before buying.",
                     "amount":"Save "+fmt(sv)+"/month"})

    if sr < 20:
        recs.append({"icon":"⚡","title":"Apply 50-30-20 Rule","priority":"HIGH",
                     "body":(f"Savings rate {sr:.1f}% (target 20%). "
                             f"Needs:{fmt(inc*.5)} | Wants:{fmt(inc*.3)} | Savings:{fmt(inc*.2)}"),
                     "amount":"Target: "+fmt(inc*.2)+"/month"})

    inv_pct = float(udf["investment"].mean()) / inc * 100
    if inv_pct < 10:
        recs.append({"icon":"🌱","title":"Diversify Investments","priority":"MEDIUM",
                     "body":"Investment below 10%. Consider 60% Equity MF + 30% Debt MF + 10% Gold ETF.",
                     "amount":"Target: "+fmt(inc*.15)+"/month"})
    return recs[:5]

def chat_response(uid, msg, lang="en"):
    udf  = get_user_df(uid)
    msg  = msg.lower().strip()
    name = USERS[uid]["name"].split()[0]
    inc  = float(udf["income"].mean())
    sav  = float(udf["savings"].mean())
    sr   = float(udf["savings_rate"].mean())
    exp  = float(udf["total_expense"].mean())
    pred = predictions(udf)
    hs   = health_score(udf)
    recs = recommendations(udf)
    sip  = max(500, round(sav * 0.6 / 500) * 500)
    ef   = round(exp * 6)

    if any(w in msg for w in ["hello","hi","hey","start","namaste","नमस्ते"]):
        r = (f"Hi {name}! 👋 I'm FinZen AI.\n\n"
             f"Your Health Score: **{hs['score']}/100** — {hs['grade']}\n"
             f"Top priority: {recs[0]['icon']} {recs[0]['title']}\n\n"
             f"Ask me about savings, SIP, budget, emergency fund, or predictions!")

    elif any(w in msg for w in ["score","health","grade"]):
        bd = hs["breakdown"]
        r  = (f"**Financial Health Score: {hs['score']}/100 — {hs['grade']}**\n\n"
              + "\n".join(f"• {b['label']}: {b['pts']}/{b['max']} pts" for b in bd)
              + f"\n\n💡 Biggest boost: increase investments to 15% of income.")

    elif any(w in msg for w in ["saving","save","बचत"]):
        r = (f"📊 Avg monthly savings: **{fmt(sav)}** ({sr:.1f}% rate)\n"
             f"🎯 Target: 20% savings rate\n"
             f"📅 Next month prediction: **{fmt(pred['next_pred'])}**\n"
             f"📈 Trend: {pred['direction']}\n\n"
             f"💡 Tip: Auto-transfer savings on salary day before spending!")

    elif any(w in msg for w in ["sip","invest","mutual fund","mf","निवेश"]):
        sip1 = round(sip * 12 * ((1.12**1 - 1) / 0.12))
        sip3 = round(sip * 12 * ((1.12**3 - 1) / 0.12))
        sip5 = round(sip * 12 * ((1.12**5 - 1) / 0.12))
        r = (f"**Recommended SIP: {fmt(sip)}/month** at 12% CAGR:\n\n"
             f"• 1 Year  → {fmt(sip1)}\n"
             f"• 3 Years → {fmt(sip3)}\n"
             f"• 5 Years → {fmt(sip5)}\n\n"
             f"💡 Start with Parag Parikh Flexi Cap or Nifty 50 Index Fund on Groww/Zerodha Coin!")

    elif any(w in msg for w in ["emergency","fund","आपातकाल"]):
        r = (f"**Emergency Fund Target: {fmt(ef)}** (6 months of expenses)\n\n"
             f"• Save {fmt(round(ef/12))}/month\n"
             f"• Reach target in 12 months\n"
             f"• Park in Liquid MF (better than savings account)\n\n"
             f"💡 Automate transfer on the 1st of every month!")

    elif any(w in msg for w in ["budget","overspend","spend","expense","खर्च"]):
        high = [(c, float(udf[c].mean())) for c in EXPENSE_COLS
                if float(udf[c].mean()) / inc * 100 > IDEAL_PCT[c]]
        if high:
            top  = sorted(high, key=lambda x: -x[1])[:3]
            body = "\n".join(f"• {c.title()}: {fmt(v)} ({v/inc*100:.1f}% vs ideal {IDEAL_PCT[c]}%)" for c,v in top)
            r = (f"⚠️ Overspending detected:\n\n{body}\n\n"
                 f"**50-30-20 Rule:**\n"
                 f"• Needs (50%): {fmt(inc*.5)}\n"
                 f"• Wants (30%): {fmt(inc*.3)}\n"
                 f"• Savings (20%): {fmt(inc*.2)}")
        else:
            r = f"✅ Great job {name}! Spending is well-controlled in all categories!"

    elif any(w in msg for w in ["predict","forecast","next","future","भविष्य"]):
        r = (f"**Savings Predictions for {name}:**\n\n"
             f"📅 Next month: {fmt(pred['next_pred'])}\n"
             f"📊 Trend: {pred['direction']} ({pred['slope']:+.0f}/month)\n"
             f"🗓️ 3-Year cumulative: {fmt(pred['f3y'])}\n"
             f"🚀 5-Year cumulative: {fmt(pred['f5y'])}\n"
             f"⚡ Risk level: {pred['risk']} (CV: {pred['cv']})")

    elif any(w in msg for w in ["risk","जोखिम"]):
        r = (f"**Financial Risk: {pred['risk']}**\n\n"
             f"• Savings volatility CV: {pred['cv']}\n"
             f"• Savings rate: {sr:.1f}%\n"
             f"• Investment rate: {float(udf['investment'].mean())/inc*100:.1f}%\n\n"
             f"💡 Reduce risk: emergency fund + auto-invest + equity/debt/gold diversification")

    elif any(w in msg for w in ["recommend","advice","tip","suggestion","सुझाव"]):
        r = "**Top Recommendations:**\n\n" + "\n".join(
            f"{rc['icon']} **{rc['title']}** [{rc['priority']}]\n   → {rc['amount']}" for rc in recs[:3])

    elif any(w in msg for w in ["vacation","trip","travel","holiday","छुट्टी"]):
        months_needed = round(50000 / (sav * 0.3)) if sav > 0 else 12
        r = (f"✈️ **Travel Planning for {name}:**\n\n"
             f"• Domestic trip: ₹30K–₹60K\n"
             f"• International: ₹1.5L–₹3L\n\n"
             f"Save {fmt(sav * 0.3)}/month → ₹50K trip in {months_needed} months!\n"
             f"💡 Open a dedicated 'Travel' recurring deposit.")

    elif any(w in msg for w in ["food","खाना","dining"]):
        avg_food = float(udf["food"].mean())
        fpct     = avg_food / inc * 100
        r = (f"🍱 Food spending: **{fmt(avg_food)}/month** ({fpct:.1f}% of income)\n"
             f"Ideal: 15% = {fmt(inc * 0.15)}\n\n"
             f"💡 Tips:\n• Meal prep on Sundays (saves ₹2K+/month)\n"
             f"• Zomato/Swiggy max 2×/week\n"
             f"• Cook at home → save {fmt(max(0, avg_food - inc*0.15))}/month!")

    else:
        r = (f"Hi {name}! 🧠 Quick snapshot:\n\n"
             f"• Income: {fmt(inc)}/month\n"
             f"• Savings: {fmt(sav)}/month ({sr:.1f}%)\n"
             f"• Health Score: {hs['score']}/100 — {hs['grade']}\n\n"
             f"Try asking: **'my SIP plan'** · **'budget advice'** · "
             f"**'predict savings'** · **'emergency fund'** · **'am I overspending?'**")

    prefix = {"hi":"🇮🇳 ","mr":"🟠 "}.get(lang,"")
    return prefix + r


#  SESSION STATE

if "uid"       not in st.session_state: st.session_state.uid       = None
if "chat"      not in st.session_state: st.session_state.chat      = []
if "lang"      not in st.session_state: st.session_state.lang      = "en"
if "goals"     not in st.session_state: st.session_state.goals     = [
    {"icon":"🏖️","name":"Europe Trip",       "target":150000, "saved":42000,  "months":8},
    {"icon":"🏠","name":"Home Down Payment", "target":1000000,"saved":180000, "months":36},
    {"icon":"💻","name":"MacBook Pro",       "target":200000, "saved":65000,  "months":6},
    {"icon":"🛡️","name":"Emergency Fund",    "target":300000, "saved":95000,  "months":12},
]


#  LOGIN PAGE

def page_login():
    st.markdown("""
    <div style="text-align:center;padding:50px 0 30px;">
        <div style="font-family:'Syne',sans-serif;font-size:52px;font-weight:800;color:#e2e4f0;">
            🧠 Fin<span style="color:#4fffb0;">Zen</span>
            <span style="color:#6b7196;font-size:26px;font-weight:400;">AI</span>
        </div>
        <div style="font-size:15px;color:#6b7196;margin-top:10px;">
            AI Personal Financial Advisor for Gen-Z
        </div>
        <div style="display:inline-block;margin-top:14px;padding:4px 14px;
                    background:rgba(79,255,176,.08);border:1px solid rgba(79,255,176,.25);
                    border-radius:20px;font-size:12px;color:#4fffb0;">
            Transaction-Based Predictive Analytics
        </div>
    </div>
    """, unsafe_allow_html=True)

    _, mid, _ = st.columns([1, 1.4, 1])
    with mid:
        st.markdown('<div class="fz-card">', unsafe_allow_html=True)
        st.markdown('<div class="fz-card-title">� Login to Your Account</div>', unsafe_allow_html=True)

        username = st.text_input("Email", placeholder="Enter your email (e.g., arjun.sharma@email.com)")
        password = st.text_input("Password", type="password", placeholder="Enter your password")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔐 Login", use_container_width=True):
            for uid, u in USERS.items():
                if username.strip().lower() == u["email"].lower() and password == u["password"]:
                    st.session_state.uid  = uid
                    st.session_state.chat = []
                    st.rerun()
                    break
            else:
                st.error("Invalid username or password")

        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown(
            '<div style="text-align:center;font-size:11px;color:#6b7196;margin-top:10px;">'
            '🔒 Demo app · No real financial data stored</div>',
            unsafe_allow_html=True,
        )


#  SIDEBAR

def render_sidebar():
    u = USERS[st.session_state.uid]
    with st.sidebar:
        st.markdown(f"""
        <div style="text-align:center;padding:14px 0 18px;">
            <div style="font-family:'Syne',sans-serif;font-size:22px;font-weight:800;">
                🧠 Fin<span style="color:#4fffb0;">Zen</span> AI
            </div>
        </div>
        <div style="background:#151825;border:1px solid #1e2235;border-radius:12px;
                    padding:14px;margin-bottom:20px;">
            <div style="font-size:30px;margin-bottom:6px;">{u['emoji']}</div>
            <div style="font-weight:700;font-size:14px;">{u['name']}</div>
            <div style="font-size:11px;color:#4fffb0;background:rgba(79,255,176,.1);
                        padding:2px 8px;border-radius:20px;display:inline-block;margin-top:4px;">
                {u['role']}
            </div>
            <div style="font-size:11px;color:#6b7196;margin-top:4px;">📍 {u['city']}</div>
        </div>
        """, unsafe_allow_html=True)

        page = st.radio(
            "nav",
            ["📊  Dashboard","🔍  Analysis","📈  Predictions",
             "🎯  Goals","🔮  What-If","💬  AI Advisor"],
            label_visibility="collapsed",
        )

        st.markdown("---")
        lang_sel = st.selectbox("🌐 Language", ["English","हिंदी","मराठी"],
                                label_visibility="visible")
        st.session_state.lang = {"English":"en","हिंदी":"hi","मराठी":"mr"}[lang_sel]

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("← Sign Out", use_container_width=True, type="secondary"):
            st.session_state.uid  = None
            st.session_state.chat = []
            st.rerun()
    return page


#  PAGE 1 — DASHBOARD

def page_dashboard():
    uid = st.session_state.uid
    udf = get_user_df(uid)
    u   = USERS[uid]
    hs  = health_score(udf)
    cs  = credit_score(udf)
    pr  = predictions(udf)
    rcs = recommendations(udf)

    avg_inc  = float(udf["income"].mean())
    avg_exp  = float(udf["total_expense"].mean())
    avg_sav  = float(udf["savings"].mean())
    avg_sr   = float(udf["savings_rate"].mean())
    sip      = max(500, round(avg_sav * 0.6 / 500) * 500)
    ef       = round(avg_exp * 6)
    risk_p   = "Conservative" if avg_sr<15 else "Moderate" if avg_sr<25 else "Aggressive"

    st.markdown(f'<div class="pg-title">📊 Financial Dashboard</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="pg-sub">Welcome back, {u["name"].split()[0]} — your money overview · Dec 2024</div>', unsafe_allow_html=True)

    # ── Hero: score + stats ──
    col_sc, col_st = st.columns([1, 2])

    with col_sc:
        grade_col = hs["color"]
        st.markdown(f"""
        <div class="fz-hero">
            <div class="fz-score-num">{hs['score']}</div>
            <div style="font-size:11px;color:#6b7196;">/ 100</div>
            <div style="font-family:'Syne',sans-serif;font-size:17px;font-weight:700;
                        color:{grade_col};margin-top:4px;">{hs['grade']}</div>
            <div style="font-size:12px;color:#6b7196;margin-top:2px;margin-bottom:16px;">
                Financial Health Score
            </div>
        """, unsafe_allow_html=True)
        for b in hs["breakdown"]:
            pct  = b["pts"] / b["max"]
            bcol = "#4fffb0" if pct>=.7 else "#ffd166" if pct>=.4 else "#ff5f7e"
            st.markdown(f"""
            <div style="margin-bottom:8px;">
                <div style="display:flex;justify-content:space-between;font-size:11px;
                            color:#6b7196;margin-bottom:3px;">
                    <span>{b['label']}</span>
                    <span style="color:{bcol};font-family:'DM Mono',monospace;">{b['pts']}/{b['max']}</span>
                </div>
                <div style="height:4px;background:#1e2235;border-radius:4px;overflow:hidden;">
                    <div style="height:100%;width:{pct*100:.0f}%;background:{bcol};border-radius:4px;"></div>
                </div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Credit Score
        credit_col = cs["color"]
        st.markdown(f"""
        <div class="fz-hero" style="margin-top:20px;">
            <div class="fz-score-num">{cs['score']}</div>
            <div style="font-size:11px;color:#6b7196;">/ 900</div>
            <div style="font-family:'Syne',sans-serif;font-size:17px;font-weight:700;
                        color:{credit_col};margin-top:4px;">{cs['grade']}</div>
            <div style="font-size:12px;color:#6b7196;margin-top:2px;margin-bottom:16px;">
                Credit Score
            </div>
        """, unsafe_allow_html=True)
        for b in cs["breakdown"]:
            pct  = b["pts"] / b["max"]
            bcol = "#4fffb0" if pct>=.7 else "#ffd166" if pct>=.4 else "#ff5f7e"
            st.markdown(f"""
            <div style="margin-bottom:8px;">
                <div style="display:flex;justify-content:space-between;font-size:11px;
                            color:#6b7196;margin-bottom:3px;">
                    <span>{b['label']}</span>
                    <span style="color:{bcol};font-family:'DM Mono',monospace;">{b['pts']}/{b['max']}</span>
                </div>
                <div style="height:4px;background:#1e2235;border-radius:4px;overflow:hidden;">
                    <div style="height:100%;width:{pct*100:.0f}%;background:{bcol};border-radius:4px;"></div>
                </div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_st:
        r1c1, r1c2, r1c3 = st.columns(3)
        r1c1.metric("Monthly Income",  fmt(avg_inc),  "Avg 2024")
        r1c2.metric("Net Savings",     fmt(avg_sav),  f"{avg_sr:.1f}% rate")
        r1c3.metric("Total Expenses",  fmt(avg_exp),  "Monthly avg")

        r2c1, r2c2, r2c3 = st.columns(3)
        r2c1.metric("Savings Rate",   f"{avg_sr:.1f}%",
                    "✅ On target" if avg_sr>=20 else "⚠️ Below 20%")
        r2c2.metric("Suggested SIP",  fmt(sip), "Monthly invest")
        r2c3.metric("Risk Profile",   risk_p,   "Based on history")

    st.divider()

    # ── Charts ──
    ch1, ch2 = st.columns(2)
    months_lbl = [MONTHS[int(r.month)-1] for _, r in udf.iterrows()]

    with ch1:
        st.markdown('<div class="fz-card-title">📊 Income vs Expense vs Savings</div>', unsafe_allow_html=True)
        fig = go.Figure()
        fig.add_bar(x=months_lbl, y=udf["income"].tolist(),       name="Income",   marker_color=C["purple"], marker_cornerradius=4)
        fig.add_bar(x=months_lbl, y=udf["total_expense"].tolist(),name="Expenses", marker_color=C["red"],    marker_cornerradius=4)
        fig.add_scatter(x=months_lbl, y=udf["savings"].tolist(),  name="Savings",
                        line=dict(color=C["green"],width=2.5), mode="lines+markers",
                        marker=dict(size=6,color=C["green"]),
                        fill="tozeroy", fillcolor="rgba(79,255,176,.07)")
        fig.update_layout(**PL, barmode="group", height=280, yaxis_tickprefix="₹")
        st.plotly_chart(fig, use_container_width=True)

    with ch2:
        st.markdown('<div class="fz-card-title">🥧 Expense Breakdown</div>', unsafe_allow_html=True)
        avgs   = [(col, float(udf[col].mean())) for col in EXPENSE_COLS if float(udf[col].mean()) > 0]
        labels = [a[0].title() for a in avgs]
        vals   = [a[1]         for a in avgs]
        colors = [C.get(a[0],"#87ceeb") for a in avgs]
        fig2   = go.Figure(go.Pie(
            labels=labels, values=vals, hole=0.62,
            marker=dict(colors=colors, line=dict(color="#0e101a", width=3)),
            textinfo="label+percent", textfont=dict(size=10, color="#e2e4f0"),
            hovertemplate="<b>%{label}</b><br>₹%{value:,}<extra></extra>",
        ))
        fig2.update_layout(**PL, height=280)
        st.plotly_chart(fig2, use_container_width=True)

    # ── Recommendations ──
    st.divider()
    st.markdown('<div class="pg-title" style="font-size:18px;">💡 Personalized Recommendations</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    rc1, rc2 = st.columns(2)
    for i, r in enumerate(rcs):
        pc  = "fz-tag-red" if r["priority"]=="HIGH" else "fz-tag-yellow"
        with (rc1 if i%2==0 else rc2):
            st.markdown(f"""
            <div class="rec-card">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
                    <div class="rec-title">{r['icon']} {r['title']}</div>
                    <span class="{pc}">{r['priority']}</span>
                </div>
                <div class="rec-body">{r['body']}</div>
                <div class="rec-amt">{r['amount']}</div>
            </div>""", unsafe_allow_html=True)


#  PAGE 2 — ANALYSIS

def page_analysis():
    uid = st.session_state.uid
    udf = get_user_df(uid)
    inc = float(udf["income"].mean())
    sav = float(udf["savings"].mean())
    cv  = float(udf["savings"].std()) / sav if sav > 0 else 0

    st.markdown('<div class="pg-title">🔍 Transaction Analysis</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-sub">Deep dive into your 12-month spending patterns</div>', unsafe_allow_html=True)

    k1,k2,k3,k4 = st.columns(4)
    k1.metric("Avg Monthly Income",  fmt(inc))
    k2.metric("Avg Monthly Savings", fmt(sav))
    k3.metric("Savings Volatility",  "Low 🟢" if cv<.15 else "Medium 🟡" if cv<.3 else "High 🔴")
    k4.metric("Best Month Savings",  fmt(float(udf["savings"].max())))
    st.divider()

    months_lbl = [MONTHS[int(r.month)-1] for _, r in udf.iterrows()]

    # Savings trend
    fig = make_subplots(specs=[[{"secondary_y":True}]])
    fig.add_trace(go.Scatter(x=months_lbl, y=udf["savings"].tolist(), name="Savings ₹",
                             line=dict(color=C["green"],width=2.5), mode="lines+markers",
                             marker=dict(size=6), fill="tozeroy",
                             fillcolor="rgba(79,255,176,.07)"), secondary_y=False)
    fig.add_trace(go.Scatter(x=months_lbl, y=udf["savings_rate"].tolist(), name="Rate %",
                             line=dict(color=C["purple"],width=2,dash="dot"),
                             mode="lines+markers", marker=dict(size=5)), secondary_y=True)
    fig.update_layout(**PL, title="Monthly Savings Trend & Rate", height=260)
    fig.update_yaxes(tickprefix="₹", secondary_y=False, gridcolor="#1e2235")
    fig.update_yaxes(ticksuffix="%", secondary_y=True,  gridcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

    col_radar, col_tbl = st.columns([1, 2])

    with col_radar:
        st.markdown('<div class="fz-card-title">📡 Spending vs Ideal Benchmark</div>', unsafe_allow_html=True)
        cats      = [c.title() for c in EXPENSE_COLS]
        actual    = [float(udf[c].mean())/inc*100 for c in EXPENSE_COLS]
        ideal_v   = [IDEAL_PCT[c] for c in EXPENSE_COLS]
        fig3 = go.Figure()
        fig3.add_trace(go.Scatterpolar(r=actual+[actual[0]], theta=cats+[cats[0]],
                                        name="Your Spending", fill="toself",
                                        fillcolor="rgba(79,255,176,.1)",
                                        line=dict(color=C["green"],width=2)))
        fig3.add_trace(go.Scatterpolar(r=ideal_v+[ideal_v[0]], theta=cats+[cats[0]],
                                        name="Ideal", fill="toself",
                                        fillcolor="rgba(108,99,255,.07)",
                                        line=dict(color=C["purple"],width=1.5,dash="dash")))
        fig3.update_layout(**PL, height=310,
                           polar=dict(bgcolor="#0e101a",
                                      radialaxis=dict(gridcolor="#1e2235",linecolor="#1e2235",
                                                      tickfont=dict(size=8),ticksuffix="%"),
                                      angularaxis=dict(gridcolor="#1e2235",linecolor="#1e2235",
                                                       tickfont=dict(size=9,color="#9ca3c0"))))
        st.plotly_chart(fig3, use_container_width=True)

    with col_tbl:
        st.markdown('<div class="fz-card-title">📋 Category Breakdown</div>', unsafe_allow_html=True)
        rows = []
        for c in EXPENSE_COLS:
            avg = float(udf[c].mean())
            pct = avg / inc * 100
            idl = IDEAL_PCT[c]
            status  = ("✅ On Track" if pct<=idl else "⚠️ Slightly Over" if pct<=idl*1.4 else "🔴 Over Budget")
            rows.append({"Category":c.title(), "Avg/Month":fmt(avg),
                         "Annual":fmt(avg*12), "% Income":f"{pct:.1f}%",
                         "Ideal":f"{idl}%", "Status":status})
        st_df = pd.DataFrame(rows)
        st.dataframe(st_df, use_container_width=True, hide_index=True)


#  PAGE 3 — PREDICTIONS

def page_predictions():
    uid  = st.session_state.uid
    udf  = get_user_df(uid)
    pred = predictions(udf)
    inc  = float(udf["income"].mean())

    st.markdown('<div class="pg-title">📈 Predictive Analytics</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-sub">AI-powered forecasts from your 12-month transaction history</div>', unsafe_allow_html=True)

    k1,k2,k3,k4 = st.columns(4)
    k1.metric("Next Month Savings",  fmt(pred["next_pred"]), "Predicted")
    k2.metric("Avg Monthly Savings", fmt(pred["avg_sav"]),   "Historical")
    k3.metric("3-Year Forecast",     fmt(pred["f3y"]),       "Cumulative")
    k4.metric("5-Year Forecast",     fmt(pred["f5y"]),       "Cumulative")
    st.divider()

    # 5-year forecast
    base  = pred["monthly_cum"]
    cons  = [round(v*.8) for v in base]
    opti  = [round(v*1.2) for v in base]
    xlbl  = [f"M{i+1}" for i in range(60)]
    fig   = go.Figure()
    fig.add_scatter(x=xlbl, y=opti, name="Optimistic (+20%)",
                    line=dict(color=C["green"],width=1.5),
                    fill="tozeroy", fillcolor="rgba(79,255,176,.05)", mode="lines")
    fig.add_scatter(x=xlbl, y=base, name="Moderate (Base)",
                    line=dict(color=C["purple"],width=2.5), mode="lines+markers",
                    marker=dict(size=3,color=C["purple"]))
    fig.add_scatter(x=xlbl, y=cons, name="Conservative (-20%)",
                    line=dict(color=C["yellow"],width=1.5,dash="dot"), mode="lines")
    fig.update_layout(**{k: v for k, v in PL.items() if k != 'xaxis'}, title="5-Year Cumulative Savings Forecast", height=290,
                      yaxis_tickprefix="₹",
                      xaxis=dict(tickvals=list(range(0,60,12)),
                                 ticktext=["Year 1","Year 2","Year 3","Year 4","Year 5"]))
    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    col_next, col_risk = st.columns(2)

    with col_next:
        st.markdown('<div class="fz-card-title">📅 Next Month Prediction</div>', unsafe_allow_html=True)
        tdir_col = C["green"] if pred["slope"]>=0 else C["red"]
        st.markdown(f"""
        <div class="fz-card">
            <div style="font-family:'DM Mono',monospace;font-size:40px;color:#4fffb0;margin-bottom:8px;">
                {fmt(pred['next_pred'])}
            </div>
            <div style="font-size:13px;color:#9ca3c0;">
                Trend: <span style="color:{tdir_col}">{pred['direction']}</span>
                &nbsp;·&nbsp; Slope: <span style="font-family:'DM Mono',monospace;">{pred['slope']:+.0f}/mo</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        for scenario, val, col_ in [
            ("Optimistic (+20%)", pred["next_pred"]*1.2, C["green"]),
            ("Base",              pred["next_pred"],      C["purple"]),
            ("Conservative",      pred["next_pred"]*.8,  C["yellow"]),
        ]:
            bar = min(100, val/max(pred["avg_sav"],1)/1.4*100)
            st.markdown(f"""
            <div style="margin-bottom:10px;">
                <div style="display:flex;justify-content:space-between;font-size:12px;color:#9ca3c0;margin-bottom:3px;">
                    <span>{scenario}</span>
                    <span style="color:{col_};font-family:'DM Mono',monospace;">{fmt(val)}</span>
                </div>
                <div style="height:4px;background:#1e2235;border-radius:4px;overflow:hidden;">
                    <div style="height:100%;width:{bar:.0f}%;background:{col_};border-radius:4px;"></div>
                </div>
            </div>""", unsafe_allow_html=True)

    with col_risk:
        st.markdown('<div class="fz-card-title">⚠️ Risk Assessment</div>', unsafe_allow_html=True)
        rc = C["green"] if "Low" in pred["risk"] else C["yellow"] if "Medium" in pred["risk"] else C["red"]
        emoji_r = "🟢" if "Low" in pred["risk"] else "🟡" if "Medium" in pred["risk"] else "🔴"
        st.markdown(f"""
        <div class="fz-card">
            <div style="font-family:'Syne',sans-serif;font-size:24px;font-weight:700;color:{rc};">
                {emoji_r} {pred['risk']}
            </div>
            <div style="font-size:12px;color:#6b7196;margin-top:4px;">
                Volatility CV: {pred['cv']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        risk_factors = []
        sr = float(udf["savings_rate"].mean())
        if float(udf["entertainment"].mean())/inc*100 > 8:
            risk_factors.append(("High Entertainment", f"{float(udf['entertainment'].mean())/inc*100:.1f}%", "medium"))
        if float(udf["shopping"].mean())/inc*100 > 12:
            risk_factors.append(("Excess Shopping", f"{float(udf['shopping'].mean())/inc*100:.1f}%", "medium"))
        if pred["cv"] > 0.30:
            risk_factors.append(("Inconsistent Savings", f"CV:{pred['cv']}", "high"))
        if sr < 15:
            risk_factors.append(("Low Savings Rate", f"{sr:.1f}%", "high"))
        if float(udf["investment"].mean())/inc*100 < 5:
            risk_factors.append(("Under-Investing", f"{float(udf['investment'].mean())/inc*100:.1f}%", "medium"))

        if risk_factors:
            for f, v, sev in risk_factors:
                sc = C["red"] if sev=="high" else C["yellow"]
                st.markdown(f"""
                <div style="display:flex;justify-content:space-between;align-items:center;
                            padding:9px 14px;background:#151825;border-radius:9px;margin-bottom:7px;
                            border:1px solid #1e2235;">
                    <span style="font-size:13px;">{f}</span>
                    <div style="display:flex;gap:8px;align-items:center;">
                        <span style="font-family:'DM Mono',monospace;font-size:12px;color:#9ca3c0;">{v}</span>
                        <span style="color:{sc};font-size:10px;font-weight:700;
                                     background:{sc}18;padding:2px 8px;border-radius:20px;
                                     border:1px solid {sc}40;">{sev.upper()}</span>
                    </div>
                </div>""", unsafe_allow_html=True)
        else:
            st.success("✅ No major risk factors detected!")

#  PAGE 4 — GOALS

def page_goals():
    uid = st.session_state.uid
    udf = get_user_df(uid)
    avg_sav = float(udf["savings"].mean())
    goals   = st.session_state.goals

    st.markdown('<div class="pg-title">🎯 Goal Planner</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-sub">Track and achieve your financial milestones</div>', unsafe_allow_html=True)

    total_rem = sum(max(0, g["target"]-g["saved"]) for g in goals)
    sip_need  = min(avg_sav, total_rem/24) if total_rem > 0 else 0

    k1,k2,k3 = st.columns(3)
    k1.metric("Active Goals",      len(goals))
    k2.metric("Total Remaining",   fmt(total_rem))
    k3.metric("Monthly SIP Needed", fmt(sip_need)+"/mo")
    st.divider()

    GOAL_COLS = ["#4fffb0","#6c63ff","#ffd166","#ff5f7e","#4ecdc4","#f8a5c2"]
    cols = st.columns(2)
    for i, g in enumerate(goals):
        pct       = min(100, g["saved"]/g["target"]*100)
        remaining = g["target"] - g["saved"]
        monthly   = remaining / g["months"] if g["months"] > 0 else remaining
        gc        = GOAL_COLS[i % len(GOAL_COLS)]
        with cols[i%2]:
            st.markdown(f"""
            <div class="fz-card" style="border-top:3px solid {gc};">
                <div style="font-size:30px;margin-bottom:8px;">{g['icon']}</div>
                <div style="font-family:'Syne',sans-serif;font-size:15px;font-weight:700;">{g['name']}</div>
                <div style="font-family:'DM Mono',monospace;font-size:22px;color:{gc};margin:8px 0 14px;">{fmt(g['target'])}</div>
                <div style="height:6px;background:#1e2235;border-radius:6px;overflow:hidden;margin-bottom:8px;">
                    <div style="height:100%;width:{pct:.0f}%;background:linear-gradient(90deg,{gc},{gc}88);border-radius:6px;"></div>
                </div>
                <div style="display:flex;justify-content:space-between;font-size:12px;color:#6b7196;margin-bottom:14px;">
                    <span>{fmt(g['saved'])} saved</span>
                    <span style="color:{gc};font-weight:700;">{pct:.0f}%</span>
                    <span>{fmt(remaining)} left</span>
                </div>
                <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
                    <div style="background:#151825;border-radius:8px;padding:9px 12px;">
                        <div style="font-size:10px;color:#6b7196;margin-bottom:2px;">Monthly SIP</div>
                        <div style="font-family:'DM Mono',monospace;font-size:13px;color:{gc};">{fmt(monthly)}</div>
                    </div>
                    <div style="background:#151825;border-radius:8px;padding:9px 12px;">
                        <div style="font-size:10px;color:#6b7196;margin-bottom:2px;">Months Left</div>
                        <div style="font-family:'DM Mono',monospace;font-size:13px;color:#9ca3c0;">{g['months']} mo</div>
                    </div>
                </div>
            </div>""", unsafe_allow_html=True)

    st.divider()
    with st.expander("➕ Add New Goal"):
        gc1,gc2,gc3,gc4 = st.columns(4)
        g_icon   = gc1.selectbox("Icon", ["🏖️","🏠","📚","💻","🚗","💍","🛡️","💰","🎓","✈️","🏋️","🎵"])
        g_name   = gc2.text_input("Goal Name", placeholder="e.g. Europe Trip")
        g_target = gc3.number_input("Target (₹)", min_value=1000, step=5000, value=100000)
        g_months = gc4.number_input("Months", min_value=1, max_value=120, value=12)
        if st.button("✓ Save Goal", type="primary"):
            if g_name.strip():
                st.session_state.goals.append(
                    {"icon":g_icon,"name":g_name.strip(),"target":int(g_target),"saved":0,"months":int(g_months)})
                st.success(f"✅ Goal '{g_name}' added!")
                st.rerun()
            else:
                st.error("Please enter a goal name.")


#  PAGE 5 — WHAT-IF SIMULATOR

def page_whatif():
    uid = st.session_state.uid
    udf = get_user_df(uid)

    avg_inc    = float(udf["income"].mean())
    base_sav   = float(udf["savings"].mean())
    avg_ent    = float(udf["entertainment"].mean())
    avg_shop   = float(udf["shopping"].mean())

    st.markdown('<div class="pg-title">🔮 What-If Simulator</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-sub">See how small changes today create massive financial impact tomorrow</div>', unsafe_allow_html=True)

    col_ctrl, col_res = st.columns([1, 2])

    with col_ctrl:
        st.markdown('<div class="fz-card-title">⚙️ Adjust Parameters</div>', unsafe_allow_html=True)
        target = st.number_input("🎯 Goal Target Amount (₹)", min_value=10000, value=500000, step=10000, help="Set your savings goal")
        extra_pct = st.slider("💰 Extra savings from income (%)", 0, 20, 0,
                               help="Redirect this % of income to savings")
        cut_ent   = st.slider("🎬 Cut Entertainment (%)",         0, 80, 0, step=5)
        cut_shop  = st.slider("🛍️ Cut Shopping (%)",              0, 80, 0, step=5)
        sip_inp   = st.slider("📈 Monthly SIP Amount (₹)",        0, 20000, 0, step=500)

    # Compute simulation
    extra      = avg_inc  * (extra_pct / 100)
    saved_ent  = avg_ent  * (cut_ent   / 100)
    saved_shop = avg_shop * (cut_shop  / 100)
    total_xtra = extra + saved_ent + saved_shop
    new_sav    = base_sav + total_xtra
    new_sr     = new_sav / avg_inc * 100
    sip        = sip_inp if sip_inp > 0 else max(500, round(new_sav*.6/500)*500)

    def sip_val(monthly, yrs, rate=0.12):
        n = yrs*12; r = rate/12
        return round(monthly*(((1+r)**n-1)/r)*(1+r))

    base_months = round(target/base_sav, 1) if base_sav>0 else 9999
    new_months  = round(target/new_sav,  1) if new_sav >0 else 9999

    with col_res:
        st.markdown('<div class="fz-card-title">📊 Simulation Results</div>', unsafe_allow_html=True)
        rc1,rc2,rc3 = st.columns(3)
        rc1.metric("Current Savings",  fmt(base_sav))
        rc2.metric("New Savings",      fmt(new_sav),
                   delta=f"+{fmt(total_xtra)}/mo" if total_xtra>0 else None)
        rc3.metric("New Savings Rate", f"{new_sr:.1f}%")

        rc4,rc5,rc6 = st.columns(3)
        rc4.metric(f"Goal ({fmt(target)}) Now",       f"{base_months} mo")
        rc5.metric(f"Goal ({fmt(target)}) New Pace",  f"{new_months} mo",
                   delta=f"-{round(base_months-new_months,1)} months" if new_months<base_months else None)
        rc6.metric("SIP Amount",            fmt(sip)+"/mo")

        st.markdown("---")
        st.markdown('<div class="fz-card-title">📈 SIP Growth at 12% CAGR</div>', unsafe_allow_html=True)
        sc1,sc2,sc3 = st.columns(3)
        sc1.metric("1 Year",  fmt(sip_val(sip,1)))
        sc2.metric("3 Years", fmt(sip_val(sip,3)))
        sc3.metric("5 Years", fmt(sip_val(sip,5)))

    st.divider()
    fc1, fc2 = st.columns(2)

    with fc1:
        lbl = [f"M{m}" for m in range(1,25)]
        fig = go.Figure()
        fig.add_scatter(x=lbl, y=[round(base_sav*m) for m in range(1,25)],
                        name="Current Pace", line=dict(color=C["red"],width=2),
                        fill="tozeroy", fillcolor="rgba(255,95,126,.06)", mode="lines")
        fig.add_scatter(x=lbl, y=[round(new_sav*m) for m in range(1,25)],
                        name="With Changes", line=dict(color=C["green"],width=2.5),
                        fill="tozeroy", fillcolor="rgba(79,255,176,.08)", mode="lines")
        fig.update_layout(**PL, title="24-Month Savings Comparison",
                          height=250, yaxis_tickprefix="₹")
        st.plotly_chart(fig, use_container_width=True)

    with fc2:
        rate = 0.12/12
        sip_vals = [round(sip*(((1+rate)**(m+1)-1)/rate)*(1+rate)) for m in range(60)]
        lbl60    = [f"M{i+1}" for i in range(60)]
        fig2 = go.Figure(go.Bar(
            x=lbl60, y=sip_vals,
            marker=dict(color=[f"hsl({135+i*2},75%,55%)" for i in range(60)],
                        cornerradius=3),
        ))
        fig2.update_layout(**{k: v for k, v in PL.items() if k != 'xaxis'}, title="5-Year SIP Wealth Growth",
                           height=250, yaxis_tickprefix="₹",
                           xaxis=dict(tickvals=list(range(0,60,12)),
                                      ticktext=["Yr 1","Yr 2","Yr 3","Yr 4","Yr 5"]))
        st.plotly_chart(fig2, use_container_width=True)


#  PAGE 6 — AI CHAT ADVISOR

def page_chat():
    uid  = st.session_state.uid
    lang = st.session_state.lang

    st.markdown('<div class="pg-title">💬 AI Financial Advisor</div>', unsafe_allow_html=True)
    st.markdown('<div class="pg-sub">Multilingual · Personalized · Explainable</div>', unsafe_allow_html=True)

    QPROMPTS = {
        "en": ["What's my savings rate?","Suggest a SIP plan","Emergency fund status",
               "Am I overspending?","Predict next month","Food spending advice",
               "What's my risk level?","Best budget tip"],
        "hi": ["मेरी बचत दर?","SIP सुझाव दें","आपातकालीन निधि?",
               "क्या मैं ज़्यादा खर्च कर रहा हूं?","भविष्यवाणी","खाने पर खर्च"],
        "mr": ["माझी बचत दर?","SIP सुचवा","आपत्कालीन निधी?",
               "मी जास्त खर्च करतो का?","अंदाज सांगा","जेवणावर खर्च"],
    }
    prompts = QPROMPTS.get(lang, QPROMPTS["en"])

    # Quick prompt buttons
    cols_q = st.columns(4)
    for i, q in enumerate(prompts):
        with cols_q[i % 4]:
            if st.button(q, key=f"qp_{i}", use_container_width=True, type="secondary"):
                st.session_state.chat.append({"role":"user","text":q})
                resp = chat_response(uid, q, lang)
                st.session_state.chat.append({"role":"ai","text":resp})
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Chat history
    chat_container = st.container()
    with chat_container:
        if not st.session_state.chat:
            welcome = {
                "en": "Hi! 👋 I'm FinZen AI — your personal financial advisor. Click a quick prompt above or type your question below!",
                "hi": "नमस्ते! 👋 मैं FinZen AI हूं। ऊपर कोई प्रश्न चुनें या नीचे टाइप करें!",
                "mr": "नमस्कार! 👋 मी FinZen AI आहे. वरून प्रश्न निवडा किंवा खाली लिहा!",
            }
            st.markdown(f"""
            <div class="chat-ai">
                <div class="chat-ai-lbl">FINZEN AI</div>
                {welcome.get(lang, welcome['en'])}
            </div>""", unsafe_allow_html=True)

        for msg in st.session_state.chat:
            if msg["role"] == "user":
                st.markdown(f'<div class="chat-user">{msg["text"]}</div>', unsafe_allow_html=True)
            else:
                clean = msg["text"].replace("\n","<br>")
                st.markdown(f"""
                <div class="chat-ai">
                    <div class="chat-ai-lbl">FINZEN AI</div>
                    {clean}
                </div>""", unsafe_allow_html=True)

    # Input row
    st.markdown("<br>", unsafe_allow_html=True)
    inp_col, btn_col = st.columns([5,1])
    ph = {"en":"Ask about your finances...","hi":"अपना सवाल लिखें...","mr":"प्रश्न लिहा..."}.get(lang,"Ask...")
    user_input = inp_col.text_input("msg", placeholder=ph, label_visibility="collapsed", key="chat_msg")
    send       = btn_col.button("Send ↑", use_container_width=True, type="primary")

    if send and user_input.strip():
        st.session_state.chat.append({"role":"user","text":user_input.strip()})
        resp = chat_response(uid, user_input.strip(), lang)
        st.session_state.chat.append({"role":"ai","text":resp})
        st.rerun()

    if st.session_state.chat:
        if st.button("🗑️ Clear Chat", type="secondary"):
            st.session_state.chat = []
            st.rerun()


#  MAIN ROUTER

def main():
    if not st.session_state.uid:
        page_login()
        return

    page = render_sidebar()

    if   "Dashboard"  in page: page_dashboard()
    elif "Analysis"   in page: page_analysis()
    elif "Prediction" in page: page_predictions()
    elif "Goals"      in page: page_goals()
    elif "What-If"    in page: page_whatif()
    elif "Advisor"    in page: page_chat()

if __name__ == "__main__":
    main()
