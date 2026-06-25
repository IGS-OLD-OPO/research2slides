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

<div class="absolute inset-0" style="background:rgba(5,5,25,0.55)" />

<div class="relative z-10">

# Hermes Agent

### 自我改進 AI Agent 框架技術評估

<div class="text-sm text-gray-300 mt-1">
  命名自希臘神話赫爾墨斯（Hermēs）——眾神信使，穿梭邊界、傳遞訊息
</div>

<div class="text-xl text-gray-200 mt-6 mb-4 italic">
  "The Agent That Grows With You"
</div>

<div class="pt-12 text-gray-300">
  Nous Research ・ 技術評估報告 ・ 2026.06.24
</div>

</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-400 z-10"><SlideCurrentNo /> / <SlidesTotal /></div>

<style>
h1 { text-shadow: 0 2px 16px rgba(0,0,0,0.9) !important; }
h3 { text-shadow: 0 1px 10px rgba(0,0,0,0.9) !important; }
</style>

<!--
今天要跟大家介紹的是 Nous Research 開發的開源 AI Agent 框架——Hermes Agent 的技術評估。
這份報告結合了原始碼分析、實際部署測試，以及企業應用視角，目標是評估它是否值得我們進一步導入。
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
    <div class="text-5xl font-bold text-blue-600">201K</div>
    <div class="text-gray-600 text-sm mt-1">GitHub Stars</div>
  </div>
  <div>
    <div class="text-5xl font-bold text-green-600">35.8K</div>
    <div class="text-gray-600 text-sm mt-1">Forks</div>
  </div>
  <div>
    <div class="text-5xl font-bold text-purple-600">1,534</div>
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

# 評估路線圖

<div class="text-xs text-gray-500 mb-4">圍繞 5 個企業導入評估面相</div>

<div class="grid grid-cols-5 gap-3 mt-2">
  <div class="border border-blue-400 rounded-lg p-3 bg-blue-50">
    <div class="font-bold text-blue-700 text-sm mb-2">🧠 Skill 沉澱</div>
    <div class="text-xs text-gray-600 space-y-1">
      <div>Learning Loop</div>
      <div>Skill 生命週期</div>
      <div>background review</div>
    </div>
  </div>
  <div class="border border-purple-400 rounded-lg p-3 bg-purple-50">
    <div class="font-bold text-purple-700 text-sm mb-2">💾 長期記憶</div>
    <div class="text-xs text-gray-600 space-y-1">
      <div>分層記憶架構</div>
      <div>session_search</div>
      <div>Honcho 整合</div>
    </div>
  </div>
  <div class="border border-green-400 rounded-lg p-3 bg-green-50">
    <div class="font-bold text-green-700 text-sm mb-2">💰 Token 成本</div>
    <div class="text-xs text-gray-600 space-y-1">
      <div>多模型路由</div>
      <div>5 天實測 token 用量</div>
    </div>
  </div>
  <div class="border border-amber-400 rounded-lg p-3 bg-amber-50">
    <div class="font-bold text-amber-700 text-sm mb-2">🎯 應用場景</div>
    <div class="text-xs text-gray-600 space-y-1">
      <div>遊戲營運 Bot</div>
      <div>社群 262 案例</div>
    </div>
  </div>
  <div class="border border-red-400 rounded-lg p-3 bg-red-50">
    <div class="font-bold text-red-700 text-sm mb-2">🛡 資安</div>
    <div class="text-xs text-gray-600 space-y-1">
      <div>SOUL.md 管控</div>
      <div>Promptware 防禦</div>
      <div>指令審批機制</div>
    </div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
這份報告的五個評估維度是根據企業導入 AI Agent 的核心顧慮設計的。
接下來每個面向都有 2-3 頁深入說明，包含原始碼確認和實測數據。
-->

---
layout: default
---

# Agent 越用越聰明：Learning Loop — 三台引擎

```mermaid {scale: 0.75}
flowchart LR
    A["🎯 任務完成"] -->|"自動回顧"| B["🔨 建造 Skill\n封裝可重複流程"]
    B -->|"skill_manage"| C["💾 維護記憶\nMEMORY.md + 偏好"]
    C -->|"Curator 維護"| D["🧬 演化治理\n自動整理/棄用"]
    D -->|"下次自動套用"| A
```

<div class="grid grid-cols-3 gap-3 mt-4">
  <div class="p-2 border border-blue-300 rounded bg-blue-50 text-xs">
    <div class="font-mono font-bold text-blue-700 mb-1">🔨 造 (Build)</div>
    Agent 把成功流程封裝成 skill，避免重複發明輪子。
  </div>
  <div class="p-2 border border-green-300 rounded bg-green-50 text-xs">
    <div class="font-mono font-bold text-green-700 mb-1">💾 修 (Maintain)</div>
    跨對話寫入記憶，支援全文搜尋與稽核，不因換 session 就遺失。
  </div>
  <div class="p-2 border border-orange-300 rounded bg-orange-50 text-xs">
    <div class="font-mono font-bold text-orange-700 mb-1">🧬 續 (Evolve)</div>
    Curator 引擎閒置一定時間自動整理/棄用過時 skill，防止知識腐化。
  </div>
</div>

<div class="mt-3 p-2 bg-gray-100 rounded text-xs text-gray-600">
  三個引擎分開處理「新建/維護/演化」三件事，缺一就會退化到單純對話机器人。
</div>

<div class="grid grid-cols-3 gap-2 mt-2">
  <div class="p-2 bg-gray-100 rounded border border-gray-400 text-xs"><span class="font-bold">記憶回顧觸發：</span>每 <span class="font-mono font-bold">10</span> 回合（使用者訊息計數）</div>
  <div class="p-2 bg-gray-100 rounded border border-gray-400 text-xs"><span class="font-bold">技能回顧觸發：</span>每累積 <span class="font-mono font-bold">10</span> 次工具呼叫</div>
  <div class="p-2 bg-orange-50 rounded border border-orange-400 text-xs"><span class="font-bold text-orange-700">負面過濾觸發：</span>background_review.py 偵測失敗模式，加入黑名單</div>
</div>
<div class="text-xs text-gray-500 mt-1">均可在 <span class="font-mono">config.yaml</span> 調整 <span class="font-mono">nudge_interval</span>・背景 daemon thread 執行，不阻塞使用者回應</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

---
layout: default
---

# Skill 生命週期狀態

<div class="grid grid-cols-2 gap-6 mt-4">
  <div class="flex flex-col gap-2">
    <div class="flex flex-col items-center gap-1">
      <div class="px-6 py-3 bg-green-100 border-2 border-green-500 rounded-xl text-center w-full">
        <div class="font-bold text-green-700 text-sm">active</div>
        <div class="text-xs text-gray-600 mt-0.5">正常使用中，自動套用</div>
      </div>
      <div class="px-6 py-3 bg-yellow-100 border-2 border-yellow-500 rounded-xl text-center w-full">
        <div class="font-bold text-yellow-700 text-sm">stale</div>
        <div class="text-xs text-gray-600 mt-0.5">Curator 標記，等待複查</div>
      </div>
      <div class="px-6 py-3 bg-gray-100 border-2 border-gray-400 rounded-xl text-center w-full">
        <div class="font-bold text-gray-600 text-sm">archived</div>
        <div class="text-xs text-gray-600 mt-0.5">歸檔，不再自動套用，可隨時 rollback</div>
      </div>
    </div>
    <div class="p-2 bg-blue-50 border border-blue-300 rounded text-xs">
      🔒 <strong>永不刪除：</strong>版本歷史完整保留，<code>patch_count</code> 追蹤每次修訂，隨時可 rollback
    </div>
    <div class="p-2 bg-green-50 border border-green-300 rounded text-xs">
      📌 <strong>pin 機制：</strong>重要 Skill 加 pin，Curator 不自動淘汰，即使長期閒置
    </div>
  </div>
  <div class="flex flex-col justify-center gap-2">
    <div class="text-xs text-gray-500 font-bold">實測：skills-meta.json </div>
    <ZoomImg src="/vscode-skills-meta-json.jpg">
      <div class="rounded border border-gray-300 shadow-sm overflow-hidden" style="height: 270px;">
        <img src="/vscode-skills-meta-json.jpg" class="w-full h-full" style="object-fit: cover; object-position: left top;" />
      </div>
    </ZoomImg>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
