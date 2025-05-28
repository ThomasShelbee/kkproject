<script>
import {api_host} from "@/api.js"
import UpperPart from "@/components/UpperPart.vue";
import LowerPart from "@/components/LowerPart.vue";
import Basket from "@/components/Basket.vue";

export default {
    name: "ItemPage",
    components: {Basket, LowerPart, UpperPart},
    methods: {
        openCart() {
            this.isCartVisible = true;
        },
        // Закрывает редактор
        closeCart() {
            this.isCartVisible = false;
        },
        changeCategory() {
            this.$emit("changeCategory", this.category);
            this.$router.push('/');
        },
        addToCart() {
            let a = 0;
            for (let item of this.cartItems) {
                if (item.url === this.item.url) {
                    if (item.size === this.itemSize) {
                        item.quantity++;
                        a = 1;
                    }
                }
            }
            if (a === 0) {
                this.cartItems.push({url: this.item.url, size: this.itemSize, title: this.item.title, quantity: 1, price: this.item.price});
            }
            this.openCart()
        }
    },
    data() {
        return {
            url: this.$route.params.url,
            item: this.items.find(item => item.url === this.$route.params.url),
            isCartVisible: false,
            itemSize: "S",
            host: api_host,
        }
    }
}
</script>

<template>
    <UpperPart @changeCategory="changeCategory"
               @purchase="openCart()"></UpperPart>
    <div v-show="isCartVisible">
        <Basket @closeBasket="closeCart"></Basket>
    </div>
    <div class="container">
        <div class="row">
            <div class="col-md-6">
                <div class="carousel" style="margin: 10px auto">
                    <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
                        <div class="carousel-indicators">
                            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0"
                                    class="active" aria-current="true" aria-label="Slide 1"></button>
                            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"
                                    aria-label="Slide 2"></button>
                        </div>
                        <div class="carousel-inner">
                            <div class="carousel-item active">
                                <img :src="host + '/api/get-picture/' + this.item.url"
                                     class="d-block w-100"
                                     alt="">
                            </div>
                            <div class="carousel-item">
                                <img :src="host + '/api/get-picture/' + this.item.url +'2'"
                                     class="d-block w-100"
                                     alt="">
                            </div>
                        </div>
                        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators"
                                data-bs-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Previous</span>
                        </button>
                        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators"
                                data-bs-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Next</span>
                        </button>
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <h1 style="color: #FFFFFF;">{{ this.item.title }}</h1>
                <h4 style="color: #FFFFFF; margin-top: 30px">{{this.item.price}}p</h4>

                    <select name="size" v-model="this.itemSize">

                        <option v-show="this.item.s_size > 0" value="S">S</option>

                        <option v-show="this.item.m_size > 0" value="M">M</option>

                        <option v-show="this.item.l_size > 0" value="L">L</option>

                        <option v-show="this.item.xl_size > 0" value="XL">XL</option>

                    </select>

                <p><a class="btn btn-light" @click="addToCart()">В корзину</a></p>

                <p style="color: #FFFFFF; margin-top: 30px">{{ this.item.description }}</p>
            </div>
        </div>
    </div>


    <LowerPart></LowerPart>
</template>

<style scoped>
.container {
    justify-content: center
}
.carousel {
    @media(max-width: 600px) {
        max-width: 90vw
    }
    @media(min-width: 600px) {
        max-width: 30vw
    }
}
</style>