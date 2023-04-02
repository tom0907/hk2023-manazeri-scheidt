<template>
  <div class="select-lang">
    <select v-model="$i18n.locale">
      <option :key="`locale-sk`" value="sk">🇸🇰&emsp;SK</option>
      <option :key="`locale-en`" value="en">🇬🇧&emsp;EN</option>
    </select>
  </div>
</template>

<script>
export default {
  name: "LocaleSwitcher",
  data() {
    return { locales: ["sk", "en"] };
  },
};
</script>

<style>
*,
*::before,
*::after {
  box-sizing: border-box;
}

.select-lang {
  appearance: none;
  background-color: white;
  border: none;
  font-family: inherit;
  font-size: inherit;
  cursor: inherit;
  top: 20px;
  position: fixed;
  right: 50px;
  z-index: 1050;
  text-align: right !important;
}

select::-ms-expand {
  display: none;
  font-size: 0.5rem;
}

:root {
  --select-focus: blue;
  --select-arrow: var(--select-border);
}

.select {
  max-width: 3.5ch;
  font-size: 2.6rem;
  cursor: pointer;
  background-color: transparent;
  display: inline-block;
}

select option {
  font-size: 1rem;
}
</style>