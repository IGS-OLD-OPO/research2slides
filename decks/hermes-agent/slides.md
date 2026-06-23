---
theme: seriph
background: /hero-art.webp
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

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
今天要跟大家介紹的是 Nous Research 開發的開源 AI Agent 框架——Hermes Agent 的技術評估。
這份報告結合了原始碼分析、實際部署測試，以及企業應用視角，目標是評估它是否值得我們進一步導入。
-->
---
layout: default
---

# Hermes — 從神話到 AI

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <p class="text-gray-800 leading-relaxed">
      在希臘神話中，<strong class="text-amber-600">赫爾墨斯（Hermēs）</strong>是奧林匹斯十二主神中最靈活的一位——身兼眾神信使、商業之神、邊界之神。
    </p>
    <p class="text-gray-800 leading-relaxed mt-4">
      他穿梭於神界與人界之間，傳遞訊息、調度資源，從不受邊界束縛。
    </p>
    <div class="mt-4 text-sm text-gray-600">
      讀音：英文 <span class="text-gray-700 font-mono">HUR-meez</span>・法文 <span class="text-gray-700 font-mono">air-MEZ</span>
    </div>
  </div>
  <div>
    <div class="grid grid-cols-3 gap-4">
      <div class="border border-gray-400 rounded-lg p-4 text-center">
        <div class="text-3xl mb-2">🐎</div>
        <div class="font-bold text-orange-700 text-sm mb-1">Hermès</div>
        <div class="text-xs text-gray-600">高級馬具工坊（1837）</div>
      </div>
      <div class="border border-gray-400 rounded-lg p-4 text-center">
        <div class="text-3xl mb-2">🔧</div>
        <div class="font-bold text-blue-700 text-sm mb-1">Harness</div>
        <div class="text-xs text-gray-600">測試框架 / 控制套件</div>
      </div>
      <div class="border border-gray-400 rounded-lg p-4 text-center">
        <div class="text-3xl mb-2">🤖</div>
        <div class="font-bold text-green-700 text-sm mb-1">Agent</div>
        <div class="text-xs text-gray-600">駕馭大語言模型</div>
      </div>
    </div>
  </div>
</div>

<div class="mt-5 p-3 bg-gray-800 rounded-lg border border-gray-600 text-center">
  <span class="text-gray-100 text-sm">神話信使・奢華馬具・AI 框架——三個世界，同一個名字</span>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
希臘神話中赫爾墨斯的三個特質：靈活、穿梭邊界、傳遞訊息——恰好對應 AI Agent 要做的事：跨工具調度、跨平台操作、傳遞使用者意圖。
Harness 英文還有「駕馭、善用」的意思，做為框架名字非常貼切。
-->
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
    <div class="text-5xl font-bold text-blue-600">195K</div>
    <div class="text-gray-600 text-sm mt-1">GitHub Stars</div>
  </div>
  <div>
    <div class="text-5xl font-bold text-green-600">34.1K</div>
    <div class="text-gray-600 text-sm mt-1">Forks</div>
  </div>
  <div>
    <div class="text-5xl font-bold text-purple-600">1,415</div>
    <div class="text-gray-600 text-sm mt-1">Contributors</div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
195K stars 代表這不是一個小型實驗專案，是目前 GitHub 上 AI Agent 類別中社群規模最大的之一。
MIT 授權很關鍵：可以自由商用、修改、部署，不需要擔心版權問題。
「self-improving」是最核心的定位，等一下會詳細說明這代表什麼。
-->
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

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
最重要的一點：Hermes 不綁定任何一家 AI 供應商。
今天用 Claude，明天 GPT-5 出來覺得效果更好或更便宜，改一行 config 就換，不需要重寫任何程式碼。
OpenRouter 是一個聚合平台，一個 API key 可以打 200+ 個模型，是最靈活的接入方式。
-->
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

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
PoC 的門檻非常低：$5/月的 VPS，大約台幣 160 元，就能把 Hermes 跑起來。
不需要先投入大量基礎設施成本就能驗證可行性。
如果 PoC 成功，同一套程式碼可以直接擴展到 GPU 叢集，不需要重寫。
這個彈性讓「先試再說」的策略非常合理。
-->
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

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
最大的好處：使用者完全不需要學新的介面或工具。
業務同仁在 Slack 打個訊息，Agent 就去查資料、整理報表、回傳結果。
後面的遊戲營運 Bot 案例就是在 Telegram 上直接操作的，可以感受一下實際的互動體驗。
-->
---
layout: default
---

# 架構解析 — 三層設計

```mermaid {scale: 0.75}
flowchart TB
    subgraph IF["① 介面層"]
        direction TB
        cli["CLI / TUI"]
        msg["Telegram · Discord\nSlack · WhatsApp"]
        web["Web Dashboard"]
        ide["VS Code / Zed（ACP）"]
    end
    subgraph AG["② Agent 邏輯層"]
        direction TB
        aa["AIAgent\nrun_agent.py"]
        mt["model_tools.py\n動態工具派發"]
    end
    subgraph EX["③ 執行層"]
        direction TB
        local["Local · Docker · SSH"]
        cloud["Modal · Singularity\n（GPU 叢集）"]
    end
    IF --> AG --> EX
```

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
三層分離讓我們可以「換一層不動另一層」。
例如：今天用 Slack，改天想換成 Line，只需要改介面層的設定，Agent 邏輯完全不用動。
或者：現在在本機跑，之後要擴展到 GPU 叢集，也只是換執行層，程式碼不變。
這個設計對企業長期維護很友善。
-->
---
layout: default
---

# 架構解析 — Runtime Modes & 設定

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <div class="text-sm font-bold text-gray-500 mb-3">四種啟動入口</div>

| Mode | Entry Point |
|------|-------------|
| CLI | `cli.py` |
| 訊息平台 Gateway | `gateway/run.py` |
| Editor (ACP) | VS Code / Zed 整合 |
| Web UI | 瀏覽器 Dashboard |

  </div>
  <div>
    <div class="text-sm font-bold text-gray-500 mb-3">HERMES_HOME（<span class="font-mono">~/.hermes/</span>）</div>
    <div class="flex flex-col gap-2 text-sm">
      <div class="p-2 bg-gray-100 rounded font-mono">config.yaml <span class="text-gray-500 font-sans">— 模型、工具設定</span></div>
      <div class="p-2 bg-gray-100 rounded font-mono">SOUL.md <span class="text-gray-500 font-sans">— Agent 人格定義</span></div>
      <div class="p-2 bg-gray-100 rounded font-mono">MEMORY.md <span class="text-gray-500 font-sans">— 長期記憶</span></div>
      <div class="p-2 bg-gray-100 rounded font-mono">.env <span class="text-gray-500 font-sans">— API 金鑰</span></div>
    </div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
