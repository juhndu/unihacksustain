<template>
	<div class="modal" id="myModal">
		<!-- Modal content -->
		<div class="modal-content">
			<span @click="hideModal" class="close">&times;</span>
			<div class="flex-container">
				<div>
					<!--left hand side of page
					name
					badges
					comments
					rating  -->
					<table>
						<!-- whole table  -->
						<tr>
							<td>
								<table>
									<tr>
										<td>
											<!-- left hand side of the table  -->
											<h3>name of restraunt</h3>
										</td>
										<td>badges go here</td>
										<td><!-- integers to go here  -->
										star rating goes here(enviornmental) star rating (Zomato)<br></td>
									</tr>
									<tr></tr>
								</table>picture goes here comments go here
							</td>
							<td>
								<!-- right hand side of the table  -->
								<!--  REVIEW OF restraunt-->
								<h2>Review</h2>
								<table>
									<tr>
										<td></td>
									</tr>
									<tr>
										<td>How is the quality of the Vegetarian option</td>
										<td>
											<br>
											<form id="review" name="review">
												<input name="veg_opt" type="radio" value="100"> Good<br>
												<input name="veg_opt" type="radio" value="0"> Bad<br>
												<input name="veg_opt" type="radio" value=" "> N/A<br>
											</form>
										</td>
									</tr>
									<tr>
										<td>waste?</td>
										<td><br>
										<input name="question2" type="radio" value="100"> upvote<br>
										<input name="question2" type="radio" value=""> neutral<br>
										<input name="question2" type="radio" value="0"> downvote<br></td>
									</tr>
									<tr>
										<td>
											water?<br>
											<form>
												<input name="question3" type="radio" value="100"> upvote<br>
												<input name="question3" type="radio" value=" "> neutral<br>
												<input name="question3" type="radio" value="0"> downvote<br>
												<table>
													<tr>
														<td>is produce locally sourced?<br>
														<input name="local" type="radio" value="100"> Yes<br>
														<input name="local" type="radio" value="0"> No<br>
														<input name="local" type="radio" value=""> I dont Know<br></td>
													</tr>
												</table><!-- @Eugene please fix submit button :)  -->
												<button form="review" type="submit" value="Submit">Submit</button>
											</form>
										</td>
									</tr>
								</table>
							</td>
						</tr>
					</table>
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
    methods: {
        hideModal(){
			console.log("Hiding modal");
            this.$store.commit('toggleModal');
        }
	},
	mounted(){
		
	},
	components: {

    },
    data: function(){
        return {
			name: "Hello world"
        }
    },
    directives: {
        ClickOutside
    }
}
</script>
<style scoped> 
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
	position: fixed; /* Stay in place */
	z-index: 1; /* Sit on top */
	padding-top: 100px; /* Location of the box */
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
