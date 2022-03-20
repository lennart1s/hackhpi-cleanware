<script>
import { Line } from 'vue-chartjs';

export default {
  extends: Line,
  data: () => ({
    valuesA: [425, 413, 511, 538, 553, 588, 552, 430, 428],
    valuesB: [310, 322, 341, 372, 374, 407, 410, 408, 410],
  }),
  mounted() {
    this.renderChart({
      labels: ['-8h', '-7h', '-6h', '-5h', '-4h', '-3h', '-2h', '-1h', '-0h'],
      datasets: [
        {
          label: 'Total Energy Consumption',
          data: this.valuesA,
          backgroundColor: 'rgba(245, 90, 0, 0.3)',
        },
        {
          label: 'Reneawble Energy',
          data: this.valuesB,
          backgroundColor: 'rgba(32, 212, 41, 0.3)',
        },
      ],
    }, {
      responsive: false,
    });
  },
  methods: {
    update() {

    },
  },
};
</script>

<style scoped lang="stylus">
canvas
  width: 800px
  height: 400px
</style>