右邊的 SOUL.md 和 MEMORY.md 是後面深入解析的重點，先記住它們的存在。
所有設定集中在 ~/.hermes/ 這個資料夾，部署和備份都很容易。
四種啟動模式覆蓋了大部分的企業使用場景：CLI 給工程師，Gateway 給業務通訊，Web UI 給管理者。
-->
---
layout: default
---

# 六大核心技術特色

<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="border border-gray-400 rounded-lg p-4">
    <div class="text-3xl mb-2">🧠</div>
    <strong>自我改進學習迴圈</strong>
    <p class="text-sm text-gray-700 mt-2">任務完成自動提取可複用技能，越用越聰明</p>
  </div>
  <div class="border border-gray-400 rounded-lg p-4">
    <div class="text-3xl mb-2">📋</div>
    <strong>SOUL.md 行為控制</strong>
    <p class="text-sm text-gray-700 mt-2">Agent 人格可版本控制，各部門隔離管理</p>
  </div>
  <div class="border border-gray-400 rounded-lg p-4">
    <div class="text-3xl mb-2">💾</div>
    <strong>三層持久記憶</strong>
    <p class="text-sm text-gray-700 mt-2">跨對話累積知識，支援全文搜尋與稽核</p>
  </div>
  <div class="border border-gray-400 rounded-lg p-4">
    <div class="text-3xl mb-2">🛡</div>
    <strong>Promptware 防禦</strong>
    <p class="text-sm text-gray-700 mt-2">對抗記憶污染攻擊，v0.15 已加入寫入保護</p>
  </div>
  <div class="border border-gray-400 rounded-lg p-4">
    <div class="text-3xl mb-2">🤖</div>
    <strong>Multi-agent 自癒</strong>
    <p class="text-sm text-gray-700 mt-2">子代理失效自動偵測回收，支援無人值守長任務</p>
  </div>
  <div class="border border-gray-400 rounded-lg p-4">
    <div class="text-3xl mb-2">🔧</div>
    <strong>工具生態與企業可靠性</strong>
    <p class="text-sm text-gray-700 mt-2">Tool Gateway + Plugin + 多層模型保障</p>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
這六個是讓 Hermes 與其他 Agent 框架不同的地方。
接下來每一項都會有一張獨立的投影片深入說明，包含原始碼層級的確認和企業風險評估。
-->
---
layout: default
---

# Agent 越用越聰明：Learning Loop

```mermaid {scale: 0.75}
flowchart LR
    A["🎯 任務完成"] -->|"自動回顧"| B["📦 封裝 Skill\nskill_manage"]
    B -->|"Python 工具 + MD"| C["💾 MEMORY.md"]
    C -->|"Curator 維護"| D["🤖 Autonomous\nCurator"]
    D -->|"下次自動套用"| A
```

<div class="grid grid-cols-2 gap-3 mt-2">
  <div class="p-2 bg-gray-100 rounded border border-gray-400 text-xs"><span class="font-bold">記憶回顧觸發：</span>每 <span class="font-mono font-bold">10</span> 回合（使用者訊息計數）</div>
  <div class="p-2 bg-gray-100 rounded border border-gray-400 text-xs"><span class="font-bold">技能回顧觸發：</span>每累積 <span class="font-mono font-bold">10</span> 次工具呼叫</div>
</div>
<div class="text-xs text-gray-500 mt-1">均可在 <span class="font-mono">config.yaml</span> 調整 <span class="font-mono">nudge_interval</span>・背景 daemon thread 執行，不阻塞使用者回應</div>

<div class="grid grid-cols-3 gap-2 mt-3">
  <div class="border border-green-600 rounded p-2 text-xs">✅ 重複任務零人工撰碼：同類需求第二次起自動套用</div>
  <div class="border border-green-600 rounded p-2 text-xs">✅ 部門隔離：多 Profile 各自維護專屬 Skill Bundle</div>
  <div class="border border-green-600 rounded p-2 text-xs">✅ 知識不腐化：Curator 閒置 7 天觸發，自動合併 / 棄用過時 Skill</div>
</div>

<div class="mt-2 p-2 border border-red-500 rounded-lg text-xs text-red-700">
  ⚠️ 企業注意：自動生成的 Skill 為 Python 程式碼，無人工審核閘門，受監管環境需自建 code review 流程
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
這是「self-improving」的具體實現，也是 Hermes 最核心的差異化功能。
重點：同類任務第一次做需要時間，第二次起 Agent 會自動套用上次提取的技能，不需使用者重新說明。
技能是背景執行提取的，不會讓使用者等待。
Curator 機制很重要：避免技能庫一直累積舊的、過時的技能——閒置 7 天會自動整理。
風險要特別提：自動生成的技能是 Python 程式碼，在受監管環境（例如金融、法規）需要建立 code review 流程。
-->
---
layout: default
---

# `SOUL.md`：Agent 行為的版本控制單元

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <div class="text-xs text-gray-400 mb-2">~/.hermes/SOUL.md</div>
    <div class="p-3 bg-gray-800 rounded text-xs font-mono text-green-300 leading-relaxed">
      # 身份<br>
      你是法務部門的 AI 助理。<br><br>
      # 行為邊界<br>
      不得提供具體法律建議。<br>
      回應需附加「請諮詢專業律師」。
    </div>
    <div class="mt-4 text-xs text-gray-500">啟動時注入 system prompt 前置區段</div>
    <div class="mt-3 p-2 bg-gray-100 rounded text-xs text-gray-700">
      → 可納入 Git 版控、PR review、CI/CD<br>
      ≈ <strong>IaC for Agent behavior</strong>
    </div>
  </div>
  <div class="flex flex-col gap-3 justify-center">
    <div class="border border-gray-300 rounded p-3 text-sm text-center">⚖️ 法務 Agent<br><span class="text-xs text-gray-500">合規語氣 + 免責提示</span></div>
    <div class="border border-gray-300 rounded p-3 text-sm text-center">🎧 客服 Agent<br><span class="text-xs text-gray-500">親切語氣 + 退款授權範圍</span></div>
    <div class="border border-gray-300 rounded p-3 text-sm text-center">🛠 工程 Agent<br><span class="text-xs text-gray-500">技術語氣 + 生產環境禁令</span></div>
  </div>
