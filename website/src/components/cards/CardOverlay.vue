<template>
  <modal class="wrapper" name="wrapper"
    :draggable="true"
    transition="none"
    classes="wrapper"
    width="35%"
    height="60%"
    :shiftX="X"
    :shiftY="Y"
    @closed="$emit('closed')"
    :clickToClose="false"
  >
    <slot></slot>
  </modal>
</template>

<script>
export default {
  name: 'CardModal',
  props: {
    X: {
      Type: Number,
      default: 0.5,
    },
    Y: {
      Type: Number,
      default: 0.5,
    },
  },
  components: {
  },
  methods: {
    show() {
      this.$modal.show('wrapper');
    },
    hide() {
      this.$modal.hide('wrapper');
    },
  },
  computed: {
  },
  mounted() {
    this.show();
  },
};
</script>

<style lang="stylus">
.vm--overlay
  background-color: transparent
</style>
