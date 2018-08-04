import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		restaurants:[
			{
				id: 123,
				name: "Jambo Jambo African Restaurant",
				location: "93 Glebe Point Rd, Glebe NSW 2037",
				rating: 3,
				image_url: 'https://www.goodfood.com.au/content/dam/images/2/a/3/9/9/image.related.articleLeadwide.620x349.2acpu.png/1354145773360.jpg'
			}
		],
		application: {
			modal_id: null,
			modal_open: false,
			search_data: ""
		},
		userLocation: {
			lng: null,
			lat: null
		}
	},
	mutations: {
		toggleModal (state, modal_id){
			this.state.application.modal_id = modal_id;
			if(this.state.application.modal_open == true){
				this.state.application.modal_open = false;
			}else{
				this.state.application.modal_open = true;
			}
		},
		modifyRestaurants (state){

		},
		updateData (state, data){
			this.state.restaurants = data;
		},
		updateSearch (state, data){
			console.log(data);
			this.state.application.search_data = data;
		}
	},
	computed: {
		application (){
			return this.$store.getters.applicationState;
		}
	},
	getters: {
		applicationState: state => {
			return state.application;
		},
		userLocation: state => {
			return state.userLocation;
		},
		restaurants: state => {
			return state.restaurants;
		}
	}
})
