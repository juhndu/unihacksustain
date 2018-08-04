<template>
	<div class="nav">
        <a href="#">Sustain</a>
        <div class="right-side">
            <div class="filter-container">
                <div @click="toggleFilter(0)" v-bind:class="{ 'filter-item--active' : filter0 }" class="filter-item">a</div>
                <div @click="toggleFilter(1)" v-bind:class="{ 'filter-item--active' : filter1 }" class="filter-item">b</div>
                <div @click="toggleFilter(2)" v-bind:class="{ 'filter-item--active' : filter2 }" class="filter-item">c</div>
                <div @click="toggleFilter(3)" v-bind:class="{ 'filter-item--active' : filter3 }" class="filter-item">d</div>
            </div>
            <input v-model="searchContent" type="text" class="search-bar" placeholder="Search">
        </div>
	</div>
</template>

<script>
// @ is an alias to /src

export default {
	name: 'navigation',
	components: {

    },
    data: function(){
        return {
            searchContent: "",
            filter0: true,
            filter1: true,
            filter2: true,
            filter3: true,
        }
    },
    methods: {
        toggleFilter(filterNumber){
            if (filterNumber == 0){
                this.filter0 ? this.filter0 = false: this.filter0 = true;
            }
            if (filterNumber == 1){
                this.filter1 ? this.filter1 = false: this.filter1 = true;
            }
            if (filterNumber == 2){
                this.filter2 ? this.filter2 = false: this.filter2 = true;
            }
            if (filterNumber == 3){
                this.filter3 ? this.filter3 = false: this.filter3 = true;
            }
        }
    },
    watch : {
        searchContent: function (val){

            /* PLUG INTO THE API HERE */



            console.log(val);
        }
    }
}
</script>
<style scoped>
    .nav{
        background-color: gray;
        display: flex;
        justify-content: space-between;
        padding: 20px;
        align-items: center;
    }
    a{
        font-size: 2em;
    }

    .search-bar{
        padding: 10px;
        font-size: 14px;
        min-width: 200px;
    }
    .filter-container{
        display: flex;
    }
    .filter-item{
        padding: 10px;
        margin-right: 5px;
        background-color: blue;
    }
    .filter-item--active{
        padding: 10px;
        margin-right: 5px;
        background-color: red;
    }



    .right-side{
        display: flex;
    }


	@media only screen and (max-width: 600px){
        .nav{
            flex-direction: column;
        }
	}


</style>
