<script>
import { Bar } from 'vue-chartjs';

export default {
  extends: Bar,
  mounted() {
    this.renderChart({
      labels: ['0', '1', '2', '3'],
      datasets: [
        {
          label: 'Power Consumption',
          data: [2, 5, 4, 8],
        },
      ],
    }, {
      responsive: false,
    });
  },
};
</script>
