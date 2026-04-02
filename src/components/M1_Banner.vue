<template>
  <div class="banner">
    <!-- 背景图区域（等比例占位） -->
    <div class="bg-area">
      <!-- 背景图 -->
      <img class="bg" :src="bgImg" alt="" />
      <!-- 烟花 Canvas -->
      <canvas ref="fireworksCanvas" class="fireworks"></canvas>
      <!-- Logo 独立绝对定位 -->
      <img class="logo" :src="logoImg" alt="美团闪购" />
      <!-- 标题图片 -->
      <img class="biaoti" :src="biaotiImg" alt="标题" />
      <!-- 右侧后台+袋鼠图 -->
      <img class="dashboard" :src="dashboardImg" alt="" />
    </div>

    <!-- 底部摘要卡片（流内布局，自然撑开模块底部） -->
    <div class="summary-card">
      <p class="summary-text">
        通过聚焦商家重点问题解决与核心商家深度建联，2025年商家体验脱贫<span class="hl">目标全面达成</span>，重点问题解决
        <span class="hl">56</span>个，解决率
        <span class="hl">50.9%</span>；重点商家建联
        <span class="hl">40</span>家，目标达成
        <span class="hl">100%</span>，为26年商家端体验脱贫奠定了坚实基础。
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import bgImg from '../assets/images/backgroundimage.png'
import logoImg from '../assets/images/logo@2x.png'
import dashboardImg from '../assets/images/dashboard-preview.png'
import biaotiImg from '../assets/images/biaoti@2x.png'

const fireworksCanvas = ref(null)
let animationId = null
let triggerTimer = null

const COLORS = ['#FFD700', '#FF6B6B', '#87CEEB', '#98FB98', '#DDA0DD']

function random(min, max) {
  return Math.random() * (max - min) + min
}

function createParticles(ctx, x, y) {
  const particles = []
  const count = 30
  for (let i = 0; i < count; i++) {
    const angle = (Math.PI * 2 / count) * i + random(-0.2, 0.2)
    const speed = random(1.5, 4)
    particles.push({
      x, y,
      vx: Math.cos(angle) * speed,
      vy: Math.sin(angle) * speed,
      alpha: 1,
      color: COLORS[Math.floor(Math.random() * COLORS.length)],
      radius: random(2, 4),
      decay: random(0.012, 0.022),
      gravity: 0.06,
    })
  }
  return particles
}

function launchFireworks() {
  const canvas = fireworksCanvas.value
  if (!canvas) return
  const ctx = canvas.getContext('2d')
  const W = canvas.width
  const H = canvas.height

  const count = Math.floor(random(3, 6))
  let allParticles = []
  for (let i = 0; i < count; i++) {
    const ex = random(W * 0.1, W * 0.9)
    const ey = random(H * 0.1, H * 0.7)
    allParticles = allParticles.concat(createParticles(ctx, ex, ey))
  }

  function animate() {
    ctx.clearRect(0, 0, W, H)
    allParticles.forEach(p => {
      p.x += p.vx
      p.y += p.vy
      p.vy += p.gravity
      p.vx *= 0.98
      p.alpha -= p.decay
      if (p.alpha < 0) p.alpha = 0
      ctx.save()
      ctx.globalAlpha = p.alpha
      ctx.beginPath()
      ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2)
      ctx.fillStyle = p.color
      ctx.fill()
      ctx.restore()
    })
    const alive = allParticles.some(p => p.alpha > 0)
    if (alive) {
      animationId = requestAnimationFrame(animate)
    } else {
      ctx.clearRect(0, 0, W, H)
    }
  }

  if (animationId) cancelAnimationFrame(animationId)
  animate()
}

function startLoop() {
  launchFireworks()
  triggerTimer = setInterval(launchFireworks, 2500)
}

onMounted(() => {
  const canvas = fireworksCanvas.value
  if (!canvas) return
  const parent = canvas.parentElement
  canvas.width = parent.offsetWidth
  canvas.height = parent.offsetHeight
  startLoop()
})

onUnmounted(() => {
  if (animationId) cancelAnimationFrame(animationId)
  if (triggerTimer) clearInterval(triggerTimer)
})
</script>

<style scoped>
.banner {
  position: relative;
  width: 100%;
  overflow: visible;
}

/* 背景图区域：等比例占位（526/750 ≈ 70.13%），所有绝对定位元素相对于此定位 */
.bg-area {
  position: relative;
  width: 100%;
  padding-top: 70.13%;
  overflow: visible;  /* 改这里 */
}

/* 背景图 */
.bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: contain;
  object-position: center top;
  z-index: 0;
}

/* 烟花 canvas */
.fireworks {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  pointer-events: none;
}

/* Logo 独立绝对定位 */
.logo {
  position: absolute;
  left: -1px;
  top: 18px;
  width: 98px;
  height: 30px;
  object-fit: contain;
  z-index: 3;
}

/* 标题图片 */
.biaoti {
  position: absolute;
  left: 16px;
  top: 82px;
  width: 227px;
  height: 77px;
  object-fit: contain;
  z-index: 5;
  pointer-events: none;
}

/* 右侧后台图 */
.dashboard {
  position: absolute;
  left: 203px;
  top: 59px;
  width: 177px;
  height: 133px;
  object-fit: contain;
  z-index: 2;
  pointer-events: none;
}

/* 底部摘要卡片（流内布局，与背景图区域有负 margin 上移叠压） */
.summary-card {
  position: relative;
  margin: -78px 16px 0;
  background:  linear-gradient(180deg, rgba(255, 255, 255, 0.5) 0%, #FFFFFF 100%);
  border-radius: 16px;
  border: 2px solid #FFFFFF;
  padding: 16px;
  z-index: 3;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.summary-text {
  font-size: 13px;
  line-height: 1.8;
  color: #333;
  margin: 0;
}

/* 高亮字样式已提取至全局 global.css 中的 .hl */
</style>