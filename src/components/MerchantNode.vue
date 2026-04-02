<template>
  <img class="city-bubble" :src="bubbleCity" :alt="cityAlt" />
  <div class="node-card">
    <div class="avatar-wrap">
      <img class="avatar-border" :src="avatarBorder" aria-hidden="true" />
      <img class="avatar-img" :src="avatarImg" :alt="nameAlt" />
    </div>
    <div class="node-name">{{ nameAlt }}</div>
    <div class="node-meta">
      <span class="meta-date">{{ dateAlt }}</span>
      <span class="meta-div">|</span>
      <span class="meta-city">{{ cityAlt2 }}</span>
    </div>
    <img v-if="highlight" class="node-highlight" :src="highlight" :alt="highlightAlt" />
    <div v-else class="node-highlight-placeholder"></div>
  </div>
</template>

<style scoped>
/* 顶部城市气泡 */
.city-bubble {
  width: 31px;
  height: 19px;
  margin-bottom: 4px;
  flex-shrink: 0;
  object-fit: contain;
}

/* 主体卡片 */
.node-card {
  width: 60px;
  border-radius: 10px;
  padding: 0px 4px 4px 4px;
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
  font-size: 10px;
  font-weight: 500;
  color: #333333;
  line-height: 14px;
  text-align: center;
  max-width: 52px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  margin-top: 1px;
}

/* 日期|城市行 */
.node-meta {
  display: flex;
  align-items: center;
  gap: 2px;
  font-size: 8px;
  color: #666666;
  line-height: 10px;
}

.meta-date {
  font-size: 8px;
  color: #666666;
}

.meta-div {
  font-size: 8px;
  color: #CCCCCC;
  margin: 0 1px;
}

.meta-city {
  font-size: 8px;
  color: #666666;
}

/* 亮点标签 */
.node-highlight {
  width: 50px;
  height: 8px;
  object-fit: contain;
  margin-top: 1px;
}

/* 亮点标签占位符：无标签时保持高度 */
.node-highlight-placeholder {
  width: 50px;
  height: 8px;
  margin-top: 1px;
  flex-shrink: 0;
}
</style>

<script setup>
defineProps({
  /** 城市气泡切图 */
  bubbleCity: { type: String, required: true },
  /** 城市气泡 alt 文本 */
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
  /** 亮点标签切图（可选，不提供则不显示） */
  highlight: { type: String, default: '' },
  /** 亮点标签 alt */
  highlightAlt: { type: String, default: '' },
})
</script>
