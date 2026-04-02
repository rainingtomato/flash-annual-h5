<template>
  <div class="m6-wrap" ref="rootEl">
    <!-- 背景装饰：上半部分切图 -->
    <img
      class="deco-top"
      src="https://s3plus.meituan.net/mcopilot-pub/copilot/chat/assets/f5b67a0db100344f8a012dcdcdb883f0.png"
      aria-hidden="true"
    />
    <!-- 背景装饰：下半部分切图 -->
    <img
      class="deco-bottom"
      src="https://s3plus.meituan.net/mcopilot-pub/copilot/chat/assets/d8c0508f5921ed8f5a0c4e326db1f98c.png"
      aria-hidden="true"
    />

    <!-- 标题 -->
    <div class="module-title m6-title">商家拜访时间线</div>

    <!-- 路径容器 -->
    <div class="path-wrap" ref="pathWrap">
      <svg
        class="path-svg"
        viewBox="0 0 650 1224"
        xmlns="http://www.w3.org/2000/svg"
      >
        <!-- clipPath：从上到下展开，用于路径入场动画 -->
        <defs>
          <clipPath id="reveal-clip">
            <rect
              ref="clipRectEl"
              x="0" y="0"
              width="650"
              :height="clipHeight"
            />
          </clipPath>
        </defs>

        <!-- 跑道填充色块（受 clipPath 控制，从上到下展开） -->
        <path
          clip-path="url(#reveal-clip)"
          d="M102,1224L378.5,1224L378.5,1220L102,1220Q82.060776,1220,63.854591,1212.2994Q46.267956,1204.861,32.703535,1191.2965Q19.138924,1177.7319,11.7005062,1160.1455Q4,1141.9395,4,1122L4,1118.6667Q4,1098.7274,11.7004757,1080.5214Q19.138878,1062.9349,32.703434,1049.3704Q46.267982,1035.8058,63.854393,1028.3673Q82.060364,1020.6668,101.99971,1020.6667L548.00031,1020.6653Q568.75073,1020.6653,587.7038,1012.6487Q606.00885,1004.9063,620.125,990.7901Q634.24115,976.67389,641.98352,958.36884Q650,939.41571,650,918.66528L650,915.33234Q650,894.58185,641.98346,875.62866Q634.24103,857.32361,620.12476,843.20734Q606.00836,829.091,587.70343,821.34869Q568.75037,813.33228,547.99969,813.33234L102.00029,813.33368Q82.060944,813.33374,63.854797,805.63324Q46.268341,798.19482,32.703648,784.63019Q19.139008,771.06561,11.7005444,753.47913Q4.000007200000001,735.27307,4.0000076,715.33368L4,712.00024Q4,692.06091,11.7004814,673.85492Q19.138937,656.26843,32.703455000000005,642.70386Q46.268013,629.13928,63.854439,621.70081Q82.060425,614.00031,101.999779,614.00024L548.00024,613.99927Q568.75061,613.99921,587.7038,605.98267Q606.00879,598.2403,620.125,584.12402Q634.24121,570.00781,641.98352,551.70282Q650,532.74969,650,511.99927L650,508.66617Q650,487.91571,641.98346,468.96249Q634.24109,450.65747,620.12482,436.54123Q606.00848,422.42493,587.70355,414.68262Q568.75043,406.66614,547.99988,406.6662L102.00014,406.66684Q82.060783,406.66687,63.854691,398.96637Q46.268196,391.52792,32.703587999999996,377.96335Q19.138969,364.39874,11.7005138,346.81229Q3.9999928000000002,328.60623,3.9999924,308.66684L4,305.33344Q4,285.39407,11.7004967,267.18805Q19.138948,249.60156,32.70351,236.03699Q46.268063,222.47243,63.854546,215.03395Q82.060593,207.33342,101.999931,207.3334L548.00006,207.33308Q568.75061,207.33307,587.70367,199.31657Q606.00861,191.57423,620.12488,177.45793Q634.24109,163.34172,641.98346,145.03665Q650,126.08341,650,105.33305L649.99994,101.999939Q649.99994,81.249466,641.98346,62.296371Q634.24109,43.991405,620.12482,29.875101Q606.00854,15.758827,587.70361,8.016489Q568.75049,0.0000018999999999991246,548,0L78,0L78,4L548,4Q567.93933,4.0000014,586.14539,11.7005062Q603.73193,19.138979,617.29645,32.703527Q630.86108,46.268166,638.2995,63.854576Q645.99994,82.060471,645.99994,102.00002L646,105.33305Q646,125.27242,638.2995,143.47845Q630.86102,161.06496,617.29651,174.6295Q603.73193,188.19408,586.14545,195.63255Q567.93939,203.33307,548.00006,203.33308L101.999931,203.3334Q81.249435,203.33344,62.296333,211.34993Q43.991306,219.09232,29.87508,233.20856Q15.758842,247.32481,8.016479,265.62982Q0,284.58292,0,305.33344L-0.0000075999999999964984,308.66684Q-0.0000075999999999964984,329.41739,8.016496700000001,348.37051Q15.75886,366.67551,29.875162,380.79178Q43.991436,394.90802,62.296486,402.65039Q81.249641,410.66687,102.00014,410.66684L547.99988,410.6662Q567.93927,410.66617,586.14532,418.36664Q603.73187,425.80508,617.29645,439.36966Q630.86102,452.93423,638.2995,470.52072Q646,488.72675,646,508.66617L646,511.99927Q646,531.93866,638.29956,550.14459Q630.86115,567.73096,617.29651,581.29565Q603.73193,594.86029,586.14557,602.29871Q567.93958,609.99921,548.00024,609.99927L101.999763,610.00024Q81.249405,610.00031,62.296227,618.01685Q43.991249,625.75922,29.875025,639.87549Q15.758781,653.99176,8.0164623,672.29669Q0,691.24976,0,712.00024L0.0000075999999999964984,715.33368Q0.000008100000000066387,736.08423,8.016527700000001,755.03735Q15.758945,773.34247,29.875225,787.45868Q43.991592,801.57501,62.2966,809.31732Q81.249672,817.33374,102.00031,817.33368L547.99969,817.33234Q567.93903,817.33228,586.1452,825.03278Q603.73169,832.47119,617.29639,846.03583Q630.86102,859.60046,638.2995,877.18689Q646,895.39288,646,915.33234L646,918.66528Q646,938.60468,638.29956,956.81061Q630.86115,974.39703,617.29651,987.96173Q603.73199,1001.52631,586.14557,1008.9648Q567.9397,1016.6653,548.00031,1016.6653L101.999695,1016.6667Q81.249207,1016.6668,62.296181,1024.6833000000001Q43.991322,1032.4257,29.875004,1046.542Q15.758812,1060.6582,8.0164566,1078.9633Q0,1097.9164,0,1118.6667L0,1122Q-5.00000000069889e-7,1142.7505,8.016488599999999,1161.7036Q15.75886,1180.0087,29.875109,1194.1249Q43.991409,1208.2412,62.296387,1215.9835Q81.249481,1224,102,1224Z"
          fill-rule="evenodd"
          fill="#EEEEEE"
          fill-opacity="1"
        />
      </svg>

      <!-- 商家节点：通过数据驱动渲染 -->
      <div
        v-for="(node, index) in nodes"
        :key="node.id"
        class="merchant-node"
        :class="[node.posClass, { 'is-visible': isVisible }]"
        :style="{ '--delay': `${pathDuration + index * NODE_STAGGER}s` }"
      >
        <MerchantNode
          :bubbleBg="node.bubbleBg"
          :bubbleCity="node.bubbleCity"
          :cityAlt="node.cityAlt"
          :avatarBorder="node.avatarBorder"
          :avatarImg="node.avatarImg"
          :nameSrc="node.nameSrc"
          :nameAlt="node.nameAlt"
          :metaDate="node.metaDate"
          :dateAlt="node.dateAlt"
          :metaDivider="node.metaDivider"
          :metaCity="node.metaCity"
          :cityAlt2="node.cityAlt2"
          :highlight="node.highlight"
          :highlightAlt="node.highlightAlt"
        />
      </div>
    </div>

    <!-- 底部结语 -->
    <div class="ending">
      <div class="ending-line"></div>
      <div class="ending-text">雄关漫道真如铁，而今迈步从头越！</div>
      <div class="ending-line"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import MerchantNode from './MerchantNode.vue'
