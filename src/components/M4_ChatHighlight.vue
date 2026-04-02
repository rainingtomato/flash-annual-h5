<template>
  <div ref="rootEl">
    <p class="module-title">重点问题解决展示</p>

    <div class="case-wrapper">
    <div class="case-list">
      <div
        v-for="(c, cIdx) in cases"
        :key="c.merchantName"
        class="case-block"
        :class="{ 'has-divider': cIdx > 0 }"
      >
        <!-- 对话行：左侧头像 + 右侧内容 -->
        <div class="dialog-row">
          <!-- 左侧头像 -->
          <div class="merchant-logo" :style="{ background: c.bgColor }">
            <span class="logo-text">{{ c.logoText }}</span>
          </div>

          <!-- 右侧：商家信息 + 气泡列 -->
          <div class="dialog-content">
            <!-- 商家信息 -->
            <div class="merchant-info">
              <div class="merchant-name">{{ c.merchantName }}</div>
              <div class="merchant-category">{{ c.category }}</div>
            </div>

            <!-- 气泡列表 -->
            <div class="bubble-list">
              <template v-for="(msg, mIdx) in c.messages" :key="mIdx">
                <!-- 用户提问：靠左，灰色气泡，左侧SVG尾巴 -->
                <div
                  v-if="msg.type === 'user'"
                  class="bubble bubble-user"
                  :ref="el => { if (el) registerBubble(el, cIdx, mIdx) }"
                >
                  <template v-if="msg.parts">
                    <template v-for="(part, pIdx) in msg.parts" :key="pIdx">
                      <span v-if="part.hl" class="bubble-hl"> {{ part.text }} </span>
                      <template v-else>{{ part.text }}</template>
                    </template>
                  </template>
                  <template v-else>{{ msg.text }}</template>
                </div>

                <!-- 产品回复：靠右，橙色气泡，右侧SVG尾巴 -->
                <div
                  v-else-if="msg.type === 'reply'"
                  class="bubble bubble-reply"
                  :ref="el => { if (el) registerBubble(el, cIdx, mIdx) }"
                >
                  {{ msg.text }}
                </div>
              </template>
            </div>
          </div>
        </div>
      </div>
    </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const rootEl = ref(null)

const bubbleMap = []

function registerBubble(el, cIdx, mIdx) {
  if (!bubbleMap[cIdx]) bubbleMap[cIdx] = []
  bubbleMap[cIdx][mIdx] = el
  if (el) {
    el.style.opacity = '0'
    el.style.transform = 'translateY(16px)'
    el.style.transition = 'none'
  }
}

const cases = [
  {
    merchantName: '八马茶业',
    logoText: '八马茶业',
    category: '营销-自营销-商品券',
    bgColor: '#FFF0E6',
    messages: [
      { type: 'user', text: '配置商品券活动添加门店的数量是否可扩充一下？目前最多只能添加2000家门店' },
      { type: 'reply', text: '商品券活动设置优化啦，可圈选的门店范围支持到5000家' },
      { type: 'user', parts: [
        { text: '这个商品券产品更新的' },
        { text: ' 很可以 很好用 ', hl: true },
        { text: '，感谢产品团队的快速响应和优质输出~' },
      ]},
    ]
  },
  {
    merchantName: '玫瑰之约',
    logoText: '玫瑰之约',
    category: '营销-自营销-消息触达',
    bgColor: '#FFF0E6',
    messages: [
      { type: 'user', text: '目前自营销的活动操作记录都是通过站内信告知的，信息太多了根本没法及时查看，查看入口太深，有时候根本找不到对应的信息是哪条' },
      { type: 'reply', text: '新增了折扣活动操作记录，可实时查看折扣商品所有信息变更记录啦' },
      { type: 'user', parts: [
        { text: '非常感谢' },
        { text: ' 闪购产品团队 ', hl: true },
        { text: '的支持，解决我们非常头疼的一个点，希望后面可以和产品团队多交流' },
      ]},
    ]
  }
]

