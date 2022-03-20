<script>
import { Pie } from 'vue-chartjs';

export default {
  extends: Pie,
  mounted() {
    this.renderChart({
      labels: ['Red', '1', '2', '3'],
      datasets: [
        {
          label: 'Power Consumption',
          data: [2, 5, 4, 8],
          backgroundColor: [
            'rgba(70, 100, 40)',
            'rgba(20, 180, 200)',
          ],
        },
      ],
    }, {
      responsive: false,
    });
  },
};
</script>