import beijingBubble from '../assets/city-bubbles/beijing@2x.png'

const rootEl   = ref(null)
const pathWrap = ref(null)

// ── 动画参数 ──
const PATH_DURATION = 1       // SVG路径展开时长（秒）
const NODE_STAGGER  = 0.08   // 节点交错延迟（秒）
const pathDuration  = PATH_DURATION

// clipPath 高度：用于驱动 SVG 从上到下展开
const clipHeight = ref(0)

// 是否进入视口
const isVisible = ref(false)

// ── 公共静态资源（暂时全部使用同一套占位图，后续逐个替换） ──
const BUBBLE_BG    = 'https://s3plus.meituan.net/mcopilot-pub/copilot/chat/assets/43918240669eae6e2b1a584087eef067.svg'
const BUBBLE_CITY  = 'https://s3plus.meituan.net/mcopilot-pub/copilot/chat/assets/6ff3af5a67d051d13482be3370f0139e.png'
const AVATAR_BORDER= 'https://s3plus.meituan.net/mcopilot-pub/copilot/chat/assets/885f8ef35eb2fef66533930fb3d3a1fa.svg'
const AVATAR_IMG   = 'https://s3plus.meituan.net/mcopilot-pub/copilot/chat/assets/00d1126e79c333d0a862018472a4aa7d.png'
const NAME_SRC     = 'https://s3plus.meituan.net/mcopilot-pub/copilot/chat/assets/da897d45fa400563bc3336c0b63abef3.png'
const META_DATE    = 'https://s3plus.meituan.net/mcopilot-pub/copilot/chat/assets/d582f4c6fcf043190eeb9754c405d92e.png'
const META_DIV     = 'https://s3plus.meituan.net/mcopilot-pub/copilot/chat/assets/45e28772df86a963f06ef2b125d042f6.svg'
const META_CITY    = 'https://s3plus.meituan.net/mcopilot-pub/copilot/chat/assets/ad863f8fe788411c79c9f94b19acd3da.png'
const HIGHLIGHT    = 'https://s3plus.meituan.net/mcopilot-pub/copilot/chat/assets/dd3c399d925e61e33391e6975c357871.png'