</div>

<div class="mt-3 p-3 border border-red-500 rounded-lg text-sm text-red-700">
  ⚠️ 純文字，無原生 ACL — 有 HERMES_HOME 寫入權限者可靜默修改人格，建議搭配 OS 層或 Secret Manager 保護
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
類比 IaC（Infrastructure as Code）——SOUL.md 就是「Agent 行為即程式碼」。
把 Agent 的身份、語氣、授權範圍寫成一份 Markdown 文件，可以 Git 版控。
誰改了 Agent 的行為，commit history 一清二楚；不同部門維護各自的 SOUL.md，互不干擾。
風險必須提：SOUL.md 是純文字，沒有原生的存取控制。
任何有 ~/.hermes/ 寫入權限的人都能靜默修改 Agent 的人格，建議搭配 OS 層檔案權限或 Secret Manager 保護。
-->
---
layout: default
---

# 記憶不中斷：三層記憶架構

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="flex flex-col gap-2">
    <div class="border border-blue-400 rounded-lg p-4">
      <div class="text-blue-500 font-bold text-sm mb-1">短期 — Context Window</div>
      <div class="text-xs text-gray-600">當前對話即時推理，會話結束即消失</div>
    </div>
    <div class="flex justify-center text-gray-400 text-xs">▼ 每回合結束 sync_all() 寫入</div>
    <div class="border border-purple-400 rounded-lg p-4">
      <div class="text-purple-500 font-bold text-sm mb-1">中期 — SQLite FTS5 全文索引</div>
      <div class="text-xs text-gray-600">回合結束自動寫入；下回合開始 <span class="font-mono">prefetch_all()</span> 召回相關記憶注入 context</div>
    </div>
    <div class="flex justify-center text-gray-400 text-xs">▼ 每 10 回合 background review 寫入</div>
    <div class="border border-green-400 rounded-lg p-4">
      <div class="text-green-500 font-bold text-sm mb-1">長期 — MEMORY.md + 向量 DB</div>
      <div class="text-xs text-gray-600">由背景 review agent fork 定期寫入；USER.md 記錄使用者偏好 ／ Skill 知識庫</div>
    </div>
  </div>
  <div class="flex flex-col gap-4 justify-center">
    <div class="p-4 bg-blue-50 rounded-lg border border-blue-200 text-sm">
      💡 <strong>實際場景</strong><br>
      <span class="text-gray-600">三週後繼續同一專案，無需重新交代背景</span>
    </div>
    <div class="p-4 bg-green-50 rounded-lg border border-green-200 text-sm">
      📋 <strong>稽核友善</strong><br>
      <span class="text-gray-600">MEMORY.md 為純文字，IT 可直接備份與審計；background review fork 受工具白名單保護</span>
    </div>
    <div class="p-3 border border-red-400 rounded-lg text-xs text-red-700">
      ⚠️ 寫入 MEMORY.md 的內容由 AI 自主判斷（原始碼無明確過濾規則），企業需評估資料治理策略
    </div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
可以類比成三層：工作記憶（context window）、筆記本（SQLite）、知識庫（MEMORY.md）。
最實際的場景：三週後回來繼續上次的工作，不需要重新交代背景——Agent 自己會召回相關記憶。
對 IT 的好處：MEMORY.md 是純文字，不是黑盒子，可以直接備份、稽核、甚至手動編輯。
風險：AI 自主決定要記什麼，原始碼沒有明確的過濾規則，敏感資訊可能被寫入。企業需要考慮資料治理策略。
-->
---
layout: default
---

# Promptware 防禦：對抗記憶污染攻擊

<div class="grid grid-cols-2 gap-8 mt-4">
  <div>
    <div class="text-xs text-gray-400 mb-3">攻擊鏈（Brainworm-class）</div>
    <div class="flex flex-col gap-2 text-sm">
      <div class="p-2 bg-red-50 border border-red-300 rounded">📄 外部內容（網頁、文件、工具輸出）</div>
      <div class="flex justify-center text-red-400 text-xs">▼ 混入惡意指令</div>
      <div class="p-2 bg-red-50 border border-red-300 rounded">💾 寫入 MEMORY.md / skill_manage</div>
      <div class="flex justify-center text-red-400 text-xs">▼ 持久化感染</div>
      <div class="p-2 bg-red-50 border border-red-300 rounded">🔁 跨會話持續執行攻擊者指令</div>
    </div>
    <div class="mt-3 p-2 bg-green-50 border border-green-400 rounded text-xs text-green-700">
      🛡 v0.15.0 在記憶寫入路徑前加入攔截驗證
    </div>
  </div>
  <div class="flex flex-col gap-2 justify-center">
    <div class="text-xs text-gray-500 font-bold mb-1">原始碼確認：已有保護</div>
    <div class="p-2 border border-green-500 rounded text-xs text-green-700">✅ Review fork 工具白名單：危險指令全部 auto-deny</div>
    <div class="p-2 border border-green-500 rounded text-xs text-green-700">✅ Fork 隔離：<span class="font-mono">skip_memory=True</span>，不碰外部 memory plugin</div>
    <div class="text-xs text-gray-500 font-bold mt-2 mb-1">仍需企業自行處理</div>
    <div class="p-2 border border-red-400 rounded text-xs text-red-700">❌ SOUL.md：純文字，無簽名 / checksum，寫入不留稽核日誌</div>
    <div class="p-2 border border-red-400 rounded text-xs text-red-700">❌ <span class="font-mono">auth.json</span>（OAuth token）與 SOUL.md 同存於 <span class="font-mono">~/.hermes/</span></div>
    <div class="p-2 border border-yellow-500 rounded text-xs text-yellow-800">⚠️ MCP 工具輸出是否在 Brainworm 防禦範圍內？原始碼未確認</div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
Promptware / Brainworm 是一種新型攻擊，專門針對有持久記憶的 AI Agent。
攻擊流程：讓 Agent 讀取含惡意指令的外部內容（例如網頁、文件）→ Agent 把指令寫入 MEMORY.md → 下次對話自動執行攻擊者的指令。
v0.15 已有基本防護，這部分我們有看過原始碼確認。
但仍有兩個企業需要自行處理的缺口：SOUL.md 沒有防篡改機制、auth.json 和 SOUL.md 放在同一個資料夾。
-->
---
layout: default
---

# 資安全貌：風險與企業部署建議