let observer = null

function runAnimation() {
  const allBubbles = []
  cases.forEach((c, cIdx) => {
    c.messages.forEach((_, mIdx) => {
      const el = bubbleMap[cIdx]?.[mIdx]
      if (el) allBubbles.push(el)
    })
  })

  allBubbles.forEach((el, i) => {
    setTimeout(() => {
      el.style.transition = 'opacity 0.4s ease, transform 0.4s ease'
      el.style.opacity = '1'
      el.style.transform = 'translateY(0)'
    }, i * 120 + 50)
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
    { threshold: 0.1 }
  )
  if (rootEl.value) observer.observe(rootEl.value)
})

onUnmounted(() => {
  if (observer) observer.disconnect()
})
</script>

<style scoped>
.case-wrapper {
  margin-top: 8px;
  border: 1px solid #EEEEEE;
  border-radius: 12px;
  padding: 12px 10px;
}

.case-list {
  display: flex;
  flex-direction: column;
  gap: 0;
}

.case-block {
  padding-bottom: 4px;
}

/* 分隔线 */
.case-block.has-divider {
  border-top: 2px dashed #EEEEEE;
  padding-top: 16px;
  margin-top: 16px;
}

/* 对话行：头像 + 内容横排 */
.dialog-row {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  gap: 6px;
}

/* 左侧头像 */
.merchant-logo {
  flex-shrink: 0;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  border: 1px solid #EEEEEE;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.logo-text {
  font-size: 7px;
  color: #FF8C00;
  text-align: center;
  line-height: 1.2;
  word-break: break-all;
  padding: 2px;
}

/* 右侧内容区 */
.dialog-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 12px;
  min-width: 0;
}

/* 商家信息 */
.merchant-info {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.merchant-name {
  font-size: 15px;
  font-weight: bold;
  color: #1A1A1A;
}

.merchant-category {
  font-size: 11px;
  color: #999;
}

/* 气泡列表 */
.bubble-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

/* 通用气泡 */
.bubble {
  max-width: 95%;
  font-size: 13px;
  line-height: 1.7;
  word-break: break-all;
}

/* 用户提问：靠左，浅灰背景，左侧SVG尾巴 */
.bubble-user {
  align-self: flex-start;
  background: #F8F8F8;
  border-radius: 8px;
  padding: 6px 8px;
  color: #1A1A1A;
  position: relative;
  margin-left: 0px;
}

/* 左侧气泡尾巴（SVG图标） */
.bubble-user::before {
  content: '';
  position: absolute;
  left: -8px;
  top: 50%;
  transform: translateY(-50%);
  width: 8px;
  height: 12px;
  background-image: url('https://s3plus.meituan.net/mcopilot-pub/copilot/chat/assets/7617b7c6c9a95ac362355d40a50c06bc.svg');
  background-repeat: no-repeat;
  background-size: contain;
}

/* 产品回复：靠右，浅橙色背景，右侧SVG尾巴 */
.bubble-reply {
  align-self: flex-end;
  background: #FFD2A2;
  border-radius: 8px;
  padding: 6px 8px;
  color: #1A1A1A;
  position: relative;
  margin-right: 0px;
}

/* 右侧气泡尾巴（SVG图标） */
.bubble-reply::after {
  content: '';
  position: absolute;
  right: -7px;
  top: 50%;
  transform: translateY(-50%);
  width: 8px;
  height: 12px;
  background-image: url('https://s3plus.meituan.net/mcopilot-pub/copilot/chat/assets/b601eaa0fde09794ca4b02fb35637185.svg');
  background-repeat: no-repeat;
  background-size: contain;
}

/* 气泡内高亮文字 */
.bubble-hl {
  color: #FF7300;
  font-weight: bold;
}

/* 高亮字样式已改为引用全局 .hl 样式 */
</style>