Skill 生命週期管理是 Hermes 與一般對話機器人的根本差異之一。
三態模型：active（使用中）→ stale（閒置標記）→ archived（歸檔保留）。
永不刪除原則讓企業放心：知識不會因為 AI 自動清理而消失。
pin 機制是企業部署的重要工具——針對業務核心的 Skill（例如報表格式規範），加 pin 防止 Curator 自動淘汰。
-->

---
layout: default
---

# background_review.py

<div class="grid grid-cols-2 gap-6 mt-4">
  <div>
    <div class="text-xs text-gray-500 mb-2">四類應被屏蔽的 Skill 模式</div>
    <div class="overflow-x-auto">
      <table class="table-auto border-collapse w-full text-xs">
        <thead>
          <tr class="bg-gray-100">
            <th class="border border-gray-300 px-2 py-1.5 text-left">類型</th>
            <th class="border border-gray-300 px-2 py-1.5 text-left">說明</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="border border-gray-300 px-2 py-1.5 font-bold text-red-700">錯誤結果</td>
            <td class="border border-gray-300 px-2 py-1.5">執行後產生錯誤或不正確輸出的 Skill</td>
          </tr>
          <tr class="bg-gray-50">
            <td class="border border-gray-300 px-2 py-1.5 font-bold text-orange-700">過度通用</td>
            <td class="border border-gray-300 px-2 py-1.5">適用範圍太廣導致被濫用（例如：「回答所有問題」）</td>
          </tr>
          <tr>
            <td class="border border-gray-300 px-2 py-1.5 font-bold text-yellow-700">重複冗餘</td>
            <td class="border border-gray-300 px-2 py-1.5">與現有 Skill 高度重疊，功能差異不大</td>
          </tr>
          <tr class="bg-gray-50">
            <td class="border border-gray-300 px-2 py-1.5 font-bold text-gray-700">低頻低效</td>
            <td class="border border-gray-300 px-2 py-1.5">使用率極低且封裝無效率，與直接對話相比無明顯優勢</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="flex flex-col gap-3 justify-center">
    <div class="p-3 bg-gray-800 rounded text-xs font-mono text-green-300 leading-relaxed">
      "The goal of negative learning is not to punish the agent for mistakes, but to ensure the skill library only retains patterns that genuinely improve performance."
    </div>
    <div class="p-3 bg-orange-50 border border-orange-300 rounded text-xs text-orange-800">
      🔄 <strong>與 Curator 的分工：</strong><br>
      background_review.py 負責「哪些該學/不該學」；
      Curator 負責「哪些該整理」（正向治理）
    </div>
    <div class="p-2 bg-blue-50 border border-blue-300 rounded text-xs text-blue-700">
      💡 差異化亮點：大多數 Agent 框架只有「學習」機制；Hermes 明確設計「不該學什麼」，防止 Skill 庫腐化
    </div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
大多數 AI Agent 框架只關注「學到了什麼」，Hermes 的差異化在於同樣關注「不該學什麼」。
background_review.py 是負面學習的核心——定期掃描 Skill 庫，把四類問題 Skill 加入黑名單。
這解決了一個實際痛點：AI 自動學習可能積累很多低品質或冗餘的 Skill，時間久了 Skill 庫就變成垃圾場。
黑名單機制確保 Skill 庫保持精簡、高品質。
-->
---
layout: default
---

# 分層記憶架構

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
    <div class="flex justify-center text-gray-400 text-xs">▼ 選用外部插件</div>
    <div class="border border-indigo-300 rounded-lg p-3 bg-indigo-50">
      <div class="text-indigo-600 font-bold text-sm mb-1">第四層（選用）— Honcho / 外部記憶服務</div>
      <div class="text-xs text-gray-600">Honcho 插件（<span class="font-mono">plugins/memory/honcho/</span>）；跨用戶、跨 Agent 的共享長期記憶，需額外部署</div>
    </div>
  </div>
  <div class="flex flex-col gap-4 justify-center">
    <div class="p-4 bg-blue-50 rounded-lg border border-blue-200 text-sm">
      💡 <strong>實際場景</strong><br>
      <span class="text-gray-600">三週後繼續同一專案，無需重新交代背景</span>
    </div>
    <div class="p-4 bg-green-50 rounded-lg border border-green-200 text-sm">
      📋 <strong>稽核友善</strong><br>
      <span class="text-gray-600">MEMORY.md 為純文字，可直接備份與審計</span>
    </div>
    <div class="p-3 border border-red-400 rounded-lg text-xs text-red-700">
      ⚠️ 寫入 MEMORY.md 的內容由 AI 自主判斷（原始碼無明確過濾規則），企業、專案維護者需評估資料治理策略
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

# 多模型支援，一套框架

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

<div class="mt-4 border-l-4 border-blue-500 pl-4 py-2 bg-blue-50 rounded-r">
  <div class="text-sm text-gray-700 italic leading-relaxed">
    「企業的關鍵不在於找到最強的模型，而在於知道如何 <strong>orchestrate</strong> AI——讓不同工具協作，解決複雜問題。」
  </div>
  <div class="text-xs text-gray-500 mt-1">— Satya Nadella，Microsoft CEO（Microsoft Build 2026）</div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
最重要的一點：Hermes 不綁定任何一家 AI 供應商。
今天用 Claude，明天 GPT-5 出來覺得效果更好或更便宜，改一行 config 就換，不需要重寫任何程式碼。
OpenRouter 是一個聚合平台，一個 API key 可以打 200+ 個模型，是最靈活的接入方式。
Nadella 強調的 orchestrate，正是 Hermes 多模型支援的核心設計理念：不鎖定單一供應商，按任務特性派發最合適的模型。
-->

---
layout: default
---

# Token 消耗 — 實際用量與成本分析

<div class="text-xs text-gray-500 font-bold mb-2">Hermes 實際 API 用量（2026-06-18 ~ 2026-06-22）</div>

<ZoomImg src="/token-usage-table.jpg">
  <img src="/token-usage-table.jpg" class="rounded-lg border border-gray-300 w-full shadow-sm" style="max-height: 300px; object-fit: contain; object-position: left;" />
