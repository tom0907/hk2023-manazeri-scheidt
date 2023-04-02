<template>
  <div class="header">
    <a href="https://www.scheidt-bachmann.sk/sk/"
      ><img src="../images/sblogo.png" class="logo"
    /></a>
  <LanguageSwitcher />
  </div>
</template>

<style>
.header {
    background-color: #fdc200;
    border-bottom: 4px solid #fdc200;
    justify-content: center;
    align-items: center;
    padding: 25px 0;
    position: fixed;
    left: 0;
    right: 0;
    top: 0;
    display: flex;
    z-index: 1000;
  }
  
  /* Add styles to the logo image */
  .logo {
    width: 230px;
    height: 30px;
    object-fit: contain;
  }
</style>

<script>
import axios from "axios";
import LanguageSwitcher from "./LanguageSwitcher.vue";

export default {
  name: "NavigationBar",
  components: {
    LanguageSwitcher,
  },
  data() {
    return {
    };
  },
  methods: {
  },
  mounted: function () {
  },
};
</script>
