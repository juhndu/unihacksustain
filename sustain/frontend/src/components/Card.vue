<template>
	<div class="card" @click="openModal()">
        <h4>{{ data.name }}</h4>
        <img :src="data.image_url">
        <star-rating v-model="rating"></star-rating>
    </div>
</template>

<script>
// @ is an alias to /src
import StarRating from 'vue-star-rating'

export default {
    name: 'card',
    props: ['data'],
	components: {
        StarRating
    },
	methods: {
		openModal(){
            this.$store.commit('toggleModal', this.data.id);
		}
	},
    data: function(){
        return {
            rating: 3
        }
    }
}
</script>
<style scoped>
    .card{
        padding: 10px;
        background-color: lightgray;
        display: flex;
        flex-direction: column;
        text-align: left;
    }
    .button{
        min-width: 100px;
        background-color: rgb(255, 136, 0);
        display: flex;
        justify-content: center;
        padding: 10px;
    }
    .bottom-modal{
        display: flex;
        justify-content: flex-end;
    }


    img{
        width: 200px;
    }

</style>
