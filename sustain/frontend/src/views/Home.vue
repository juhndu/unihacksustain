<template>
	<div class="home">
		<navigation></navigation>
		<location-services></location-services>
		<div class="cards">
			<card 
				v-for="restaurant in restaurants"
				v-bind:data="{ 
					id: restaurant.id,
					name: restaurant.name,
					rating: restaurant.rating,
					image_url: restaurant.image_url
				}"
				
				></card>
		</div>
		<div class="footer">

			<h2>This is the footer</h2>

		</div>


		<modal v-if="this.application.modal_open"></modal>
	</div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Navigation from '@/components/Nav.vue';
import Card from '@/components/Card.vue';
import LocationServices from '@/components/LocationServices.vue';
import Modal from '@/components/Modal.vue';

export default {
	name: 'home',
	components: {
		HelloWorld,
		Navigation,
		Card,
		LocationServices,
		Modal
	},
	computed: {
		restaurants (){
			return this.$store.state.restaurants;
		},
		application (){
			return this.$store.getters.applicationState;
		}
	}
}
</script>
<style scoped>
	.cards{
		margin: 20px;
		display: grid;
		grid-template-columns: 1fr 1fr;
		grid-gap: 20px;
	}

	@media only screen and (max-width: 600px){
		.cards{
			grid-template-columns: 1fr;
		}
	}

	.footer{
		background-color: gray;
		padding: 30px;
	}

</style>