/** 生成一个节点数据（所有图片占位，方便后续逐个替换） */
const makeNode = (id, posClass, overrides = {}) => {
  const node = {
    id,
    posClass,
    bubbleBg:    BUBBLE_BG,
    bubbleCity:  BUBBLE_CITY,
    cityAlt:     '京',
    avatarBorder:AVATAR_BORDER,
    avatarImg:   AVATAR_IMG,
    nameSrc:     NAME_SRC,
    nameAlt:     '小鹿驾到',
    metaDate:    META_DATE,
    dateAlt:     '0806',
    metaDivider: META_DIV,
    metaCity:    META_CITY,
    cityAlt2:    '北京',
    highlight:   HIGHLIGHT,
    highlightAlt:'宠物品类仓店',
    ...overrides,
  }
  // 如果 overrides 中有 cityAlt 但没有 cityAlt2，自动同步
  if (overrides.cityAlt && !overrides.cityAlt2) {
    node.cityAlt2 = overrides.cityAlt
  }
  return node
}

// ── 26个节点数据,posClass 对应 CSS 定位类 ──
// 城市标签图片映射
const cityBubbles = {
  '北京': 'src/assets/city-bubbles/beijing@2x.png',
  '上海': 'src/assets/city-bubbles/shagnhai@2x.png',
  '广州': 'src/assets/city-bubbles/guangdong@2x.png',
  '深圳': 'src/assets/city-bubbles/guangdong@2x.png', 
  '南京': 'src/assets/city-bubbles/jiangsu@2x.png',
  '杭州': 'src/assets/city-bubbles/zhejiang@2x.png',
  '重庆': 'src/assets/city-bubbles/chongqing2x.png',
  '昆明': 'src/assets/city-bubbles/yunnan@2x.png',
  '西安': 'src/assets/city-bubbles/shanxi@2x.png'
}

