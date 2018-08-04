<template>
	<div class="location-services" @click="getLocation">
		<div v-if="!this.state">Activate location services. <i class="material-icons"> location_on</i></div>
		<div v-if="this.state">Location services are working! <i class="material-icons"> location_on</i></div>
	</div>
</template>

<script>
export default {
	name: 'HelloWorld',
	props: {
	msg: String

	},
    data: function(){
        return {
			state: false
        }
    },
	methods: {
		getLocation(){
			this.$getLocation()
			.then(coordinates => {
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
