import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		restaurants:[
			{
				id: 123,
				name: "Jambo Jambo African Restaurant",
				rating: 3,
				image_url: 'https://www.goodfood.com.au/content/dam/images/2/a/3/9/9/image.related.articleLeadwide.620x349.2acpu.png/1354145773360.jpg'
			},
			{
				id: 124,
				name: "Tetsuya's Restaurant",
				rating: 5,
				image_url: 'https://www.broadsheet.com.au/media/cache/c6/ea/c6ea30e8dfd8952f06eec8e15cc1925a.jpg'
			},
			{
				id: 125,
				name: "Ester Restuarant",
				rating: 4,
				image_url: 'https://www.broadsheet.com.au/media/cache/1a/10/1a10358a3124576b4c8b2b2cc994fbe7.jpg'
			}
		],
		application: {
			modal_id: null,
			modal_open: false,
		}
	},
	mutations: {
		toggleModal (state, modal_id){
			this.state.modal_id = modal_id;
			if(this.state.application.modal_open == true){
				this.state.application.modal_open = false;
			}else{
				this.state.application.modal_open = true;
			}
		},
		modifyRestaurants (state){
			
		}
	},
	actions: {

	},
	getters: {
		applicationState: state => {
			return state.application;
		}
	}
})