</ZoomImg>

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="p-3 border border-blue-300 rounded bg-blue-50 text-xs">
    <div class="font-bold text-blue-700 mb-1">Claude Code vs Hermes Agent</div>
    Claude Code 使用 Sonnet 4-6；Hermes Agent 使用 Step 3.7 Flash——相同工作負載，不同模型選擇。
  </div>
  <div class="p-3 border border-orange-300 rounded bg-orange-50 text-xs">
    <div class="font-bold text-orange-700 mb-1">成本落差</div>
    Sonnet $8.71 vs Step $1.33（同一天）：相同 token 量，成本差 <strong>6.5 倍</strong>。
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

---
layout: default
---

# 多平台整合 — 在現有工具中使用 AI

Agent 透過主流通訊平台操作，使用者不需學新介面

<div class="grid grid-cols-2 gap-8 mt-4 items-center">
  <div class="flex flex-col gap-4">
    <div class="grid grid-cols-2 gap-3">
      <div class="border border-gray-400 rounded-xl px-4 py-4 text-center">
        <div class="text-3xl">💬</div>
        <div class="text-sm mt-1">Telegram</div>
      </div>
      <div class="border border-gray-400 rounded-xl px-4 py-4 text-center">
        <div class="text-3xl">🎮</div>
        <div class="text-sm mt-1">Discord</div>
      </div>
      <div class="border border-gray-400 rounded-xl px-4 py-4 text-center">
        <div class="text-3xl">💼</div>
        <div class="text-sm mt-1">Slack</div>
      </div>
      <div class="border border-gray-400 rounded-xl px-4 py-4 text-center">
        <div class="text-3xl">📱</div>
        <div class="text-sm mt-1">WhatsApp</div>
      </div>
    </div>
    <div class="p-4 bg-blue-50 border border-blue-300 rounded-xl text-sm">
      📌 <strong>實際場景：</strong>工程師或業務人員直接在 Slack 發指令給 Agent，完成自動化任務，不需切換工具
    </div>
  </div>
  <div class="flex flex-col items-center">
    <ZoomImg src="/messaging-integrations.jpg">
      <img src="/messaging-integrations.jpg" class="rounded-lg border border-gray-300 shadow-sm max-h-[350px] object-contain mx-auto" />
    </ZoomImg>
    <div class="text-xs text-gray-500 mt-2 text-center">Hermes 內建 messaging integrations 列表（部分平台）</div>
  </div>
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

# 使用場景

<div class="grid grid-cols-2 gap-6 mt-4">
  <div>
    <div class="text-xs font-bold text-green-700 mb-3">✅ 適合導入的場景</div>
    <div class="flex flex-col gap-2 text-xs">
      <div class="p-2 bg-green-50 border border-green-300 rounded">🔍 非技術人員用自然語言查內部資料</div>
      <div class="p-2 bg-green-50 border border-green-300 rounded">🔄 IT / 工程部門重複性自動化任務</div>
      <div class="p-2 bg-green-50 border border-green-300 rounded">🤖 需要多步驟無人值守的長任務</div>
      <div class="p-2 bg-green-50 border border-green-300 rounded">🏢 多部門各自維護行為隔離的 AI 助理（SOUL.md 分離管理）</div>
      <div class="p-2 bg-green-50 border border-green-300 rounded">🔀 需靈活切換底層模型、降低廠商鎖定的場合</div>
    </div>
  </div>
  <div>
    <div class="text-xs font-bold text-red-700 mb-3">⚠️ 需謹慎或暫緩的場景</div>
    <div class="flex flex-col gap-2 text-xs">
      <div class="p-2 bg-red-50 border border-red-300 rounded">🏦 高合規監管環境（金融、醫療、法務）以預設配置直接上線</div>
      <div class="p-2 bg-red-50 border border-red-300 rounded">🔒 需要細粒度 ACL 的場合（SOUL.md / MEMORY.md 無原生存取控制）</div>
      <div class="p-2 bg-red-50 border border-red-300 rounded">🛠 無 Python 能力自建 guardrails，且無監管直接部署</div>
      <div class="p-2 bg-yellow-50 border border-yellow-300 rounded">⚙️ 自動生成的 Skill（Python 程式碼）直接進生產環境，無 code review 流程</div>
    </div>
  </div>
</div>

<div class="mt-3 p-2 bg-gray-100 border border-gray-300 rounded text-xs text-gray-600 text-center">
  核心前提：啟用 Docker 沙箱
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
這頁是技術評估章節的收尾，把所有技術特色和資安分析轉化為「能用/不能用」的直接答案。
左欄是已驗證或有強理由的適合場景；右欄是需要額外準備或有已知缺口的場景。
最下方的「核心前提」很重要：Docker + 白名單不是可選項，是把右欄風險降到可接受範圍的必要條件。
-->
---
layout: default
---

# 遊戲營運 Bot：用中文提問，Bot 自動出報告

<div class="flex items-center gap-4 mb-4">
  <div class="text-gray-600 text-sm italic">Hermes Agent + BigQuery，遊戲運營同仁無需寫 SQL，直接提問得到完整對比分析</div>

</div>

<div class="grid grid-cols-2 gap-6">
  <div>
    <div class="text-xs text-gray-400 mb-2">RD7 金猴爺營運 Bot 對話實例</div>
    <div class="bg-gray-900 rounded-lg p-4">
      <div class="text-gray-400 text-xs mb-3">使用者 · 14:32</div>
      <div class="bg-blue-600 rounded-lg px-3 py-2 text-white text-right mb-4 text-sm ml-8">
        黃金週與卡片最終戰成效交叉比對一下
      </div>
      <div class="text-gray-400 text-xs mb-1">RD7 Bot</div>
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
layout: default
---

# 資料準備：Bot 要餵的三類知識

<div class="text-gray-600 text-sm italic mb-4">Bot 要懂業務，得先給它正確的地圖和字典</div>

<div class="grid grid-cols-3 gap-5">
  <div class="border border-blue-300 rounded-lg p-5 bg-blue-50 flex flex-col gap-3">
    <div class="font-bold text-blue-700 text-sm">01 · 數據儀表</div>
    <div class="text-sm text-gray-700">BigQuery 表的中文名、用途、寫入頻率、欄位語意。Bot 才知道「要打開哪張表」。</div>
  </div>
  <div class="border border-amber-300 rounded-lg p-5 bg-amber-50 flex flex-col gap-3">
    <div class="font-bold text-amber-700 text-sm">02 · 歷史 Query 範例</div>
    <div class="text-sm text-gray-700">把過去寫過的 SQL 收進來。Bot 用最像的範本改造，避免從零亂湊出錯誤的查詢。</div>
  </div>
  <div class="border border-green-300 rounded-lg p-5 bg-green-50 flex flex-col gap-3">
    <div class="font-bold text-green-700 text-sm">03 · 一般營運知識</div>
    <div class="text-sm text-gray-700">縮寫、行話、人話對映：DAU 是什麼、員工要不要排除、CN 的定義…Bot 才聽得懂業務語言。</div>
  </div>
</div>

<div class="mt-5 p-3 bg-gray-100 border border-gray-300 rounded text-xs text-gray-600 text-center">
  三類知識是一次性的初始準備——完成後 Bot 會透過 Learning Loop 持續自我更新
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

# 社群驗證：262 則真實案例

<div class="text-xs text-gray-500 font-bold mb-2">官方 User Stories — Enterprise / Business Ops 精選場景</div>

<ZoomImg src="/user-stories-enterprise.png">
  <img src="/user-stories-enterprise.png" class="rounded-lg border border-gray-300 shadow-sm block mx-auto" style="max-height: 200px; max-width: 100%;" />
</ZoomImg>

