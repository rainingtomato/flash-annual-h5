<template>
  <div class="city-bubble">
    <img class="bubble-bg" :src="bubbleBg" aria-hidden="true" />
    <img class="bubble-city" :src="bubbleCity" :alt="cityAlt" />
  </div>
  <div class="node-card">
    <div class="avatar-wrap">
      <img class="avatar-border" :src="avatarBorder" aria-hidden="true" />
      <img class="avatar-img" :src="avatarImg" :alt="nameAlt" />
    </div>
    <img class="node-name" :src="nameSrc" :alt="nameAlt" />
    <div class="node-meta">
      <img class="meta-date" :src="metaDate" :alt="dateAlt" />
      <img class="meta-div" :src="metaDivider" aria-hidden="true" />
      <img class="meta-city" :src="metaCity" :alt="cityAlt2" />
    </div>
    <img class="node-highlight" :src="highlight" :alt="highlightAlt" />
  </div>
</template>

<style scoped>
/* 顶部城市气泡 */
.city-bubble {
  position: relative;
  width: 31px;
  height: 18px;
  margin-bottom: 4px;
  flex-shrink: 0;
}

.bubble-bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.bubble-city {
  position: absolute;
  width: 9px;
  height: 10px;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

/* 主体卡片 */
.node-card {
  width: 60px;
  border-radius: 10px;
  padding: 5px 4px 4px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2px;
}

/* 头像区域 */
.avatar-wrap {
  position: relative;
  width: 32px;
  height: 32px;
  flex-shrink: 0;
}

.avatar-border {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.avatar-img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border-radius: 50%;
}

/* 商家名 */
.node-name {
  width: 40px;
  height: 14px;
  object-fit: contain;
  margin-top: 1px;
}

/* 日期|城市行 */
.node-meta {
  display: flex;
  align-items: center;
  gap: 2px;
}

.meta-date {
  width: 22px;
  height: 10px;
  object-fit: contain;
}

.meta-div {
  width: 1px;
  height: 6px;
  opacity: 0.1;
}

.meta-city {
  width: 18px;
  height: 10px;
  object-fit: contain;
}

/* 亮点标签 */
.node-highlight {
  width: 50px;
  height: 8px;
  object-fit: contain;
  margin-top: 1px;
}
</style>

<script setup>
defineProps({
  /** 城市气泡背景 SVG */
  bubbleBg: { type: String, required: true },
  /** 城市气泡文字切图 */
  bubbleCity: { type: String, required: true },
  /** 城市气泡 alt 文本（城市首字） */
  cityAlt: { type: String, default: '' },
  /** 头像边框 SVG */
  avatarBorder: { type: String, required: true },
  /** 头像图片 */
  avatarImg: { type: String, required: true },
  /** 商家名切图 */
  nameSrc: { type: String, required: true },
  /** 商家名 alt */
  nameAlt: { type: String, default: '' },
  /** 日期切图 */
  metaDate: { type: String, required: true },
  /** 日期 alt */
  dateAlt: { type: String, default: '' },
  /** 分隔线 SVG */
  metaDivider: { type: String, required: true },
  /** 城市文字切图 */
  metaCity: { type: String, required: true },
  /** 城市 alt */
  cityAlt2: { type: String, default: '' },
  /** 亮点标签切图 */
  highlight: { type: String, required: true },
  /** 亮点标签 alt */
  highlightAlt: { type: String, default: '' },
})
</script>
