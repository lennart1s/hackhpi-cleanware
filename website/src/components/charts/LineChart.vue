<script>
import { Line } from 'vue-chartjs';

export default {
  extends: Line,
  mounted() {
    this.renderChart({
      labels: ['-8h', '-7h', '-6h', '-5h', '-4h', '-3h', '-2h', '-1h', '-0h'],
      datasets: [
        {
          label: 'Total Energy Consumption',
          data: [2, 5, 4, 8],
          backgroundColor: 'rgba(245, 90, 0, 0.3)',
        },
        {
          label: 'Reneawble Energy',
          data: [1, 6, 4, 7],
          backgroundColor: 'rgba(32, 212, 41, 0.3)',
        },
      ],
    }, {
      responsive: false,
    });
  },
};
</script>

<style scoped lang="stylus">
canvas
  width: 800px
  height: 400px
</style>