<div class="text-xs text-gray-400 mt-1 mb-3 text-center">hermes-agent.nousresearch.com/docs/user-stories</div>

<div class="grid grid-cols-3 gap-3">
  <div class="border border-blue-300 rounded-lg p-3 bg-blue-50">
    <div class="font-bold text-blue-700 text-sm">定時自動推報</div>
    <div class="text-xs text-gray-600 mt-1">「每個工作日早上 9 點整理收件夾推到 Slack」——每日摘要主動推送，不需人工觸發</div>
  </div>
  <div class="border border-green-300 rounded-lg p-3 bg-green-50">
    <div class="font-bold text-green-700 text-sm">會議記錄自動化</div>
    <div class="text-xs text-gray-600 mt-1">自動轉錄 Google Meet／Teams，產出摘要與行動項目；敏感資料走本地模型不出機器</div>
  </div>
  <div class="border border-purple-300 rounded-lg p-3 bg-purple-50">
    <div class="font-bold text-purple-700 text-sm">多遊戲 Chief of Staff 架構</div>
    <div class="text-xs text-gray-600 mt-1">主 Agent 跨專案統覽；每個遊戲 / 部門有獨立 sub-agent + 各自記憶，1 個 Slack 頻道 = 1 個 Agent (Note: OpenAB on Discord)</div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
這頁說明我們自己的 BQ Bot 不是孤例——官方文件有 262 則來自社群的真實案例，涵蓋 15 個分類。
Enterprise 分類有 9 則，Business Ops 有 16 則，都是真實的企業或團隊部署。
三個延伸場景：定時推報（現有 Bot 功能延伸）、會議記錄（可立即應用）、多遊戲 Chief of Staff（組織擴展的藍圖）。
-->
---
layout: default
---

# 實測①：Skill 自動成長追蹤

<div class="text-xs text-gray-500 mb-3"><code>hermes-self-improvement-log</code> 02:00 agent 自己 commit </div>

<ZoomImg src="/github-hermes-self-improvement-log.jpg">
  <img src="/github-hermes-self-improvement-log.jpg" class="rounded-lg border border-gray-300 w-full shadow-sm" style="max-height: 340px; object-fit: contain; object-position: left;" />
</ZoomImg>

<div class="mt-3 text-sm text-gray-600">
  部署後 repo <code>skills/</code>、<code>memories/</code>、<code>cron/</code> 三個資料夾由 agent 自行維護，<code>SOUL.md</code> 與 <code>config.yaml</code> 作為行為邊界。
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

---
layout: default
---

# 實測②：Agent 主動補寫技能記錄

<div class="text-xs text-gray-500 mb-3">一次 Slidev 部署任務結束後，agent 自動 patch <code>skills/software-development/slidev-authoring/SKILL.md</code> </div>

<ZoomImg src="/github-skill-md-diff.jpg">
  <img src="/github-skill-md-diff.jpg" class="rounded-lg border border-gray-300 w-full shadow-sm" style="max-height: 340px; object-fit: contain; object-position: left;" />
</ZoomImg>

<div class="mt-3 text-sm text-gray-600">
  它記下了「self-hosted runner 需要 IP allowlist」、「靜態資源要先 <code>git add</code>」這兩個坑——下次遇到同樣問題，agent 已經知道答案。
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

---
layout: default
---

# 實測③：Bot 回報任務完成

<div class="text-xs text-gray-500 mb-3">14/14 CI steps 通過，GitHub Pages 上線，agent 同時自動 patch SKILL.md </div>

<ZoomImg src="/telegram-deploy-success.jpg">
  <img src="/telegram-deploy-success.jpg" class="rounded-lg border border-gray-300 w-full shadow-sm" style="max-height: 340px; object-fit: contain; object-position: left;" />
</ZoomImg>

<div class="mt-3 text-sm text-gray-600">
  整個 CI/CD 流程的觸發、監控、回報都在 Telegram 完成；任務結束後 agent 自動做了一次 Skill 沉澱。
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

---
layout: default
---

# 實測④：Model 失敗時的回應

<div class="text-xs text-gray-500 mb-3">Free model provider 連線失敗</div>

<ZoomImg src="/telegram-model-provider-error.jpg">
  <img src="/telegram-model-provider-error.jpg" class="rounded-lg border border-gray-300 w-full shadow-sm" style="max-height: 340px; object-fit: contain; object-position: left;" />
</ZoomImg>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

---
layout: default
---

# 指令審批機制（Command Approval）

<div class="grid grid-cols-2 gap-6 mt-4">
  <div>
    <div class="text-xs text-gray-500 font-bold mb-3">三種審批模式（<span class="font-mono">approvals.mode</span>）+ cron 安全邊界</div>
    <div class="flex flex-col gap-2">
      <div class="flex items-center gap-3 p-2 border border-gray-300 rounded">
        <span class="shrink-0 px-2 py-0.5 bg-orange-500 text-white rounded text-xs font-mono font-bold">manual</span>
        <span class="text-xs text-gray-700">每次都手動確認（最安全，預設）</span>
      </div>
      <div class="flex items-center gap-3 p-2 border border-gray-300 rounded">
        <span class="shrink-0 px-2 py-0.5 bg-blue-500 text-white rounded text-xs font-mono font-bold">smart</span>
        <span class="text-xs text-gray-700">LLM 輔助判斷，低風險自動放行、高風險提示確認</span>
      </div>
      <div class="flex items-center gap-3 p-2 border border-gray-300 rounded">
        <span class="shrink-0 px-2 py-0.5 bg-red-600 text-white rounded text-xs font-mono font-bold">off</span>
        <span class="text-xs text-gray-700">等同 YOLO，跳過所有審批（不建議）</span>
      </div>
    </div>
  </div>
  <div class="flex flex-col gap-3 justify-center">
    <div class="p-2 bg-gray-50 border border-gray-300 rounded text-xs mb-1">
      <div class="font-bold text-gray-600 mb-1">模式 → 人機迴路對應</div>
      <div class="flex flex-col gap-1">
        <div class="flex items-center gap-2"><span class="font-mono text-orange-600 font-bold">manual</span><span class="text-gray-500">→</span><span class="text-gray-700">Human-<strong>in</strong>-the-loop（每次確認，最安全）</span></div>
        <div class="flex items-center gap-2"><span class="font-mono text-blue-600 font-bold">smart</span><span class="text-gray-500">→</span><span class="text-gray-700">Human-<strong>on</strong>-the-loop（LLM 初篩，高風險才提示）</span></div>
        <div class="flex items-center gap-2"><span class="font-mono text-red-600 font-bold">off</span><span class="text-gray-500">→</span><span class="text-gray-700">Human-<strong>out</strong>-of-the-loop（全自動，不建議）</span></div>
      </div>
    </div>
    <div class="p-3 bg-green-50 border border-green-300 rounded text-xs">
      ✅ <strong>企業導入建議：</strong><br>
      初期以 <span class="font-mono text-orange-600">manual</span> 模式上線，熟悉 Agent 行為後，再針對已知安全操作切換 <span class="font-mono text-blue-600">smart</span>；cron 排程建議維持 <span class="font-mono text-orange-600">manual</span>
    </div>
    <div class="p-3 bg-red-50 border border-red-300 rounded text-xs">
      ⚠️ <strong>避免：</strong>直接使用 <span class="font-mono text-red-600">off</span> 模式——跳過所有審批，等同開放本機執行權限
    </div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
