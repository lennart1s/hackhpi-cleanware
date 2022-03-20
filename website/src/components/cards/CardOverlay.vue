<template>
  <modal class="wrapper" name="wrapper"
    :draggable="Draggable"
    transition="none"
    classes="wrapper"
    :width="Width"
    :height="Height"
    :shiftX="X"
    :shiftY="Y"
    @closed="$emit('closed')"
    :clickToClose="true"
  >
    <slot></slot>
  </modal>
</template>

<script>
export default {
  name: 'CardModal',
  props: {
    ShowOnMount: {
      Type: Boolean,
      default: false,
    },
    Draggable: {
      Type: Boolean,
      default: true,
    },
    X: {
      Type: Number,
      default: 0.5,
    },
    Y: {
      Type: Number,
      default: 0.5,
    },
    Width: {
      Type: String,
      default: '300px',
    },
    Height: {
      Type: String,
      default: '250px',
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
    if (this.ShowOnMount) {
      this.show();
    }
  },
};
</script>

<style lang="stylus">
.vm--overlay
  background-color: transparent
</style>
