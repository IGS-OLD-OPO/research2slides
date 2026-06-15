---
theme: seriph
background: https://cover.sli.dev
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
transition: slide-left
title: <!-- 工具名稱 --> 技術評估
mdc: true
---

# <!-- 工具名稱 -->

### <!-- 一句話定位 -->

<div class="pt-12 text-gray-200">
  <!-- 開發方 --> ・ 技術評估報告 ・ <!-- YYYY.MM.DD -->
</div>

---
layout: two-cols
---

# 專案概覽

<v-clicks>

- **名稱**：<!-- 工具名稱 -->
- **開發方**：<!-- 開發方 -->
- **授權**：<!-- 授權類型 -->
- **定位**：<!-- 官方定位一句話 -->
- **主要語言**：<!-- 語言 %>

</v-clicks>

::right::

<div class="flex flex-col gap-6 mt-8 ml-8 text-center">
  <div>
    <div class="text-5xl font-bold text-blue-600"><!-- Stars --></div>
    <div class="text-gray-600 text-sm mt-1">GitHub Stars</div>
  </div>
  <div>
    <div class="text-5xl font-bold text-green-600"><!-- Forks --></div>
    <div class="text-gray-600 text-sm mt-1">Forks</div>
  </div>
  <div>
    <div class="text-5xl font-bold text-purple-600"><!-- Contributors --></div>
    <div class="text-gray-600 text-sm mt-1">Contributors</div>
  </div>
</div>

---
layout: default
---

# 核心特色

<div class="grid grid-cols-3 gap-4">
  <div class="border border-gray-400 rounded-lg p-4">
    <div class="text-3xl mb-3"><!-- emoji --></div>
    <strong><!-- 特色 1 --></strong>
    <p class="text-sm text-gray-700 mt-2"><!-- 說明 --></p>
  </div>
  <div class="border border-gray-400 rounded-lg p-4">
    <div class="text-3xl mb-3"><!-- emoji --></div>
    <strong><!-- 特色 2 --></strong>
    <p class="text-sm text-gray-700 mt-2"><!-- 說明 --></p>
  </div>
  <div class="border border-gray-400 rounded-lg p-4">
    <div class="text-3xl mb-3"><!-- emoji --></div>
    <strong><!-- 特色 3 --></strong>
    <p class="text-sm text-gray-700 mt-2"><!-- 說明 --></p>
  </div>
</div>

---
layout: default
---

# 架構解析

<div class="grid grid-cols-2 gap-8">
  <div>

```
<!-- 工具名稱 -->/
├── <!-- 模組 1 -->   # <!-- 說明 -->
├── <!-- 模組 2 -->   # <!-- 說明 -->
└── <!-- 模組 3 -->   # <!-- 說明 -->
```

  </div>
  <div class="flex flex-col gap-3 justify-center text-sm text-white">
    <div class="p-3 bg-gray-800 rounded"><!-- 技術棧 1 --></div>
    <div class="p-3 bg-gray-800 rounded"><!-- 技術棧 2 --></div>
    <div class="p-3 bg-gray-800 rounded"><!-- 技術棧 3 --></div>
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
      <li><!-- 優勢 1 --></li>
      <li><!-- 優勢 2 --></li>
      <li><!-- 優勢 3 --></li>
    </ul>
  </div>
  <div class="border border-yellow-700 rounded-lg p-5">
    <h3 class="text-yellow-700 mb-3">⚠️ 注意事項</h3>
    <ul class="space-y-2 text-sm">
      <li><!-- 注意 1 --></li>
      <li><!-- 注意 2 --></li>
      <li><!-- 注意 3 --></li>
    </ul>
  </div>
</div>

<div class="mt-5 p-4 bg-blue-900 bg-opacity-40 rounded-lg border border-blue-600">
  <span class="text-white">🎯 <strong>建議：</strong><!-- 一句話建議 --></span>
</div>

---
layout: center
class: text-center
---

# 謝謝

<div class="text-gray-600 mt-4 text-sm">
  資料來源：github.com/<!-- org/repo --><br>
  報告日期：<!-- YYYY.MM.DD -->
</div>