指令審批是企業部署中最直接的安全控制點——決定 Agent 能做什麼。
三種模式對應三種人機迴路層次：manual（人在迴路）、smart（人在外圈）、off（全自動）。
與部署姿態互補：審批控制「哪些指令進來」，OS 邊界控制「執行後的爆炸半徑」。
兩者缺一不可：只有審批沒有隔離，AI 被繞過時無底線；只有隔離沒有審批，使用體驗差且難以追責。
-->
---
layout: default
---

# 評估結論

<div class="grid grid-cols-3 gap-4 mt-4">
  <div class="border border-green-600 rounded-lg p-4">
    <div class="font-bold text-green-700 mb-3 text-sm">它能做什麼？</div>
    <ul class="text-xs text-gray-700 space-y-2">
      <li>✅ 非技術人員自然語言查資料<br><span class="text-gray-400">（已驗證：遊戲營運 Bot）</span></li>
      <li>✅ 跨工具自動化重複性任務</li>
      <li>✅ 多 Agent 無人值守長任務</li>
      <li>✅ 各部門隔離的 AI 助理<br><span class="text-gray-400">（SOUL.md 行為控制）</span></li>
    </ul>
  </div>
  <div class="border border-yellow-600 rounded-lg p-4">
    <div class="font-bold text-yellow-700 mb-3 text-sm">資安風險如何？</div>
    <ul class="text-xs text-gray-700 space-y-2">
      <li>✅ CVE 相較於 OpenCalw 少很多</li>
      <li>⚠️ 進程內防護為啟發式，非真正隔離</li>
      <li>⚠️ 預設部署非最安全配置</li>
      <li>🟡 <strong>容器化後</strong>可接受部署於非高敏環境</li>
    </ul>
  </div>
  <div class="border border-blue-600 rounded-lg p-4">
    <div class="font-bold text-blue-700 mb-3 text-sm">下一步</div>
    <ul class="text-xs text-gray-700 space-y-2">
      <li>🎯 啟動 PoC 試用場景</li>
      <li>🐳 Docker 沙箱 + Gateway 白名單為基本前提</li>
      <li>📋 以遊戲營運查詢為起點，驗證業務場景</li>
      <li>🔒 確認資料治理策略後再擴大部署</li>
    </ul>
  </div>
</div>

<div class="mt-4 p-3 bg-gray-50 border border-gray-400 rounded-lg text-xs text-gray-700">
  <strong>MIT 授權・195K Stars・Python 技術能力前提</strong>——技術能力充足的前提下，列為內部 AI Agent 基礎框架候選，建議以容器隔離 + 白名單管控在非高敏環境啟動 PoC。
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
三欄直接回答評估的核心問題。
能做什麼：遊戲營運 Bot 是已驗證的場景，不是假設。
資安：定性是「成長中」——無 CVE、有誠實揭露，但需要企業主動配置，不能開箱即用。
下一步：PoC 門檻極低，NT$160 就能在真實業務場景驗證，沒有不試的理由。
-->

---
layout: default
---

# Claude 平台近期動向

<div class="text-xs text-gray-500 mb-4">2026 Q1–Q2 發布，與 Hermes Agent 應用場景高度重疊的功能方向</div>

<div class="grid grid-cols-2 gap-4 mt-2">
  <div class="border border-purple-300 rounded-lg p-4 bg-purple-50">
    <div class="font-bold text-purple-700 text-sm mb-2">💬 Claude Tag for Slack</div>
    <div class="text-xs text-gray-600 space-y-1">
      <div>在 Slack 頻道直接 @Claude 派任務</div>
      <div>跨頻道 context memory，async 任務回報</div>
      <div>Enterprise / Team 方案 beta</div>
    </div>
  </div>
  <div class="border border-blue-300 rounded-lg p-4 bg-blue-50">
    <div class="font-bold text-blue-700 text-sm mb-2">📱 Cowork + Dispatch</div>
    <div class="text-xs text-gray-600 space-y-1">
      <div>手機派任務 → 桌機執行，同一對話串跨裝置同步</div>
      <div>出門在外用手機發指令，回到座位無縫接手</div>
      <div>需同時開 Desktop app + 手機 app（Pro/Max）</div>
    </div>
  </div>
  <div class="border border-green-300 rounded-lg p-4 bg-green-50">
    <div class="font-bold text-green-700 text-sm mb-2">🖥️ Remote Control</div>
    <div class="text-xs text-gray-600 space-y-1">
      <div>手機透過 Claude 存取桌機的所有資源</div>
      <div>檔案、connector、plugin、computer use 全部可遙控</div>
      <div>桌機需保持開機且 app 在前景</div>
    </div>
  </div>
  <div class="border border-amber-300 rounded-lg p-4 bg-amber-50">
    <div class="font-bold text-amber-700 text-sm mb-2">🤖 Multi-agent Orchestration</div>
    <div class="text-xs text-gray-600 space-y-1">
      <div>Lead agent 拆解任務，sub-agent 平行執行</div>
      <div>Claude Finance：預建 10 個財務 agent</div>
      <div>Managed Agents 支援排程（cron）自動執行</div>
    </div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

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
  報告日期：2026.06.24
</div>
<div class="text-gray-600 mt-2 text-sm">
  Co-author：佳宏 — 技術評估與內容審閱
</div>
<div class="text-gray-600 mt-2 text-sm">
  Co-author：Hermes Agent — 協助投影片內容編修與自動化流程
</div>
<div class="text-gray-600 mt-2 text-sm">
  Co-author：Claude — 原始碼分析、資安風險審查、投影片內容編修
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
開放 Q&A。
如果有關於資安評估、PoC 規劃、或技術細節的問題，歡迎提出。
-->

---
layout: center
class: text-center
---
# Appendix

<div class="text-gray-400 mt-4 text-lg">技術細節與案例設定參考</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>
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
        <span>啟用 Docker terminal-backend（<code>terminal.backend: docker</code>）沙箱化 shell/file 輸出；注意 code-exec、MCP、Plugin/Skill 不在此範圍——需整程式容器化才能全覆蓋（見「部署姿態選擇」）</span>
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

<div class="grid grid-cols-2 gap-3 mt-3">
  <div class="p-2 bg-gray-50 border border-gray-300 rounded text-xs text-gray-700 flex items-center gap-3">
    <span class="font-bold whitespace-nowrap">資安成熟度：🟡 成長中</span>
    <span class="text-gray-500">誠實揭露防護邊界、有完整 Threat Model，但預設部署姿態非最安全——技術能力充足的企業在容器隔離後可部署，暫不建議高敏感生產環境以預設配置直接使用</span>
  </div>
  <div class="p-2 bg-blue-50 border border-blue-300 rounded text-xs text-blue-700">
    📬 <strong>負責任揭露：</strong><span class="font-mono">security@nousresearch.com</span><br>
    90 天揭露視窗；SECURITY.md 中有 PGP 金鑰
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
這頁是技術特色章節的資安總結，整合所有特色的風險面向。
重點一：沒有已知 CVE 是好消息；供應鏈風險是真實存在的，litellm 和 mistralai 都曾發生投毒，Hermes 的應對是內建 OSV-Scanner。
重點二：官方 SECURITY.md 自承，所有進程內機制（審批門、輸出編輯、模式掃描）都是「啟發式」，不是真正安全邊界。Docker terminal-backend 提供有意義但有限的隔離（只涵蓋 shell/file），整程式容器化才是完整邊界。
重點三：預設部署不是最安全配置，企業上線前必須主動啟用 Docker terminal-backend、設 Gateway 白名單、限制資源。
整體定位：比同類開源 AI Agent 框架更有資安自覺，但尚不到「企業開箱即用」的成熟度。
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
layout: default
---

