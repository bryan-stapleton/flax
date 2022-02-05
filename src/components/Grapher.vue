<template>
<GChart
    type="BubbleChart"
    :data="dataset"
    :options="chart_options"
/>
</template>

<script>
import { GChart } from 'vue-google-charts'

export default {
    name: 'Grapher',
    components: {
        GChart
    }, 
    props: {
        dataset: {type: [ Array, Object ]},
        chart_options:  {type: [ Array, Object ]}
    },
    data () {
        return {}
    }
}
</script>