<template>
	<div>
		{{ activeCard }}
		<!-- Trigger/Open The Modal -->
		<button id="myBtn">Review Me</button> <!-- The Modal -->
		<div class="modal" id="myModal">
			<!-- Modal content -->
			<div class="close-button">close</div>
			<div v-click-outside="hideModal" class="modal-content">
				<!-- <span @click="hideModal" class="close">&times;</span> -->
				<div class="flex-container">
					<!-- whole table  -->
					<div class="main-div">
						<div class="left-side">
							<!-- left hand side of the table  -->
							<h2>{{ activeCard.name }}</h2>
							<div class="badges">
								<div v-for="badge in activeCard.badges" class="badge">
									<div v-if="badge.name == 'local'"><img class="badge-item" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAKkSURBVGhD7dpL6A1hHMbx41oiUQhFNooiLBQbKyXZyE5IJEkWYkUsiPoXC5fcQlm6hBWllKQohY2dsEFy2bjf+T6LU2/Tc86ZOed958yUpz47M+/v9Z55LzP/RoKMwDLsxEmcwynsw0qMQ6WzFFfwGX/b+IXb2IihqEzm4xZc0Z08wQr0PVvwE67IIs5gOErPIByHK6pbdzAGpUYPriumVzcxBKVEM88fuEJiOILk0dC/hysgFv0nLUTSDMA1Hpuel2QZiy9wDWe9wW5oap6CWdiEx3D/3lmMJFkN12DWdYyGy2Dsh7suS7uCJLkE12DoHvKsB4fgrg+9hDoePe/gGgzNRZ6MxGu4e4RmImq00XMNhR6gSA7D3Se0HFEzHa6h0FkUyTq4+4TWI2rydKTow6mF1d0nFL0jmoVcQ6EbKBJNz+4+oSWIHm25XWNN35D30KRN5yO4+zT9htau6DkN12DoBPJkFdz1obtIEg2zazBrG9plETqdImUDkmQYXsE1mnUV8xBmKg7iB9w1oY8YhWTZC9dwK1r0HuI5imz99TNOmkn4Ctd4LOrwbCTPMbgCYrmMUqJt+Xe4Inql0ZiD0qIXbq6QXmmSKDXTEHtUNBrZma6UHIUrqFvn0ZdMwAe4oorSSz5tTPuWPXCFFZV83egU7YrfwhWXl9YlzYR9z3a4AvPSSbES0feQF3BFdqLN40RUJpvhCu3kACoVvQJ6BldsK9rhjkflovO1K7iVyo1GMxqVvOcVrRs6n1Q2u+AKz7qASkefHfTbd8WHFqDy0YcaV3yT3g/XIjPgOtC0BrXJfbhOfIJeYNcmW+E60reterdp9fNai9rFrfSTUbtcRNgJfYGqZfTXQWFHrqGW0fMQdqTvp8Buo8/LTwM78D/t02j8A5eq+1w+pl4sAAAAAElFTkSuQmCC"></div>
									<div v-if="badge.name == 'veg'"><img class="badge-item" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAMmSURBVGhD7dlJyI1RHMfxF5nHsFAyi4UxEaJYUBQlKxbIRuYFWdhYWMjGwhSykCEJKVMohY2EMpWdKVNmkSnj93e9/5xO5+XtPude59T91Sfec9/u8z/3ee6Z3rpaavn/aVf/b9bpjJuYW/op07TAOfzEBwxGltkMdcLcRhtklWn4AbcjshXZpCOewu+EfMdYZJGNCHXCXEITJJ3++IpQB1wzkHS2I1S47zySTRd8RKjwkIFIMvPgF/sEz702sxJJ5gj8Yg/ggddmTiDJvIZf7GJoIvTb5RqSi2bsULGjcNFrM4+QXAYgVKwGgINem3mG5DIMoWKVDQi9dhXJpQdCxSoLEHrtEJKLlhxv4RfbCuO8NrMIf0tbdEc/9IUe06pkF/xidae0Q/zmtIlWxj3hpiVmYj/uwP19own3OrSKng11NHomwr/wZCiX4bafhEV3cz4ewv2dxtJ3bSm0G42WM3AvYrP3Orjt46F0giZG97VyfcZeRFn69Ib7XTkOZSSsTY+Oon2LPk1rj0WP8R70QqFMgPboetN3aA7lLh6jK5riFPwiYlINq6Gzg7KjR8d2iVPUQFZg9O//lkYs/8KVcgODUHa6QbO6brOb1niB0EXvYQtmYQTaw6JRrQ/0wayBdpqhc4GQT9DqvFC0a3SzDO5FNKRuwlD40WOpDmlY1si0Ftuwo94FuO/1L1HPC9zV8FH484mK16d3GhqJ3EKKsEEmSjQ06k1V4HK4hxDqwBLch19EUTrt7IBoWYiXGFP66U+06NT+JFREUdqh+ne9cDRB+hOW2r4gVERRrzAc0eM/SjsRKiCGN9BAUdFoktJ6K1RADJp8h6CiUSeOIVRADDoz0+qhotGjtQ+hAorSfKSJ0pZEFY0uZBe+BY1gbjHl0pyjDVhVMh22pNCSQcsNLTvUvhsNbaYaorlIZ2lapFYtWlJrKLQitNQIRdvZqVgFnerrgE97nLPQX78OYz20ZIk6wTUm+l6oEOuEzrOy+8uVotNG64Rods8ueqTewzqh8b0qo0rsaPnh3o05yDKTYCPVFTRDttHwqP2FDhtqqaWWrFJX9wt5bWk0DNqDpwAAAABJRU5ErkJggg=="></div>
									<div v-if="badge.name == 'water'"><img class="badge-item" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAALsSURBVGhD1dpLqE1RHMfxI+9Hkbe8H0kYGMiAAZlLKFNKjDySyEBMDckrJInEyIBIRgYGSCKSvFISeUTyzuP7u9paZ9//3mvt016ndX71qXtu+5z1X2fvu/de/30bJRmAcxjZ9aqDcxx/cBU99YtOzDJoEplt6LgMx2u4E/mKmeionIE7icx1dMwhthTWJDJbkXz64jGsCWQ+IvmzmL5tq/i8w0g2A/EGVuF5PzERSWYjrKKL7EM7swA9/v1YHG3wDFbBRb5gMNqRufiMXV2vSjIfVrE+qxA7g/AEGu83FqIwe5AvMsQFxM5+uGPqrKrJmbkGd+NQbxEzi6G9kB9XkzPzCvmNQw1BjOhbfwprTE1uEbpF91HWG0KMRYzshjVe5gF6oSkPYW3s8wO9UXcmI+TLXY+mHIS1oc8VxMhpWOPl6QLe9Ic/B79gbVxmBerOVOjOwRrPshlNyZ/mfC7De6VtIYdgjVfkBfrgf/RC1wVr47xbiHFV7wfdXVtjllmCpmjRtBOfYL1Bu1x7Tk2JGMkvr0OdhBktddfiGM7jBDZhAmLmKKxCfd4jqahbYxUaYgSSSdGVPMQ8JJO7sIoMMR21Zwa0/q+aU7CK9PmAplNwHdGx+hzqUlaNr4NTpPCs1Wp0gbyIbIDVqBK9/ybcIn2+YxpqzRq4g+i0OA5VoqLewf2cMrpM1Jrx0LGaH0h7qGpmw9df+wZ9cbVGh4TuvawBpZUB+2M77sP9LK1Kj2ASas9KuIPlafChaDXDMAtaxEXrPetGL6SVpAZH0glts2o1OQVJRnvjJazCLVprJJl1sAouou7kGCSXG7AKLrMFSUXHu1WojyafVKp2712jkUwOwCoyRGkjut3REtgqMkTVm8moOQuryBDLkUx2wCoyRJTVXKvRPw9YLX+fO0guRf9YUEa9q+SiZe0jWAVbkn6srabdbViFu/ai2/OM1KIOxgbcg1u81tOXkNR1IzSjoMfJWggVPrSsP43GX8sGsP2zpWHuAAAAAElFTkSuQmCC"></div>
									<div v-if="badge.name == 'waste'"><img class="badge-item" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGsSURBVGhD7dq/K0VxGMfxm19FoSQpm4lB2FHKRBJlMtiUxWJAFpuN7Fb/gQmLVVlMFoVsiuRHIT/eT91vPenp3HM7v255PvVa7nPP934/0b3nnnNLKWUGJ3jBTwyfOMcKGlAT2YK12biO0IhCM4pvWBusxhoKzT70hr5wh6sI13iHPu4SheYCekNjiJMOPEAf245M0oZJzEe4h97MAqznWeSvo49dhvU8MYseVJ1W/H2hor1iGLHSjSXswFqsaIeQ/Q0hMiOwFqg164iMF8lZxSKdsN41ak0f/memcVwDNpAo8iFl/Y/m7QCJ4kVS5kVCKhV5gpzFisfyY8EHwky8Qc+foefyFUDPtcyLDCBETsP1TM6LdORDTM+noHMDPde8SIgXgRcxeJEQLwIvYvAiIV4EXsTgRUK8CLyIwYuEeBF4EYMXCalUZBXhCvli+bFAfhCgr6DLZvR8G3r+936klnmRvHiRkDlYC+dtF4kid7Dk0qe1eJ7kfn/i7MFaPC9nqEPiNOMU1otk7Ra9SC1N2ETUW2Sa5Mq9/GCnC5mkHv0Yx0RGBtGCKlIq/QI+C+St9GvhtAAAAABJRU5ErkJggg=="></div>
								</div>
							</div>

							<div class="ratings">
								<small>Sustainability: </small>
								<star-rating
									v-model="this.activeCard.sustain_rating"
									v-bind:star-size="20"
									v-bind:increment="0.1"
									:border-width="0"
									:read-only="true"
									active-color="rgb(64, 207, 71)">
								</star-rating>
								<small>Zomato: </small>
								<star-rating
									v-model="this.activeCard.rating"
									v-bind:star-size="15"
									v-bind:increment="0.1"
									:read-only="true"
									:border-width="0"
									active-color="rgb(64, 207, 71)" >
								</star-rating>
							</div>

							<img class="image" :src="activeCard.imgUrl">
							<h2>Comments</h2>
							<div class="comments">
								<div v-if="activeCard.comments.length == 0">
									<small>There are currently no comments to display</small>
								</div>
								<div v-for="comment in activeCard.comments" class="comment-item">
									<h4>{{ comment.comment }}</h4>
									<hr>
								</div>
							</div>

						</div>
						<div class="right-side">
							<!-- right hand side of the table  -->
							<!--  REVIEW OF restraunt-->
							<h2>Review</h2>
							<hr>
							<div class="question">
								How is the quality of the vegetarian options?
								<div class="answer-container">
									<i class="answer-item material-icons" v-bind:class="{ activeThumbUp: this.vegetarian_options == 1 }" @click="modifyVeg(1)">thumb_up</i>
									<i class="answer-item material-icons" v-bind:class="{ activeThumb: this.vegetarian_options == null }" @click="modifyVeg()">remove_circle</i>
									<i class="answer-item material-icons" v-bind:class="{ activeThumbDown: this.vegetarian_options == 0 }" @click="modifyVeg(0)">thumb_down</i>
								</div>
							</div>
							<div class="question">
								How does the restaurant deal with waste?
								<div class="answer-container">
									<i class="answer-item material-icons" v-bind:class="{ activeThumbUp: this.waste == 1 }" @click="modifyWaste(1)">thumb_up</i>
									<i class="answer-item material-icons" v-bind:class="{ activeThumb: this.waste == null }" @click="modifyWaste()">remove_circle</i>
									<i class="answer-item material-icons" v-bind:class="{ activeThumbDown: this.waste == 0 }" @click="modifyWaste(0)">thumb_down</i>
								</div>
							</div>
							<div class="question">
								Does the restaurant sustainably use water?
								<div class="answer-container">
									<i class="answer-item material-icons" v-bind:class="{ activeThumbUp: this.water == 1 }" @click="modifyWater(1)">thumb_up</i>
									<i class="answer-item material-icons" v-bind:class="{ activeThumb: this.water == null }" @click="modifyWater()">remove_circle</i>
									<i class="answer-item material-icons" v-bind:class="{ activeThumbDown: this.water == 0 }" @click="modifyWater(0)">thumb_down</i>
								</div>
							</div>
							<div class="question">
								Does the restaurant use local ingredients?
								<div class="answer-container" @click="test()">
									<i class="answer-item material-icons" v-bind:class="{ activeThumbUp: this.locally_produced == 1 }" @click="modifyLocal(1)">thumb_up</i>
									<i class="answer-item material-icons" v-bind:class="{ activeThumb: this.locally_produced == null }" @click="modifyLocal()">remove_circle</i>
									<i class="answer-item material-icons" v-bind:class="{ activeThumbDown: this.locally_produced == 0 }" @click="modifyLocal(0)">thumb_down</i>
								</div>
							</div>
							<h2>Comments</h2>
							<input class="form-control" id="comment" v-model="comment" placeholder="Any comments?">
							<div class="button" @click="submitReview">Submit</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import ClickOutside from 'vue-click-outside'
