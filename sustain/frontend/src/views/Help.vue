<template>
	<div>
	
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
	data: function(){
        return {
			loading: false
        }
    },
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


</style>
