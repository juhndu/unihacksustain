<template>
	<div class="home">
		<navigation></navigation>

		<div class="cards">
			<card></card>
			<card></card>
			<card></card>
			<card></card>
			<card></card>
			<card></card>

		</div>



	</div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import Navigation from '@/components/Nav.vue';
import Card from '@/components/Card.vue';

export default {
	name: 'home',
	components: {
		HelloWorld,
		Navigation,
		Card
	}
}
</script>
<style scoped>
	.cards{
		margin: 20px;
		display: grid;
		grid-template-columns: 1fr 1fr;
		grid-gap: 10px;
	}

	@media only screen and (max-width: 600px){
		.cards{
			grid-template-columns: 1fr;
		}
	}

</style>
