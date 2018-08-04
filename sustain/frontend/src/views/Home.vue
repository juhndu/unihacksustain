<template>
	<div class="home">
		<navigation></navigation>
		<location-services @updatemap="alert()"></location-services>
		<GmapMap
			ref="mapRef"
			:center="{lat: -33.882617, lng: 151.194348}"
			:zoom="15"
			style="height: 300px">
		</GmapMap>

		<div class="cards">
			<card v-if='application.search_data == ""'
				v-for="restaurant in restaurants"
				v-bind:data="{ 
					id: restaurant.id,
					name: restaurant.name,
					rating: restaurant.rating,
					image_url: restaurant.imgUrl,
					sustain_rating: restaurant.sustain_rating,
					location: restaurant.locality,
					badges: restaurant.badges
				}"></card>



		</div>
		<div class="footer">
			<small>Made by Sustain group for Unihack Sydney.</small>
		</div>

		{{ application.search_data }}


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
		restaurantsFiltered (){
			return this.$store.getters.restaurants.find(x => x.name = this.application.search_data);
		},
		restaurants (){
			return this.$store.getters.restaurants;
		},
		application (){
			return this.$store.getters.applicationState;
		}
	},
	mounted () {
		this.$http.get('http://172.16.6.162:8000/api/search/').then((response) => {
			this.$store.commit('updateData', response.data);
		})
	},
	methods: {
		alert(){

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
		display: flex;
		background-color: white;
		padding: 25px;
	}

	#map {
  		height: 200px;
	}

/* Optional: Makes the sample page fill the window. */


</style>
