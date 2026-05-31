import os
import json

WORKSPACE_DIR = "/Users/ccchang/Documents/採購法題庫"
JSON_PATH = "/Users/ccchang/.gemini/antigravity-ide/brain/8d9223c7-40b1-4af6-9ad3-77aaf66ce85d/scratch/parsed_questions.json"
OUTPUT_HTML_PATH = os.path.join(WORKSPACE_DIR, "重點筆記", "政府採購法之總則、招標及決標題庫_重點筆記.html")

def main():
    # 確保輸出資料夾存在
    os.makedirs(os.path.dirname(OUTPUT_HTML_PATH), exist_ok=True)
    
    # 讀取結構化題目 JSON
    if not os.path.exists(JSON_PATH):
        print(f"Error: JSON file not found at {JSON_PATH}")
        return
        
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)
        
    print(f"Loaded {len(questions)} questions from JSON.")
    
    # 定義精選經典題解析資料
    classic_explanations = {
        "mcq_16": {
            "title": "後續擴充採購金額之計算方式",
            "desc": "經常性採購中，若招標文件已載明後續擴充之期間、金額或數量，其「採購金額」應將**首期金額與後續擴充之預估總金額合併計算**。本題預估首年 90 萬 + 續約 2 年共 180 萬，因此總採購金額為 **270 萬元**（屬公告金額以上採購），而非僅以首年 90 萬元計算。",
            "law": "《政府採購法施行細則》第6條規定"
        },
        "mcq_41": {
            "title": "限制性招標之專屬權利範圍排除",
            "desc": "政府採購法第 22 條第 1 項第 2 款之專屬權利包括：專利權、著作權、電路布局權等。但**明文排除「商標專用權」**！因此，機關不可僅因該產品具有特定商標，即逕採限制性招標洽特定廠商辦理，此為考試極為高頻的文字陷阱。",
            "law": "《政府採購法施行細則》第22條第1項"
        },
        "mcq_110": {
            "title": "標價偏低不予發還押標金之例外",
            "desc": "依政府採購法第 31 條第 2 項，廠商有冒名投標、借牌、得標後拒不簽約等影響採購公正之違規行為時，其押標金不予發還。但若僅是「**標價偏低，未於期限內提出合理說明**」，此屬不予決標予該廠商之範疇，其**押標金仍應發還**，不可予以沒收！",
            "law": "《政府採購法》第31條第2項、第58條規定"
        },
        "mcq_93": {
            "title": "電子領標等標期縮短與法定底限",
            "desc": "機關辦理電子領標，等標期得縮短 **3 日**。但為了確保廠商有足夠時間準備投標文件，縮短後仍設有法定最低限制：**公告金額以上之採購縮短後不得少於 7 日**；未達公告金額之採購縮短後不得少於 **5 日**。",
            "law": "《招標期限標準》第9條之規定"
        },
        "mcq_30": {
            "title": "機關人員採購迴避之親屬範疇",
            "desc": "依採購法第 15 條，機關辦理採購之承辦、監辦人員，若涉及本人、配偶、**三親等以內血親或姻親**、或共同生活家屬之利益時，應行迴避。特別注意：此親屬範疇**不包括「前配偶」**！離職後 3 年內亦不得接洽離職前 5 年內之職務相關事務。",
            "law": "《政府採購法》第15條利益衝突迴避"
        }
    }
    
    html_template = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>政府採購法之總則、招標及決標 - 互動備考系統</title>
    <meta name="description" content="政府採購法之總則、招標及決標系統化重點筆記與互動式模擬備考系統，助您迅速掌握考試重點，高分通關！">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;700;900&family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
    
    <style>
        :root {
            --bg-primary: #0b0f19;
            --bg-secondary: #111827;
            --bg-card: #1f2937;
            --bg-card-hover: #374151;
            --text-primary: #f9fafb;
            --text-secondary: #9ca3af;
            --text-muted: #6b7280;
            --accent-primary: #10b981; /* Emerald Green */
            --accent-primary-glow: rgba(16, 185, 129, 0.15);
            --accent-secondary: #f43f5e; /* Rose/Coral Red */
            --accent-warning: #f59e0b; /* Amber */
            --border-color: rgba(255, 255, 255, 0.08);
            --glow-green: 0 0 15px rgba(16, 185, 129, 0.3);
            --glow-red: 0 0 15px rgba(244, 63, 94, 0.3);
            --transition-speed: 0.3s;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            scroll-behavior: smooth;
        }

        body {
            background-color: var(--bg-primary);
            color: var(--text-primary);
            font-family: 'Noto Sans TC', 'Outfit', sans-serif;
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* Scrollbar styling */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: var(--bg-primary);
        }
        ::-webkit-scrollbar-thumb {
            background: var(--bg-card);
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: var(--text-muted);
        }

        /* Header Navigation */
        header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
            background: rgba(11, 15, 25, 0.7);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-color);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 1.25rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            color: var(--text-primary);
        }

        .logo span {
            color: var(--accent-primary);
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
        }

        nav {
            display: flex;
            gap: 1.5rem;
        }

        nav a {
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 0.95rem;
            font-weight: 500;
            transition: color var(--transition-speed);
            position: relative;
            padding: 0.25rem 0;
        }

        nav a:hover, nav a.active {
            color: var(--text-primary);
        }

        nav a.active::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: var(--accent-primary);
            border-radius: 2px;
            box-shadow: var(--glow-green);
        }

        /* Hero Section */
        .hero {
            padding: 8rem 2rem 4rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
            position: relative;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: -200px;
            left: 50%;
            transform: translateX(-50%);
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(16, 185, 129, 0.08) 0%, rgba(11, 15, 25, 0) 70%);
            z-index: -1;
            pointer-events: none;
        }

        .hero h1 {
            font-size: 2.75rem;
            font-weight: 900;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, var(--text-primary) 30%, #a7f3d0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
        }

        .hero p {
            font-size: 1.15rem;
            color: var(--text-secondary);
            max-width: 600px;
            margin: 0 auto 2rem auto;
        }

        .hero-stats {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 1.5rem;
        }

        .hero-stat {
            background: rgba(31, 41, 55, 0.4);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 0.75rem 1.5rem;
            backdrop-filter: blur(8px);
        }

        .hero-stat .num {
            font-family: 'Outfit', sans-serif;
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--accent-primary);
        }

        .hero-stat .lbl {
            font-size: 0.85rem;
            color: var(--text-secondary);
        }

        /* Container & Grid layout */
        main {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        section {
            margin-bottom: 6rem;
            scroll-margin-top: 80px;
        }

        .section-title {
            font-size: 1.75rem;
            font-weight: 700;
            margin-bottom: 2rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            position: relative;
        }

        .section-title::after {
            content: '';
            flex-grow: 1;
            height: 1px;
            background: var(--border-color);
        }

        .section-title svg {
            color: var(--accent-primary);
            width: 28px;
            height: 28px;
        }

        /* Board 1: Core Architecture Card Grid */
        .arch-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
            gap: 1.5rem;
        }

        .arch-card {
            background-color: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 2rem;
            transition: all var(--transition-speed);
            position: relative;
            overflow: hidden;
        }

        .arch-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: var(--accent-primary);
            opacity: 0.7;
        }

        .arch-card:hover {
            transform: translateY(-5px);
            border-color: rgba(16, 185, 129, 0.3);
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(16, 185, 129, 0.05);
        }

        .arch-card-icon {
            background: var(--accent-primary-glow);
            color: var(--accent-primary);
            width: 42px;
            height: 42px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.25rem;
        }

        .arch-card h3 {
            font-size: 1.2rem;
            font-weight: 700;
            margin-bottom: 0.75rem;
            color: var(--text-primary);
        }

        .arch-card ul {
            list-style: none;
        }

        .arch-card li {
            font-size: 0.95rem;
            color: var(--text-secondary);
            margin-bottom: 0.6rem;
            padding-left: 1.25rem;
            position: relative;
        }

        .arch-card li::before {
            content: '✦';
            position: absolute;
            left: 0;
            top: 0;
            color: var(--accent-primary);
            font-size: 0.8rem;
        }

        /* Board 2: Number Codes Counters */
        .number-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1.5rem;
        }

        .num-card {
            background: linear-gradient(145deg, var(--bg-secondary) 0%, rgba(31, 41, 55, 0.8) 100%);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 1.75rem;
            text-align: center;
            transition: all var(--transition-speed);
        }

        .num-card:hover {
            border-color: rgba(245, 158, 11, 0.4);
            transform: translateY(-3px);
        }

        .num-val {
            font-family: 'Outfit', sans-serif;
            font-size: 2.5rem;
            font-weight: 800;
            color: var(--accent-warning);
            margin-bottom: 0.5rem;
            line-height: 1;
            text-shadow: 0 0 10px rgba(245, 158, 11, 0.2);
        }

        .num-title {
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 0.5rem;
        }

        .num-desc {
            font-size: 0.85rem;
            color: var(--text-secondary);
        }

        /* Board 3: Trap Table */
        .trap-container {
            background-color: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            overflow: hidden;
        }

        .trap-table {
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        }

        .trap-table th {
            background-color: rgba(31, 41, 55, 0.5);
            padding: 1rem 1.5rem;
            font-size: 0.95rem;
            font-weight: 700;
            color: var(--text-primary);
            border-bottom: 1px solid var(--border-color);
        }

        .trap-row {
            border-bottom: 1px solid var(--border-color);
            transition: background-color var(--transition-speed);
            cursor: pointer;
        }

        .trap-row:hover {
            background-color: rgba(255, 255, 255, 0.02);
        }

        .trap-row td {
            padding: 1.25rem 1.5rem;
            font-size: 0.95rem;
            vertical-align: top;
        }

        .trap-wrong {
            color: var(--accent-secondary);
            font-weight: 500;
        }

        .trap-right {
            color: var(--accent-primary);
            font-weight: 500;
        }

        .trap-detail {
            background-color: rgba(17, 24, 39, 0.6);
            display: none;
            border-bottom: 1px solid var(--border-color);
        }

        .trap-detail-content {
            padding: 1.5rem;
            font-size: 0.9rem;
            color: var(--text-secondary);
            border-left: 4px solid var(--accent-warning);
        }

        .trap-tag {
            display: inline-block;
            font-size: 0.75rem;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            background: rgba(245, 158, 11, 0.15);
            color: var(--accent-warning);
            margin-bottom: 0.5rem;
            font-weight: 500;
        }

        /* Board 4: Classic Explanations */
        .classic-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }

        .classic-card {
            background-color: var(--bg-secondary);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 1.75rem;
            transition: border-color var(--transition-speed);
        }

        .classic-card:hover {
            border-color: rgba(16, 185, 129, 0.3);
        }

        .classic-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 1rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 0.75rem;
        }

        .classic-num-lbl {
            background: var(--accent-primary-glow);
            color: var(--accent-primary);
            font-family: 'Outfit', sans-serif;
            font-weight: 800;
            font-size: 0.85rem;
            padding: 0.25rem 0.6rem;
            border-radius: 6px;
        }

        .classic-title {
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-primary);
        }

        .classic-law {
            font-size: 0.8rem;
            color: var(--accent-warning);
            background: rgba(245, 158, 11, 0.1);
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            margin-top: 0.25rem;
            display: inline-block;
        }

        .classic-body {
            font-size: 0.95rem;
            color: var(--text-secondary);
            margin-bottom: 1rem;
        }

        .classic-exp {
            background: rgba(255, 255, 255, 0.03);
            border-left: 3px solid var(--accent-primary);
            padding: 1rem;
            border-radius: 0 8px 8px 0;
            font-size: 0.9rem;
            color: var(--text-primary);
        }

        /* Interactive Quiz Section */
        .quiz-container {
            background-color: var(--bg-secondary);
            border: 2px solid rgba(16, 185, 129, 0.25);
            border-radius: 20px;
            padding: 2.5rem;
            box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.5);
            position: relative;
            overflow: hidden;
        }

        .quiz-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 1rem;
        }

        .quiz-info {
            font-size: 0.95rem;
            color: var(--text-secondary);
        }

        .quiz-score-lbl {
            background: rgba(16, 185, 129, 0.1);
            color: var(--accent-primary);
            padding: 0.35rem 0.75rem;
            border-radius: 30px;
            font-weight: 700;
            font-size: 0.9rem;
        }

        .quiz-question {
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 1.5rem;
            line-height: 1.5;
        }

        .quiz-options {
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            margin-bottom: 1.5rem;
        }

        .quiz-option-btn {
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            padding: 1rem 1.25rem;
            border-radius: 10px;
            cursor: pointer;
            text-align: left;
            font-size: 0.95rem;
            font-family: inherit;
            transition: all 0.2s;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .quiz-option-btn:hover:not(:disabled) {
            background-color: var(--bg-card-hover);
            border-color: rgba(255, 255, 255, 0.15);
            transform: translateX(3px);
        }

        .quiz-option-btn.correct {
            background-color: rgba(16, 185, 129, 0.15) !important;
            border-color: var(--accent-primary) !important;
            color: var(--accent-primary);
            font-weight: 700;
            box-shadow: var(--glow-green);
        }

        .quiz-option-btn.wrong {
            background-color: rgba(244, 63, 94, 0.15) !important;
            border-color: var(--accent-secondary) !important;
            color: var(--accent-secondary);
            font-weight: 700;
            box-shadow: var(--glow-red);
        }

        .quiz-feedback {
            background-color: rgba(31, 41, 55, 0.5);
            border-radius: 12px;
            padding: 1.25rem;
            margin-top: 1.5rem;
            display: none;
            border-left: 4px solid var(--accent-primary);
            animation: fadeIn 0.3s ease-in-out;
        }

        .quiz-feedback h4 {
            font-size: 0.95rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
        }

        .quiz-feedback p {
            font-size: 0.9rem;
            color: var(--text-secondary);
        }

        .quiz-nav-btns {
            display: flex;
            justify-content: space-between;
            margin-top: 1.5rem;
            gap: 1rem;
        }

        .quiz-action-btn {
            background-color: var(--bg-primary);
            border: 1px solid var(--border-color);
            color: var(--text-primary);
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-family: inherit;
            cursor: pointer;
            transition: all var(--transition-speed);
            font-weight: 500;
            flex: 1;
            text-align: center;
        }

        .quiz-action-btn:hover:not(:disabled) {
            background-color: var(--bg-card);
            border-color: var(--text-secondary);
        }

        .quiz-action-btn:disabled {
            opacity: 0.3;
            cursor: not-allowed;
        }

        .quiz-action-btn.primary-btn {
            background-color: var(--accent-primary);
            color: var(--bg-primary);
            border: none;
            font-weight: 700;
        }

        .quiz-action-btn.primary-btn:hover {
            background-color: #059669;
            box-shadow: var(--glow-green);
        }

        /* Alert styling inside text */
        .info-alert {
            background: rgba(16, 185, 129, 0.05);
            border-left: 4px solid var(--accent-primary);
            padding: 1rem 1.25rem;
            border-radius: 0 8px 8px 0;
            margin: 1.5rem 0;
        }

        .info-alert-title {
            font-weight: 700;
            color: var(--accent-primary);
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.95rem;
            margin-bottom: 0.25rem;
        }

        .info-alert-desc {
            font-size: 0.9rem;
            color: var(--text-secondary);
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(5px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Responsive styling */
        @media (max-width: 768px) {
            header {
                padding: 1rem;
                flex-direction: column;
                gap: 1rem;
            }
            nav {
                gap: 1rem;
                width: 100%;
                justify-content: center;
                overflow-x: auto;
                padding-bottom: 0.25rem;
            }
            .hero {
                padding: 10rem 1rem 3rem 1rem;
            }
            .hero h1 {
                font-size: 2rem;
            }
            .arch-grid {
                grid-template-columns: 1fr;
            }
            .quiz-container {
                padding: 1.5rem;
            }
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 4rem 2rem;
            color: var(--text-muted);
            font-size: 0.85rem;
            border-top: 1px solid var(--border-color);
            margin-top: 4rem;
        }

        footer p {
            margin-bottom: 0.5rem;
        }
    </style>
</head>
<body>

    <!-- Header Navigation -->
    <header>
        <div class="logo">
            <span>PCC</span> 政府採購法備考系統
        </div>
        <nav>
            <a href="#hero" class="active">主頁</a>
            <a href="#arch">核心架構</a>
            <a href="#numbers">數字密碼</a>
            <a href="#traps">易錯陷阱</a>
            <a href="#classics">經典題庫</a>
            <a href="#quiz">模擬測驗</a>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero" id="hero">
        <h1>政府採購法之總則、招標及決標</h1>
        <p>系統化備考重點提煉與離線互動小測驗。專為中華民國公共工程委員會「採購專業人員考試」精準打造。</p>
        <div class="hero-stats">
            <div class="hero-stat">
                <div class="num">200</div>
                <div class="lbl">精選選擇題</div>
            </div>
            <div class="hero-stat">
                <div class="num">5 大</div>
                <div class="lbl">常見易錯陷阱</div>
            </div>
            <div class="hero-stat">
                <div class="num">100%</div>
                <div class="lbl">忠於標準答案</div>
            </div>
        </div>
    </section>

    <main>
        
        <!-- Board 1: Core Architecture -->
        <section id="arch">
            <h2 class="section-title">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
                </svg>
                🎯 第一板塊：核心知識架構
            </h2>
            <div class="arch-grid">
                
                <div class="arch-card">
                    <div class="arch-card-icon">
                        <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"></path></svg>
                    </div>
                    <h3>總則與適用範圍</h3>
                    <ul>
                        <li><strong>採購法定分類</strong>：分為工程定作、財物買受/租賃、勞務委任等三大類（第7條）。</li>
                        <li><strong>受機關補助採購</strong>：補助金額達 <strong>50% 以上</strong>且在<strong>公告金額以上</strong>者適用採購法。應由「補助機關」負責監督與監辦，而非其上級機關（第4條）。</li>
                        <li><strong>請託關說與迴避</strong>：涉及本人、配偶、三親等內血親或姻親、共同生活家屬利益時應行迴避（第15條）。離職承辦、監辦人員 <strong>3年內</strong>不得代理廠商向原任職機關接洽離職前 <strong>5年內</strong>相關事務。</li>
                    </ul>
                </div>

                <div class="arch-card">
                    <div class="arch-card-icon">
                        <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                    </div>
                    <h3>招標方式與資格限制</h3>
                    <ul>
                        <li><strong>招標法規程序</strong>：分為公開招標、選擇性招標與限制性招標。經常性採購得建立 <strong>6家以上</strong>合格廠商名單（第21條）。</li>
                        <li><strong>專屬權利之範圍</strong>：第22條第1項第2款之專屬權利<strong>明確排除「商標專用權」</strong>（第22條）。</li>
                        <li><strong>同等品與品牌限制</strong>：技術規格若無國際/國家標準，應列舉 <strong>3家以上</strong>特定廠牌並註明「或同等品」（第26條）。</li>
                        <li><strong>共同投標與統包</strong>：共同投標須檢附公證或認證之協議書，連帶負履約責任（第25條）。統包不得採限制性招標第9款評選。</li>
                    </ul>
                </div>

                <div class="arch-card">
                    <div class="arch-card-icon">
                        <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"></path></svg>
                    </div>
                    <h3>等標期、押標金與決標</h3>
                    <ul>
                        <li><strong>等標期縮短機制</strong>：電子領標得縮短 <strong>3日</strong>，公開閱覽得縮短 <strong>5日</strong>。變更招標文件非重大改變且於截止日前 <strong>5日</strong>公告者，得免延長等標期。</li>
                        <li><strong>押標金與保證金</strong>：額度以不逾標價之 <strong>5%</strong> 且不逾新臺幣 <strong>5,000萬元</strong>為原則（第30條）。電子投標押標金減收上限為 <strong>10%</strong>。</li>
                        <li><strong>底價與廢標</strong>：底價於開標前應予保密。廢標（無決標）後機關應刊登無法決標公告（第27條）。</li>
                    </ul>
                </div>

            </div>
        </section>

        <!-- Board 2: Number Codes -->
        <section id="numbers">
            <h2 class="section-title">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 20l4-16m2 16l4-16M6 9h14M4 15h14"></path>
                </svg>
                🔢 第二板塊：常考「數字、比例與時限」密碼
            </h2>
            <div class="number-grid">
                
                <div class="num-card">
                    <div class="num-val">150 萬</div>
                    <div class="num-title">公告金額門檻</div>
                    <div class="num-desc">現行政府採購公告金額定為新臺幣 150 萬元，為區分招標作業程序之關鍵分水嶺。</div>
                </div>

                <div class="num-card">
                    <div class="num-val">5,000 萬</div>
                    <div class="num-title">查核金額 (工程/財物)</div>
                    <div class="num-desc">工程與財物採購之查核金額為 5,000 萬元（勞務為 1,000 萬），此門檻以上需報請上級機關派員監辦。</div>
                </div>

                <div class="num-card">
                    <div class="num-val">5% / 5,000萬</div>
                    <div class="num-title">押標金法定上限</div>
                    <div class="num-desc">押標金以不逾預算金額或標價之 5% 為原則，且絕對上限不得逾新臺幣 5,000 萬元。</div>
                </div>

                <div class="num-card">
                    <div class="num-val">50%</div>
                    <div class="num-title">追加工程與補助限制</div>
                    <div class="num-desc">法人團體受補助採購適用本法之金額比率門檻；亦為限制性招標追加工程契約金額之累計上限比率。</div>
                </div>

                <div class="num-card">
                    <div class="num-val">3日 / 5日</div>
                    <div class="num-title">電子領標與公閱縮短</div>
                    <div class="num-desc">電子領標得縮短等標期 3 日；招標前辦理公開閱覽得縮短等標期 5 日。</div>
                </div>

                <div class="num-card">
                    <div class="num-val">3年 / 5年</div>
                    <div class="num-title">離職人員迴避限制</div>
                    <div class="num-desc">離職承辦、監辦人員 3 年內不得向原任職機關接洽離職前 5 年內與職務有關之事務。</div>
                </div>

                <div class="num-card">
                    <div class="num-val">10% / 50%</div>
                    <div class="num-title">保證金減收上限</div>
                    <div class="num-desc">電子投標廠商押標金/保證金減收上限為 10%；經評選優良廠商減收上限為 50%。</div>
                </div>

                <div class="num-card">
                    <div class="num-val">30%</div>
                    <div class="num-title">資訊服務預付款上限</div>
                    <div class="num-desc">資訊服務評選得預付一部分費用，但預付款以不超過契約總額上限之 30% 為原則。</div>
                </div>

            </div>
        </section>

        <!-- Board 3: Trap Table -->
        <section id="traps">
            <h2 class="section-title">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>
                </svg>
                ⚠️ 第三板塊：選擇題常考易錯「文字陷阱」對比表
            </h2>
            
            <div class="info-alert">
                <div class="info-alert-title">
                    <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    備考心法提示：點擊下方表格各列，可展開查閱該易錯題型的法規深度釋義。
                </div>
                <div class="info-alert-desc">本單元的文字陷阱高度集中於「監辦層級」、「專屬權利範圍」、「等標期縮短底限」與「迴避資格」，務必仔細分辨。</div>
            </div>

            <div class="trap-container">
                <table class="trap-table">
                    <thead>
                        <tr>
                            <th style="width: 45%;">❌ 題庫常見錯誤敘述（混淆干擾項）</th>
                            <th style="width: 55%;">⭕ 正確法規與實務觀念</th>
                        </tr>
                    </thead>
                    <tbody>
                        
                        <tr class="trap-row" onclick="toggleTrapDetail('trap_1')">
                            <td class="trap-wrong">法人或團體接受機關補助辦理採購，受補助者於辦理查核金額以上採購之開標，應受補助機關之上級機關監督。</td>
                            <td class="trap-right">是非觀念為 X。受補助採購適用採購法者，其辦理查核金額以上採購，應受「補助機關」派員監督監辦，而非其上級機關。</td>
                        </tr>
                        <tr class="trap-detail" id="trap_1">
                            <td colspan="2">
                                <div class="trap-detail-content">
                                    <span class="trap-tag">法規依據：《政府採購法》第4條及其施行細則</span>
                                    <p>受機關補助辦理採購之法人或團體，其採購程序雖適用採購法，但該團體本身並無「上級機關」。因此，其查核金額以上採購之監辦、核准等權限，均是由「補助機關」來實施監督，而非補助機關之上級機關。</p>
                                </div>
                            </td>
                        </tr>

                        <tr class="trap-row" onclick="toggleTrapDetail('trap_2')">
                            <td class="trap-wrong">機關依採購法第22條第1項第2款辦理限制性招標，所稱之專屬權利包含商標專用權。</td>
                            <td class="trap-right">是非觀念為 X。採購法第22條第1項第2款所定之專屬權利，**明確排除「商標專用權」**！</td>
                        </tr>
                        <tr class="trap-detail" id="trap_2">
                            <td colspan="2">
                                <div class="trap-detail-content">
                                    <span class="trap-tag">法規依據：《政府採購法施行細則》第22條第1項</span>
                                    <p>專屬權利指專利權、著作權、電路布局權或其他經主管機關認定之專屬權利，但明文不包括商標專用權。機關不得僅以特定商標為由逕採限制性招標，以免規避公開競爭程序。</p>
                                </div>
                            </td>
                        </tr>

                        <tr class="trap-row" onclick="toggleTrapDetail('trap_3')">
                            <td class="trap-wrong">機關辦理統包採購，得依採購法第22條第1項第9款規定辦理公開評選優勝廠商。</td>
                            <td class="trap-right">是非觀念為 X。統包採購包含設計與施工等，**不得**依第22條第1項第9款規定之評選專業、技術、資訊或設計服務方式辦理。</td>
                        </tr>
                        <tr class="trap-detail" id="trap_3">
                            <td colspan="2">
                                <div class="trap-detail-content">
                                    <span class="trap-tag">法規依據：《政府採購法》第24條及統包實務規範</span>
                                    <p>統包採購之招標方式應採公開招標或選擇性招標（若符合限制性招標其他款則依其規定），但其本質非單純之勞務委任，因此不適用第22條第1項第9款（委託專業、技術、資訊或設計服務）之招標方式。</p>
                                </div>
                            </td>
                        </tr>

                        <tr class="trap-row" onclick="toggleTrapDetail('trap_4')">
                            <td class="trap-wrong">機關依採購法第22條第1項第11款規定採購房地產，其訂有底價者，底價訂定之時機為辦理公告前、開標前或比價前。</td>
                            <td class="trap-right">是非觀念為 X。房地產採購底價訂定時機非屬上述，答案應選「以上皆非」。</td>
                        </tr>
                        <tr class="trap-detail" id="trap_4">
                            <td colspan="2">
                                <div class="trap-detail-content">
                                    <span class="trap-tag">法規依據：《機關指定地區採購房地產作業辦法》</span>
                                    <p>指定地區採購房地產時，底價之訂定應於「勘選小組」或「徵選小組」實地勘選適合需要之房地產後，並於進行「議價前」訂定之。因此在公告前、開標前、比價前等時機訂定均不正確。</p>
                                </div>
                            </td>
                        </tr>

                        <tr class="trap-row" onclick="toggleTrapDetail('trap_5')">
                            <td class="trap-wrong">機關人員利益衝突迴避條款之範圍，包括本人、配偶、二親等內親屬、前配偶及共同生活之親屬利益。</td>
                            <td class="trap-right">是非觀念為 X。迴避條款所定之親屬利益範圍，**不包括「前配偶」**。</td>
                        </tr>
                        <tr class="trap-detail" id="trap_5">
                            <td colspan="2">
                                <div class="trap-detail-content">
                                    <span class="trap-tag">法規依據：《政府採購法》第15條</span>
                                    <p>採購法第15條利益衝突之親屬迴避範疇包括：本人、配偶、三親等以內之血親或姻親，以及共同生活之家屬。因「前配偶」在法律上婚姻關係已消滅，且非法定血親或姻親，因此不列入法定強制迴避範圍。</p>
                                </div>
                            </td>
                        </tr>

                    </tbody>
                </table>
            </div>
        </section>

        <!-- Board 4: Classic Explanations -->
        <section id="classics">
            <h2 class="section-title">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
                </svg>
                📝 第四板塊：精選經典題解析
            </h2>
            <div class="classic-grid">
                
                <div class="classic-card">
                    <div class="classic-header">
                        <div>
                            <span class="classic-title">精選題 1：後續擴充採購金額之計算方式</span>
                            <br>
                            <span class="classic-law">__LAW_MCQ_16__</span>
                        </div>
                        <span class="classic-num-lbl">選擇第 16 題</span>
                    </div>
                    <div class="classic-body">
                        <strong>題目</strong>：某機關擬委外編印月刊，預估1年12期為新臺幣90萬元，並於招標公告及招標文件敘明履約情形良好者，將依採購法第22條第1項第7款續約2年。該採購之採購金額為？
                        <br>
                        <strong>選項</strong>：(1)新臺幣90萬元。 (2)新臺幣180萬元。 (3)新臺幣270萬元。 (4)決標金額。
                        <br>
                        <strong>答案</strong>：(3) 新臺幣270萬元。
                    </div>
                    <div class="classic-exp">
                        <strong>核心解析</strong>：__DESC_MCQ_16__
                    </div>
                </div>

                <div class="classic-card">
                    <div class="classic-header">
                        <div>
                            <span class="classic-title">精選題 2：限制性招標之專屬權利排除</span>
                            <br>
                            <span class="classic-law">__LAW_MCQ_41__</span>
                        </div>
                        <span class="classic-num-lbl">選擇第 41 題</span>
                    </div>
                    <div class="classic-body">
                        <strong>題目</strong>：下列何者不是屬採購法第22條第1項第2款因無其他合適替代標的得採限制性招標所稱之專屬權利？
                        <br>
                        <strong>選項</strong>：(1)商標專用權。 (2)專利權。 (3)著作權。 (4)電路布局權。
                        <br>
                        <strong>答案</strong>：(1) 商標專用權。
                    </div>
                    <div class="classic-exp">
                        <strong>核心解析</strong>：__DESC_MCQ_41__
                    </div>
                </div>

                <div class="classic-card">
                    <div class="classic-header">
                        <div>
                            <span class="classic-title">精選題 3：標價偏低不予發還押標金之例外</span>
                            <br>
                            <span class="classic-law">__LAW_MCQ_110__</span>
                        </div>
                        <span class="classic-num-lbl">選擇第 110 題</span>
                    </div>
                    <div class="classic-body">
                        <strong>題目</strong>：廠商繳納押標金不予發還之情形，下列何者為非？
                        <br>
                        <strong>選項</strong>：(1)冒用他人名義或證件投標。 (2)得標後拒不簽約。 (3)廠商之標價偏低，有採購法第58條所定情形而未於機關通知期限內提出合理之說明者。 (4)借用他人名義或證件投標。
                        <br>
                        <strong>答案</strong>：(3) 廠商之標價偏低，有採購法第58條所定情形而未於機關通知期限內提出合理之說明者。
                    </div>
                    <div class="classic-exp">
                        <strong>核心解析</strong>：__DESC_MCQ_110__
                    </div>
                </div>

                <div class="classic-card">
                    <div class="classic-header">
                        <div>
                            <span class="classic-title">精選題 4：電子領標等標期縮短與法定底限</span>
                            <br>
                            <span class="classic-law">__LAW_MCQ_93__</span>
                        </div>
                        <span class="classic-num-lbl">選擇第 93 題</span>
                    </div>
                    <div class="classic-body">
                        <strong>題目</strong>：機關辦理採購，依採購法第93條之1規定辦理電子領標並於招標公告敘明者，等標期得縮短A日。但縮短後不得少於B日？
                        <br>
                        <strong>選項</strong>：(1)A=2日；B=5日。 (2)A=3日；B=5日。 (3)A=3日；B=7日。 (4)A=5日；B=10日。
                        <br>
                        <strong>答案</strong>：(3) A=3日；B=7日。 （註：本題預設採購案件為公告金額以上，故縮短後不得少於7日）
                    </div>
                    <div class="classic-exp">
                        <strong>核心解析</strong>：__DESC_MCQ_93__
                    </div>
                </div>

                <div class="classic-card">
                    <div class="classic-header">
                        <div>
                            <span class="classic-title">精選題 5：機關人員採購迴避之親屬範疇</span>
                            <br>
                            <span class="classic-law">__LAW_MCQ_30__</span>
                        </div>
                        <span class="classic-num-lbl">選擇第 30 題</span>
                    </div>
                    <div class="classic-body">
                        <strong>題目</strong>：機關人員對於與採購有關之事項，下列何者不是應迴避之情形？
                        <br>
                        <strong>選項</strong>：(1)涉及本人、配偶利益。 (2)涉及二親等以內親屬利益。 (3)涉及前配偶或三親等以內血親或姻親利益。 (4)涉及共同生活家屬利益。
                        <br>
                        <strong>答案</strong>：(3) 涉及前配偶或三親等以內血親或姻親利益。
                    </div>
                    <div class="classic-exp">
                        <strong>核心解析</strong>：__DESC_MCQ_30__
                    </div>
                </div>

            </div>
        </section>

        <!-- Board 5: Interactive Quiz -->
        <section id="quiz">
            <h2 class="section-title">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path>
                </svg>
                ⚔️ 互動式模擬測驗 (全題庫 200 題隨機挑戰)
            </h2>
            
            <div class="quiz-container">
                <div class="quiz-header">
                    <div class="quiz-info" id="quiz-progress">載入題目中...</div>
                    <div class="quiz-score-lbl" id="quiz-score">得分: 0 / 0 (0%)</div>
                </div>
                <div class="quiz-question" id="quiz-question">
                    讀取資料中...
                </div>
                <div class="quiz-options" id="quiz-options">
                    <!-- Options injected here by JS -->
                </div>
                <div class="quiz-feedback" id="quiz-feedback">
                    <h4 id="quiz-feedback-title">法規依據與解析</h4>
                    <p id="quiz-feedback-text">解析載入中...</p>
                </div>
                <div class="quiz-nav-btns">
                    <button class="quiz-action-btn" id="quiz-prev-btn" onclick="prevQuestion()" disabled>上一題</button>
                    <button class="quiz-action-btn primary-btn" id="quiz-next-btn" onclick="nextQuestion()">下一題</button>
                </div>
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer>
        <p>© 115 採購專業人員考試備考網頁 - 政府採購法之總則、招標及決標</p>
        <p>依據最新中華民國行政院公共工程委員會標準題庫提煉，100% 精準無編造</p>
    </footer>

    <!-- Injected Questions Data -->
    <script>
        const mcqsData = __QUESTIONS_DATA__;
        
        let allQuestions = [];
        
        // Process MCQs
        mcqsData.forEach(q => {
            allQuestions.push({
                id: q.id,
                type: 'mcq',
                question: "[選擇題 " + q.id + "] " + q.question,
                choices: Object.entries(q.choices).map(([key, val]) => ({
                    num: parseInt(key),
                    text: "(" + key + ") " + val
                })),
                answer: q.answer,
                law: q.law,
                explanation: getExplanation(q.id, q.answer, q.law)
            });
        });

        // Function to dynamically supply explanation
        function getExplanation(qid, correctAns, law) {
            const db = {
                1: "機關購買房地產（買受）屬於財物採購（第2條、第7條），應適用採購法。變賣或標售財物屬於收入，不適用採購法；補助選定非屬採購本體。",
                2: "購買冷凍食品（肉品）屬於財物之買受，適用採購法。買匯、出租及標售（收入）皆不適用。",
                3: "土地之出租屬於機關收入，非採購法所稱之採購（工程之定作、財物之買受、租賃、勞務之委任或僱傭）。",
                4: "受機關補助辦理採購，補助金額占採購金額達半數以上，且補助金額在公告金額以上者，適用採購法（第4條）。",
                6: "受補助之法人或團體，其查核金額以上採購，應報請「補助機關」派員監督監辦，而非補助機關之上級機關（第4條）。",
                8: "指定廠牌公開徵求報價單辦理決標涉限制競爭（小額採購除外，50萬已達公告金額1/10以上非小額）；限制製造廠代理商或特定轄區經驗亦限制競爭。不適用條約協定限我國投標是合法的。",
                11: "權利之買受或租賃，歸類於「財物採購」（第7條）。",
                12: "查核金額以上之採購，開標、比價、議價、決標及驗收，應報請上級機關派員監辦（第12條）。",
                16: "採購金額應包括後續擴充預估總金額。90萬 + 90萬*2年 = 270萬元（第12條/細則第6條）。",
                23: "採購案之承辦人員負責採購執行，為避免角色衝突，不得同時擔任該採購案之監辦人員（第13條）。",
                24: "公告金額指新臺幣 150 萬元（第13條最新規定）。",
                30: "利益迴避條款之親屬範疇不包括「前配偶」（第15條）。",
                31: "離職人員 3 年內不得為本人或代理廠商向原任職機關接洽處理離職前 5 年內與職務有關之事務（第15條）。",
                41: "專屬權利包括專利權、著作權、電路布局權等，但明確排除「商標專用權」（第22條細則）。",
                42: "機關辦理評選專業服務、技術服務、資訊服務或設計競賽，第1次開標不受3家限制，1家投標即可開標（第22條第1項第9款）。",
                54: "委託資訊服務預付款上限以不超過契約總額之 30% 為原則（第22條）。",
                62: "追加工程限制之 50% 係指「追加累計金額占原主契約金額之比率」（第22條）。",
                73: "統包採購包含設計與施工，不得依第22條第1項第9款（單純勞務評選）方式辦理限制性招標。",
                81: "僅在招標文件要求特定廠牌並註明「或同等品」是不夠的，必須符合「無國際/國家標準且無法精確說明招標要求」之法定前提（第26條）。",
                91: "非屬重大改變且於截止日前 5 日公告或書面通知廠商者，得免延長等標期（第28條）。",
                93: "電子領標得縮短等標期 3 日，但縮短後公告金額以上不得少於 7 日（第28條/招標期限標準）。",
                97: "招標前辦理公開閱覽，等標期得縮短 5 日，但縮短後不得少於 10 日（第28條/招標期限標準）。",
                107: "押標金應於招標文件規定廠商以特定方式繳納，不應要求「將現金附於投標文件內遞送」，此舉違反押標金保證金格式與收受實務（第30條）。",
                108: "押標金額度以不逾標價之 5% 為原則，且不得逾新臺幣 5,000 萬元（第30條）。",
                110: "標價偏低未提合理說明，應不予決標，但其押標金仍應發還，不屬於不予發還押標金之範疇（第31條）。"
            };
            
            let baseExp = db[qid] || `本題標準答案為：(${correctAns})。`;
            if (law) {
                baseExp += `【法規依據：${law}】`;
            }
            return baseExp;
        }

        // Shuffle questions
        function shuffle(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
            return array;
        }

        // Shuffle questions for randomized experience
        allQuestions = shuffle(allQuestions);

        let currentIndex = 0;
        let score = 0;
        let answeredCount = 0;
        let userSelections = {};

        function loadQuestion(index) {
            const q = allQuestions[index];
            const progress = document.getElementById("quiz-progress");
            const questionTitle = document.getElementById("quiz-question");
            const optionsContainer = document.getElementById("quiz-options");
            const feedback = document.getElementById("quiz-feedback");
            const prevBtn = document.getElementById("quiz-prev-btn");
            
            progress.innerText = `題目進度: ${index + 1} / ${allQuestions.length} [選擇題]`;
            questionTitle.innerText = q.question;
            optionsContainer.innerHTML = "";
            
            feedback.style.display = "none";
            prevBtn.disabled = index === 0;

            const previouslySelected = userSelections[index];
            const hasAnswered = previouslySelected !== undefined;

            q.choices.forEach(opt => {
                const btn = document.createElement("button");
                btn.className = "quiz-option-btn";
                btn.innerText = opt.text;
                btn.disabled = hasAnswered;

                if (hasAnswered) {
                    const optKey = opt.num;
                    const correctAns = q.answer;
                    
                    if (optKey === correctAns) {
                        btn.classList.add("correct");
                    }
                    if (optKey === previouslySelected && previouslySelected !== correctAns) {
                        btn.classList.add("wrong");
                    }
                } else {
                    btn.onclick = () => selectOption(index, opt.num);
                }
                
                optionsContainer.appendChild(btn);
            });

            if (hasAnswered) {
                showFeedback(q);
            }
        }

        function selectOption(index, optionNum) {
            if (userSelections[index] !== undefined) return;
            
            const q = allQuestions[index];
            userSelections[index] = optionNum;
            answeredCount++;
            
            if (optionNum === q.answer) {
                score++;
            }
            
            updateScore();
            loadQuestion(index);
        }

        function showFeedback(q) {
            const feedback = document.getElementById("quiz-feedback");
            const feedbackText = document.getElementById("quiz-feedback-text");
            feedbackText.innerText = q.explanation;
            feedback.style.display = "block";
        }

        function updateScore() {
            const scoreLbl = document.getElementById("quiz-score");
            const pct = answeredCount > 0 ? Math.round((score / answeredCount) * 100) : 0;
            scoreLbl.innerText = `得分: ${score} / ${answeredCount} (${pct}%)`;
        }

        function nextQuestion() {
            if (currentIndex < allQuestions.length - 1) {
                currentIndex++;
                loadQuestion(currentIndex);
            } else {
                alert(`模擬測驗結束！您的最終得分是：${score} / ${allQuestions.length}！`);
            }
        }

        function prevQuestion() {
            if (currentIndex > 0) {
                currentIndex--;
                loadQuestion(currentIndex);
            }
        }

        // Table Trap Toggle Function
        function toggleTrapDetail(id) {
            const detailRow = document.getElementById(id);
            if (detailRow.style.display === "table-row") {
                detailRow.style.display = "none";
            } else {
                detailRow.style.display = "table-row";
            }
        }

        // Smooth scroll for nav active state
        window.addEventListener('scroll', () => {
            let current = '';
            const sections = document.querySelectorAll('section');
            const navLinks = document.querySelectorAll('nav a');
            
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                if (pageYOffset >= sectionTop - 120) {
                    current = section.getAttribute('id');
                }
            });
            
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href').includes(current)) {
                    link.classList.add('active');
                }
            });
        });

        // Load first question on init
        window.onload = () => {
            loadQuestion(0);
        };
    </script>
