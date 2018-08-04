<template>
	<div class="location-services">
		<div @click="getLocation" class="location-item" v-if="!this.state && !isLoading">Activate location services.</div>
		<div class="location-item" v-if="this.state && !isLoading">Location services are working!</div>
		<pulse-loader v-if="isLoading" color="rgb(239, 255, 239)"></pulse-loader>
	</div>
</template>

<script>
import PulseLoader from 'vue-spinner/src/PulseLoader.vue';

export default {
	name: 'LocationServices',
	components: {
    	PulseLoader
  	},
    data: function(){
        return {
			isLoading: false,
			state: false
        }
    },
	methods: {
		getLocation(){
			this.isLoading = true;
			this.$getLocation()
			.then(coordinates => {
				this.isLoading = false;
				this.state = true;
				console.log(coordinates);

				// this.axios.get("http://api.geonames.org/findNearestIntersection?lat=37.451&lng=-122.18&username=demo").then((response) => {
				// 	console.log(response.data)
				// })

			});
		}
	}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.location-services{
	display: flex;
	justify-content: flex-end;
	background-color: #d6d6d6;
	padding: 10px;
	height: 30px;
}

.location-item{
	align-items: center;
	display: flex;
}

.v-spinner{
	display: flex;
	align-items: center;
}
</style>