<div class="grid grid-cols-2 gap-6 mt-4">
  <div>
    <div class="text-xs text-gray-500 font-bold mb-2">架構層面風險</div>
    <div class="flex flex-col gap-1.5 text-xs">
      <div class="p-2 bg-yellow-50 border border-yellow-400 rounded">⚠️ 進程內防護均為<strong>啟發式（heuristics）</strong>，非真正安全邊界；LLM 被對抗操控時可被繞過</div>
      <div class="p-2 bg-yellow-50 border border-yellow-400 rounded">⚠️ <code>SOUL.md</code> / <code>MEMORY.md</code>：純文字、無 ACL、無簽名，有寫入權限可靜默篡改人格與記憶</div>
      <div class="p-2 bg-yellow-50 border border-yellow-400 rounded">⚠️ Skills / Plugins 與主進程同等權限，無自動沙箱，安裝前審查責任落在操作員</div>
      <div class="p-2 bg-yellow-50 border border-yellow-400 rounded">⚠️ API 金鑰明文儲存於 <code>~/.hermes/.env</code>，不支援 Vault / KMS</div>
      <div class="p-2 bg-green-50 border border-green-400 rounded text-green-700">✅ 供應鏈：內建 OSV-Scanner CI；litellm / mistralai 投毒事件已列入掃描清單</div>
      <div class="p-2 bg-green-50 border border-green-400 rounded text-green-700">✅ 無已知直接歸屬 Hermes Agent 的 CVE</div>
    </div>
  </div>
  <div>
    <div class="text-xs text-gray-500 font-bold mb-2">企業部署優先建議</div>
    <div class="flex flex-col gap-1.5 text-xs">
      <div class="flex items-start gap-2 p-2 bg-gray-50 border border-gray-200 rounded">
        <span class="shrink-0 px-1.5 py-0.5 bg-red-500 text-white rounded text-[10px] font-bold">高</span>
        <span>啟用 Docker 沙箱（<code>terminal.backend: docker</code>）——預設 local backend 無容器隔離</span>
      </div>
      <div class="flex items-start gap-2 p-2 bg-gray-50 border border-gray-200 rounded">
        <span class="shrink-0 px-1.5 py-0.5 bg-red-500 text-white rounded text-[10px] font-bold">高</span>
        <span>Gateway 嚴格白名單；絕不使用 <code>GATEWAY_ALLOW_ALL_USERS=true</code></span>
      </div>
      <div class="flex items-start gap-2 p-2 bg-gray-50 border border-gray-200 rounded">
        <span class="shrink-0 px-1.5 py-0.5 bg-red-500 text-white rounded text-[10px] font-bold">高</span>
        <span>以非 root 用戶運行，設定 CPU / 記憶體資源上限</span>
      </div>
      <div class="flex items-start gap-2 p-2 bg-gray-50 border border-gray-200 rounded">
        <span class="shrink-0 px-1.5 py-0.5 bg-orange-400 text-white rounded text-[10px] font-bold">中</span>
        <span>Skills 安裝前強制人工 code review（Skills 為 Python 程式碼）</span>
      </div>
      <div class="flex items-start gap-2 p-2 bg-gray-50 border border-gray-200 rounded">
        <span class="shrink-0 px-1.5 py-0.5 bg-orange-400 text-white rounded text-[10px] font-bold">中</span>
        <span>OSV-Scanner 改設 <code>fail-on-vuln: true</code>（預設為警告、不擋關）</span>
      </div>
      <div class="flex items-start gap-2 p-2 bg-gray-50 border border-gray-200 rounded">
        <span class="shrink-0 px-1.5 py-0.5 bg-orange-400 text-white rounded text-[10px] font-bold">中</span>
        <span>考慮 HashiCorp Vault / Bitwarden Secrets 替代明文 .env</span>
      </div>
    </div>
  </div>
</div>

<div class="mt-3 p-2 bg-gray-50 border border-gray-300 rounded text-xs text-gray-700 flex items-center gap-3">
  <span class="font-bold whitespace-nowrap">資安成熟度：🟡 成長中</span>
  <span class="text-gray-500">誠實揭露防護邊界、有完整 Threat Model，但預設部署姿態非最安全——技術能力充足的企業在容器隔離後可部署，暫不建議高敏感生產環境以預設配置直接使用</span>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
這頁是整個資安評估的總結，銜接上一頁的 Brainworm 防禦。
重點一：沒有已知 CVE 是好消息；供應鏈風險是真實存在的，litellm 和 mistralai 都曾發生投毒，Hermes 的應對是內建 OSV-Scanner。
重點二：官方 SECURITY.md 自承，所有進程內機制（審批門、輸出編輯、模式掃描）都是「啟發式」，不是真正安全邊界。唯一的真正邊界是 OS 沙箱（Docker）。
重點三：預設部署不是最安全配置，企業上線前必須主動啟用 Docker 沙箱、設 Gateway 白名單、限制資源。
整體定位：比同類開源 AI Agent 框架更有資安自覺，但尚不到「企業開箱即用」的成熟度。
-->
---
layout: two-cols
class: kanban-slide
---

# Multi-agent Kanban 自癒能力

```mermaid {scale: 0.6}
flowchart TD
    Master(["主代理"]) -->|"派生"| A["子代理 A"]
    Master -->|"派生"| B["子代理 B ⚠️"]
    Master -->|"派生"| C["子代理 C"]
    A & B & C -->|"狀態寫入"| KB[("📋 Kanban")]
    B -->|"心跳中斷"| Z["殭屍標記"]
    Z -->|"自動偵測"| R["任務回收"]
    R -->|"承接繼續"| C
```

::right::

<div class="flex flex-col gap-3 mt-24">
  <div class="border border-green-600 rounded p-3 text-sm">✅ 無人值守長任務：子代理失效不需人工介入</div>
  <div class="border border-green-600 rounded p-3 text-sm">✅ 任務狀態可審計：Kanban 提供完整生命週期記錄</div>
  <div class="border border-green-600 rounded p-3 text-sm">✅ 跨 session 持久化：配合 /goal 追蹤多日工作流</div>
  <div class="mt-4 p-2 border border-yellow-400 rounded text-xs text-yellow-700">
    ⚠️ v0.13.0 推出，尚無公開 benchmark — 建議 PoC 自行驗證可靠性
  </div>
</div>

