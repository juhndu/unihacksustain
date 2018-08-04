<template>
	<div class="card" @click="openModal()">
        <div class="image">
            <img :src="data.image_url">
        </div>
        <div class="bottom-content">
                <div class="bottom-content-title align-top">
                    <h2>{{ data.name }}</h2>
                    <h3>{{ data.location }}</h3>
                </div>

                <div class="align-bottom">
                    <small>Sustainability: </small>
                    <star-rating 
                        v-model="rating"
                        v-bind:star-size="20"
                        v-bind:increment="0.5"
                        :border-width="0"
                        active-color="rgb(64, 207, 71)">
                    </star-rating>
                    <small>Zomato: </small>
                    <star-rating 
                        v-model="rating"
                        v-bind:star-size="15"
                        v-bind:increment="0.5"
                        :border-width="0"
                        active-color="rgb(64, 207, 71)" >
                    </star-rating>
                </div>
        </div>
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
    .bottom-content{
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }


    .bottom-content-title{
        display: flex;
        flex-direction: column;
    }
    h2{
        color: #4f4f4f;
        margin: 0px;
    }
    h3{
        margin: 0px;
        color: rgb(131, 131, 131);
    }
    .image{
        height: 150px;
        overflow: hidden;
    }
    img{
        border-radius: 5px;
        width: 100%;
    }
    .bottom-content{

        padding: 15px;
    }
    .card{
        border-radius: 5px;
        background-color: rgb(232, 242, 232);
        box-shadow: 0 0 12px 0 hsla(0, 0%, 0%, 0.2);
        display: flex;
        flex-direction: column;
        text-align: left;
    }
    .card:hover{
        box-shadow: 0 0 12px 0 hsla(0, 0%, 0%, 0.5);
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

</style>
