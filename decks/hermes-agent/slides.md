---
theme: seriph
background: https://cover.sli.dev
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
title: Hermes Agent 技術評估
mdc: true
---

# Hermes Agent

### 自我改進 AI Agent 框架技術評估

<div class="pt-12 text-gray-200">
  Nous Research ・ 技術評估報告 ・ 2026.06.12
</div>

---
layout: center
class: text-center
---

# 這個名字，不只是個名字

<div class="text-6xl mt-8">𓂀</div>

<div class="text-gray-600 mt-6 text-lg">
  Hermes・Hermès・Harness
</div>

---
layout: default
---

# Hermes — 眾神的信使

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <div class="text-5xl mb-4">⚡</div>
    <p class="text-gray-800 leading-relaxed">
      在希臘神話中，<strong class="text-amber-600">赫爾墨斯（Hermēs）</strong>是奧林匹斯十二主神中最靈活的一位——身兼眾神信使、商業之神、邊界之神。
    </p>
    <p class="text-gray-800 leading-relaxed mt-4">
      他穿梭於神界與人界之間，傳遞訊息、調度資源，從不受邊界束縛。
    </p>
    <div class="mt-6 text-sm text-gray-600">
      讀音：英文 <span class="text-gray-700 font-mono">HUR-meez</span>・法文 <span class="text-gray-700 font-mono">air-MEZ</span>
    </div>
  </div>
  <div class="flex flex-col gap-4 justify-center">
    <div class="border border-gray-400 rounded-lg p-4 text-sm">
      <div class="text-yellow-700 font-bold mb-1">📨 信使</div>
      <div class="text-gray-700">在模型、工具與平台之間傳遞指令</div>
    </div>
    <div class="border border-gray-400 rounded-lg p-4 text-sm">
      <div class="text-blue-700 font-bold mb-1">🌐 邊界之神</div>
      <div class="text-gray-700">自由穿越 Telegram、Slack、Discord 等邊界</div>
    </div>
    <div class="border border-gray-400 rounded-lg p-4 text-sm">
      <div class="text-green-700 font-bold mb-1">⚡ 速度與智慧</div>
      <div class="text-gray-700">快速、可靠地執行與學習</div>
    </div>
  </div>
</div>

---
layout: default
---

# Hermès → Harness — 從馬具到 AI

<div class="grid grid-cols-3 gap-6 mt-6">
  <div class="border border-gray-400 rounded-lg p-5 text-center">
    <div class="text-4xl mb-3">🐎</div>
    <div class="font-bold text-orange-700 mb-2">Hermès 愛馬仕</div>
    <div class="text-sm text-gray-700">
      1837 年，創辦人 Thierry Hermès 開設<strong class="text-gray-900">高級馬具工坊</strong>，專為貴族馴馬、駕馭烈馬
    </div>
  </div>
  <div class="border border-gray-400 rounded-lg p-5 text-center">
    <div class="text-4xl mb-3">🔧</div>
    <div class="font-bold text-blue-700 mb-2">Harness 馬具</div>
    <div class="text-sm text-gray-700">
      軟體工程中，<strong class="text-gray-900">Harness</strong> 指「測試框架或控制套件」——將難以預測的事物引導、馴服
    </div>
  </div>
  <div class="border border-gray-400 rounded-lg p-5 text-center">
    <div class="text-4xl mb-3">🤖</div>
    <div class="font-bold text-green-700 mb-2">Agent Harness</div>
    <div class="text-sm text-gray-700">
      <strong class="text-gray-900">駕馭大語言模型</strong>，將難以預測的 AI 引導發揮最大效能
    </div>
  </div>
</div>

<div class="mt-6 p-4 bg-gray-800 rounded-lg border border-gray-600 text-center">
  <span class="text-gray-100 text-sm">神話信使・奢華馬具・AI 框架——三個世界，同一個名字</span>
</div>

---
layout: two-cols
---

# 專案概覽

<v-clicks>

