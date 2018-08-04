<template>
	<div class="location-services" @click="getLocation">
		<div v-if="!this.state && !isLoading">Activate location services. <i class="material-icons"> location_on</i></div>
		<div v-if="this.state && !isLoading">Location services are working! <i class="material-icons"> location_on</i></div>
		<pulse-loader v-if="isLoading"></pulse-loader>
	</div>
</template>

<script>
import PulseLoader from 'vue-spinner/src/PulseLoader.vue';

export default {
	name: 'HelloWorld',
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
	background-color: antiquewhite;
	padding: 10px;
}
</style>
