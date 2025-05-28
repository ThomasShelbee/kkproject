<script>

import {api_host} from "@/api.js"

export default {
    name: "UpperPart",
    methods: {
        openBasket() {
            this.$emit("purchase");
        },
        changeCategory(cat) {
            this.category.page = cat;
            this.$emit("changeCategory");
        }
    },
    data() {
        return {
            host: api_host,
        }
    }
}
</script>

<template>
    <h1 style="margin-top: 30px; text-align: center;"><a href="/" style="text-decoration: none; color: white">KK CLOTHING<sup>&reg</sup></a></h1>
    <div class="position-absolute top-0 end-0" style="margin-top: 15px; margin-right: 15px">
        <button class="btn btn-primary btn-sm border-0" style="border: none; padding: 0; background: none;" @click="openBasket()" type="button">
            <img class="cart" style="text-decoration: none;" :src="host + '/api/get-picture/basket'" alt="">
        </button>
    </div>
    <p style="margin-top: 30px; border-top: 5px solid white;"></p>
    <div style="margin-top: 30px;">
        <div class="row" style="margin-left: 10vw; margin-right: 10vw">
            <!--:class="{'selected': this.localCategory === 'all'}" -->
            <button v-if="category.page === 'all'" @click="changeCategory('all')" class="selected col-12 col-md-4 col-lg-2 p-1">Всё</button>
            <button v-else @click="changeCategory('all')" class="notSelected col-md-4 col-lg-2 p-1">Всё</button>

            <button v-if="category.page === 'hoodie'" @click="changeCategory('hoodie')" class="selected col-12 col-md-4 col-lg-2 p-1">Худи</button>
            <button v-else @click="changeCategory('hoodie')" class="notSelected col-12 col-md-4 col-lg-2 p-1">Худи</button>

            <button v-if="category.page === 'long-sleeve'" @click="changeCategory('long-sleeve')" class="selected col-12 col-md-4 col-lg-2 p-1">Лонгсливы</button>
            <button v-else @click="changeCategory('long-sleeve')" class="notSelected col-12 col-md-4 col-lg-2 p-1">Лонгсливы</button>

            <button v-if="category.page === 't-shirt'" @click="changeCategory('t-shirt')" class="selected col-12 col-md-4 col-lg-2 p-1">Футболки</button>
            <button v-else @click="changeCategory('t-shirt')" class="notSelected col-12 col-md-4 col-lg-2 p-1">Футболки</button>

            <button v-if="category.page === 'cap'" @click="changeCategory('cap')" class="selected col-12 col-md-4 col-lg-2 p-1">Кепки</button>
            <button v-else @click="changeCategory('cap')" class="notSelected col-12 col-md-4 col-lg-2 p-1">Кепки</button>

            <button v-if="category.page === 'accessory'" @click="changeCategory('accessory')" class="selected col-12 col-md-4 col-lg-2 p-1">Аксессуары</button>
            <button v-else @click="changeCategory('accessory')" class="notSelected col-12 col-md-4 col-lg-2 p-1">Аксессуары</button>
        </div>
    </div>
    <p style="margin-top: 30px; border-top: 5px solid white;"></p>
</template>

<style scoped>
.selected {
    color: #808080;
    border: none;
    padding: 0;
    background: none;
    border-bottom: 2px solid #808080;
}
.notSelected {
    color: #FFFFFF;
    border: none;
    padding: 0;
    background: none;
    border-bottom: 2px solid white;
}
.cart {
    @media (max-width: 600px) {
        margin-top: 10px;
        max-width: 50px;
    }
    @media (min-width: 600px) {
        margin-top: 10px;
        max-width: 70px;
    }
}
</style>