const nodes = [
  // 第1行（左→右）
  makeNode( 1, 'node-1', {
    bubbleCity: cityBubbles['北京'],
    cityAlt: '北京',
    avatarImg: 'src/assets/avatarImg/logo1@2x.png',
    nameAlt: '斑马超市',
    dateAlt: '0729',
    highlight: '',
    highlightAlt: ''
  }),
  makeNode( 2, 'node-2', {
    bubbleCity: cityBubbles['北京'],
    cityAlt: '北京',
    avatarImg: 'src/assets/avatarImg/logo2@2x.png', 
    nameAlt: '小鹿驾到',
    dateAlt: '0806',
    highlight: '',  // 待补充亮点标签图片
    highlightAlt: '宠物品类仓店'
  }),
  makeNode( 3, 'node-3', {
    bubbleCity: cityBubbles['上海'],
    cityAlt: '上海',
    avatarImg: 'src/assets/avatarImg/logo3@2x.png',
    nameAlt: '飞利浦',
    dateAlt: '0814',
    highlight: '',
    highlightAlt: ''
  }),
  makeNode( 4, 'node-4', {
    bubbleCity: cityBubbles['上海'],
    cityAlt: '上海',
    avatarImg: 'src/assets/avatarImg/logo4@2x.png', 
    nameAlt: '飞科',
    dateAlt: '0815',
    highlight: '',  // 待补充亮点标签图片
    highlightAlt: '最强工区'
  }),
  // 第2行（右→左）
  makeNode( 5, 'node-r2-1', {
    bubbleCity: cityBubbles['广州'],
    cityAlt: '广州',
    avatarImg: 'src/assets/avatarImg/logo5@2x.png', 
    dateAlt: '0818',
    highlight: '',
    highlightAlt: ''
  }),
  makeNode( 6, 'node-r2-2', {
    bubbleCity: cityBubbles['广州'],
    cityAlt: '广州',
    avatarImg: 'src/assets/avatarImg/logo6@2x.png', 
    nameAlt: '名创优品',
    dateAlt: '0819',
    highlight: '',
    highlightAlt: ''
  }),
  makeNode( 7, 'node-r2-3', {
    bubbleCity: cityBubbles['北京'],
    cityAlt: '北京',
    avatarImg: 'src/assets/avatarImg/logo7@2x.png',
    nameAlt: '小米',
    dateAlt: '0821',
    highlight: '',  // 待补充亮点标签图片
    highlightAlt: '14000家门店'
  }),
  makeNode( 8, 'node-r2-4', {
    bubbleCity: cityBubbles['深圳'],
    cityAlt: '深圳',
    avatarImg: 'src/assets/avatarImg/logo8@2x.png',  
    nameAlt: '百果园',
    dateAlt: '0911',
    highlight: '',
    highlightAlt: ''
  }),
  // 第3行（左→右）
  makeNode( 9, 'node-r3-1', {
    bubbleCity: cityBubbles['北京'],
    cityAlt: '北京',
    avatarImg: 'src/assets/avatarImg/logo9@2x.png', 
    nameAlt: '嗨特购',
    dateAlt: '0916',
    highlight: '',
    highlightAlt: ''
  }),
  makeNode(10, 'node-r3-2', {
    bubbleCity: cityBubbles['上海'],
    cityAlt: '上海',
    avatarImg: 'src/assets/avatarImg/logo10@2x.png', 
    nameAlt: '锅圈',
    dateAlt: '0917',
    highlight: '',
    highlightAlt: ''
  }),
  makeNode(11, 'node-r3-3', {
    bubbleCity: cityBubbles['上海'],
    cityAlt: '上海',
    avatarImg: 'src/assets/avatarImg/logo11@2x.png',  
    nameAlt: '玩具反斗城',
    dateAlt: '0918',
    highlight: '',
    highlightAlt: ''
  }),
  makeNode(12, 'node-r3-4', {
    bubbleCity: cityBubbles['北京'],
    cityAlt: '北京',
    avatarImg: 'src/assets/avatarImg/logo12@2x.png',  
    nameAlt: '小天才',
    dateAlt: '0923',
    highlight: '',  // 待补充亮点标签图片
    highlightAlt: '电商运营团队转型'
  }),
  // 第4行（右→左）
  makeNode(13, 'node-r4-1', {
    bubbleCity: cityBubbles['上海'],
    cityAlt: '上海',
    avatarImg: 'src/assets/avatarImg/logo13@2x.png',  
    nameAlt: '好想来',
    dateAlt: '0924',
    highlight: '',
    highlightAlt: ''
  }),
  makeNode(14, 'node-r4-2', {
    bubbleCity: cityBubbles['深圳'],
    cityAlt: '深圳',
    avatarImg: 'src/assets/avatarImg/logo14@2x.png',  
    nameAlt: '八马茶业',
    dateAlt: '1010',
    highlight: '',
    highlightAlt: ''
  }),
  makeNode(15, 'node-r4-3', {
    bubbleCity: cityBubbles['南京'],
    cityAlt: '南京',
    avatarImg: 'src/assets/avatarImg/logo15@2x.png',  
    nameAlt: '酒易淘',
    dateAlt: '1015',
    highlight: '',  // 待补充亮点标签图片
    highlightAlt: '首创酒类24小时无人仓'
  }),
  makeNode(16, 'node-r4-4', {
    bubbleCity: cityBubbles['上海'],
    cityAlt: '上海',
    avatarImg: 'src/assets/avatarImg/logo16@2x.png',  
    nameAlt: '罗森',
    dateAlt: '1023',
    highlight: '',  // 待补充亮点标签图片
    highlightAlt: '日系企业文化'
  }),
  // 第5行（左→右）
  makeNode(17, 'node-r5-1', {
    bubbleCity: cityBubbles['上海'],
    cityAlt: '上海',
    avatarImg: 'src/assets/avatarImg/logo17@2x.png',  
    nameAlt: '全家',
    dateAlt: '1023',
    highlight: '',
    highlightAlt: ''
  }),
  makeNode(18, 'node-r5-2', {
    bubbleCity: cityBubbles['广州'],
    cityAlt: '广州',
    avatarImg: 'src/assets/avatarImg/logo18@2x.png', 
    nameAlt: '鸣鸣很忙',
    dateAlt: '1030',
    highlight: '',
    highlightAlt: ''
  }),
  makeNode(19, 'node-r5-3', {
    bubbleCity: cityBubbles['杭州'],
    cityAlt: '杭州',
    avatarImg: 'src/assets/avatarImg/logo19@2x.png',  
    nameAlt: '苏泊尔',
    dateAlt: '1107',
    highlight: '',  // 待补充亮点标签图片
    highlightAlt: '老牌企业转型'
  }),
  makeNode(20, 'node-r5-4', {
    bubbleCity: cityBubbles['南京'],
    cityAlt: '南京',
    avatarImg: 'src/assets/avatarImg/logo20@2x.png',  
    nameAlt: '孩子王',
    dateAlt: '1113',
    highlight: '',
    highlightAlt: ''
  }),
  // 第6行（右→左）
  makeNode(21, 'node-r6-1', {
    bubbleCity: cityBubbles['重庆'],
    cityAlt: '重庆',
    avatarImg: 'src/assets/avatarImg/logo21@2x.png',  
    nameAlt: '菜老包',
    dateAlt: '1120',
    highlight: '',  // 待补充亮点标签图片
    highlightAlt: '食材夫妇代运营'
  }),
  makeNode(22, 'node-r6-2', {
    bubbleCity: cityBubbles['重庆'],
    cityAlt: '重庆',
    avatarImg: 'src/assets/avatarImg/logo22@2x.png', 
    nameAlt: '玫瑰之约',
    dateAlt: '1120',
    highlight: '',  // 待补充亮点标签图片
    highlightAlt: '浓浓阿里味儿'
  }),
  makeNode(23, 'node-r6-3', {
    bubbleCity: cityBubbles['上海'],
    cityAlt: '上海',
    avatarImg: 'src/assets/avatarImg/logo23@2x.png',  
    nameAlt: '晨光文具',
    dateAlt: '1124',
    highlight: '',
    highlightAlt: ''
  }),
  makeNode(24, 'node-r6-4', {
    bubbleCity: cityBubbles['昆明'],
    cityAlt: '昆明',
    avatarImg: 'src/assets/avatarImg/logo24@2x.png',  
    nameAlt: 'TT美妆',
    dateAlt: '1210',
    highlight: '',
    highlightAlt: ''
  }),
  // 第7行（左→右，较短，2个）
  makeNode(25, 'node-r7-1', {
    bubbleCity: cityBubbles['西安'],
    cityAlt: '西安',
    avatarImg: 'src/assets/avatarImg/logo25@2x.png', 
    nameAlt: '千姿鲜花坊',
    dateAlt: '1218',
    highlight: '',
    highlightAlt: ''
  }),
  makeNode(26, 'node-r7-2', {
    bubbleCity: cityBubbles['深圳'],
    cityAlt: '深圳',
    avatarImg: 'src/assets/avatarImg/logo26@2x.png',  
    nameAlt: '周大生',
    dateAlt: '1224',
    highlight: '',  // 待补充亮点标签图片
    highlightAlt: '即时零售新品类'
  }),
]

