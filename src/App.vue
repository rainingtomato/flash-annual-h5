<template>
  <div id="app-container">
    <!-- 模块1：Banner（全宽无圆角） -->
    <section class="module-banner">
      <M1Banner />
    </section>

    <!-- 模块2：重点问题解决情况 -->
    <section class="module-card module-card--first">
      <M2IssueStats />
    </section>

    <!-- 模块3：最佳员工 -->
    <section class="module-card">
      <M3BestEmployee />
    </section>

    <!-- 模块4：对话气泡高光反馈 -->
    <section class="module-card">
      <M4ChatHighlight />
    </section>

    <!-- 模块5：线下拜访与共振群数据 -->
    <section class="module-card">
      <M5MerchantStats />
    </section>

    <!-- 模块6：商家拜访时间线 -->
    <section class="module-card module-card--m6">
      <M6VisitTimeline />
    </section>
  </div>
</template>

<script setup>
import M1Banner from './components/M1_Banner.vue'
import M2IssueStats from './components/M2_IssueStats.vue'
import M3BestEmployee from './components/M3_BestEmployee.vue'
import M4ChatHighlight from './components/M4_ChatHighlight.vue'
import M5MerchantStats from './components/M5_MerchantStats.vue'
import M6VisitTimeline from './components/M6_VisitTimeline.vue'
</script>

<style scoped>
#app-container {
  width: 100%;
  max-width: 375px;
  margin: 0 auto;
  min-height: 100vh;
  background: ##FFECD2;
  padding-bottom: 40px;
  overflow-y: auto;
}

/* 模块1 Banner：全宽无圆角无 margin 无 shadow */
.module-banner {
  width: 100%;
}

/* 通用模块卡片 */
.module-card {
  background: #FFFFFF;
  border-radius: 12px;
  margin: 10px 10px;
  padding: 18px 12px;
}

/* 模块2 顶部无需额外留空 */
.module-card--first {
  margin-top: 12px;
}

/* 模块6：无内边距，由组件内部自行控制 */
.module-card--m6 {
  padding: 0;
  overflow: hidden;
}
</style>
