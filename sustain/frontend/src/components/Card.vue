<template>
	<div class="card">
        <h2>Restarant Name</h2>
        <p>Testing</p>
        <star-rating v-model="rating"></star-rating>
        <div class="bottom-modal">
            <div class="button">Rate</div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import StarRating from 'vue-star-rating'

export default {
	name: 'card',
	components: {
        StarRating
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


</style>
