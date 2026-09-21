import gradio as gr
import requests


# =========================================================
# N8N WEBHOOK
# =========================================================

N8N_WEBHOOK_URL = "https://kianaz.app.n8n.cloud/webhook/content-qc"


# =========================================================
# AI CONTENT QC FUNCTION
# =========================================================

def analyze_content(content):

    if not content or not content.strip():
        return "لطفاً ابتدا متن محتوا را وارد کنید."

    try:

        response = requests.post(
            N8N_WEBHOOK_URL,
            json={
                "content": content
            },
            timeout=120
        )

        response.raise_for_status()

        return response.text

    except requests.exceptions.Timeout:

        return "زمان پاسخ‌گویی n8n تمام شد. لطفاً دوباره تلاش کنید."

    except requests.exceptions.RequestException as e:

        return f"خطا در اتصال به n8n:\n\n{str(e)}"


# =========================================================
# PREMIUM BLACK + PURPLE CSS
# =========================================================

css = """
@import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap');

:root {
    --black: #111111;
    --purple: #6D5DFB;
    --purple-dark: #5B4BE7;
    --purple-light: #F1EFFF;
    --bg: #F7F7F9;
    --white: #FFFFFF;
    --text: #18181B;
    --text-soft: #52525B;
    --muted: #8A8A93;
    --border: #E5E5EA;
    --border-purple: #DDD8FF;
    --success: #12B76A;
}

* {
    font-family: 'Vazirmatn', sans-serif !important;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0 !important;
    background: var(--bg) !important;
    direction: rtl;
}

.gradio-container {
    max-width: 1440px !important;
    margin: auto !important;
    padding: 0 42px 55px !important;

    background:
        radial-gradient(
            circle at 50% 4%,
            rgba(109,93,251,.075),
            transparent 28%
        ),
        var(--bg) !important;
}


/* =====================================================
   NAVBAR
   ===================================================== */

#navbar {
    height: 78px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid var(--border);
    margin-bottom: 0;
    direction: rtl;
}

#brand {
    display: flex;
    align-items: center;
    gap: 12px;
}

#brand-icon {
    width: 42px;
    height: 42px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
    background: var(--black);
    color: white;
    font-size: 19px;

    box-shadow:
        0 8px 22px rgba(17,17,17,.16);

    transition: .25s ease;
}

#brand-icon:hover {
    background: var(--purple);

    box-shadow:
        0 10px 25px rgba(109,93,251,.28);

    transform: rotate(6deg);
}

#brand-name {
    font-size: 17px;
    font-weight: 900;
    color: var(--black);
    letter-spacing: -.3px;
}

#brand-subtitle {
    display: block;
    margin-top: 2px;
    font-size: 9px;
    color: var(--muted);
    direction: ltr;
    text-align: right;
}

#system-status {
    display: flex;
    align-items: center;
    gap: 8px;

    padding: 8px 14px;

    background: rgba(255,255,255,.8);
    border: 1px solid var(--border);
    border-radius: 30px;

    font-size: 10px;
    color: var(--text-soft);

    box-shadow:
        0 4px 14px rgba(0,0,0,.025);
}

#status-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--success);

    box-shadow:
        0 0 0 4px rgba(18,183,106,.10);
}


/* =====================================================
   HERO
   ===================================================== */

#hero {
    position: relative;

    padding: 70px 20px 48px;

    text-align: center;
    direction: rtl;

    overflow: hidden;
}

#hero::before {
    content: "";

    position: absolute;

    width: 420px;
    height: 420px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(109,93,251,.12),
            transparent 68%
        );

    top: -220px;
    left: 50%;

    transform: translateX(-50%);

    pointer-events: none;
}

#hero-label {
    position: relative;

    display: inline-flex;

    align-items: center;
    justify-content: center;

    gap: 8px;

    padding: 7px 14px;

    background: var(--purple-light);

    border: 1px solid var(--border-purple);

    color: var(--purple-dark);

    border-radius: 30px;

    font-size: 9px;
    font-weight: 800;

    letter-spacing: .4px;

    margin-bottom: 20px;

    box-shadow:
        0 5px 18px rgba(109,93,251,.06);
}

#hero-label span {
    color: #A9A1FF;
}

#hero h1 {
    position: relative;

    margin: 0 auto;

    max-width: 850px;

    font-size: 44px;
    line-height: 1.55;

    font-weight: 900;

    letter-spacing: -1.5px;

    color: var(--black);

    text-align: center !important;

    direction: rtl;
}

#hero h1 span {
    position: relative;
    color: var(--purple);
}

#hero h1 span::after {
    content: "";

    position: absolute;

    right: 0;
    left: 0;

    bottom: -2px;

    height: 5px;

    background: rgba(109,93,251,.12);

    border-radius: 10px;
}

#hero p {
    position: relative;

    max-width: 690px;

    margin: 18px auto 0;

    color: var(--text-soft);

    font-size: 13px;
    line-height: 2.2;

    text-align: center !important;

    direction: rtl;
}


/* =====================================================
   STATS
   ===================================================== */

#stats-row {
    direction: rtl;
    margin-bottom: 4px;
}

.stat-card {
    position: relative;

    background: var(--white);

    border: 1px solid var(--border);

    border-radius: 18px;

    padding: 20px 18px;

    min-height: 105px;

    direction: rtl;

    text-align: center;

    overflow: hidden;

    transition:
        transform .25s ease,
        box-shadow .25s ease,
        border-color .25s ease;
}

.stat-card::before {
    content: "";

    position: absolute;

    top: 0;
    right: 20%;
    left: 20%;

    height: 2px;

    background: var(--purple);

    opacity: 0;

    transition: .25s ease;
}

.stat-card:hover {
    transform: translateY(-4px);

    border-color: var(--border-purple);

    box-shadow:
        0 12px 28px rgba(109,93,251,.08);
}

.stat-card:hover::before {
    opacity: 1;
}

.stat-title {
    color: var(--muted);
    font-size: 9px;
    margin-bottom: 8px;
}

.stat-value {
    color: var(--black);
    font-size: 21px;
    font-weight: 900;
    letter-spacing: -.3px;
}

.stat-description {
    color: #85858E;
    font-size: 9px;
    margin-top: 5px;
}


/* =====================================================
   WORKSPACE
   ===================================================== */

#workspace {
    position: relative;

    margin-top: 30px;

    background: var(--white);

    border: 1px solid #DFDFE5;

    border-radius: 24px;

    padding: 27px;

    box-shadow:
        0 20px 50px rgba(24,24,27,.065);

    overflow: hidden;
}

#workspace::before {
    content: "";

    position: absolute;

    top: 0;
    bottom: 0;
    right: 0;

    width: 3px;

    background:
        linear-gradient(
            to bottom,
            var(--purple),
            rgba(109,93,251,.15)
        );
}


/* =====================================================
   WORKSPACE HEADER
   ===================================================== */

.workspace-header {
    display: flex;

    flex-direction: column;

    align-items: center;
    justify-content: center;

    margin-bottom: 20px;

    text-align: center !important;

    direction: rtl;
}

.workspace-title {
    font-size: 15px;
    font-weight: 900;
    color: var(--black);

    text-align: center !important;
    direction: rtl;
}

.workspace-caption {
    margin-top: 5px;

    font-size: 8px;

    color: #A1A1AA;

    text-align: center !important;

    direction: ltr;

    letter-spacing: .5px;
}


/* =====================================================
   INPUT / OUTPUT
   ===================================================== */

#workspace .gradio-row {
    gap: 18px !important;
}

#workspace .gradio-column {
    gap: 0 !important;
}

#input-box {
    border: 1px solid #E2E2E7 !important;

    border-radius: 17px !important;

    background: #FCFCFD !important;

    box-shadow: none !important;

    overflow: hidden;

    transition: .25s ease;
}

#input-box:focus-within {
    border-color: #BEB7FF !important;

    box-shadow:
        0 0 0 4px rgba(109,93,251,.07) !important;
}

#output-box {
    position: relative;

    border: 1px solid var(--border-purple) !important;

    border-radius: 17px !important;

    background:
        linear-gradient(
            135deg,
            #FFFFFF 0%,
            #FBFAFF 100%
        ) !important;

    box-shadow:
        inset 3px 0 0 var(--purple),
        0 8px 24px rgba(109,93,251,.035) !important;

    overflow: hidden;
}

textarea {
    direction: rtl !important;

    text-align: right !important;

    font-size: 13px !important;

    line-height: 2.2 !important;

    color: #3F3F46 !important;

    background: transparent !important;
}

textarea::placeholder {
    color: #A1A1AA !important;
    opacity: 1 !important;
}


/* =====================================================
   BUTTON
   ===================================================== */

#analyze-btn {
    position: relative;

    margin-top: 19px;

    height: 57px !important;

    border-radius: 14px !important;

    background: var(--black) !important;

    color: white !important;

    border: none !important;

    font-size: 14px !important;

    font-weight: 800 !important;

    letter-spacing: -.2px;

    box-shadow:
        0 10px 25px rgba(17,17,17,.17);

    transition:
        transform .2s ease,
        background .2s ease,
        box-shadow .2s ease;
}

#analyze-btn:hover {
    transform: translateY(-3px);

    background: var(--purple) !important;

    box-shadow:
        0 14px 30px rgba(109,93,251,.27);
}

#analyze-btn:active {
    transform: translateY(0);
}


/* =====================================================
   FEATURES
   ===================================================== */

#features-section {
    margin-top: 50px;

    direction: rtl;

    text-align: center;
}

#features-title {
    margin-bottom: 7px;

    font-size: 18px;

    font-weight: 900;

    color: var(--black);

    text-align: center !important;

    direction: rtl;
}

#features-subtitle {
    margin-bottom: 22px;

    font-size: 10px;

    color: var(--muted);

    text-align: center !important;
}

#features-row {
    direction: rtl;

    gap: 14px !important;
}

.feature {
    position: relative;

    background: var(--white);

    border: 1px solid var(--border);

    border-radius: 18px;

    padding: 23px 18px 21px;

    height: 100%;

    direction: rtl;

    text-align: center !important;

    overflow: hidden;

    transition:
        transform .25s ease,
        border-color .25s ease,
        box-shadow .25s ease;
}

.feature:hover {
    transform: translateY(-5px);

    border-color: var(--border-purple);

    box-shadow:
        0 14px 30px rgba(109,93,251,.08);
}

.feature-number {
    font-family: Arial, sans-serif !important;

    color: var(--purple);

    font-size: 26px;

    line-height: 1;

    font-weight: 900;

    margin-bottom: 14px;

    text-align: center !important;

    opacity: .9;
}

.feature-title {
    font-size: 13px;

    font-weight: 900;

    color: var(--black);

    text-align: center !important;
}

.feature-text {
    font-size: 10px;

    line-height: 2;

    color: #71717A;

    margin-top: 7px;

    text-align: center !important;
}


/* =====================================================
   FOOTER
   ===================================================== */

#footer {
    text-align: center;

    padding: 42px 0 8px;

    color: #A1A1AA;

    font-size: 9px;

    direction: ltr;
}


/* =====================================================
   MOBILE
   ===================================================== */

@media(max-width: 800px) {

    .gradio-container {
        padding: 0 15px 35px !important;
    }

    #navbar {
        height: 68px;
    }

    #brand-subtitle {
        display: none;
    }

    #system-status {
        display: none;
    }

    #hero {
        padding: 45px 10px 35px;
    }

    #hero h1 {
        font-size: 29px;

        line-height: 1.7;

        letter-spacing: -.7px;
    }

    #hero p {
        font-size: 11px;

        line-height: 2;

        padding: 0 5px;
    }

    #workspace {
        margin-top: 20px;

        padding: 17px;

        border-radius: 19px;
    }

    #workspace .gradio-row {
        gap: 14px !important;
    }

    .workspace-title {
        font-size: 13px;
    }

    .workspace-caption {
        font-size: 8px;
    }

    .stat-card {
        min-height: 85px;

        padding: 15px 10px;
    }

    .stat-value {
        font-size: 17px;
    }

    #analyze-btn {
        height: 52px !important;
    }

    #features-title {
        font-size: 16px;
    }

    .feature {
        padding: 20px 15px;
    }
}
"""


