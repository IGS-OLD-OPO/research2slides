#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('decks/hermes-agent/slides.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Split into blocks on --- separators (not inside code blocks)
blocks = []
current = []
in_code = False
for line in content.split('\n'):
    if line.strip().startswith('```'):
        in_code = not in_code
    if not in_code and line.strip() == '---':
        blocks.append('\n'.join(current))
        current = []
    else:
        current.append(line)
if current:
    blocks.append('\n'.join(current))

# --- Modify Cover to add Hermes origin subtitle ---
blocks[2] = blocks[2].replace(
    '### 自我改進 AI Agent 框架技術評估',
    '### 自我改進 AI Agent 框架技術評估\n\n<div class="text-sm text-gray-300 mt-1">\n  命名自希臘神話赫爾墨斯（Hermēs）——眾神信使，穿梭邊界、傳遞訊息\n</div>'
)

# --- New evaluation roadmap slide (replaces P6) ---
roadmap_fm = 'layout: default'
roadmap_content = '''# 評估路線圖

<div class="text-xs text-gray-500 mb-4">本報告圍繞 5 個企業導入評估要點展開，每個面向皆有原始碼或實測佐證</div>

<div class="grid grid-cols-5 gap-3 mt-2">
  <div class="border border-blue-400 rounded-lg p-3 bg-blue-50">
    <div class="font-bold text-blue-700 text-sm mb-2">🧠 Skill 沉澱</div>
    <div class="text-xs text-gray-600 space-y-1">
      <div>Learning Loop</div>
      <div>三態生命週期</div>
      <div>負面學習黑名單</div>
    </div>
  </div>
  <div class="border border-purple-400 rounded-lg p-3 bg-purple-50">
    <div class="font-bold text-purple-700 text-sm mb-2">💾 長期記憶</div>
    <div class="text-xs text-gray-600 space-y-1">
      <div>三層記憶架構</div>
      <div>session_search</div>
      <div>Honcho 整合</div>
    </div>
  </div>
  <div class="border border-green-400 rounded-lg p-3 bg-green-50">
    <div class="font-bold text-green-700 text-sm mb-2">💰 Token 成本</div>
    <div class="text-xs text-gray-600 space-y-1">
      <div>多模型路由</div>
      <div>5 天實測用量</div>
      <div>成本估算</div>
    </div>
  </div>
  <div class="border border-amber-400 rounded-lg p-3 bg-amber-50">
    <div class="font-bold text-amber-700 text-sm mb-2">🎯 應用場景</div>
    <div class="text-xs text-gray-600 space-y-1">
      <div>八種協作模式</div>
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

<div class="mt-5 p-3 bg-gray-50 border border-gray-300 rounded text-xs text-gray-600 text-center">
  受眾：企業 IT / 技術決策者　・　目標：評估 Hermes Agent 是否值得導入，以及在什麼條件下導入
</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>

<!--
這份報告的五個評估維度是根據企業導入 AI Agent 的核心顧慮設計的。
接下來每個面向都有 2-3 頁深入說明，包含原始碼確認和實測數據。
-->'''

# --- Clean appendix title ---
appendix_fm = 'layout: center\nclass: text-center'
appendix_content = '''# Appendix

<div class="text-gray-400 mt-4 text-lg">技術細節與案例設定參考</div>

<div class="absolute bottom-4 right-4 text-sm text-gray-500"><SlideCurrentNo /> / <SlidesTotal /></div>'''

# --- Build new block sequence ---
# Format: each entry is a list of blocks to include consecutively
# [fm_block, content_block] for normal slides
# [content_block] for no-frontmatter slides (like the case study separator)
# ['<string>', '<string>'] for new slides

selected = [
    # === COVER (global fm + modified cover content) ===
    blocks[1], blocks[2],

    # === P3 専案概覽 ===
    blocks[5], blocks[6],

    # === NEW: Evaluation roadmap ===
    roadmap_fm, roadmap_content,

    # === Skill section ===
    blocks[13], blocks[14],   # P7 Learning Loop
    blocks[15], blocks[16],   # P8 Skill 生命週期
    blocks[17], blocks[18],   # P9 負面學習

    # === Memory section ===
    blocks[21], blocks[22],   # P11 三層記憶
    blocks[23], blocks[24],   # P12 session_search

    # === Token section (P4 moved here as context) ===
    blocks[7],  blocks[8],    # P4 多模型支援 (moved from opening)
    blocks[39], blocks[40],   # P20 Token 消耗

    # === Use-case section ===
    blocks[9],  blocks[10],   # P5 多平台整合 (moved here)
    blocks[41], blocks[42],   # P21 適用場景 vs 不適用
    blocks[43], blocks[44],   # P22 chapter break 實際落地案例
    blocks[51], blocks[52],   # P26 八種協作模式 (moved before Bot)
    blocks[45], blocks[46],   # P23 遊戲營運 Bot
    blocks[47], blocks[48],   # P24 資料準備
    blocks[49], blocks[50],   # P25 社群驗證

    # === Security section (moved to end, before conclusion) ===
    blocks[19], blocks[20],   # P10 SOUL.md (moved from after negative learning)
    blocks[25], blocks[26],   # P13 Promptware
    blocks[35], blocks[36],   # P18 指令審批機制
    blocks[33], blocks[34],   # P17 企業可靠性
    blocks[37], blocks[38],   # P19 資安全貌

    # === Conclusion ===
    blocks[53], blocks[54],   # P27 評估結論
    blocks[55], blocks[56],   # P28 資料來源
    blocks[57], blocks[58],   # P29 謝謝

    # === Appendix ===
    appendix_fm, appendix_content,   # Clean appendix title
    blocks[27], blocks[28],   # P14 Kanban (moved to appendix)
    blocks[29], blocks[30],   # P15 Tool Gateway (moved to appendix)
    blocks[31], blocks[32],   # P16 Plugin (moved to appendix)
    blocks[61],               # "案例實作細節參考" separator (no frontmatter)
    blocks[62], blocks[63],   # App DailyUserInfoSnapshot
    blocks[64], blocks[65],   # App 歷史 Query
    blocks[66], blocks[67],   # App 一般營運知識
    blocks[68], blocks[69],   # App 附錄C 架構解析三層
    blocks[70], blocks[71],   # App 附錄B 部署彈性
    blocks[72], blocks[73],   # App 架構解析 Runtime Modes
    blocks[74], blocks[75],   # App Curator 四道剎車
    blocks[76], blocks[77],   # App Curator 四道剎車（續）
    blocks[78], blocks[79],   # App 以 OS 為邊界
]

# Reconstruct: first block is global frontmatter, no leading blank needed
# Reconstruction: '---\n' + '\n---\n'.join(selected)
result = '---\n' + '\n---\n'.join(selected)

with open('decks/hermes-agent/slides.md', 'w', encoding='utf-8', newline='\n') as f:
    f.write(result)

print('Done! slides.md rewritten.')
print(f'Selected blocks: {len(selected)}')
print(f'Output size: {len(result)} chars')
