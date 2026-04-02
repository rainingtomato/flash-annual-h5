<template>
  <div ref="rootEl">
    <p class="module-title">年度最佳同学</p>

    <div class="employee-list">
      <div
        v-for="(item, index) in employees"
        :key="item.seed"
        class="employee-card"
        :class="{ 'no-border': index === employees.length - 1 }"
        :ref="el => { if (el) cardEls[index] = el }"
      >
        <!-- 左侧头像 -->
        <div class="avatar-wrap">
          <img
            :src="item.photo"
            :alt="item.name"
            class="avatar-img"
          />
        </div>

        <!-- 右侧描述 -->
        <div class="desc-wrap">
          {{ item.desc }}
          <span class="hl">{{ item.name }}</span>
          {{ item.descAfter }}
          <span class="highlight">{{ item.highlight }}</span>
          {{ item.unit }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted } from 'vue'
import photo1 from '../assets/images/photo1.png'
import photo2 from '../assets/images/photo2.png'
import photo3 from '../assets/images/photo3.png'

const rootEl = ref(null)
const cardEls = reactive([])

const employees = [
  {
    photo: photo1,
    desc: '营销组解决问题数、目标达成率双高，其中',
    name: '李弦',
    descAfter: '同学解决了',
    highlight: '16',
    unit: '个重点问题，是解决问题最多的同学！'
  },
  {
    photo: photo2,
    desc: '商家及后台组的',
    name: '冯雅婕',
    descAfter: '同学，在经营指导改版中深入一线调研',
    highlight: '9',
    unit: '次，是一线调研次数最多的同学！'
  },
  {
    photo: photo3,
    desc: '商品组的',
    name: '陈舒婷',
    descAfter: '同学，结合商家经营场景，解决了商品组',
    highlight: '60%',
    unit: '以上的重点问题，是最了解连锁商品经营的同学！'
  }
]

let observer = null

function runAnimation() {
  cardEls.forEach((el, index) => {
    if (!el) return
    // 先重置
    el.style.opacity = '0'
    el.style.transform = 'translateY(20px)'
    el.style.transition = 'none'

    setTimeout(() => {
      el.style.transition = 'opacity 0.5s ease, transform 0.5s ease'
      el.style.opacity = '1'
      el.style.transform = 'translateY(0)'
    }, index * 150 + 50)
  })
}

onMounted(() => {
  // 初始设为不可见
  cardEls.forEach(el => {
    if (el) {
      el.style.opacity = '0'
      el.style.transform = 'translateY(20px)'
    }
  })

  observer = new IntersectionObserver(
    (entries) => {
      if (entries[0].isIntersecting) {
        runAnimation()
        observer.disconnect()
      }
    },
    { threshold: 0.15 }
  )
  if (rootEl.value) observer.observe(rootEl.value)
})

onUnmounted(() => {
  if (observer) observer.disconnect()
})
</script>

<style scoped>
.employee-list {
  margin-top: 4px;
}

.employee-card {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding: 16px 0;
}

/* 非最后一项底部加虚线分隔（引用全局 .divider 样式，此处用伪元素实现方向一致） */
.employee-card:not(:last-child) {
  border-bottom: 2px dashed #EEEEEE;
}

/* 头像 */
.avatar-wrap {
  flex-shrink: 0;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  overflow: hidden;
  border: 0px 
}

.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

/* 描述区 */
.desc-wrap {
  flex: 1;
  font-size: 14px;
  line-height: 1.8;
  color: #444;
}

/* 人名样式已改为引用全局 .hl 高亮字样式 */
</style>
