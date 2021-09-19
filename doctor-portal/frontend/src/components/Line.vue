<template>
<div id="gd"></div>
</template>

<script lang="">
import { defineComponent } from 'vue';
import Plotly from "plotly.js-dist-min"
export default defineComponent({
  name: 'LineChart',
  data(){
    return {
      y: []
    }
  },
  
  mounted(){
    this.axios.get("https://hackmit2021-backend.azurewebsites.net/patient/1").then(resp => {
      console.log(resp.data)
      // testData.datasets[0].label = resp.data.glucoses[0].resource.subject.display
      for( var i = 0; i < resp.data.glucoses.length; i++){
        // console.log(testData.datasets[0].data)
        this.y.push(parseInt(resp.data.glucoses[i].resource.text.div))
      }
      console.log(this.y)
      Plotly.newPlot("gd", /* JSON object */ {
          "data": [{ "y": this.y }],
          "layout": { "width": 600, "height": 400}
      })
      
    })
    
  },

  
});
</script>