# Promptware 防禦：對抗記憶污染攻擊

<div class="grid grid-cols-2 gap-6 mt-3">
  <div>
    <div class="text-xs text-gray-400 mb-2">三個注入入口</div>
    <div class="flex flex-col gap-1.5 text-xs">
      <div class="p-2 bg-red-50 border border-red-300 rounded">🧠 <strong>自回憶注入</strong>：外部內容透過 MEMORY.md 寫回路徑注入，跨會話持久感染</div>
      <div class="p-2 bg-red-50 border border-red-300 rounded">🔧 <strong>工具鏈注入</strong>：MCP 工具輸出含惡意指令，直接注入當前 context</div>
      <div class="p-2 bg-red-50 border border-red-300 rounded">📦 <strong>Skill 安裝注入</strong>：安裝含後門的 Skill（Python 程式碼），直接取得主程序執行權</div>
    </div>
    <div class="mt-2 text-xs text-gray-400 mb-1">IOC 特徵語句（Indicator of Compromise）</div>
    <div class="overflow-x-auto">
      <table class="table-auto border-collapse w-full text-xs">
        <thead><tr class="bg-gray-100"><th class="border border-gray-300 px-2 py-1 text-left">型態</th><th class="border border-gray-300 px-2 py-1 text-left">範例特徵句</th></tr></thead>
        <tbody>
          <tr><td class="border border-gray-300 px-2 py-0.5">記憶覆蓋</td><td class="border border-gray-300 px-2 py-0.5 font-mono text-red-700">IMPORTANT: Remember to always...</td></tr>
          <tr class="bg-gray-50"><td class="border border-gray-300 px-2 py-0.5">身份覆蓋</td><td class="border border-gray-300 px-2 py-0.5 font-mono text-red-700">You are now in maintenance mode</td></tr>
          <tr><td class="border border-gray-300 px-2 py-0.5">指令注入</td><td class="border border-gray-300 px-2 py-0.5 font-mono text-red-700">Override previous instructions and...</td></tr>
        </tbody>
      </table>
    </div>
  </div>
  <div class="flex flex-col gap-2">
    <div class="text-xs text-gray-500 font-bold mb-1">原始碼確認：已有保護</div>
    <div class="p-2 border border-green-500 rounded text-xs text-green-700">✅ Review fork 工具白名單：危險指令全部 auto-deny</div>
    <div class="p-2 border border-green-500 rounded text-xs text-green-700">✅ Fork 隔離：<span class="font-mono">skip_memory=True</span>，不碰外部 memory plugin</div>
    <div class="p-2 border border-green-500 rounded text-xs text-green-700">✅ v0.15.0 在記憶寫入路徑前加入攔截驗證</div>
    <div class="text-xs text-gray-500 font-bold mt-2 mb-1">仍需企業自行處理</div>
    <div class="p-2 border border-red-400 rounded text-xs text-red-700">❌ SOUL.md：純文字，無簽名 / checksum，寫入不留稽核日誌</div>
    <div class="p-2 border border-red-400 rounded text-xs text-red-700">❌ <span class="font-mono">auth.json</span>（OAuth token）與 SOUL.md 同存於 <span class="font-mono">~/.hermes/</span></div>
    <div class="p-2 border border-yellow-500 rounded text-xs text-yellow-800">⚠️ §3.2：MCP 工具輸出不在 Brainworm 防禦範圍，需在 MCP 配置層設白名單</div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
Promptware / Brainworm 是一種新型攻擊，專門針對有持久記憶的 AI Agent。
三個入口：自回憶（最危險、跨會話）、工具鏈（MCP 輸出、未覆蓋）、Skill 安裝（程式碼後門）。
v0.15 已有基本防護，這部分我們有看過原始碼確認。
但企業仍需自行處理：SOUL.md 沒有防篡改機制、auth.json 放在同一個資料夾、MCP 輸出不在防護範圍。
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
      → 可納入 Git 版控、PR review、CI/CD
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

# session_search：把不該用 LLM 的活還給 SQLite

<div class="text-xs text-gray-500 mb-3">跨對話召回不靠 LLM 生成——直接查索引，快 4500 倍</div>

<div class="overflow-x-auto">
  <table class="table-auto border-collapse w-full text-xs">
    <thead>
      <tr class="bg-gray-100">
        <th class="border border-gray-300 px-2 py-1.5 text-center">模式</th>
        <th class="border border-gray-300 px-2 py-1.5 text-left">說明</th>
        <th class="border border-gray-300 px-2 py-1.5 text-left">典型用途</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="border border-gray-300 px-2 py-1.5 text-center font-mono font-bold text-blue-600">DISCOVERY</td>
        <td class="border border-gray-300 px-2 py-1.5">列出所有歷史對話索引</td>
        <td class="border border-gray-300 px-2 py-1.5">瀏覽有哪些過去的工作</td>
      </tr>
      <tr class="bg-gray-50">
        <td class="border border-gray-300 px-2 py-1.5 text-center font-mono font-bold text-blue-600">SCROLL</td>
        <td class="border border-gray-300 px-2 py-1.5">按時間線瀏覽對話片段</td>
        <td class="border border-gray-300 px-2 py-1.5">「找上週同一時間做的事」</td>
      </tr>
      <tr>
        <td class="border border-gray-300 px-2 py-1.5 text-center font-mono font-bold text-blue-600">READ</td>
        <td class="border border-gray-300 px-2 py-1.5">全文搜尋 + FTS5 索引精確召回</td>
        <td class="border border-gray-300 px-2 py-1.5">「找所有提到 BigQuery 的對話」</td>
      </tr>
      <tr class="bg-gray-50">
        <td class="border border-gray-300 px-2 py-1.5 text-center font-mono font-bold text-blue-600">BROWSE</td>
        <td class="border border-gray-300 px-2 py-1.5">語意向量搜尋（近義召回）</td>
        <td class="border border-gray-300 px-2 py-1.5">「找所有類似這次報表任務的對話」</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="grid grid-cols-2 gap-3 mt-3">
  <div class="p-3 bg-green-50 border border-green-300 rounded text-xs text-green-800">
    🚀 <strong>4500x 加速：</strong>SQLite FTS5 全文索引比 LLM 召回快 4500 倍，且結果確定性更高——查「BigQuery」一定找到包含這個詞的對話，不會有 LLM 幻覺
  </div>
  <div class="p-3 bg-blue-50 border border-blue-300 rounded text-xs text-blue-700">
    🧠 <strong>設計哲學：</strong>「不該讓 LLM 做的事，就不要讓 LLM 做」——記憶搜尋是確定性問題，用確定性工具（SQLite）解，省 Token 又可靠
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
session_search 是 Hermes 記憶架構中最低調但最有技術含量的設計決策之一。
四種模式覆蓋了不同的召回需求：從按時間瀏覽到語意搜尋。
4500x 加速不是誇大——SQLite FTS5 全文索引的搜尋速度遠超 LLM 生成，而且結果可重現、無幻覺。
設計哲學：只有需要「理解」才用 LLM；「搜尋」是確定性問題，用確定性工具。
-->
---
layout: default
---

