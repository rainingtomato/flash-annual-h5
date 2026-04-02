<template>
  <div ref="rootEl">
    <p class="module-title">商家建联进度</p>
    <p class="module-subtitle">
      2025年建联商家目标 <span class="highlight">40</span> 家，截止12月31日建联 <span class="highlight">40</span> 家，目标达成！
    </p>

    <!-- 数据网格区 -->
    <div class="stats-grid" style="margin-top:12px">
      <!-- 第一行：2列（5:6 比例） -->
      <div class="grid-row grid-2">
        <div
          v-for="(item, idx) in stats.slice(0, 2)"
          :key="item.label"
          class="stat-card"
          :class="{ 'card-highlight': item.highlight, [`card-col-${idx}`]: true }"
        >
          <div class="stat-label">{{ item.label }}</div>
          <div class="stat-num-row">
            <span class="stat-num" :ref="el => { if (el) numEls[idx] = el }">0</span>
            <span class="stat-unit">{{ item.unit }}</span>
          </div>
          <div class="stat-desc">{{ item.desc }}</div>
          <!-- 建联商家卡片装饰切图 -->
          <img
            v-if="idx === 0"
            src="https://s3plus.meituan.net/mcopilot-pub/copilot/chat/assets/9af1731216b2bdcc8b863b6390c04b8b.png"
            class="card-deco-img"
          />
        </div>
      </div>

      <!-- 第二行：3列（7:5:5 比例） -->
      <div class="grid-row grid-3">
        <div
          v-for="(item, idx) in stats.slice(2)"
          :key="item.label"
          class="stat-card"
          :class="[`card-row2-${idx}`]"
        >
          <div class="stat-label">{{ item.label }}</div>
          <div class="stat-num-row">
            <span class="stat-num" :ref="el => { if (el) numEls[idx + 2] = el }">0</span>
            <span class="stat-unit">{{ item.unit }}</span>
          </div>
          <div class="stat-desc">{{ item.desc }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted } from 'vue'

const rootEl = ref(null)
const numEls = reactive([])

const stats = [
  { label: '建联商家数量',     num: 40,  unit: '家',  desc: '覆盖闪购全部一级品类，分散在全国10个城市', highlight: true },
  { label: '线下拜访人次',     num: 115, unit: '人次', desc: '最多拜访次数："小柴购"承接3次\n最多拜访人次："小米"承接10人次' },
  { label: '共振群维护商家数量', num: 23,  unit: '个',  desc: '活跃度前三名：小柴购-鹏哥、小鹿驾到-良哥、小米-楠丁老师' },
  { label: '商家拜访记录',     num: 22,  unit: '篇',  desc: '浏览次数最多的是《拜访记录-酒易淘》（88次）' },
  { label: '商家端周报',       num: 16,  unit: '篇',  desc: '同步闪购平台规则26条，产品功能迭代24条' },
]

function easeOut(t) {
  return 1 - Math.pow(1 - t, 3)
}

function countUp(el, target, duration = 1000) {
  const start = performance.now()
  function frame(now) {
    const elapsed = now - start
    const progress = Math.min(elapsed / duration, 1)
    el.textContent = Math.round(easeOut(progress) * target)
    if (progress < 1) requestAnimationFrame(frame)
  }
  requestAnimationFrame(frame)
}

let observer = null

onMounted(() => {
  observer = new IntersectionObserver(
    (entries) => {
      if (entries[0].isIntersecting) {
        stats.forEach((item, idx) => {
          const el = numEls[idx]
          if (el) countUp(el, item.num, 1000)
        })
        observer.disconnect()
      }
    },
    { threshold: 0.2 }
  )
  if (rootEl.value) observer.observe(rootEl.value)
})

onUnmounted(() => {
  if (observer) observer.disconnect()
})
</script>

<style scoped>
.grid-row {
  display: grid;
  gap: 6px;
}

/* 第一行：建联商家(5) : 线下拜访(6) */
.grid-2 {
  grid-template-columns: 5fr 6fr;
}

/* 第二行：共振群(6) : 拜访记录(5) : 周报(5) */
.grid-3 {
  grid-template-columns: 7fr 5fr 5fr;
  margin-top: 6px;
}

/* 通用卡片 */
.stat-card {
  background: #F9F9F9;
  border-radius: 8px;
  padding: 10px;
  position: relative;
  overflow: hidden;
}

/* 建联商家卡片装饰切图 */
.card-deco-img {
  position: absolute;
  right: 0;
  bottom: 0;
  width: 88px;
  height: 88px;
  pointer-events: none;
}

.stat-card.card-highlight {
  background: #FFF3E0;
}

.stat-label {
  font-size: 12px;
  color: #888;
  margin-bottom: 6px;
}

.stat-num-row {
  display: flex;
  align-items: baseline;
  gap: 4px;
}

.stat-num {
  font-size: 22px;
  font-weight: 1000;
  color: #1A1A1A;
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

.stat-unit {
  font-size: 14px;
  color: #666;
  margin-left: 2px;
}

.stat-desc {
  font-size: 11px;
  color: #999;
  margin-top: 6px;
  line-height: 1.6;
  white-space: pre-line;
}
</style>