- **名稱**：Hermes Agent
- **開發方**：Nous Research
- **授權**：MIT（可免費商用）
- **定位**：「The self-improving AI agent」
- **主要語言**：Python 82.6%、TypeScript 13.4%

</v-clicks>

::right::

<div class="flex flex-col gap-6 mt-8 ml-8 text-center">
  <div>
    <div class="text-5xl font-bold text-blue-600">191K</div>
    <div class="text-gray-600 text-sm mt-1">GitHub Stars</div>
  </div>
  <div>
    <div class="text-5xl font-bold text-green-600">33.3K</div>
    <div class="text-gray-600 text-sm mt-1">Forks</div>
  </div>
  <div>
    <div class="text-5xl font-bold text-purple-600">1,415</div>
    <div class="text-gray-600 text-sm mt-1">Contributors</div>
  </div>
</div>

---
layout: default
---

# 核心特色：自我改進學習迴圈

<div class="text-gray-600 italic mb-6">
  「Creates skills from experience, improves them during use, builds a deepening model of who you are across sessions」
</div>

<div class="grid grid-cols-3 gap-4">
  <div class="border border-gray-400 rounded-lg p-4">
    <div class="text-3xl mb-3">🧠</div>
    <strong>持久記憶</strong>
    <p class="text-sm text-gray-700 mt-2">跨對話累積知識，不需每次重頭開始，搭配全文搜尋回溯歷史</p>
  </div>
  <div class="border border-gray-400 rounded-lg p-4">
    <div class="text-3xl mb-3">⚡</div>
    <strong>自動技能生成</strong>
    <p class="text-sm text-gray-700 mt-2">從複雜任務中自動提取可複用技能，累積組織專屬知識庫</p>
  </div>
  <div class="border border-gray-400 rounded-lg p-4">
    <div class="text-3xl mb-3">👤</div>
    <strong>用戶建模</strong>
    <p class="text-sm text-gray-700 mt-2">持續理解使用者偏好，個人化回應方式與工作流程</p>
  </div>
</div>

---
layout: default
---

# 多模型支援 — 200+ 模型，一套框架

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>

| 提供商 | 類型 |
|--------|------|
| OpenRouter | 多模型聚合平台 |
| Nous Portal | Nous 自家模型 |
| OpenAI | GPT 系列 |
| NVIDIA NIM | 企業級推論 |
| Hugging Face | 開源模型 |
| 自訂 Endpoint | 本地 / 私有雲 |

  </div>
  <div class="flex flex-col justify-center">
    <div class="p-4 bg-blue-900 bg-opacity-30 rounded-lg border border-blue-700">
      <div class="font-bold text-black mb-2">💡 對企業的意義</div>
      <p class="text-sm text-black">
        無需改動程式碼即可切換底層模型，降低廠商鎖定風險。未來若有更好或更便宜的模型，可隨時替換。
      </p>
    </div>
  </div>
</div>

---
layout: default
---

# 部署彈性 — 從個人到企業規模

<div class="grid grid-cols-2 gap-6 mt-6">
  <div class="border border-green-700 rounded-lg p-5">
    <h3 class="text-green-700 mb-4">🚀 輕量部署</h3>
    <ul class="space-y-2 text-sm">
      <li>✅ 本機終端機（立即可用）</li>
      <li>✅ $5/月 VPS（低成本驗證）</li>
      <li>✅ Docker 容器化</li>
      <li>✅ SSH 遠端機器</li>
    </ul>
  </div>
  <div class="border border-blue-700 rounded-lg p-5">
    <h3 class="text-blue-700 mb-4">🏢 企業部署</h3>
    <ul class="space-y-2 text-sm">
      <li>✅ GPU 叢集（Singularity）</li>
      <li>✅ Serverless（Modal）</li>
      <li>✅ 雲端沙箱（Daytona）</li>
      <li>✅ 多平台訊息閘道</li>
    </ul>
  </div>
</div>

---
layout: default
---

# 多平台整合 — 在現有工具中使用 AI

Agent 透過主流通訊平台操作，使用者不需學新介面

