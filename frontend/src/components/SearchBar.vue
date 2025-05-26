<script>
export default {
    name: "SearchBar",
    props: {
        // Проп "search": получает текущее значение строки поиска от родительского компонента
        search: {
            type: String,
            required: true
        },
    },
    emits: ['update:search'], // Определяем событие, которое будет отправлять изменения строки поиска
    methods: {
        // Метод для обработки ввода текста в строку поиска
        updateSearch(event) {
            // Отправляем значение текста в родительский компонент через событие "update:search"
            this.$emit('update:search', event.target.value);
        }
    }
}
</script>

<template>
    <div class="search-bar mb-3">
        <!-- Поле ввода для строки поиска -->
        <input
            type="text"
        class="form-control"
        :value="search"
        @input="updateSearch"
        placeholder="Поиск задачи..."
        />
    </div>
</template>

<style scoped>
</style>