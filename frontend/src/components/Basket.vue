<script>
import {api_host} from "@/api.js"
import {getPromos} from "@/api";
import {sendPurchase} from "@/api";

export default {
    name: "Basket",
    props: ['items'],
    data() {
        return {
            localPurchase: {
                name: "",
                phone: "",
                email: "",
                promo: "",
                discount: 0,
                sum: null,
                cart: null
            },
            localPromo: null,
            promos: getPromos(),
            mainSum: null,
            host: api_host,
        };
    },
    methods: {
        // Метод для сохранения изменений или добавления нового артиста
        Purchase() {
            this.localPurchase.promo = this.promoUsed.title;
            this.localPurchase.cart = this.cartItems;
            this.localPurchase.sum = this.mainSum;
            this.localPurchase.discount = this.promoUsed.price;
            sendPurchase(this.localPurchase);
        },
        checkPromo(localPromo) {
            let localMessage = "Такого промокода нет";
            if (this.promoUsed.price !== 0) {
                localMessage = "Промокод уже использован";
            }
            else {
                for (let promo in this.promos) {
                    if (this.promos[promo].title === localPromo) {
                        this.promoUsed.title = this.promos[promo].title;
                        this.promoUsed.price = this.promos[promo].price;
                        localMessage = "Промокод успешно применен";
                        this.promos.pop(promo.id);
                        break;
                    }
                }
            }
            this.message.text = localMessage;
            return this.checkSum();
        },
        changeQuantityLess(item) {
            if (item.quantity === 1) {
                this.cartItems.pop(item)
            }
            else {
                item.quantity -= 1;
            }
        },
        changeQuantityMore(item) {
            item.quantity += 1;
        },
        removeItem(item) {
            this.cartItems.pop(item)
        },
        checkSum() {
            let localSum = 0;
            for (let item in this.cartItems) {
                localSum += this.cartItems[item].price * this.cartItems[item].quantity;
            }
            console.log(this.promoUsed);
            this.mainSum = localSum - this.promoUsed.price;
            return this.mainSum;
        },
        closeBasket() {
            this.$emit("closeBasket");
        },
    },
    computed: {
        sum() {
            return this.checkSum();
        }
    },
    async mounted() {
        this.promos = await getPromos();
    }
}
</script>

<template>
    <div class="basket">
        <div
            class="modal fade show"
            style="display: block; background-color: rgba(0, 0, 0, 0.5);">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h3>Ваш заказ:</h3>
                        <button type="button" class="btn-close" aria-label="Закрыть" @click="closeBasket"></button>
                    </div>
                    <div class="modal-body">
                        <div id="upper-part">
                            <ul class="list-group">
                                <li class="list-group-item" v-for="item in this.cartItems">
                                    <span><img style="max-width:50px" :src="host + '/api/get-picture/' + item.url" alt=""></span>
                                    <span>{{item.title}}: </span>
                                    <span>{{item.size}}</span>
                                    <span><button @click="changeQuantityLess(item); checkSum()" type="submit">-</button></span>
                                    <span>{{item.quantity}}</span>
                                    <span><button @click="changeQuantityMore(item); checkSum()" type="submit">+</button></span>
                                    <span>{{item.price}}P</span>
                                    <span><button @click="removeItem(item); checkSum()" type="submit">x</button></span>
                                </li>
                            </ul>

                        </div>

                        <div id="lower-part">
                            <form @submit.prevent="Purchase">
                                <div class="mb-3">
                                    <label for="purchase-name" class="form-label">ФИО</label>
                                    <input
                                        id="purchase-name"
                                        v-model="localPurchase.name"
                                        type="text"
                                        class="form-control"
                                        placeholder="Иванов Иван Иванович"
                                        required
                                    />
                                </div>

                                <div class="mb-3">
                                    <label for="purchase-phone" class="form-label">Номер телефона</label>
                                    <input
                                        id="purchase-phone"
                                        v-model="localPurchase.phone"
                                        type="tel"
                                        class="form-control"
                                        placeholder="+7 (999) 999-99-99"
                                        required
                                    />
                                </div>

                                <div class="mb-3">
                                    <label for="purchase-email" class="form-label">Почта</label>
                                    <input
                                        id="purchase-email"
                                        v-model="localPurchase.email"
                                        type="email"
                                        class="form-control"
                                        placeholder="Email"
                                        required
                                    />
                                </div>

                                <div class="mb-3">
                                    <label for="purchase-promo" class="form-label">Промокод</label>
                                    <form id="purchase-promo" @submit.prevent="checkPromo(localPromo)">
                                        <div v-if="this.promoUsed.price !== 0">
                                            <input
                                                type="text"
                                                class="form-control"
                                                placeholder="Промокод"
                                                :value="this.promoUsed.title"
                                                required
                                            />
                                        </div>
                                        <div v-else>
                                            <input
                                                v-model="localPromo"
                                                type="text"
                                                class="form-control"
                                                placeholder="Промокод"
                                                required
                                            />
                                        </div>
                                        <span><button type="submit">Активировать</button></span>
                                    </form>
                                    <p>{{this.message.text}}</p>
                                </div>
                                <h5>Сумма заказа: {{sum}}P</h5>
                                <!-- Кнопки -->
                                <div class="d-flex justify-content-between">
                                    <a href="/"><button type="submit" class="btn btn-success">Заказать</button></a>
                                </div>
                            </form>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>