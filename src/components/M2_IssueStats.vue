<template>
  <div ref="rootEl">
    <!-- 标题 -->
    <p class="module-title">重点问题解决情况</p>

    <!-- 副标题 -->
    <p class="module-subtitle">
      2025年重点问题总计 <span class="highlight">110个</span>，目标解决率 <span class="highlight">50%</span>，截止12月31日，重点问题解决率 <span class="highlight">50.9%</span>，目标达成！
    </p>

    <!-- 条形图列表 -->
    <div class="bar-list">
      <div
        v-for="(item, index) in categories"
        :key="item.name"
        class="bar-row"
      >
        <!-- 左侧：名称 + 数量 -->
        <div class="bar-label" :class="{ 'is-highlight': item.highlight }">
          {{ item.name }} {{ item.count }}个
        </div>

        <!-- 中间：进度条 -->
        <div class="bar-track">
          <div
            class="bar-fill"
            :class="item.rate >= 100 ? 'fill-orange' : 'fill-gray'"
            :ref="el => { if (el) fillEls[index] = el }"
          ></div>
        </div>

        <!-- 右侧：百分比 -->
        <div class="bar-rate" :class="{ 'rate-orange': item.rate >= 100 }">
          {{ item.rate }}%<template v-if="item.rate >= 100"> 🤩</template>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted } from 'vue'

const rootEl = ref(null)
const fillEls = reactive([])

const categories = [
  { name: '营销',      count: 31, rate: 111, highlight: true },
  { name: '商品魔方2.0', count: 4,  rate: 100 },
  { name: '商品',      count: 12, rate: 85.7 },
  { name: '店铺设置',  count: 1,  rate: 25 },
  { name: '经营指导',  count: 6,  rate: 100 },
  { name: '账号',      count: 2,  rate: 100 },
]

function targetWidth(rate) {
  return rate >= 100 ? '100%' : `${rate}%`
}

let observer = null

function runAnimation() {
  categories.forEach((item, index) => {
    const el = fillEls[index]
    if (!el) return
    el.style.width = '0%'
    el.style.transition = 'none'
    setTimeout(() => {
      el.style.transition = `width 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94)`
      el.style.width = targetWidth(item.rate)
    }, index * 100 + 50)
  })
}

onMounted(() => {
  observer = new IntersectionObserver(
    (entries) => {
      if (entries[0].isIntersecting) {
        runAnimation()
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
/* 条形图容器 */
.bar-list {
  background: #fff;
  border-radius: 10px;
  padding: 12px;
  margin-top: 12px;
  border: 1.2px solid #EEEEEE;
}

/* 每行 */
.bar-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 10px;
}

.bar-row:last-child {
  margin-bottom: 0;
}

/* 左侧标签 */
.bar-label {
  width: 100px;
  flex-shrink: 0;
  font-size: 13px;
  color: #555;
  line-height: 1.3;
  text-align: right;
}

.bar-label.is-highlight {
  color: #FF8C00;
  font-weight: bold;
}

/* 进度条轨道 */
.bar-track {
  flex: 1;
  height: 10px;
  background: #F0F0F0;
  border-radius: 2px 2px 0px 0px;
  overflow: hidden;
}

/* 进度条填充（宽度由 JS 控制） */
.bar-fill {
  width: 0%;
  height: 100%;
  border-radius: 2px 2px 0px 0px;
}

.fill-orange {
  background: #FF8C00;
}

.fill-gray {
  background: #CCCCCC;
}

/* 右侧百分比 */
.bar-rate {
  width: 52px;
  flex-shrink: 0;
  text-align: left;
  font-size: 13px;
  color: #999;
  white-space: nowrap;
}

.bar-rate.rate-orange {
  color: #FF8C00;
  font-weight: bold;
}
</style>