<div class="flex gap-4 mt-6 flex-wrap">
  <div class="border border-gray-400 rounded-lg px-5 py-3 text-center">
    <div class="text-2xl">💬</div>
    <div class="text-sm mt-1">Telegram</div>
  </div>
  <div class="border border-gray-400 rounded-lg px-5 py-3 text-center">
    <div class="text-2xl">🎮</div>
    <div class="text-sm mt-1">Discord</div>
  </div>
  <div class="border border-gray-400 rounded-lg px-5 py-3 text-center">
    <div class="text-2xl">💼</div>
    <div class="text-sm mt-1">Slack</div>
  </div>
  <div class="border border-gray-400 rounded-lg px-5 py-3 text-center">
    <div class="text-2xl">📱</div>
    <div class="text-sm mt-1">WhatsApp</div>
  </div>
  <div class="border border-gray-400 rounded-lg px-5 py-3 text-center">
    <div class="text-2xl">🔒</div>
    <div class="text-sm mt-1">Signal</div>
  </div>
</div>

<div class="mt-6 p-4 bg-yellow-900 bg-opacity-30 rounded-lg border border-yellow-700 text-sm">
  📌 <strong>實際場景：</strong>工程師或業務人員直接在 Slack 發指令給 Agent，完成自動化任務，不需切換工具
</div>

---
layout: default
---

# 架構解析

<div class="grid grid-cols-2 gap-8">
  <div>

```
hermes-agent/
├── agent/       # 核心 Agent 邏輯
├── skills/      # 技能系統（程序記憶）
├── tools/       # 40+ 內建工具
├── providers/   # LLM 提供商整合
├── gateway/     # 訊息平台連接
├── plugins/     # 擴充套件系統
└── web/         # Web 介面
```

  </div>
  <div class="flex flex-col gap-3 justify-center text-sm text-white">
    <div class="p-3 bg-gray-800 rounded">🐍 Python 3.11 核心</div>
    <div class="p-3 bg-gray-800 rounded">🔍 FTS5 全文搜尋（歷史對話檢索）</div>
    <div class="p-3 bg-gray-800 rounded">🔌 MCP 協議支援</div>
    <div class="p-3 bg-gray-800 rounded">⏰ 內建 Cron 排程器</div>
    <div class="p-3 bg-gray-800 rounded">🤖 子 Agent 平行工作流</div>
  </div>
</div>

---
layout: default
---

# 評估結論

<div class="grid grid-cols-2 gap-6 mt-4">
  <div class="border border-green-700 rounded-lg p-5">
    <h3 class="text-green-700 mb-3">✅ 優勢</h3>
    <ul class="space-y-2 text-sm">
      <li>社群規模龐大（191K stars），成熟度高</li>
      <li>MIT 授權，可自由商用與修改</li>
      <li>多模型支援，降低廠商鎖定風險</li>
      <li>部署彈性高，PoC 成本極低</li>
      <li>自我改進機制，長期使用價值遞增</li>
    </ul>
  </div>
  <div class="border border-yellow-700 rounded-lg p-5">
    <h3 class="text-yellow-700 mb-3">⚠️ 注意事項</h3>
    <ul class="space-y-2 text-sm">
      <li>尚無公開效能基準測試資料</li>
      <li>Python 為主，需具備相關技術資源</li>
      <li>功能複雜，導入學習曲線較高</li>
      <li>企業資料安全政策需另行評估</li>
    </ul>
  </div>
</div>

<div class="mt-5 p-4 bg-blue-900 bg-opacity-40 rounded-lg border border-blue-600">
  <span class="text-white">🎯 <strong>建議：</strong>值得列為內部 AI Agent 基礎框架候選，建議以 $5 VPS 進行一個月 PoC 驗證，成本極低風險可控</span>
</div>

---
layout: center
class: text-center
---

# 謝謝

<div class="text-gray-600 mt-4 text-sm">
  資料來源：github.com/NousResearch/hermes-agent<br>
  報告日期：2026.06.12
</div>
