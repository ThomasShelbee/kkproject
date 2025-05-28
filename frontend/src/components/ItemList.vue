<script>
import Item from "@/components/Item.vue";
import SearchBar from "@/components/SearchBar.vue";
import Basket from "@/components/Basket.vue";
import UpperPart from "@/components/UpperPart.vue";
import LowerPart from "@/components/LowerPart.vue";


export default {
    name: "ItemList",
    components: {LowerPart, UpperPart, Item, SearchBar, Basket},
    data() {
        return {
            searchText: "",
            isBasketVisible: false, // Показывать/скрывать модальное окно редактора
            editingTask: null,
            localItems: this.items,
        }
    },
    computed: {
        filteredItems() {
            const search = this.category.page.toLowerCase();
            return this.items.filter(item =>
                item.url.toLowerCase().includes(search)
            );
        }
    },
    methods: {
        openBasket() {
            this.isBasketVisible = true;
        },
        // Закрывает редактор
        closeBasket() {
            this.isBasketVisible = false;
        },
        changeCategory() {
            if (this.category.page === "all") {
                this.localItems = this.items;
            }
            else {
                this.localItems = this.filteredItems;
            }
        },
        reload() {
            window.location.reload();
        }
    },
    mounted() {
        if (this.category.page === "all") {
            this.localItems = this.items;
        }
        else {
            this.localItems = this.filteredItems;
        }
    }
}
</script>

<template>
    <UpperPart @changeCategory="changeCategory" @purchase="openBasket()"></UpperPart>
    <div class="row" style="margin-left: 10%; margin-right: 10%;">
        <Item v-for="item in this.localItems" :item="item" class="product-card"></Item>
    </div>

    <div v-show="isBasketVisible">
        <Basket @reload="reload()" @closeBasket="closeBasket"></Basket>
    </div>
    <!--<LowerPart></LowerPart>-->
</template>

<style scoped>
.product-card {
    position: relative;
    background: none;
    border-radius: 30px;
    transition: all 0.4s cubic-bezier(0.23, 1, 0.32, 1);
    max-width: 100%;
    max-height: 100%;
    cursor: pointer;
}

.product-card:hover {
    box-shadow: 0 0 60px rgba(255, 255, 255, 0.3);
    background: #400000;
    transform: scale(1.02);
}
</style>