# 八種協作模式：從 1 個 Bot 到 50 個 Agent

<div class="text-xs text-gray-500 mb-1">橙皮書 §17 — 依複雜度由低到高，按卡片控成本</div>

<table class="table-auto border-collapse w-full text-xs">
  <thead>
    <tr class="bg-gray-100">
      <th class="border border-gray-300 px-2 py-0.5 text-center">模式</th>
      <th class="border border-gray-300 px-2 py-0.5 text-left">說明</th>
      <th class="border border-gray-300 px-2 py-0.5 text-center">Agent 數</th>
      <th class="border border-gray-300 px-2 py-0.5 text-left">適用場景</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="border border-gray-300 px-2 py-0.5 text-center font-mono font-bold text-blue-600">P1</td>
      <td class="border border-gray-300 px-2 py-0.5">單 Agent 直接執行</td>
      <td class="border border-gray-300 px-2 py-0.5 text-center">1</td>
      <td class="border border-gray-300 px-2 py-0.5">查詢、單步任務（⚠️ Fan-out 慎用）</td>
    </tr>
    <tr class="bg-gray-50">
      <td class="border border-gray-300 px-2 py-0.5 text-center font-mono font-bold text-blue-600">P2</td>
      <td class="border border-gray-300 px-2 py-0.5">主 + 子 Agent 串行</td>
      <td class="border border-gray-300 px-2 py-0.5 text-center">2–5</td>
      <td class="border border-gray-300 px-2 py-0.5">多步驟、跨工具自動化（現有 BQ Bot 約此層）</td>
    </tr>
    <tr>
      <td class="border border-gray-300 px-2 py-0.5 text-center font-mono font-bold text-blue-600">P3</td>
      <td class="border border-gray-300 px-2 py-0.5">Pipeline 流水線</td>
      <td class="border border-gray-300 px-2 py-0.5 text-center">3–8</td>
      <td class="border border-gray-300 px-2 py-0.5">資料清洗、報告生成流程</td>
    </tr>
    <tr class="bg-gray-50">
      <td class="border border-gray-300 px-2 py-0.5 text-center font-mono font-bold text-blue-600">P4</td>
      <td class="border border-gray-300 px-2 py-0.5">Review 審核迴圈</td>
      <td class="border border-gray-300 px-2 py-0.5 text-center">2–4</td>
      <td class="border border-gray-300 px-2 py-0.5">需要品質把關的內容生成</td>
    </tr>
    <tr>
      <td class="border border-gray-300 px-2 py-0.5 text-center font-mono font-bold text-purple-600">P5</td>
      <td class="border border-gray-300 px-2 py-0.5">Fan-out 並行</td>
      <td class="border border-gray-300 px-2 py-0.5 text-center">5–20</td>
      <td class="border border-gray-300 px-2 py-0.5">大量同質任務並行處理</td>
    </tr>
    <tr class="bg-gray-50">
      <td class="border border-gray-300 px-2 py-0.5 text-center font-mono font-bold text-purple-600">P6</td>
      <td class="border border-gray-300 px-2 py-0.5">Kanban 自癒看板</td>
      <td class="border border-gray-300 px-2 py-0.5 text-center">5–15</td>
      <td class="border border-gray-300 px-2 py-0.5">無人值守長任務（已有 Multi-agent Kanban 頁）</td>
    </tr>
    <tr>
      <td class="border border-gray-300 px-2 py-0.5 text-center font-mono font-bold text-orange-600">P7</td>
      <td class="border border-gray-300 px-2 py-0.5">Chief of Staff 架構</td>
      <td class="border border-gray-300 px-2 py-0.5 text-center">10–30</td>
      <td class="border border-gray-300 px-2 py-0.5">跨部門多遊戲統覽（社群案例）</td>
    </tr>
    <tr class="bg-gray-50">
      <td class="border border-gray-300 px-2 py-0.5 text-center font-mono font-bold text-orange-600">P8</td>
      <td class="border border-gray-300 px-2 py-0.5">全自主 Agent 網絡</td>
      <td class="border border-gray-300 px-2 py-0.5 text-center">20–50+</td>
      <td class="border border-gray-300 px-2 py-0.5">高度自動化企業流程（需充分 PoC 驗證）</td>
    </tr>
  </tbody>
</table>

<div class="grid grid-cols-2 gap-2 mt-2">
  <div class="p-1.5 bg-blue-50 border border-blue-300 rounded text-xs text-blue-700">
    💰 <strong>按卡片控成本：</strong>每個子 Agent 是一張 Kanban 卡片，Token 消耗可追蹤；從 P2 開始試點，確認成本效益後再升級模式
  </div>
  <div class="p-1.5 bg-orange-50 border border-orange-400 rounded text-xs text-orange-800">
    ⚠️ <strong>P1 Fan-out 警告：</strong>P1 單 Agent 若被用於大量 Fan-out 任務，Token 消耗會爆炸性增長；Fan-out 場景應選 P5 並設資源上限
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
橙皮書 §17 定義了八種協作模式，從最簡單的單 Agent 到 50+ Agent 的全自主網絡。
關鍵概念：每升一個模式，複雜度和成本都會顯著上升——不是越複雜越好，而是找到適合場景的最低複雜度模式。
對我們自己的案例定位：現有的遊戲營運 BQ Bot 大約在 P2 層，已經能解決核心問題。
升級到 P7 的時機：當需要跨多個遊戲或部門統覽時，才需要 Chief of Staff 架構。
P1 Fan-out 警告很重要：很多初次使用者的直覺是「有 Agent 就派更多出去」，但 Token 消耗是線性疊加的。
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
重要的業務口徑：BQDate 是 partition 欄位，每次查詢都必須指定，否則費用爆炸。
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
左右兩張的差異：DAU 需要 NOT IN GameAccount 排除員工；營收不需要——這個口徑差異就靠範例 SQL 的註解傳達給 Bot。
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
通算金幣的公式（Coin + 25000 × Gem）是特別非直覺的業務規則，這種知識最需要明確告訴 Bot。
通算金幣的公式（Coin + 25000 × Gem）是特別非直覺的業務規則，這種知識最需要明確告訴 Bot。
-->
---
layout: default
---

## 架構解析 — 三層設計

