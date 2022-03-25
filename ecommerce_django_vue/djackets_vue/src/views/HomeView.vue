<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">Welcome to Djacket</p>
        <p class="subtitle">The Best Jacket Store Online</p>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>
      <ProductBox
        v-for="product in latestProducts"
        v-bind:key="product.id"
        v-bind:product="product"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ProductBox from '@/components/ProductBox.vue';
export default {
  name: 'HomeView',
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {
    ProductBox,
  },
  mounted() {
    document.title = 'Home | Djackets';
    this.getLatestProducts();
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true);
      await axios
        .get('/api/v1/latest-products/')
        .then((response) => {
          this.latestProducts = response.data;
        })
        .catch((err) => {
          console.log('Error', err);
        });
      this.$store.commit('setIsLoading', false);
    },
  },
};
</script>