<style>
.kanban-slide h1 {
  white-space: nowrap;
  overflow: visible;
}
</style>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
適合場景：需要長時間、多步驟的自動化任務，例如過夜跑的資料處理、多個子任務並行。
主代理派出多個子代理同時工作，Kanban 追蹤所有子代理的狀態。
如果某個子代理沒有回報心跳，系統自動標記為殭屍，任務被其他子代理接手繼續。
不需要人工監看或介入，讓「無人值守長任務」真正可行。
注意：這個功能是 v0.13.0 才加入的，相對較新，建議 PoC 時自行測試可靠性，不要直接用在關鍵流程。
-->
---
layout: default
---

# Tool Gateway — 一訂閱全工具齊備

<div class="grid grid-cols-2 gap-6 mt-4">
  <div class="text-[0.9rem]">
    <div class="font-bold text-gray-500 mb-3">隨 Nous Portal 訂閱包含</div>

| 工具 | 說明 |
|------|------|
| 🔍 Web 搜尋 + 擷取 | Firecrawl 無速率限制 |
| 🎨 圖片生成 | FLUX 2 / GPT-Image / Ideogram 等 9 款 |
| 🔊 文字轉語音 | OpenAI TTS 等多款 |
| 🌐 瀏覽器自動化 | 雲端無頭 Chrome（Browser Use） |

  </div>
  <div class="flex flex-col gap-3 justify-center">
    <div class="p-4 bg-yellow-50 border border-yellow-400 rounded-lg text-sm">
      💡 <strong>不需另開帳號：</strong>不必分別申請 Firecrawl、FAL、Browser Use——Tool Gateway 統一路由
    </div>
    <div class="p-3 bg-gray-50 border border-gray-300 rounded-lg text-sm">
      🛠 企業自建：停用 gateway 改用內部基礎設施（<span class="font-mono text-xs">use_gateway: false</span>）
    </div>
    <div class="p-2 border border-red-300 rounded text-xs text-red-700">
      ⚠️ 付費功能：Nous Portal 免費方案不含 Tool Gateway
    </div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
Tool Gateway 是 Nous Portal 訂閱的附加功能，等於幫你統一管理所有外部工具的帳號、配額和路由。
不需要分別去申請 Firecrawl、FAL、Browser Use 的帳號，Tool Gateway 一個接口全包。
企業如果有資安顧慮不想走外部 gateway，可以設定 use_gateway: false，改接自己的基礎設施。
注意：免費方案沒有這個功能。
-->
---
layout: default
---

# Plugin 系統 — 三種擴充類型

<div class="grid grid-cols-3 gap-4 mt-6">
  <div class="border border-blue-400 rounded-lg p-4">
    <div class="text-2xl mb-2">🔧</div>
    <div class="font-bold text-blue-600 mb-2">Tools / Hooks</div>
    <div class="text-sm text-gray-600">新增自訂工具 + 設置生命週期鉤子（logging、guardrails、webhooks）</div>
    <div class="mt-3 text-xs font-mono text-gray-400">hermes plugins install</div>
  </div>
  <div class="border border-purple-400 rounded-lg p-4">
    <div class="text-2xl mb-2">🧠</div>
    <div class="font-bold text-purple-600 mb-2">Memory Provider</div>
    <div class="text-sm text-gray-600">替換記憶後端：Honcho、Mem0、OpenViking、RetainDB 等跨 session 記憶</div>
    <div class="mt-3 text-xs font-mono text-gray-400">跨 session 個人化</div>
  </div>
  <div class="border border-green-400 rounded-lg p-4">
    <div class="text-2xl mb-2">📋</div>
    <div class="font-bold text-green-600 mb-2">Context Engine</div>
    <div class="text-sm text-gray-600">替換 context 管理，自訂檔案注入與壓縮策略</div>
    <div class="mt-3 text-xs font-mono text-gray-400">hermes plugins UI</div>
  </div>
</div>

<div class="mt-5 p-3 bg-gray-100 rounded text-sm text-gray-700">
  🔒 <strong>企業應用：</strong>Tools/Hooks plugin 可實作 <strong>guardrails</strong>——工具呼叫前後攔截審計，不需 fork 核心程式碼
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
三種 Plugin 中，對企業最實用的是 Tools/Hooks。
它可以在工具呼叫前後插入攔截邏輯——例如記錄所有查詢、過濾敏感指令、加入審批流程——這就是 guardrails 的實作方式。
重點：不需要 fork 核心程式碼就能加這些控管，升級 Hermes 版本時 plugin 也不受影響。
Memory Provider 可以換成企業自己信任的記憶後端，不依賴 Hermes 預設方案。
-->
---
layout: default
---

# 企業可靠性：多層模型保障

<div class="grid grid-cols-2 gap-6 mt-4">
  <div class="flex flex-col gap-3">
    <div class="border border-blue-400 rounded p-3 text-sm">
      <div class="font-bold text-blue-600 mb-1">🗺 Provider Routing</div>
      <div class="text-gray-600">依成本、速度、品質排序多個提供商，支援白名單 / 黑名單過濾</div>
    </div>
    <div class="border border-orange-400 rounded p-3 text-sm">
      <div class="font-bold text-orange-600 mb-1">🔄 Fallback Providers</div>
      <div class="text-gray-600">主要模型出錯時自動切換備援，視覺 / 壓縮任務有獨立 fallback</div>
    </div>
    <div class="border border-green-400 rounded p-3 text-sm">
      <div class="font-bold text-green-600 mb-1">🔑 Credential Pools</div>
      <div class="text-gray-600">多組 API Key 輪替，達速率上限自動換鑰，不中斷服務</div>
    </div>
    <div class="border border-purple-400 rounded p-3 text-sm">
      <div class="font-bold text-purple-600 mb-1">⚡ Prompt Caching</div>
      <div class="text-gray-600">跨 session 1 小時前綴快取（Claude / OpenRouter / Nous Portal），永遠開啟</div>
    </div>
  </div>
  <div class="flex flex-col justify-center gap-4">
    <div class="p-4 bg-blue-50 border border-blue-200 rounded-lg text-sm">
      💡 <strong>SLA 保障</strong><br>
      <span class="text-gray-600">供應商限速或故障時零介入自動切換，服務不中斷</span>
    </div>
    <div class="p-4 bg-green-50 border border-green-200 rounded-lg text-sm">
      💰 <strong>成本控管</strong><br>
      <span class="text-gray-600">Prompt caching 降低重複 context token 費用；Credential Pools 防單鑰達限</span>
    </div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