```mermaid {scale: 0.75}
flowchart TB
    subgraph IF["① 介面層"]
        direction TB
        cli["CLI / TUI"]
        msg["Telegram / Discord\nSlack / WhatsApp"]
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
        local["Local / Docker / SSH"]
        cloud["Modal / Singularity\nGPU 叢集"]
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

## 部署彈性 — 從個人到企業規模

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

# Curator 四道剎車：防止自改進失控

<div class="grid grid-cols-2 gap-6 mt-4">
  <div>
    <div class="text-xs text-gray-500 font-bold mb-3">四個抑制層，回答企業最擔心的事</div>
    <div class="flex flex-col gap-2">
      <div class="flex items-center gap-3 p-2 border border-gray-300 rounded">
        <span class="shrink-0 px-2 py-0.5 bg-gray-700 text-white rounded text-xs font-mono font-bold">01</span>
        <span class="text-xs text-gray-700">閒置觸發：<span class="font-mono">min_idle_hours</span> 設下限，不會剛學完就清理</span>
      </div>
      <div class="flex items-center gap-3 p-2 border border-gray-300 rounded">
        <span class="shrink-0 px-2 py-0.5 bg-gray-700 text-white rounded text-xs font-mono font-bold">02</span>
        <span class="text-xs text-gray-700">逾時歸檔：<span class="font-mono">archive_after_days</span> 強制封存，不隨意刪除</span>
      </div>
      <div class="flex items-center gap-3 p-2 border border-gray-300 rounded">
        <span class="shrink-0 px-2 py-0.5 bg-gray-700 text-white rounded text-xs font-mono font-bold">03</span>
        <span class="text-xs text-gray-700">版本保留：<span class="font-mono">backup.keep</span> 最多保留 5 份，可 rollback</span>
      </div>
      <div class="flex items-center gap-3 p-2 border border-gray-300 rounded">
        <span class="shrink-0 px-2 py-0.5 bg-gray-700 text-white rounded text-xs font-mono font-bold">04</span>
        <span class="text-xs text-gray-700">最小閾值：<span class="font-mono">stale_after_days</span> 過了才視為過期</span>
      </div>
    </div>
  </div>
  <div class="flex flex-col gap-3 justify-center">
    <div class="p-3 bg-green-50 border border-green-300 rounded text-xs">
      ✅ **每個參數都可配置**，企業可依法規要求（金融、醫療）調高保留天數。
    </div>
    <div class="p-3 bg-blue-50 border border-blue-300 rounded text-xs">
      💡 **與 Promptware 對齊**：自改進不是單靠「自動學習」，而是「自動學習 + 自動治理」。
    </div>
    <div class="p-3 bg-red-50 border border-red-300 rounded text-xs">
      ⚠️ 企業注意：四個閾值預設值未必符合所有產業，導入前應 review config.yaml。
    </div>
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>
---
layout: default
---

# Curator 四道剎車（續）— 參數對照表

<div class="overflow-x-auto">
  <table class="table-auto border-collapse w-full text-xs">
    <thead>
      <tr class="bg-gray-100">
        <th class="border border-gray-300 px-2 py-1 text-left">參數</th>
        <th class="border border-gray-300 px-2 py-1 text-left">預設值</th>
        <th class="border border-gray-300 px-2 py-1 text-left">用途</th>
        <th class="border border-gray-300 px-2 py-1 text-left">企業調校建議</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="border border-gray-300 px-2 py-1 font-mono">min_idle_hours</td>
        <td class="border border-gray-300 px-2 py-1">2</td>
        <td class="border border-gray-300 px-2 py-1">多久沒用才視為閒置</td>
        <td class="border border-gray-300 px-2 py-1">金融/醫療調高至 24</td>
      </tr>
      <tr>
        <td class="border border-gray-300 px-2 py-1 font-mono">interval_hours</td>
        <td class="border border-gray-300 px-2 py-1">168</td>
        <td class="border border-gray-300 px-2 py-1">Curator daemon 執行頻率</td>
        <td class="border border-gray-300 px-2 py-1">嚴格環境調低（每 24h）</td>
      </tr>
      <tr>
        <td class="border border-gray-300 px-2 py-1 font-mono">stale_after_days</td>
        <td class="border border-gray-300 px-2 py-1">30</td>
        <td class="border border-gray-300 px-2 py-1">多少天沒更新標記為過期</td>
        <td class="border border-gray-300 px-2 py-1">快速變動領域調低至 14</td>
      </tr>
      <tr>
        <td class="border border-gray-300 px-2 py-1 font-mono">archive_after_days</td>
        <td class="border border-gray-300 px-2 py-1">90</td>
        <td class="border border-gray-300 px-2 py-1">過期多久強制封存</td>
        <td class="border border-gray-300 px-2 py-1">法規要求調低至 30 或不归档</td>
      </tr>
      <tr>
        <td class="border border-gray-300 px-2 py-1 font-mono">backup.keep</td>
        <td class="border border-gray-300 px-2 py-1">5</td>
        <td class="border border-gray-300 px-2 py-1">最多保留備份份數</td>
        <td class="border border-gray-300 px-2 py-1">依磁碟空間調整，不可為 0</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="mt-3 p-2 bg-gray-100 rounded text-xs text-gray-600">
  資料來源：hermes_agent/hermes-agent/hermes_cli/config.py 段落 <span class="font-mono">curator.</span>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>
---
layout: default
---

# 以 OS 為邊界：部署姿態選擇

<div class="text-xs text-gray-500 mb-3">Docker terminal-backend ≠ 全程式沙箱——各部署姿態的實際隔離範圍對照</div>

<div class="overflow-x-auto">
  <table class="table-auto border-collapse w-full text-xs">
    <thead>
      <tr class="bg-gray-100">
        <th class="border border-gray-300 px-3 py-2 text-left">Agent 執行的動作</th>
        <th class="border border-gray-300 px-3 py-2 text-center">Local backend<br><span class="text-gray-400 font-normal">預設</span></th>
        <th class="border border-gray-300 px-3 py-2 text-center">Docker terminal-backend<br><span class="text-gray-400 font-normal">官方推薦</span></th>
        <th class="border border-gray-300 px-3 py-2 text-center">整程式容器化<br><span class="text-gray-400 font-normal">進階</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="border border-gray-300 px-3 py-2">Shell / file 指令（刪檔、跑腳本）</td>
        <td class="border border-gray-300 px-3 py-2 text-center text-red-600">直接在主機</td>
        <td class="border border-gray-300 px-3 py-2 text-center text-green-600">容器內（隔離）</td>
        <td class="border border-gray-300 px-3 py-2 text-center text-green-600">容器內（隔離）</td>
      </tr>
      <tr class="bg-gray-50">
        <td class="border border-gray-300 px-3 py-2">Code-exec 執行環境</td>
        <td class="border border-gray-300 px-3 py-2 text-center text-red-600">直接在主機</td>
        <td class="border border-gray-300 px-3 py-2 text-center text-red-600">直接在主機</td>
        <td class="border border-gray-300 px-3 py-2 text-center text-green-600">容器內（隔離）</td>
      </tr>
      <tr>
        <td class="border border-gray-300 px-3 py-2">MCP 工具 / Plugin / Skill</td>
        <td class="border border-gray-300 px-3 py-2 text-center text-red-600">直接在主機</td>
        <td class="border border-gray-300 px-3 py-2 text-center text-red-600">直接在主機</td>
        <td class="border border-gray-300 px-3 py-2 text-center text-green-600">容器內（隔離）</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="grid grid-cols-2 gap-4 mt-3">
  <div class="p-2 bg-yellow-50 border border-yellow-400 rounded text-xs text-yellow-800">
    ⚠️ <strong>SECURITY.md §2.2：</strong>「terminal-backend Docker only wraps shell/file tool outputs」——MCP、Plugin、Skill 仍在主機環境執行
  </div>
  <div class="p-2 bg-blue-50 border border-blue-300 rounded text-xs text-blue-700">
    💡 <strong>進階參考：</strong>NVIDIA OpenShell 以整程式容器化實現最嚴格隔離；適合高敏感生產環境，運維複雜度較高
  </div>
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
補充說明給技術受眾：Docker terminal-backend 只沙箱化 shell 和 file tool 的輸出。
Hermes 主程序、MCP 子程序、Plugin 和 Skill，仍然在主機環境執行。
整程式容器化才能真正全包，但需要自行搭建環境（docker-compose 或 k8s）。
-->