// ── IntersectionObserver：进入视口后触发动画 ──
let observer = null

const startAnimation = () => {
  if (isVisible.value) return
  isVisible.value = true

  // 用 requestAnimationFrame 驱动 clipHeight 从 0 → 1224
  // 时长 PATH_DURATION 秒，ease-in-out 缓动
  const totalFrames = PATH_DURATION * 60
  let frame = 0

  const easeInOut = (t) => t < 0.5 ? 2 * t * t : -1 + (4 - 2 * t) * t

  const tick = () => {
    frame++
    const progress = Math.min(frame / totalFrames, 1)
    clipHeight.value = easeInOut(progress) * 1224
    if (progress < 1) requestAnimationFrame(tick)
  }

  requestAnimationFrame(tick)
}

onMounted(() => {
  observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          startAnimation()
          observer.disconnect()
        }
      })
    },
    { threshold: 0.15 }
  )
  if (rootEl.value) observer.observe(rootEl.value)
})

onUnmounted(() => {
  observer && observer.disconnect()
})
</script>

<style scoped>
/* 整体容器 */
.m6-wrap {
  position: relative;
  overflow: hidden;
  padding: 18px 12px 24px;
}

/* 标题 */
.m6-title {
  position: relative;
  z-index: 1;
}

/* 背景装饰：上方切图 */
.deco-top {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 170px;
  object-fit: cover;
  object-position: center top;
  pointer-events: none;
  z-index: 0;
}

