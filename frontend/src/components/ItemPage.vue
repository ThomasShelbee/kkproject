<script>
import UpperPart from "@/components/UpperPart.vue";
import messageBus from '@/MessageBus.js';
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
            this.cartItems.push({url: this.item.url, size: this.itemSize, title: this.item.title, quantity: 1, price: this.item.price});
            this.openCart()
        }
    },
    data() {
        return {
            url: this.$route.params.url,
            item: this.items.find(item => item.url === this.$route.params.url),
            isCartVisible: false,
            itemSize: null
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
                <div style="max-width: 30vw; margin: 10px auto">
                    <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
                        <div class="carousel-indicators">
                            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0"
                                    class="active" aria-current="true" aria-label="Slide 1"></button>
                            <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"
                                    aria-label="Slide 2"></button>
                        </div>
                        <div class="carousel-inner">
                            <div class="carousel-item active">
                                <img :src="'http://localhost:8080/api/get-picture/' + this.item.url"
                                     class="d-block w-100"
                                     alt="">
                            </div>
                            <div class="carousel-item">
                                <img :src="'http://localhost:8080/api/get-picture/' + this.item.url +'2'"
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

                    <select name="size" v-on="itemSize">

                        <option v-show="this.item.s_size > 0" value="s_size">S</option>

                        <option v-show="this.item.m_size > 0" value="m_size">M</option>

                        <option v-show="this.item.l_size > 0" value="l_size">L</option>

                        <option v-show="this.item.xl_size > 0" value="xl_size">XL</option>

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
</style>