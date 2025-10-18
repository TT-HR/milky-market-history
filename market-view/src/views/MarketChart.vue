<template>
  <div ref="chartRef" class="w-2/3 h-200 mx-auto"></div>
</template>

<script setup lang="ts">
import * as echarts from 'echarts'
import { onMounted, ref } from 'vue'
import { getItemCost } from '@api/MarketCost.ts'

const chartRef = ref<HTMLDivElement | null>(null)

onMounted(async () => {
  const params = {
    startTime: '',
    endTime: '',
    egg: 'egg'
  }
  const res = await getItemCost(params)
  const { data, series } = res.data


  if (!chartRef.value) return
  const chart = echarts.init(chartRef.value)

  const option = {
    title: {
      text: '物品价格变化'
    },
    tooltip: {
      trigger: 'axis'
    },
    legend: {
      data: ['买入', '卖出']
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    toolbox: {
      feature: {
        saveAsImage: {}
      }
    },
    xAxis: {
      type: 'category',
      boundaryGap: false,
      data: data
    },
    yAxis: {
      type: 'value'
    },
    series: series
  }

  chart.setOption(option)

  // 响应式调整
  window.addEventListener('resize', () => chart.resize())
})
</script>

<style scoped>
/* 高度固定或使用 Tailwind 类 h-80 */
</style>