這四個機制合在一起解決兩個企業痛點：服務中斷和成本失控。
Provider Routing + Fallback：主要供應商掛掉或限速，自動切換備援，不需要人工介入，服務不中斷。
Credential Pools：多組 API Key 輪替，任何一組達到速率上限都不會卡住整個服務。
Prompt Caching 是永遠開啟的：重複的 context（例如 SOUL.md、長篇知識庫）不會重複計費，長期使用成本明顯下降。
-->
---
layout: center
class: text-center
---

# 實際落地案例

<div class="text-gray-400 mt-4 text-lg">遊戲營運 AI Bot — 自然語言查 BigQuery 的實戰驗證</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
接下來是我們自己實際跑的一個案例，用來驗證 Hermes Agent 在我們業務場景的實際能力。
場景是遊戲營運團隊每天需要查 BigQuery 資料做分析，但不是每個人都會寫 SQL。
-->
---
layout: default
---

# 遊戲營運 Bot：用中文提問，Bot 自動出報告

<div class="text-gray-600 text-sm italic mb-4">
  Hermes Agent + BigQuery，遊戲運營同仁無需寫 SQL，直接提問得到完整對比分析
</div>

<div class="grid grid-cols-2 gap-6">
  <div>
    <div class="text-xs text-gray-400 mb-2">對話實例</div>
    <div class="bg-gray-900 rounded-lg p-4">
      <div class="text-gray-400 text-xs mb-3">使用者 · 14:32</div>
      <div class="bg-blue-600 rounded-lg px-3 py-2 text-white text-right mb-4 text-sm ml-8">
        黃金週與卡片最終戰成效交叉比對一下
      </div>
      <div class="text-gray-400 text-xs mb-1">RD7 Bot · 14:35</div>
      <div class="bg-gray-700 rounded-lg p-3 text-xs text-green-300 leading-relaxed">
        <span class="text-white font-bold">FXC 最終戰 × 黃金週 BP 交叉比對 (非CN)</span><br>
        查詢區間：2026/4/1 – 5/4<br><br>
        <span class="text-yellow-300 font-bold">結論先講：</span><br>
        FXC 最終戰仍是營收主力，BP 營收占 88%。Round B 日均較 Round A 下滑 28.5%…
      </div>
    </div>
  </div>
  <div class="flex flex-col gap-3 justify-center">
    <div class="text-xs text-gray-500 font-bold mb-1">Bot 在這次對話做了什麼？</div>
    <div class="border border-amber-400 rounded-lg p-3">
      <div class="text-amber-600 font-bold text-sm mb-1">🗣 理解需求</div>
      <div class="text-gray-700 text-xs">把「黃金週 vs 卡片最終戰」翻成可查的條件</div>
    </div>
    <div class="border border-blue-400 rounded-lg p-3">
      <div class="text-blue-600 font-bold text-sm mb-1">🔍 查資料</div>
      <div class="text-gray-700 text-xs">自動到 BigQuery 跑日均、營收、買家重疊</div>
    </div>
    <div class="border border-green-400 rounded-lg p-3">
      <div class="text-green-600 font-bold text-sm mb-1">📊 做對比，下結論</div>
      <div class="text-gray-700 text-xs">Round A vs B 日均公平對比，用人話解釋數字</div>
    </div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
這是真實的對話紀錄，不是精心設計的 demo。
使用者用一句中文提問，Bot 在大約 3 分鐘內自動：理解業務語意 → 轉成 BigQuery SQL → 執行查詢 → 整理成對比報告。
使用者完全不需要懂 SQL，也不需要知道資料在哪張表。
「結論先講」的輸出格式是我們在知識庫裡定義的規則，Bot 自動遵守。
-->
---
layout: center
class: text-center
---

# 資料準備

<div class="text-gray-400 mt-4 text-lg">Bot 要懂業務，得先給它正確的『地圖』和『字典』</div>

<div class="text-gray-500 text-sm mt-2">DATA · KNOWLEDGE · QUERIES</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
Bot 能正確回答的前提，是我們事先把業務知識餵給它。
這是一次性的準備工作，之後 Bot 會自己學習和更新。
接下來三張投影片說明我們準備了哪三類知識。
-->
---
layout: default
---

# Bot 要餵的三類知識

<div class="text-gray-600 text-sm italic mb-5">少了哪一塊都會卡住：表結構、能跑的範例、聽得懂的詞彙</div>

<div class="grid grid-cols-3 gap-4">
  <div class="border border-blue-400 rounded-lg overflow-hidden">
    <div class="bg-blue-700 px-4 py-3 text-white font-bold text-sm">01 · 數據儀表</div>
    <div class="p-4">
      <div class="text-sm text-gray-700 mb-3">BigQuery 表的中文名、用途、寫入頻率、欄位語意。Bot 才知道「要打開哪張表」。</div>
      <div class="text-xs text-gray-400 font-bold mb-1">EXAMPLES</div>
      <div class="text-xs text-gray-500 italic">DailyUserInfoSnapshot · GameAccount · ...</div>
    </div>
  </div>
  <div class="border border-amber-400 rounded-lg overflow-hidden">
    <div class="bg-amber-700 px-4 py-3 text-white font-bold text-sm">02 · 歷史 Query 範例</div>
    <div class="p-4">
      <div class="text-sm text-gray-700 mb-3">把過去寫過的查 SQL 收進來。Bot 用最像的範本改造，避免從零亂湊。</div>
      <div class="text-xs text-gray-400 font-bold mb-1">EXAMPLES</div>
      <div class="text-xs text-gray-500 italic">計算 DAU · 計算營收 · 留存 · 重疊買家</div>
    </div>
  </div>
  <div class="border border-green-400 rounded-lg overflow-hidden">
    <div class="bg-green-700 px-4 py-3 text-white font-bold text-sm">03 · 一般營運知識</div>
    <div class="p-4">
      <div class="text-sm text-gray-700 mb-3">縮寫、行話、人話對映：DAU 是什麼、員工要不要排除、CN 什麼定義…</div>
      <div class="text-xs text-gray-400 font-bold mb-1">EXAMPLES</div>
      <div class="text-xs text-gray-500 italic">DAU = 日活躍 · DNU = 新玩家 · DOU = 老玩家</div>
    </div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
三類知識缺一不可：
01 數據儀表：讓 Bot 知道「去哪找資料」——沒有這個，Bot 不知道要查哪張表。
02 歷史 Query：讓 Bot 有正確的 SQL 範本可以改——沒有這個，Bot 容易從零亂湊出錯誤的查詢。
03 營運知識：讓 Bot 理解業務語言——沒有這個，Bot 可能把「新進」誤當「活躍」，算出完全不同的數字。
-->
---
layout: default
---