</body>
</html>
"""
    
    # 注入 JSON 資料
    final_html = html_template
    final_html = final_html.replace("__QUESTIONS_DATA__", json.dumps(questions, ensure_ascii=False))
    
    # 注入經典題解析的標籤與描述
    final_html = final_html.replace("__LAW_MCQ_16__", classic_explanations['mcq_16']['law'])
    final_html = final_html.replace("__DESC_MCQ_16__", classic_explanations['mcq_16']['desc'])
    
    final_html = final_html.replace("__LAW_MCQ_41__", classic_explanations['mcq_41']['law'])
    final_html = final_html.replace("__DESC_MCQ_41__", classic_explanations['mcq_41']['desc'])
    
    final_html = final_html.replace("__LAW_MCQ_110__", classic_explanations['mcq_110']['law'])
    final_html = final_html.replace("__DESC_MCQ_110__", classic_explanations['mcq_110']['desc'])
    
    final_html = final_html.replace("__LAW_MCQ_93__", classic_explanations['mcq_93']['law'])
    final_html = final_html.replace("__DESC_MCQ_93__", classic_explanations['mcq_93']['desc'])
    
    final_html = final_html.replace("__LAW_MCQ_30__", classic_explanations['mcq_30']['law'])
    final_html = final_html.replace("__DESC_MCQ_30__", classic_explanations['mcq_30']['desc'])
    
    with open(OUTPUT_HTML_PATH, "w", encoding="utf-8") as f:
        f.write(final_html)
        
    print(f"Success: Beautiful focus note HTML generated at: {OUTPUT_HTML_PATH}")

if __name__ == "__main__":
    main()