/* 背景装饰：下方切图 */
.deco-bottom {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 161px;
  object-fit: cover;
  object-position: center bottom;
  pointer-events: none;
  z-index: 0;
}

/* 路径容器 */
.path-wrap {
  position: relative;
  z-index: 1;
  width: 100%;
  margin-top: 50px;
}

/* SVG 路径 */
.path-svg {
  display: block;
  width: 100%;
  height: auto;
}

/* 商家节点：绝对定位在 path-wrap 内 */
.merchant-node {
  position: absolute;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 60px;
  z-index: 2;

  /* 初始状态：缩小 + 透明 */
  opacity: 0;
  transform: translate(-50%, -60%) scale(0);
  /* 动画默认关闭，进入视口后由 is-visible 触发 */
}

/* 进入视口后触发弹性入场动画，延迟由 CSS 变量 --delay 控制 */
.merchant-node.is-visible {
  animation: node-spring 0.5s cubic-bezier(0.34, 1.08, 0.64, 1) both;
  animation-delay: var(--delay, 0s);
}

/* 弹性缩放弹出关键帧（Spring effect） */
@keyframes node-spring {
  0% {
    opacity: 0;
    transform: translate(-50%, -60%) scale(0);
  }
  60% {
    opacity: 1;
    transform: translate(-50%, -60%) scale(1.05);
  }
  80% {
    transform: translate(-50%, -60%) scale(0.98);
  }
  100% {
    opacity: 1;
    transform: translate(-50%, -60%) scale(1);
  }
}

