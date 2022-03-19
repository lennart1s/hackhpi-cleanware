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
@import '../assets/theme.styl';

.router-link-exact-active
  background-color: $primary !important

.tab
  display: flex
  width: 14ch
  background-color: $secondary
  height: 100%
  text-align: center
  text-decoration: none
  justify-content: center
  align-items: center
  color: white
  margin: 0 .1em
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  &:hover
    background-color: $primary
    cursor: pointer
</style>
