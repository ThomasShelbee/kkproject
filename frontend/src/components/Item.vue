<script>
import {api_host} from "@/api.js"

export default {
    name: "Item",

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
    <div class="text-center col-12 col-md-6 col-lg-4 p-5" style="text-align: center;" @click="$router.push('/item/' + this.item.url)">

            <div @mouseover="showItem = true" @mouseleave="showItem = false">
                <img v-show="showItem" style="width: 100%; text-decoration: none;" :src="host + '/api/get-picture/' + this.item.url + '2'" alt="">
                <img v-show="!showItem" style="width: 100%; text-decoration: none;" :src="host + '/api/get-picture/' + this.item.url" alt="">
            </div>
            <h2 style="color: #FFFFFF; ">{{this.item.title}}</h2>
            <h5 style="color: #FFFFFF;">{{this.item.price}}p</h5>
        <!--<span><button v-show="this.item.s_size > 0">S</button></span>
        <span><button v-show="this.item.m_size > 0">M</button></span>
        <span><button v-show="this.item.l_size > 0">L</button></span>
        <span><button v-show="this.item.xl_size > 0">XL</button></span>-->
    </div>
</template>

<style scoped>
</style>