# 數據儀表｜DailyUserInfoSnapshot

<div class="text-gray-600 text-sm italic mb-4">非即時主表，覆蓋玩家屬性 + 每日聚合，是 Bot 跑分析的第一站</div>

<div class="grid grid-cols-2 gap-6">
  <div class="border border-gray-300 rounded-lg p-4">
    <div class="text-xs text-gray-400 font-bold mb-3">TABLE METADATA</div>
    <div class="flex flex-col gap-2">
      <div class="flex gap-2 text-xs"><span class="text-gray-500 w-36 shrink-0">table_id</span><span class="font-mono text-gray-700">preprocessed_bklog.<br>DailyUserInfoSnapshot</span></div>
      <div class="flex gap-2 text-xs"><span class="text-gray-500 w-36 shrink-0">中文表名</span><span class="text-gray-700">日結玩家聚合資訊</span></div>
      <div class="flex gap-2 text-xs"><span class="text-gray-500 w-36 shrink-0">table_type</span><span class="text-gray-700">Intermediate</span></div>
      <div class="flex gap-2 text-xs"><span class="text-gray-500 w-36 shrink-0">write_frequency</span><span class="text-gray-700">Daily</span></div>
      <div class="flex gap-2 text-xs"><span class="text-gray-500 w-36 shrink-0">business_domain</span><span class="text-gray-700">玩家</span></div>
      <div class="flex gap-2 text-xs"><span class="text-gray-500 w-36 shrink-0">partitions</span><span class="font-mono text-gray-700">BQDate</span></div>
    </div>
  </div>
  <div>
    <div class="text-xs text-gray-400 font-bold mb-2">BOT 最常用的欄位</div>
    <div class="flex flex-col divide-y divide-gray-100 text-xs">
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">BQDate</span><span class="text-gray-600">日期 partition（REQUIRED）</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">UserID</span><span class="text-gray-600">玩家 ID</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">Country</span><span class="text-gray-600">主要市場：CN/JP/TW/US/VN/Others</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">VipLV</span><span class="text-gray-600">當日最高 VIP</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">GameLevel</span><span class="text-gray-600">當日最高遊戲等級</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">BuyNumber</span><span class="text-gray-600">營收（不需排除員工）</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">EndBalance</span><span class="text-gray-600">持有通算金幣（金幣水位）</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">UserType</span><span class="text-gray-600">30日活躍 / 新進 / 30日回流</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">LastBuyDate</span><span class="text-gray-600">180 天內最近一次購買</span></div>
      <div class="py-1 flex gap-3"><span class="font-mono text-blue-600 w-28 shrink-0">BPBuyNumber</span><span class="text-gray-600">付費 BP 儲值金額</span></div>
    </div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
DailyUserInfoSnapshot 是 Bot 跑非即時分析的主要入口，幾乎所有 DAU、營收、留存查詢都從這裡出發。
重要的業務口徑要講清楚：BQDate 是 partition 欄位，每次查詢都必須指定，否則費用爆炸。
BuyNumber 是營收欄位，不需要排除員工；但 DAU 等人數查詢要排除員工帳號（在 GameAccount 表）。
這些規則我們寫進了知識庫，Bot 自動遵守。
-->
---
layout: default
---

# 歷史 Query 範例

<div class="text-gray-600 text-sm italic mb-4">把過去寫得不錯的 SQL 收進來，Bot 找最像的當範本改</div>

<div class="grid grid-cols-2 gap-6">
  <div class="border border-gray-300 rounded-lg p-4">
    <div class="text-xs text-gray-400 font-bold mb-3">計算 DAU &nbsp;·&nbsp; dim: BQDate</div>
    <pre class="bg-gray-50 rounded p-3 text-xs font-mono leading-snug"><span class="text-gray-400 italic">/* 非即時資料 → 用 DailyUserInfoSnapshot */</span>
<span class="text-gray-400 italic">/* 非營收資料 → 排除員工 */</span>
<span class="text-blue-600">SELECT</span> BQDate,
  <span class="text-purple-600">count</span>(<span class="text-blue-600">distinct</span> UserID) <span class="text-blue-600">AS</span> DAU
<span class="text-blue-600">FROM</span> <span class="text-green-600">`DailyUserInfoSnapshot`</span>
<span class="text-blue-600">WHERE</span> BQDate <span class="text-blue-600">BETWEEN</span> <span class="text-amber-600">'2025-08-08'</span>
  <span class="text-blue-600">AND</span> <span class="text-amber-600">'2025-08-10'</span>
  <span class="text-blue-600">AND</span> UserID <span class="text-blue-600">NOT IN</span> (
    <span class="text-blue-600">SELECT</span> UserID <span class="text-blue-600">FROM</span> <span class="text-green-600">`GameAccount`</span>
  )
<span class="text-blue-600">GROUP BY</span> BQDate
<span class="text-blue-600">ORDER BY</span> BQDate</pre>
  </div>
  <div class="border border-gray-300 rounded-lg p-4">
    <div class="text-xs text-gray-400 font-bold mb-3">計算營收 &nbsp;·&nbsp; dim: BQDate</div>
    <pre class="bg-gray-50 rounded p-3 text-xs font-mono leading-snug"><span class="text-gray-400 italic">/* 非即時資料 → 用 DailyUserInfoSnapshot */</span>
<span class="text-gray-400 italic">/* 營收資料 → 不需排除員工 */</span>
<span class="text-blue-600">SELECT</span> BQDate,
  <span class="text-purple-600">sum</span>(BuyNumber) <span class="text-blue-600">AS</span> BuyNumber
<span class="text-blue-600">FROM</span> <span class="text-green-600">`DailyUserInfoSnapshot`</span>
<span class="text-blue-600">WHERE</span> BQDate <span class="text-blue-600">BETWEEN</span> <span class="text-amber-600">'2025-08-08'</span>
  <span class="text-blue-600">AND</span> <span class="text-amber-600">'2025-08-10'</span>
<span class="text-blue-600">GROUP BY</span> BQDate
<span class="text-blue-600">ORDER BY</span> BQDate</pre>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
Bot 使用 RAG（檢索增強生成）機制：收到問題後，先找和使用者需求最相似的歷史 SQL，再修改日期範圍、條件，輸出正確的查詢。
這個做法比讓 AI 從零生成 SQL 可靠得多，因為有正確的結構和業務口徑作為參考。
注意左右兩張的差異：DAU 需要 NOT IN GameAccount 排除員工；營收不需要——這個口徑差異就靠範例 SQL 的註解傳達給 Bot。
-->
---
layout: default
---

