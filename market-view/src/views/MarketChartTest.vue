<template>
  <div class="p-6 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-4">
    <div
      v-for="item in items"
      :key="item.id"
      class="bg-white p-3 rounded-lg shadow hover:shadow-md transition cursor-pointer"
      @click="openChart(item)"
    >
      <h3 class="font-medium text-gray-800 truncate">{{ item.name }}</h3>
      <p class="text-sm text-gray-500">销量：{{ item.sales }}</p>
    </div>

    <!-- 弹窗图表 -->
    <div
      v-if="selectedItem"
      class="fixed inset-0 bg-black/50 flex justify-center items-center z-50"
      @click.self="selectedItem = null"
    >
      <div class="bg-white p-6 rounded-xl w-[80vw] max-w-2xl shadow-lg">
        <h2 class="text-lg font-semibold mb-3">{{ selectedItem.name }}</h2>
        <div ref="chartRef" class="w-full h-80"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'
import * as echarts from 'echarts'

// 商品列表
const items = ref([
  { id: 1, name: '户外灯', sales: 50 },
  { id: 2, name: '折叠椅', sales: 32 },
  { id: 3, name: '帐篷', sales: 21 },
  { id: 4, name: '登山鞋', sales: 40 },
])

const selectedItem = ref(null)
const chartRef = ref(null)
let chartInstance = null

// 假数据（7天）
const fakeChartData = {
  dates: ['2025-10-12','2025-10-13','2025-10-14','2025-10-15','2025-10-16','2025-10-17','2025-10-18'],
  series: {
    buy: [12, 15, 14, 18, 20, 22, 19],
    sell: [8, 10, 9, 13, 14, 17, 16]
  }
}

// 点击商品打开图表
async function openChart(item) {
  selectedItem.value = item
  await nextTick() // 等DOM渲染完再加载图表

  // 初始化 ECharts
  if (!chartInstance) chartInstance = echarts.init(chartRef.value)

  chartInstance.setOption({
    title: { text: '最近7天买入卖出趋势' },
    tooltip: { trigger: 'axis' },
    legend: { data: ['买入', '卖出'] },
    xAxis: { type: 'category', data: fakeChartData.dates },
    yAxis: { type: 'value' },
    series: [
      { name: '买入', type: 'line', data: fakeChartData.series.buy },
      { name: '卖出', type: 'line', data: fakeChartData.series.sell },
    ],
  })
}
</script>