# =========================================================
# GRADIO APP
# =========================================================

with gr.Blocks(
    title="AI Content QC"
) as app:

    # =====================================================
    # HEADER
    # =====================================================

    gr.HTML("""
    <div id="navbar">

        <div id="brand">

            <div id="brand-icon">
                ✦
            </div>

            <div>

                <div id="brand-name">
                    AI Content QC
                </div>

                <span id="brand-subtitle">
                    Intelligent Content Quality Platform
                </span>

            </div>

        </div>

        <div id="system-status">

            <div id="status-dot"></div>

            سیستم آماده تحلیل است

        </div>

    </div>
    """)


    # =====================================================
    # HERO
    # =====================================================

    gr.HTML("""
    <div id="hero">

        <div id="hero-label">

            ✦ AI POWERED

            <span>•</span>

            CONTENT INTELLIGENCE

        </div>

        <h1>

            کیفیت محتوای خود را

            <span>
                هوشمندانه
            </span>

            بررسی کنید.

        </h1>

        <p>

            متن فارسی خود را وارد کنید و یک گزارش کنترل کیفیت
            دقیق درباره ساختار، خوانایی، تکرار محتوا و ایرادهای
            نگارشی دریافت کنید.

        </p>

    </div>
    """)


    # =====================================================
    # STATS
    # =====================================================

    with gr.Row(elem_id="stats-row"):

        gr.HTML("""
        <div class="stat-card">

            <div class="stat-title">
                نوع تحلیل
            </div>

            <div class="stat-value">
                AI QC
            </div>

            <div class="stat-description">
                تحلیل هوشمند محتوا
            </div>

        </div>
        """)

        gr.HTML("""
        <div class="stat-card">

            <div class="stat-title">
                تمرکز اصلی
            </div>

            <div class="stat-value">
                Persian
            </div>

            <div class="stat-description">
                محتوای فارسی
            </div>

        </div>
        """)

        gr.HTML("""
        <div class="stat-card">

            <div class="stat-title">
                پردازش
            </div>

            <div class="stat-value">
                Automated
            </div>

            <div class="stat-description">
                بدون بررسی دستی
            </div>

        </div>
        """)

        gr.HTML("""
        <div class="stat-card">

            <div class="stat-title">
                خروجی
            </div>

            <div class="stat-value">
                QC Report
            </div>

            <div class="stat-description">
                گزارش قابل اقدام
            </div>

        </div>
        """)


    # =====================================================
    # WORKSPACE
    # =====================================================

    with gr.Group(elem_id="workspace"):

        gr.HTML("""
        <div class="workspace-header">

            <div class="workspace-title">
                فضای تحلیل محتوا
            </div>

            <div class="workspace-caption">
                INPUT → AI ANALYSIS → QC REPORT
            </div>

        </div>
        """)

        with gr.Row():

            # =============================================
            # INPUT
            # =============================================

            with gr.Column():

                gr.HTML("""
                <div class="workspace-header">

                    <div class="workspace-title">
                        متن محتوا
                    </div>

                    <div class="workspace-caption">
                        INPUT
                    </div>

                </div>
                """)

                content = gr.Textbox(

                    show_label=False,

                    placeholder=(
                        "مقاله یا محتوای خود را اینجا وارد کنید...\n\n"
                        "برای دریافت نتیجه دقیق‌تر، متن کامل محتوا را وارد کنید."
                    ),

                    lines=20,

                    elem_id="input-box"
                )


            # =============================================
            # OUTPUT
            # =============================================

            with gr.Column():

                gr.HTML("""
                <div class="workspace-header">

                    <div class="workspace-title">
                        گزارش هوشمند
                    </div>

                    <div class="workspace-caption">
                        AI OUTPUT
                    </div>

                </div>
                """)

                result = gr.Textbox(

                    show_label=False,

                    placeholder=(
                        "پس از تحلیل، گزارش کنترل کیفیت "
                        "در این قسمت نمایش داده خواهد شد."
                    ),

                    lines=20,

                    interactive=False,

                    elem_id="output-box"
                )


        # =================================================
        # ANALYZE BUTTON
        # =================================================

        analyze_btn = gr.Button(

            "✦  شروع تحلیل محتوا",

            elem_id="analyze-btn"
        )


    # =====================================================
    # FEATURES
    # =====================================================

    gr.HTML("""
    <div id="features-section">

        <div id="features-title">
            چه چیزهایی بررسی می‌شود؟
        </div>

        <div id="features-subtitle">
            چهار لایه اصلی برای ارزیابی کیفیت محتوای فارسی
        </div>

    </div>
    """)


    with gr.Row(elem_id="features-row"):

        gr.HTML("""
        <div class="feature">

            <div class="feature-number">
                01
            </div>

            <div class="feature-title">
                ساختار محتوا
            </div>

            <div class="feature-text">
                بررسی ترتیب بخش‌ها، تیترها و ساختار کلی محتوا.
            </div>

        </div>
        """)

        gr.HTML("""
        <div class="feature">

            <div class="feature-number">
                02
            </div>

            <div class="feature-title">
                تکرار و حشو
            </div>

            <div class="feature-text">
                شناسایی جملات، عبارت‌ها و مفاهیم تکراری.
            </div>

        </div>
        """)

        gr.HTML("""
        <div class="feature">

            <div class="feature-number">
                03
            </div>

            <div class="feature-title">
                خوانایی
            </div>

            <div class="feature-text">
                بررسی روان بودن و وضوح متن برای مخاطب.
            </div>

        </div>
        """)

        gr.HTML("""
        <div class="feature">

            <div class="feature-number">
                04
            </div>

            <div class="feature-title">
                نگارش
            </div>

            <div class="feature-text">
                شناسایی ایرادهای نگارشی واضح و قابل مشاهده.
            </div>

        </div>
        """)


    # =====================================================
    # FOOTER
    # =====================================================

    gr.HTML("""
    <div id="footer">

        AI Content QC · n8n × Google Gemini · Content Intelligence

    </div>
    """)


    # =====================================================
    # BUTTON EVENT
    # =====================================================

    analyze_btn.click(

        fn=analyze_content,

        inputs=content,

        outputs=result
    )


# =========================================================
# LAUNCH
# =========================================================

import os

app.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 10000)),
    css=css
)