# 一般營運知識｜給 Bot 的字典

<div class="text-gray-600 text-sm italic mb-4">把行話、縮寫、規則寫清楚，Bot 才不會把「新進」當「活躍」回給你</div>

<div class="grid grid-cols-2 gap-6">
  <div class="border border-gray-300 rounded-lg p-4">
    <div class="text-xs text-gray-400 font-bold mb-3">INDICATORS</div>
    <div class="flex flex-col divide-y divide-gray-100 text-xs">
      <div class="py-1 flex gap-3"><span class="font-bold text-gray-700 w-20 shrink-0">DAU</span><span class="text-gray-600">日活躍玩家數 (Daily Active Users)</span></div>
      <div class="py-1 flex gap-3"><span class="font-bold text-gray-700 w-20 shrink-0">DNU</span><span class="text-gray-600">每日新玩家數 (Daily New Users)</span></div>
      <div class="py-1 flex gap-3"><span class="font-bold text-gray-700 w-20 shrink-0">DOU</span><span class="text-gray-600">每日老玩家數 (Daily Old Users)</span></div>
      <div class="py-1 flex gap-3"><span class="font-bold text-gray-700 w-20 shrink-0">BP 營收</span><span class="text-gray-600">付費 BP 儲值金額（BPBuyNumber）</span></div>
      <div class="py-1 flex gap-3"><span class="font-bold text-gray-700 w-20 shrink-0">黑鑽</span><span class="text-gray-600">BlackDiamondTag 標示的高價值玩家</span></div>
      <div class="py-1 flex gap-3"><span class="font-bold text-gray-700 w-20 shrink-0">金幣水位</span><span class="text-gray-600">EndBalance：玩家當日持有通算金幣量</span></div>
      <div class="py-1 flex gap-3"><span class="font-bold text-gray-700 w-20 shrink-0">30日活躍</span><span class="text-gray-600">前 30 天內有上線紀錄的玩家</span></div>
      <div class="py-1 flex gap-3"><span class="font-bold text-gray-700 w-20 shrink-0">30日回流</span><span class="text-gray-600">前 30 天有過上線、但今日不是新進</span></div>
    </div>
  </div>
  <div class="pt-4">
    <div class="text-xs text-gray-400 font-bold mb-3">BOT 預設遵守的營運規則</div>
    <div class="flex flex-col gap-2">
      <div class="p-2 bg-gray-50 border-l-2 border-blue-400 rounded-r text-xs text-gray-700">非即時數據需求：一律走 DailyUserInfoSnapshot</div>
      <div class="p-2 bg-gray-50 border-l-2 border-blue-400 rounded-r text-xs text-gray-700">非營收查詢：UserID 排除 GameAccount 員工帳號</div>
      <div class="p-2 bg-gray-50 border-l-2 border-blue-400 rounded-r text-xs text-gray-700">營收查詢：不需排除員工</div>
      <div class="p-2 bg-gray-50 border-l-2 border-blue-400 rounded-r text-xs text-gray-700">Country = Others 時，看 CountryDetail 取精準國家</div>
      <div class="p-2 bg-gray-50 border-l-2 border-amber-400 rounded-r text-xs text-gray-700">通算金幣 = Coin + 25000 × Gem（贈幣同口徑）</div>
      <div class="p-2 bg-gray-50 border-l-2 border-green-400 rounded-r text-xs text-gray-700">回答先給結論，再附支持的數字與 SQL</div>
    </div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
這份字典解決了 AI 不懂業務語言的問題。
沒有這個，Bot 可能把「新進」誤解為「活躍」，算出完全錯誤的用戶數。
右側的預設規則讓 Bot 在每次回答時都自動遵守業務口徑，不需要使用者每次重複交代。
通算金幣的公式（Coin + 25000 × Gem）是特別非直覺的業務規則，這種知識最需要明確告訴 Bot。
-->
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

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
整體評估：優勢明顯，風險可控，導入門檻低。
最重要的一點：$5 VPS 一個月 PoC，大約台幣 160 元，就能在真實業務場景驗證可行性。
資安方面需要額外規劃：SOUL.md 保護、Promptware 風險評估、資料治理策略——這些是導入前要確認的事項。
建議行動：列為 AI Agent 基礎框架候選，啟動一個月 PoC。
-->
---
layout: default
---

# 資料來源

<div class="flex flex-col gap-4 mt-6">
  <div class="border border-gray-300 rounded-lg p-4">
    <div class="text-xs text-gray-400 mb-1">GitHub Repo</div>
    <div class="font-mono text-sm">github.com/NousResearch/hermes-agent</div>
  </div>
  <div class="border border-gray-300 rounded-lg p-4">
    <div class="text-xs text-gray-400 mb-1">官方文件</div>
    <div class="font-mono text-sm">hermes-agent.nousresearch.com/docs</div>
  </div>
  <div class="border border-gray-300 rounded-lg p-4">
    <div class="text-xs text-gray-400 mb-1">繁中教學手冊（chihhung, v0.15.2）</div>
    <div class="font-mono text-sm">chihhung.github.io/Blog/posts/教學/ai開發/hermes-agent生態系教學手冊</div>
  </div>
  <div class="border border-blue-300 rounded-lg p-4">
    <div class="text-xs text-blue-400 mb-1">DeepWiki — code-level 架構分析</div>
    <div class="font-mono text-sm">deepwiki.com/NousResearch/hermes-agent</div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
這份報告主要參考了四個來源。
DeepWiki 特別值得推薦：它會自動分析 GitHub repo 的程式碼並生成架構文件，對想深入了解 Hermes 內部實作的人很有幫助。
有興趣深入研究的同仁可以從 DeepWiki 開始。
-->
---
layout: center
class: text-center
---

# 謝謝

<div class="text-gray-600 mt-4 text-sm">
  報告日期：2026.06.12
</div>
<div class="text-gray-600 mt-2 text-sm">
  Co-author：佳宏 — 技術評估與內容審閱
</div>
<div class="text-gray-600 mt-2 text-sm">
  Co-author：小赫（Hermes Agent）— 協助投影片內容編修與自動化流程
</div>
<div class="text-gray-600 mt-2 text-sm">
  Co-author：Claude（Anthropic）— 原始碼分析、資安風險審查、投影片內容編修
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
開放 Q&A。
如果有關於資安評估、PoC 規劃、或技術細節的問題，歡迎提出。
-->