import StarRating from 'vue-star-rating'


// @ is an alias to /src
export default {
	name: 'Modal',
	props: ['data'],
	components: {
        StarRating
    },
    methods: {
        hideModal(){
			console.log("Hiding modal");
			this.vegetarian_options = null;
			this.waste = null;
			this.locally_produced = null;
			this.water = null;
            this.$store.commit('toggleModal');
		},
		submitReview(){
			this.axios.post('http://localhost:8000/api/restaurants/' + this.activeCard.id + '/review', {
				restaurant: this.activeCard.id,
				vegetarianUp: this.vegetarian_options,
				wasteUp: this.waste,
				waterUp: this.water,
				localUp: this.locally_produced,
				comment: this.comment
			});
			this.$http.get('http://localhost:8000/api/search/').then((response) => {
				this.$store.commit('updateData', response.data);
			})

			this.hideModal();
		},
		test(){
			console.log("TESTING");
		},
		modifyVeg(val){
			console.log(val);
			console.log("Triggered");
			this.vegetarian_options = val;
		},
		modifyWater(value){
			console.log(value);
			this.water = value;
		},
		modifyLocal(val){
			this.locally_produced = val;
		},
		modifyWaste(val){
			this.waste = val;
		}
	},
    data: function(){
        return {
			vegetarian_options: null,
			waste: null,
			water: null,
			locally_produced: null,
			comment: "",

			name: "Hello world"
        }
    },
    directives: {
        ClickOutside
	},
	computed: {
		activeCard (){
			console.log(this.$store.getters.restaurants);
			console.log(this.$store.getters.applicationState.modal_id);
			console.log(this.$store.getters.restaurants.find(x => x.id === this.$store.getters.applicationState.modal_id));
			return this.$store.getters.restaurants.find(x => x.id === this.$store.getters.applicationState.modal_id);
		}
	}

}
</script>
<style scoped>

	.close-button{
		position: absolute;
		right: 75px;
		top: 75px;
	}


	.activeThumbUp{
		color: rgb(64, 207, 71);
	}
	.activeThumbDown{
		color: rgb(247, 46, 46);
	}
	.activeThumb{
		color: blue;
	}

	.badges{
		justify-content: center;
		padding: 10px;
        margin-top: 10px;
		margin-bottom: 20px;
		/* margin-right: 10px; */
        display: flex;
		background-color: rgb(238, 238, 238);
	}

	.badge-item{
        display: flex;
        width:20px;
        padding: 10px;
        margin-right: 10px;
        border-radius: 5px;
        background-color: rgb(64, 207, 71);
        /* background-color: blue; */
    }

	.ratings{
		display: flex;
		align-items: center;
		padding: 10px;
		justify-content: space-around;
		background-color: rgb(238, 238, 238);
	}
	.comments{
		padding: 10px;
		background-color: rgb(238, 238, 238);
	}

	.main-div{
		display: grid;
		padding: 20px;
		grid-gap: 20px;
		grid-template-columns: 1fr 1fr;
	}
	@media only screen and (max-width: 900px){
		.main-div{
			grid-template-columns: 1fr;
		}
		.modal-content {
			background-color: #fefefe;
			margin: auto;
			/* padding: 20px; */
			/* border: 1px solid #888; */
			width: 90vw;
			height: 100%;
		}
	}
	.question{
		padding: 10px;
		margin: 5px;
		background-color: rgb(238, 238, 238);
	}

	.right-side{
		height: 100%;
		display: flex;
		flex-direction: column;
		/* justify-content: space-between; */
	}
	.left-side{
		/* padding:10px; */
	}
	.answer-item{
		padding: 10px;
	}
	.answer-item:hover{
		cursor: pointer;
		/* color: black; */
	}

	#comment{
		display: flex;
		font-size: 1em;
		padding: 15px;
		margin-bottom: 5px;
	}
	.button{
		padding: 10px;
		background-color: rgb(239, 255, 239);
		border: 1px solid black;
	}

	.image{
		width: 100%;
	}


	.modal {
		/* display: none; Hidden by default */
		position: fixed; /* Stay in place */
		z-index: 1; /* Sit on top */
		padding-top: 5%;
		/* padding-top: 100px; Location of the box */
		left: 0;
		top: 0;
		width: 100%; /* Full width */
		height: 100%; /* Full height */
		overflow: auto; /* Enable scroll if needed */
		background-color: rgb(0,0,0); /* Fallback color */
		background-color: rgba(0,0,0,0.6); /* Black w/ opacity */
	}

	/* Modal Content */
	.modal-content {
		background-color: #fefefe;
		margin: auto;
		/* padding: 20px; */
		/* border: 1px solid #888; */
		width: 90vw;
		height: 90vh;
	}
	/* The Close Button */
	.close {
		color: #aaaaaa;
		float: right;
		font-size: 28px;
		font-weight: bold;
	}
	.close:hover,
	.close:focus {
		color: #000;
		text-decoration: none;
		cursor: pointer;
	}

</style>
