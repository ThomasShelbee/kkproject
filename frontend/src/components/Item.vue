<script>
import {api_host} from "@/api.js"

export default {
    name: "Item",
    methods: {
        navigateToItem() {
            this.$router.push('/item/' + this.item.url);
        }
    },
    props: ['item'],
    data() {
        return {
            showItem: false,
            host: api_host
        }
    }
}
</script>

<template>
    <div class="text-center col-12 col-md-6 col-lg-4 p-5" style="text-align: center;" @click="navigateToItem()">

            <div @mouseover="showItem = true" @mouseleave="showItem = false">
                <img v-show="showItem" style="width: 100%; text-decoration: none;" :src="host + '/api/get-picture/' + this.item.url + '2'" alt="">
                <img v-show="!showItem" style="width: 100%; text-decoration: none;" :src="host + '/api/get-picture/' + this.item.url" alt="">
            </div>
            <h2 style="color: #FFFFFF; ">{{this.item.title}}</h2>
            <h5 style="color: #FFFFFF;">{{this.item.price}}p</h5>
    </div>
</template>

<style scoped>
</style>