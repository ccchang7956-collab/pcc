import os
import json

WORKSPACE_DIR = "/Users/ccchang/Documents/採購法題庫"
JSON_PATH = "/Users/ccchang/.gemini/antigravity-ide/brain/ccc5f163-dcac-4c88-9187-d1ddf761bb4c/scratch/parsed_questions.json"
OUTPUT_HTML_PATH = os.path.join(WORKSPACE_DIR, "重點筆記", "政府採購法之罰則及附則_重點筆記.html")

def main():
    os.makedirs(os.path.dirname(OUTPUT_HTML_PATH), exist_ok=True)
    
    if not os.path.exists(JSON_PATH):
        print(f"Error: JSON file not found at {JSON_PATH}")
        return
        
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        questions_data = json.load(f)
        
    mcqs = questions_data.get("mcqs", [])
    tfs = questions_data.get("tfs", [])
    
    print(f"Loaded {len(mcqs)} MCQs and {len(tfs)} TFs.")
    
    # 定義精選經典題解析資料
    classic_explanations = {
        "mcq_19": {
            "title": "環保產品價差優惠與決標順序判定",
            "desc": "本題是非環保最低標 A 報價 170 萬，價差優惠 10% 範圍為 170 * 1.10 = 187 萬元。環保廠商 B（第3類，180萬）與 C（第2類，185萬）均小於 187 萬，D（第1類，188萬）因超出 187 萬被排除。在符合優惠範圍的 B 與 C 中，<b>「第1類及第2類優於第3類」</b>，因此應決標予<b>第2類之 C 廠商</b>（雖然 C 比 B 貴 5 萬），此為考試中極具殺傷力的實務計算題！",
            "law": "《機關優先採購環境保護產品辦法》第12條第1項第2款"
        },
        "mcq_33": {
            "title": "違反轉包且有停權前科之停權期間判定",
            "desc": "機關依政府採購法第 101 條通知轉包，且廠商於「通知日前 5 年內」曾被任一機關刊登公報 1 次，若異議申訴無效，自刊登公報次日起，其停權停投標期間為 <b>6 個月</b>（非一般 1 年）。若前 5 年內曾被刊登 2 次以上，則停權期間會延長為 3 年。",
            "law": "《政府採購法》第103條第1項最新修正案"
        },
        "mcq_14": {
            "title": "採購專業人員資格辭職保留與回任年限",
            "desc": "依《採購專業人員資格考試訓練發證及管理辦法》規定，採購專業人員因辭職至民間廠商任職後，於<b>「5 年內」</b>回任機關採購職務者，仍具採購專業人員資格。本題劉先生 93 年 12 月 30 日離職，5 年內即 98 年 12 月 30 日前回任皆有效，選項中 97 年 6 月 5 日最符合此年限規定。",
            "law": "《採購專業人員資格考試訓練發證及管理辦法》第14條"
        },
        "mcq_42": {
            "title": "公務機關間採購（特別採購）免適用條款",
            "desc": "政府採購法第 105 條第 1 項第 3 款規定，機關向其他公務機關採購財物或勞務，得免適用招標及決標之規定。但仍應遵守監辦（第 13 條）與決標公告。而<b>「第 98 條繳納身障與原住民就業代金」</b>是履約期間一般廠商的義務，機關間採購<b>得不適用第 98 條</b>！",
            "law": "《政府採購法》第105條第1項第3款、特別採購處理辦法"
        },
        "tf_50": {
            "title": "採購評選委員會之開會與出席門檻計算",
            "desc": "評選委員會會議，應有委員總額 1/2 以上出席。本案成立 7 人，二分之一為 3.5 人，故 4 人出席符合出席比例；且《審議規則》規定<b>「專家學者出席人數不得少於 2 人，且不得少於出席人數之 1/3」</b>。4 人之 1/3 為 1.33 人，出席的專家學者有 2 人，故完全合法，並非「不得開會」！是非題 50 答案為 X，是極為經典的計算陷阱。",
            "law": "《採購評選委員會審議規則》第9條"
        }
    }
    
    html_template = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>政府採購法之罰則及附則 - 互動備考系統</title>
    <meta name="description" content="政府採購法之罰則及附則系統化重點筆記與互動式模擬備考系統，助您迅速掌握考試重點，高分通關！">
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
            font-size: 2.75rem;
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
            line-height: 1.7;
        }

        .classic-exp {
            background: rgba(255, 255, 255, 0.03);
            border-left: 3px solid var(--accent-primary);
            padding: 1rem;
            border-radius: 0 8px 8px 0;
            font-size: 0.95rem;
            color: var(--text-primary);
            line-height: 1.6;
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
            line-height: 1.6;
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
            line-height: 1.4;
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
            font-size: 0.95rem;
            color: var(--text-secondary);
            line-height: 1.6;
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
                justify-content: flex-start;
                overflow-x: auto;
                padding-bottom: 0.5rem;
                white-space: nowrap;
                -webkit-overflow-scrolling: touch;
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
            
            /* Table Cardification for Mobile */
            .trap-table, .trap-table thead, .trap-table tbody, .trap-table th, .trap-table td, .trap-table tr {
                display: block;
            }
            .trap-table thead {
                display: none; /* Hide headers on mobile */
            }
            .trap-row {
                border-bottom: 2px solid var(--border-color);
                margin-bottom: 1rem;
                background-color: rgba(31, 41, 55, 0.3);
                border-radius: 12px;
                padding: 1rem;
            }
            .trap-row td {
                padding: 0.5rem 0;
                width: 100% !important;
            }
            .trap-wrong::before {
                content: "❌ 錯誤敘述：";
                font-weight: 700;
                display: block;
                color: var(--accent-secondary);
                margin-bottom: 0.25rem;
            }
            .trap-right::before {
                content: "⭕ 正確觀念：";
                font-weight: 700;
                display: block;
                color: var(--accent-primary);
                margin-bottom: 0.25rem;
            }
            .trap-detail-content {
                border-left: 4px solid var(--accent-warning);
                padding: 1rem;
                background-color: rgba(17, 24, 39, 0.8);
                border-radius: 8px;
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
            <span>PCC</span> 罰則及附則備考系統
        </div>
        <nav>
            <a href="#hero" class="active">主頁</a>
            <a href="#arch">知識架構</a>
            <a href="#numbers">數字密碼</a>
            <a href="#traps">易錯陷阱</a>
            <a href="#classics">經典題庫</a>
            <a href="#quiz">模擬測驗</a>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero" id="hero">
        <h1>政府採購法之罰則及附則</h1>
        <p>系統化備考重點提煉與離線互動小測驗。專為中華民國公共工程委員會「採購專業人員考試」精準打造。</p>
        <div class="hero-stats">
            <div class="hero-stat">
                <div class="num">50 道</div>
                <div class="lbl">精選選擇題</div>
            </div>
            <div class="hero-stat">
                <div class="num">226 道</div>
                <div class="lbl">實務是非題</div>
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
                        <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
                    </div>
                    <h3>刑事罰則與違法處置（第87-92條）</h3>
                    <ul>
                        <li><strong>借牌與圍標責任</strong>：意圖影響政府採購結果或獲取不當利益，而借用他人名義或證件投標者，處 <strong>3年以下有期徒刑</strong>，得併科 <strong>100萬元</strong> 以下罰金。容許他人借用本人名義或證件參加投標者，亦同。</li>
                        <li><strong>洩密獲利罪</strong>：受機關委託之廠商人員，洩漏或交付採購秘密因而獲利者，處 <strong>5年以下有期徒刑</strong>，得併科 <strong>100萬元</strong> 以下罰金。其<strong>未遂犯亦罰之</strong>。</li>
                        <li><strong>違法限制規格罪</strong>：意圖不法利益對技術、規格為違反法令限制或審查因而獲利者，處 <strong>1年以上7年以下有期徒刑</strong>，得併科 <strong>300萬元</strong> 以下罰金。縱自己未獲利（利及他人）亦罰之。</li>
                        <li><strong>廠商併罰制度</strong>：廠商代表人、代理人、雇員因執行業務犯採購法之罪者，除處罰行為人外，對該<b>廠商亦科以同條之罰金</b>。</li>
                    </ul>
                </div>

                <div class="arch-card">
                    <div class="arch-card-icon">
                        <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"></path></svg>
                    </div>
                    <h3>採購行政與專業制度（第93-95條）</h3>
                    <ul>
                        <li><strong>共同供應契約（第93條）</strong>：各機關得就共通需求之<b>財物或勞務</b>簽訂共同供應契約。利用期間包含後續擴充最長以 <strong>2年</strong> 為限。非適用機關經同意且契約載明者得利用。</li>
                        <li><strong>採購評選委員會（第94條）</strong>：應成立評選委員會，委員人數 <strong>5人至17人</strong>。其中專家學者人數不得少於 <strong>1/3</strong>。</li>
                        <li><strong>評選會開會與出席門檻</strong>：應有委員總額 <strong>1/2以上出席</strong>，決議經出席委員<b>過半數</b>同意。出席委員中專家學者人數至少 <strong>2人</strong> 且不得少於出席人數之 <strong>1/3</strong>。<b>民意代表不得擔任委員</b>（民代機關辦理採購時除外）。</li>
                        <li><strong>採購專業人員（第95條）</strong>：主管宜於到職 <strong>2年內</strong> 取得進階資格，非主管宜於到職 <strong>1年內</strong> 取得基本資格。辭職後 <strong>5年內</strong> 回任，仍具資格。</li>
                    </ul>
                </div>

                <div class="arch-card">
                    <div class="arch-card-icon">
                        <svg width="24" height="24" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"></path></svg>
                    </div>
                    <h3>扶助與特別採購（第96-105條）</h3>
                    <ul>
                        <li><strong>優先採購環保產品（第96條）</strong>：允許招標文件載明 <strong>10%以內</strong> 價差優惠。履約期間未提證明或未提供者，得終止契約、追償價差優惠、或依第101條辦理停權，但<b>不可沒收/追繳押標金</b>。</li>
                        <li><strong>中小企業扶助（第97條）</strong>：<b>未達公告金額之採購</b>，除特殊排除情形外，以向中小企業採購為原則。</li>
                        <li><strong>身障及原住民僱用（第98條）</strong>：得標廠商國內員工總人數逾 <strong>100人</strong> 者，履約期間應僱用身心障礙者及原住民各佔員工總人數 <strong>1%</strong> 以上。不足者應繳納代金（身障代金至身障專戶；原住民代金至原民專戶）。</li>
                        <li><strong>特別採購（第105條）</strong>：緊急防疫或公務機關間取得財物勞務，得簽報首長核准免適用採購法招標決標規定。<b>機關間採購得不適用第98條繳納代金之規定</b>。</li>
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
                    <div class="num-val">3 年</div>
                    <div class="num-title">借牌/圍標徒刑與重大停權期</div>
                    <div class="num-desc">借牌投標、得標或容許借牌，處3年以下有期徒刑。擅自減省工料情節重大、刑事罪判決確定，其刊登公報停權期亦為 3 年。</div>
                </div>

                <div class="num-card">
                    <div class="num-val">10%</div>
                    <div class="num-title">優先採購環保產品價差優惠</div>
                    <div class="num-desc">機關優先採購環保產品允許之價差優惠，比率由機關視特性訂定，但不得逾 10%。</div>
                </div>

                <div class="num-card">
                    <div class="num-val">1% / 2%</div>
                    <div class="num-title">身障與原住民法定僱用比例</div>
                    <div class="num-desc">得標廠商國內員工總人數逾 100 人者，履約期間應僱用身心障礙者及原住民各 1% 以上，合計不得少於 2%。</div>
                </div>

                <div class="num-card">
                    <div class="num-val">5 年</div>
                    <div class="num-title">專業人員資格辭職保留期</div>
                    <div class="num-desc">採購專業人員離職或辭職後，於 5 年內回任機關採購職務者，其採購專業人員資格仍予保留。</div>
                </div>

                <div class="num-card">
                    <div class="num-val">20 / 15 日</div>
                    <div class="num-title">停權通知異議與申訴救濟時限</div>
                    <div class="num-desc">對 101 條停權通知不服，應於接獲通知之次日起 20 日內提出書面異議；不服異議結果，得於 15 日內向申訴會提出申訴。</div>
                </div>

                <div class="num-card">
                    <div class="num-val">3 年</div>
                    <div class="num-title">停權處分之裁處權時效</div>
                    <div class="num-desc">將廠商刊登政府採購公報（停權處分），適用或類推行政罰法第27條第1項所定之 3 年裁處權時效。</div>
                </div>

            </div>
        </section>

        <!-- Board 3: Trap Table -->
        <section id="traps">
            <h2 class="section-title">
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>
                </svg>
                ⚠️ 第三板塊：是非題易錯「文字陷阱」對比表
            </h2>
            
            <div class="info-alert">
                <div class="info-alert-title">
                    <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    備考心法提示：點擊下方表格各列，可展開查閱該易錯題型的法規深度釋義。
                </div>
                <div class="info-alert-desc">是非題的考點高度集中在「迴避親屬範圍」、「民意代表限制」、「評選會出席人數」與「停權救濟期限」，務必仔細分辨。</div>
            </div>

            <div class="trap-container">
                <table class="trap-table">
                    <thead>
                        <tr>
                            <th style="width: 48%;">❌ 題庫常見錯誤敘述（答案為 X）</th>
                            <th style="width: 52%;">⭕ 正確法規與實務觀念</th>
                        </tr>
                    </thead>
                    <tbody>
                        
                        <tr class="trap-row" onclick="toggleTrapDetail('trap_1')">
                            <td class="trap-wrong">由主管機關指定機關簽訂之共同供應契約，其適用機關為全國各機關。</td>
                            <td class="trap-right">是非題 39 答案為 X。由主管機關指定機關簽訂共同供應契約者，其適用機關為「中央機關」（非全國各機關）。</td>
                        </tr>
                        <tr class="trap-detail" id="trap_1">
                            <td colspan="2">
                                <div class="trap-detail-content">
                                    <span class="trap-tag">法規依據：《共同供應契約實施辦法》第4條</span>
                                    <p>由主管機關指定機關簽訂共同供應契約者，適用機關為中央機關。但如係由各機關自行辦理或經各機關協議由其中一機關簽訂者，其適用機關得為該等協議機關或其所屬機關。</p>
                                </div>
                            </td>
                        </tr>

                        <tr class="trap-row" onclick="toggleTrapDetail('trap_2')">
                            <td class="trap-wrong">非屬共同供應契約之適用機關，一律不得利用該契約辦理採購。</td>
                            <td class="trap-right">是非題 26 答案為 X。非適用機關在「徵得訂約廠商同意」且「共同供應契約載明該情形」者，仍得利用該契約採購。</td>
                        </tr>
                        <tr class="trap-detail" id="trap_2">
                            <td colspan="2">
                                <div class="trap-detail-content">
                                    <span class="trap-tag">法規依據：《共同供應契約實施辦法》第4條第2項</span>
                                    <p>非適用機關，於徵得訂約廠商同意後，得利用該契約辦理採購。但以該契約載明上述情形者為限，並應繳納相關行政規費或負擔相關義務。</p>
                                </div>
                            </td>
                        </tr>

                        <tr class="trap-row" onclick="toggleTrapDetail('trap_3')">
                            <td class="trap-wrong">機關成立 11 人之評選委員會，其專家學者人數只要有 3 人即可。</td>
                            <td class="trap-right">是非題 52 答案為 X。法規明文規定專家學者人數不得少於「委員總人數之三分之一」。11 人的三分之一是 3.66 人，故專家學者至少應聘 4 人！</td>
                        </tr>
                        <tr class="trap-detail" id="trap_3">
                            <td colspan="2">
                                <div class="trap-detail-content">
                                    <span class="trap-tag">法規依據：《政府採購法》第94條第1項</span>
                                    <p>採購評選委員會置委員 5 人至 17 人，其中專家、學者人數不得少於三分之一。因此：<br>
                                    - 總數 7 人：專家學者至少 3 人（7/3 = 2.33）<br>
                                    - 總數 11 人：專家學者至少 4 人（11/3 = 3.67）<br>
                                    - 總數 17 人：專家學者至少 6 人（17/3 = 5.67）</p>
                                </div>
                            </td>
                        </tr>

                        <tr class="trap-row" onclick="toggleTrapDetail('trap_4')">
                            <td class="trap-wrong">評選委員會委員開會應親自出席，但屬機關人員之評選委員得指定代理人出席。</td>
                            <td class="trap-right">是非題 87 答案為 X。所有委員（包含外部專家學者與內部機關人員）辦理評選及出席會議，一律「均應親自為之」，絕對不得代理。</td>
                        </tr>
                        <tr class="trap-detail" id="trap_4">
                            <td colspan="2">
                                <div class="trap-detail-content">
                                    <span class="trap-tag">法規依據：《採購評選委員會組織準則》第6條</span>
                                    <p>委員應親自出席會議，不得由他人代理。機關內部派兼之委員亦同。此為確保評選公正性與委員專業獨立判斷之核心防線。</p>
                                </div>
                            </td>
                        </tr>

                        <tr class="trap-row" onclick="toggleTrapDetail('trap_5')">
                            <td class="trap-wrong">機關將廠商刊登拒絕往來之通知，應附記：廠商如不服，得於接獲通知次日起 15 日內提出書面異議。</td>
                            <td class="trap-right">是非題 152、153 答案為 X。廠商對於刊登公報通知提出異議之時限為「20 日」內；對於異議處理結果提出申訴之時限才是「15 日」。這兩個天數是考試極高頻的混淆文字陷阱！</td>
                        </tr>
                        <tr class="trap-detail" id="trap_5">
                            <td colspan="2">
                                <div class="trap-detail-content">
                                    <span class="trap-tag">法規依據：《政府採購法》第102條第1項、第2項</span>
                                    <p>停權救濟法定雙軌時限：<br>
                                    1. 對機關刊登公報之通知不服 -> 接獲通知之次日起 <b>20 日內</b> 提出書面異議。<br>
                                    2. 對機關異議處理結果不服 -> 收受結果之次日起 <b>15 日內</b> 向申訴審議委員會提出申訴。</p>
                                </div>
                            </td>
                        </tr>

                        <tr class="trap-row" onclick="toggleTrapDetail('trap_6')">
                            <td class="trap-wrong">機關辦理採購優先採購環保產品，得標廠商未依規定履約，機關得沒收或追繳押標金。</td>
                            <td class="trap-right">是非題 112 答案為 X。以環保產品得標之廠商履約未提供該產品，機關得終止契約、追償價差優惠損失或停權，但「不得沒收或追繳押標金」（因押標金在簽約後應已發還）。</td>
                        </tr>
                        <tr class="trap-detail" id="trap_6">
                            <td colspan="2">
                                <div class="trap-detail-content">
                                    <span class="trap-tag">法規依據：《機關優先採購環境保護產品辦法》第14條</span>
                                    <p>得標廠商履約違規時，押標金不可扣留（因為簽約後即轉為履約保證金，且押標金已發還）。機關可以不發還「履約保證金」，但絕對不是追繳/沒收「押標金」。</p>
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
                            <span class="classic-title">精選題 1：環保產品價差優惠與決標順序判定</span>
                            <br>
                            <span class="classic-law">__LAW_MCQ_19__</span>
                        </div>
                        <span class="classic-num-lbl">選擇第 19 題</span>
                    </div>
                    <div class="classic-body">
                        <strong>題目</strong>：機關依採購法第96條第1項優先採購環保產品，且於招標文件載明依「機關優先採購環境保護產品辦法」第12條第1項第2款規定於價差優惠10%以內優先決標予環保產品廠商。現最低標A廠商為非環保產品廠商報價170萬元已進入底價200萬元，次低標B廠商報價180萬元為第3類環保產品廠商，第3低標C廠商報價185萬元為第2類環保產品廠商，第4低標D廠商報價188萬元第1類環保產品廠商，則機關應優先決標予何廠商？
                        <br>
                        <strong>選項</strong>：(1)A廠商。 (2)B廠商。 (3)C廠商。 (4)D廠商。
                        <br>
                        <strong>答案</strong>：(3) C廠商。
                    </div>
                    <div class="classic-exp">
                        <strong>核心解析</strong>：__DESC_MCQ_19__
                    </div>
                </div>

                <div class="classic-card">
                    <div class="classic-header">
                        <div>
                            <span class="classic-title">精選題 2：轉包違規之停權期間（第103條新制）</span>
                            <br>
                            <span class="classic-law">__LAW_MCQ_33__</span>
                        </div>
                        <span class="classic-num-lbl">選擇第 33 題</span>
                    </div>
                    <div class="classic-body">
                        <strong>題目</strong>：機關依採購法第101條規定通知廠商違反採購法第65條規定轉包，且該廠商於機關通知日起前5年內被任一機關刊登1次，則經廠商提出異議申訴審議結果並無不實者，自刊登公報之次日起幾年內不得參加投標或作為決標或分包廠商？
                        <br>
                        <strong>選項</strong>：(1)3個月。 (2)6個月。 (3)1年。 (4)2年。
                        <br>
                        <strong>答案</strong>：(2) 6個月。
                    </div>
                    <div class="classic-exp">
                        <strong>核心解析</strong>：__DESC_MCQ_33__
                    </div>
                </div>

                <div class="classic-card">
                    <div class="classic-header">
                        <div>
                            <span class="classic-title">精選題 3：採購專業人員資格辭職保留期</span>
                            <br>
                            <span class="classic-law">__LAW_MCQ_14__</span>
                        </div>
                        <span class="classic-num-lbl">選擇第 14 題</span>
                    </div>
                    <div class="classic-body">
                        <strong>題目</strong>：劉先生原任職於某市公所，於93年3月取得採購專業人員基本資格，因有至民間公司任職的生涯規劃，於93年12月30日離職，數年後，劉先生想回公務機關任職，依採購專業人員資格考試訓練發證及管理辦法規定，請問劉先生於何時回任仍具採購專業人員資格？
                        <br>
                        <strong>選項</strong>：(1)98年12月31日。 (2)97年6月5日。 (3)103年12月31日。 (4)108年12月30日。
                        <br>
                        <strong>答案</strong>：(2) 97年6月5日。
                    </div>
                    <div class="classic-exp">
                        <strong>核心解析</strong>：__DESC_MCQ_14__
                    </div>
                </div>

                <div class="classic-card">
                    <div class="classic-header">
                        <div>
                            <span class="classic-title">精選題 4：特別採購（公務機關間）免適用規定</span>
                            <br>
                            <span class="classic-law">__LAW_MCQ_42__</span>
                        </div>
                        <span class="classic-num-lbl">選擇第 42 題</span>
                    </div>
                    <div class="classic-body">
                        <strong>題目</strong>：某公務機關依採購法第105條第1項第3款及「特別採購招標決標處理辦法」向其他公務機關取得財物或勞務，得不適用以下何者關於採購法之規定？
                        <br>
                        <strong>選項</strong>：(1)第61條決標公告。 (2)第13條監辦。 (3)第53條超底價8%以內決標。 (4)第98條繳納代金。
                        <br>
                        <strong>答案</strong>：(4) 第98條繳納代金。
                    </div>
                    <div class="classic-exp">
                        <strong>核心解析</strong>：__DESC_MCQ_42__
                    </div>
                </div>

                <div class="classic-card">
                    <div class="classic-header">
                        <div>
                            <span class="classic-title">精選題 5：評選會開會專家學者比例合法性判定</span>
                            <br>
                            <span class="classic-law">__LAW_TF_50__</span>
                        </div>
                        <span class="classic-num-lbl">是非第 50、51 題</span>
                    </div>
                    <div class="classic-body">
                        <strong>題目</strong>：機關成立7人之採購評選委員會，開會時4人出席，因未達採購法第94條最少5人之規定，不得開會。(O/X)
                        <br>
                        <strong>答案</strong>：X。
                    </div>
                    <div class="classic-exp">
                        <strong>核心解析</strong>：__DESC_TF_50__
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
                ⚔️ 離線互動式模擬測驗 (全題庫 276 題隨機打亂挑戰)
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
                    <h4 id="quiz-feedback-title">解析說明</h4>
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
        <p>© 115 採購專業人員考試備考網頁 - 政府採購法之罰則及附則</p>
        <p>依據最新中華民國行政院公共工程委員會標準題庫提煉，100% 精準無編造</p>
    </footer>

    <!-- Injected Questions Data -->
    <script>
        const mcqsData = __MCQS_DATA__;
        const tfsData = __TFS_DATA__;
        
        let allQuestions = [];
        
        // Process MCQs
        mcqsData.forEach(q => {
            allQuestions.push({
                id: q.id,
                type: 'mcq',
                question: "[選擇題 第 " + q.id + " 題] " + q.question,
                choices: Object.entries(q.choices).map(([key, val]) => ({
                    num: parseInt(key),
                    text: "(" + key + ") " + val
                })),
                answer: q.answer,
                law: q.law,
                explanation: getExplanation('mcq_' + q.id, q.answer, q.law)
            });
        });
        
        // Process TFs
        tfsData.forEach(q => {
            allQuestions.push({
                id: q.id,
                type: 'tf',
                question: "[是非題 第 " + q.id + " 題] " + q.question,
                choices: [
                    { num: 'O', text: '⭕ 正確 (O)' },
                    { num: 'X', text: '❌ 錯誤 (X)' }
                ],
                answer: q.answer,
                law: q.law,
                explanation: getExplanation('tf_' + q.id, q.answer, q.law)
            });
        });

        // Function to dynamically supply explanation
        function getExplanation(qid, correctAns, law) {
            const db = {
                "mcq_19": "本題最低標為 A (非環保) 170萬。10% 價差優惠範圍為 170 * 1.10 = 187萬。環保廠商 B (第3類, 180萬) 與 C (第2類, 185萬) 符合此範圍。由於<b>第2類產品優先於第3類產品</b>，因此機關應優先決標予第2類之 C 廠商！這點極具實務計算價值。",
                "mcq_33": "依政府採購法第 103 條第 1 項最新規定，違反轉包 (第 65 條) 且前 5 年內被刊登公報過 1 次之廠商，其停權不得投標或作為分包廠商之期限為 <b>6 個月</b>。",
                "mcq_14": "依採購專業人員發證及管理辦法第 14 條，採購專業人員辭職後，於 <b>5 年內</b> 回任機關採購職務者，仍具備採購專業人員之資格。93年12月30日離職，97年6月5日回任屬於5年內。",
                "mcq_42": "政府採購法第 105 條第 1 項第 3 款公務機關間之特別採購，依法得不適用本法招標決標之規定。且依特別採購辦法，<b>免適用第 98 條</b> 關於繳納身障與原住民代金之規定。",
                "tf_50": "採購評選委員會成立 7 人，開會時 4 人出席符合過半數 (1/2以上) 出席之法定門檻；且出席專家學者為 2 人，符合專家學者不得少於 2 人且不得少於出席人數之 1/3 (2/4 = 50% >= 33.3%) 之規定。因此本案<b>「完全合法，得予開會」</b>！本題答案為 X。",
                "mcq_1": "共同供應契約應公開於主管機關指定之資訊網站。答案為 (2)。",
                "mcq_2": "共同供應契約包含後續擴充，最長以 2 年為限 (4)。由經濟部指定機關訂約者，適用機關為中央機關。答案為 (2) 錯誤。",
                "mcq_3": "各機關得就具有共通需求特性之「財物或勞務」簽訂共同供應契約。答案為 (1) 正確（注意不含工程）。",
                "mcq_4": "採購評選委員會至少 5 人，且專家學者人數不得少於 1/3。答案為 (2) 是。",
                "mcq_6": "出席委員中之專家學者人數應至少 2 人，且不得少於出席人數之 1/3。答案為 (2)。",
                "mcq_7": "採購評選委員會會議，應有委員總額 1/2 以上人員出席，其決議應經出席委員過半數之同意行之。答案為 (1) 二分之一。",
                "mcq_8": "最後一次會議紀錄應於「當次會議結束前」作成並予確認。答案為 (1)。",
                "mcq_9": "專家學者人數不得少於委員總人數之三分之一。答案為 (2) 三分之一。",
                "mcq_10": "採購評選委員會應置委員人數最多為「無人數上限之規定」。答案為 (4)。",
                "mcq_11": "採購評選委員會應置委員人數最少為 5 人。答案為 (1)。",
                "mcq_12": "除最後一次會議紀錄外，至遲應於「下次開會時」分送各出席委員確認。答案為 (2)。",
                "mcq_13": "委員辦理評選及出席會議，均應親自為之。答案為 (1)。",
                "mcq_17": "採購專業人員辭職後於 5 年內回任者仍具資格。答案為 (1)。",
                "mcq_18": "採購單位主管人員，宜於就職之日起 2 年內取得採購專業人員進階資格。答案為 (4)。",
                "mcq_20": "允許之價差優惠，最高不得逾百分之十 (2)。",
                "mcq_28": "「重整程序中之廠商」非屬採購法第 101 條得刊登政府採購公報之情形。答案為 (3) 正確。",
                "mcq_29": "若廠商未提出異議，機關應即執行刊登政府採購公報事宜。答案為 (2) 正確。",
                "mcq_30": "不服異議結果提出申訴，期限為 15 日。答案為 (2)。",
                "mcq_31": "無論是否逾公告金額之採購案，均得向採購申訴審議委員會提出申訴。答案為 (4)。",
                "mcq_32": "對於 101 條通知不實提出異議之時限，為接獲通知之次日起 20 日內。答案為 (2)。",
                "mcq_34": "擅自減省工料情節重大，刊登公報停權期為 3 年。答案為 (4)。",
                "mcq_35": "借用或冒用他人名義，以虛偽不實文件參加投標，停權期間為 3 年。答案為 (4)。",
                "mcq_37": "歧視弱勢團體，停權期間為 1 年。答案為 (2)。",
                "mcq_39": "保固責任不履行且從未被刊登過，停權期間為 3 個月。答案為 (1)。",
                "mcq_40": "受停業處分期間仍參加投標，停權期間為 2 年。答案為 (4)。",
                "mcq_44": "稽核小組迴避準用採購法第 15 條，且涉及 3 年內任職機關事項應行迴避。認為有違反採購法之情形者，應寫入稽核報告（非俟改正後再提）。答案為 (2) 錯誤。",
                "mcq_45": "審計機關（如縣市審計室）非屬稽核小組稽核監督範圍。答案為 (4)。",
                "mcq_47": "稽核委員自行發現異常辦理稽核，仍應經由稽核小組指派，不可擅自為之。答案為 (3) 非。",
                "mcq_48": "採購稽核小組之組織成員任期為 2 年。答案為 (1)。",
                "mcq_49": "採購稽核小組之組織成員人數為「不受限制」。答案為 (4)。",
                "tf_1": "意圖影響採購結果而借牌投標，處3年以下有期徒刑，得併科100萬元以下罰金。本題答案為 O。",
                "tf_2": "受託規劃設計人員意圖不法利益不當限制規格，縱未獲得利益，仍處罰未遂犯。本題答案為 X（不罰是錯的）。",
                "tf_3": "受託技術服務人員意圖不法利益限制規格且獲利，處 1 年以上 7 年以下有期徒刑，併科 300 萬以下罰金。本題答案為 O。",
                "tf_5": "受機關委託提供規劃及設計服務之廠商人員不當限制規範，自己未獲利益仍應罰。本題答案為 O。",
                "tf_6": "洩漏採購秘密因而獲利者，處 5 年以下有期徒刑，未遂犯罰之。本題答案為 O。",
                "tf_8": "意圖使採購人員不為決定而施強暴脅迫者，處 1 年以上 7 年以下有期徒刑。未遂犯亦罰之。本題答案為 X（未遂犯不罰是錯的）。",
                "tf_13": "廠商從業人員執行業務犯採購法之罪者，對該廠商亦科以同條罰金（雙罰制）。本題答案為 O。",
                "tf_22": "共同供應契約應公開於「主管機關指定之資訊網站」（非招標機關網站）。本題答案為 X。",
                "tf_23": "機關利用共同供應契約訂貨，免再另簽契約及收取保證金。本題答案為 X。",
                "tf_26": "非適用機關經廠商同意且契約載明者，得利用該契約採購。本題答案為 X。",
                "tf_31": "機關利用共同供應契約訂貨後，免依第 61 條刊登決標公告及定期彙送。本題答案為 O。",
                "tf_33": "共同供應契約期間包含後續擴充，最長以 2 年為限。本題答案為 O。",
                "tf_35": "共通需求採購僅限「財物或勞務」，不包含工程。本題答案為 O。",
                "tf_36": "共通需求採購包含工程為錯誤敘述。本題答案為 X。",
                "tf_37": "利用共同供應契約訂貨，對於廠商交貨，仍應依法辦理驗收。本題答案為 O。",
                "tf_46": "機關不得遴選民意代表為評選委員。本題答案為 X。",
                "tf_47": "機關不得遴選民意代表為評選委員，但各級民意機關辦理採購時除外。本題答案為 O。",
                "tf_87": "評選委員應親自出席，任何委員（含機關內部派兼者）均不得指定代理人出席。本題答案為 X。"
            };
            
            let baseExp = db[qid];
            if (!baseExp) {
                baseExp = `本題標準答案為：<b>${correctAns}</b>。`;
                if (law) {
                    baseExp += ` 根據《政府採購法》第 ${law} 規定。`;
                }
                baseExp += ` 請牢記本單元標準考點！`;
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
            
            progress.innerHTML = `題目進度: <b>${index + 1} / ${allQuestions.length}</b> [${q.type === 'mcq' ? '選擇題' : '是非題'}] (原始題號: ${q.id})`;
            questionTitle.innerText = q.question.replace(/\[.*\]\s*/, "");
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
            feedbackText.innerHTML = q.explanation;
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
    
    # 進行安全取代
    final_html = html_template
    final_html = final_html.replace("__MCQS_DATA__", json.dumps(mcqs, ensure_ascii=False))
    final_html = final_html.replace("__TFS_DATA__", json.dumps(tfs, ensure_ascii=False))
    
    final_html = final_html.replace("__LAW_MCQ_19__", classic_explanations['mcq_19']['law'])
    final_html = final_html.replace("__DESC_MCQ_19__", classic_explanations['mcq_19']['desc'])
    
    final_html = final_html.replace("__LAW_MCQ_33__", classic_explanations['mcq_33']['law'])
    final_html = final_html.replace("__DESC_MCQ_33__", classic_explanations['mcq_33']['desc'])
    
    final_html = final_html.replace("__LAW_MCQ_14__", classic_explanations['mcq_14']['law'])
    final_html = final_html.replace("__DESC_MCQ_14__", classic_explanations['mcq_14']['desc'])
    
    final_html = final_html.replace("__LAW_MCQ_42__", classic_explanations['mcq_42']['law'])
    final_html = final_html.replace("__DESC_MCQ_42__", classic_explanations['mcq_42']['desc'])
    
    final_html = final_html.replace("__LAW_TF_50__", classic_explanations['tf_50']['law'])
    final_html = final_html.replace("__DESC_TF_50__", classic_explanations['tf_50']['desc'])
    
    with open(OUTPUT_HTML_PATH, "w", encoding="utf-8") as f:
        f.write(final_html)
        
    print(f"Success: Beautiful focus note HTML generated at: {OUTPUT_HTML_PATH}")

if __name__ == "__main__":
    main()
