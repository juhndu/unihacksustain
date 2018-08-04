<template>
	<div>
		{{ activeCard }}
		<!-- Trigger/Open The Modal -->
		<button id="myBtn">Review Me</button> <!-- The Modal -->
		<div class="modal" id="myModal">
			<!-- Modal content -->
			<div class="modal-content">
				<span @click="hideModal" class="close">&times;</span>
				<div class="flex-container">
					<div>
						<table>
							<!-- whole table  -->
							<tr class="main-div">
								<td class="left-side">
									<!-- left hand side of the table  -->
									<h2>{{ activeCard.name }}</h2>
									badges go here
									{{ activeCard.rating }} star rating (Zomato)<br>
									<img class="image" :src="activeCard.imgUrl">
									<h2>Comments</h2>
									<hr>
									<div v-for="comment in activeCard.comments" class="comment-item">
										<h4>{{ comment.comment }}</h4>
										<hr>
									</div>


								</td>
								<td class="right-side">
									<!-- right hand side of the table  -->
									<!--  REVIEW OF restraunt-->
									<h2>Review</h2>
									<hr>
									<table>
										<tr>
											<td>How is the quality of the Vegetarian option?</td>
											<input name="veg_opt" type="radio" :value="1" v-model="vegetarian_options"> Good<br>
											<input name="veg_opt" type="radio" :value="0" v-model="vegetarian_options"> Bad<br>
											<input name="veg_opt" type="radio"  v-model="vegetarian_options"> N/A<br>
										</tr>
										<tr>
											<td>waste?</td>
											<td><br>
											<input name="question2" type="radio" :value="1" v-model="waste"> upvote<br>
											<input name="question2" type="radio" v-model="waste"> neutral<br>
											<input name="question2" type="radio" :value="0" v-model="waste"> downvote<br></td>
										</tr>
										<tr>
											<td>Water?</td>
											<input name="question3" type="radio" :value="1" v-model="water"> upvote<br>
											<input name="question3" type="radio" v-model="water"> neutral<br>
											<input name="question3" type="radio" :value="0" v-model="water"> downvote<br>
										</tr>
										<tr>
											<td>Locally Produced</td>
											<input name="local" type="radio" :value="1" v-model="locally_produced"> Yes<br>
											<input name="local" type="radio" :value="0" v-model="locally_produced"> No<br>
											<input name="local" type="radio" v-model="locally_produced"> I dont Know<br>
										</tr>
									</table>
										<h2>Comments</h2>
										<input class="form-control" id="comment" v-model="comment" placeholder="Testing">
										<div class="button" @click="submitReview">Submit</div>
								</td>
							</tr>
						</table>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import ClickOutside from 'vue-click-outside'

// @ is an alias to /src
export default {
	name: 'Modal',
	props: ['data'],
    methods: {
        hideModal(){
			console.log("Hiding modal");
            this.$store.commit('toggleModal');
		},
		submitReview(){
			this.axios.post('http://172.16.6.162:8000/api/restaurants/' + this.activeCard.id + '/review', {
				restaurant: this.activeCard.id,
				vegetarianUp: this.vegetarian_options,
				wasteUp: this.waste,
				waterUp: this.water,
				localUp: this.locally_produced,
				comment: this.comment
			});
			this.$http.get('http://172.16.6.162:8000/api/search/').then((response) => {
				this.$store.commit('updateData', response.data);
			})

			this.hideModal();
		}
	},
	mounted(){
		
	},
	components: {

    },
    data: function(){
        return {
			vegetarian_options: 0,
			waste: 0,
			water: 0,
			locally_produced: 0,
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

	.main-div{
		display: flex;
	}

	.right-side{
		padding-left: 20px;
		display: flex;
		flex-direction: column;
	}
	.left-side{

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

	img{
		max-height: 250px;
	}

	/* .image{
		margin-top: 20px;
		height: 400px;
		border: 0px;
	} */

	.left-size{
		width: 50%;
	}
	.right-side{
		/* width: 50%; */
	}
	/*
	-------------------SUMMARY OF PAGE------------------
	Left hand side of modal box:
	 * name
	 * badges
	 * pictures
	 * comments
	right hand side of page:
	 review
	 Options:
	   -Vegetarian options
	   -Waste
	   - Water
	*/
	/* The Modal (background) */
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
		background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
	}

	/* Modal Content */
	.modal-content {
	background-color: #fefefe;
	margin: auto;
	padding: 20px;
	border: 1px solid #888;
	width: 80%;
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
	/* .split_left{
	 width: 50%;
	 float: left;
	}
	.split_right{
	 width: 50%;
	 float: right; */
	/* } */

</style>
