<template>
  <div>
    <nav>
      <GlobalNavigation />
    </nav>
    <router-view/>
  </div>
</template>

<script>
import GlobalNavigation from '@/components/GlobalNavigation.vue'

export default {
  components: {
    GlobalNavigation
  }
}
</script>

<style lang="stylus">
body {
  margin: 0
}
</style>
