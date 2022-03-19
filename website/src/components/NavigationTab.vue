<template>
  <router-link :to="to" class="tab">
    <slot/>
  </router-link>
</template>

<script>
export default {
  name: 'NavigationTab',
  props: {
    to: Object,
  },
};
</script>

<style scoped lang="stylus">
.tab
  width: 14ch
  background-color: rgba(0, 0, 0, 0.2)
  height: 100%
  text-align: center
  &:hover
    background-color: rgba(0, 0, 0, 0.4)
    cursor: pointer
</style>
