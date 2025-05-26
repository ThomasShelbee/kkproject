<script>

import {getPromos, getPicture, deletePromoBack} from "@/api";

export default {
    name: "Basket",
    props: ['items'],
    data() {
        return {
            localPurchase: {
                name: "",
                phone: "",
                email: "",

            },
            localPromo: null,
            promoTrue: false,
            error: null,
            promos: getPromos(),
            sum: null,
        };
    },
    methods: {
        // Метод для сохранения изменений или добавления нового артиста
        savePurchase() {
            this.$emit("save", {...this.localPurchase}); // Генерируем событие сохранения с данными артиста
            this.resetForm(); // Очищаем форму после сохранения
        },
        // Сбрасываем форму к исходному состоянию
        resetForm() {
            this.localPurchase = {
                title: ""
            };
        },
        deletePromoFront(promo) {
            this.promos.pop(promo.id);
        },
        checkPromo(localPromo) {
            let localError = "Нет такого промокода";
            for (let promo in this.promos) {
                if (this.promos[promo].name === localPromo) {
                    this.sum -= localPromo.price;
                    localError = "";
                    this.promoTrue = true;
                    deletePromoBack(promo);
                    deletePromoFront(promo);
                    break;
                }
            }
            this.error = localError;
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
                localSum += item.price * item.quantity;
            }
            console.log(localSum);
            return localSum;
        },
        closeBasket() {
            this.$emit("closeBasket");
        },
        purchase() {

        }
    },
    watch: {
        purchase(newPurchase) {
            this.localPurchase = { ...newPurchase };
        }
    },
    async mounted() {
        this.promos = await getPromos();
        this.sum = await this.checkSum();
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
                                    <span><img src="http://localhost:8080/api/get-picture/{{item.url}}" alt=""></span>
                                    <span>{{item.title}}</span>
                                    <span>{{item.size}}</span>
                                    <span><button @click="changeQuantityLess(item)" type="submit">-</button></span>
                                    <span>{{item.quantity}}</span>
                                    <span><button @click="changeQuantityMore(item)" type="submit">+</button></span>
                                    <span>{{item.price}}P</span>
                                    <span><button @click="removeItem(item)" type="submit">x</button></span>
                                </li>
                            </ul>
                            <h5>Сумма заказа: {{checkSum()}}P</h5>
                        </div>

                        <div id="lower-part">
                            <form @submit.prevent="savePurchase">
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
                                        placeholder="+7 999 999 99 99"
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
                                        <input
                                            v-model="localPromo"
                                            type="text"
                                            class="form-control"
                                            placeholder="Промокод"
                                            required
                                        />
                                        <span><button type="submit">Активировать</button></span>
                                    </form>
                                    <p v-if="this.error !== null ">{{this.error}}</p>
                                    <p v-else-if="this.promoTrue">Промокод применен успешно</p>
                                </div>

                                <!-- Кнопки -->
                                <div class="d-flex justify-content-between">
                                    <button @click="purchase()" type="submit" class="btn btn-success">Купить</button>
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