/* ── 第1行（左→右）top=7% ── */
.node-1 { left: 13%;    top: 7%; }
.node-2 { left: 37.67%; top: 7%; }
.node-3 { left: 62.33%; top: 7%; }
.node-4 { left: 87%;    top: 7%; }

/* ── 第2行（右→左）top=23.67% ── */
.node-r2-1 { left: 87%;    top: 23.67%; }
.node-r2-2 { left: 62.33%; top: 23.67%; }
.node-r2-3 { left: 37.67%; top: 23.67%; }
.node-r2-4 { left: 13%;    top: 23.67%; }

/* ── 第3行（左→右）top=40.33% ── */
.node-r3-1 { left: 13%;    top: 40.33%; }
.node-r3-2 { left: 37.67%; top: 40.33%; }
.node-r3-3 { left: 62.33%; top: 40.33%; }
.node-r3-4 { left: 87%;    top: 40.33%; }

/* ── 第4行（右→左）top=57% ── */
.node-r4-1 { left: 87%;    top: 57%; }
.node-r4-2 { left: 62.33%; top: 57%; }
.node-r4-3 { left: 37.67%; top: 57%; }
.node-r4-4 { left: 13%;    top: 57%; }

/* ── 第5行（左→右）top=73.67% ── */
.node-r5-1 { left: 13%;    top: 73.67%; }
.node-r5-2 { left: 37.67%; top: 73.67%; }
.node-r5-3 { left: 62.33%; top: 73.67%; }
.node-r5-4 { left: 87%;    top: 73.67%; }

/* ── 第6行（右→左）top=90.33% ── */
.node-r6-1 { left: 87%;    top: 90.33%; }
.node-r6-2 { left: 62.33%; top: 90.33%; }
.node-r6-3 { left: 37.67%; top: 90.33%; }
.node-r6-4 { left: 13%;    top: 90.33%; }

/* ── 第7行（左→右，较短，2个）top=107% ── */
.node-r7-1 { left: 13%;    top: 107%; }
.node-r7-2 { left: 37.67%; top: 107%; }

/* 底部结语 */
.ending {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  gap: 10px;
  margin-top: 120px;
  padding: 0 4px;
}

.ending-line {
  flex: 1;
  height: 1px;
  background: #DDDDDD;
}

.ending-text {
  font-size: 11px;
  color: #999;
  white-space: nowrap;
  flex-shrink: 0;
}
</style>
