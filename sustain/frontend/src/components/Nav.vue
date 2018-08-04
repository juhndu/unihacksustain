<template>
	<div class="nav">
        <a href="#"><img class="logo" src="https://res.cloudinary.com/dkhgru81l/image/upload/v1533381402/38391707_518710195218120_1033799573040005120_n_aquyqy.jpg"></a>
        <div class="right-side">
            <div class="filter-container">
                <i @click="goToHelp" class="help material-icons">help_outline</i>
                <div @click="toggleFilter(0)" v-bind:class="{ 'filter-item--active' : filter0 }" class="filter-item"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAKkSURBVGhD7dpL6A1hHMbx41oiUQhFNooiLBQbKyXZyE5IJEkWYkUsiPoXC5fcQlm6hBWllKQohY2dsEFy2bjf+T6LU2/Tc86ZOed958yUpz47M+/v9Z55LzP/RoKMwDLsxEmcwynsw0qMQ6WzFFfwGX/b+IXb2IihqEzm4xZc0Z08wQr0PVvwE67IIs5gOErPIByHK6pbdzAGpUYPriumVzcxBKVEM88fuEJiOILk0dC/hysgFv0nLUTSDMA1Hpuel2QZiy9wDWe9wW5oap6CWdiEx3D/3lmMJFkN12DWdYyGy2Dsh7suS7uCJLkE12DoHvKsB4fgrg+9hDoePe/gGgzNRZ6MxGu4e4RmImq00XMNhR6gSA7D3Se0HFEzHa6h0FkUyTq4+4TWI2rydKTow6mF1d0nFL0jmoVcQ6EbKBJNz+4+oSWIHm25XWNN35D30KRN5yO4+zT9htau6DkN12DoBPJkFdz1obtIEg2zazBrG9plETqdImUDkmQYXsE1mnUV8xBmKg7iB9w1oY8YhWTZC9dwK1r0HuI5imz99TNOmkn4Ctd4LOrwbCTPMbgCYrmMUqJt+Xe4Inql0ZiD0qIXbq6QXmmSKDXTEHtUNBrZma6UHIUrqFvn0ZdMwAe4oorSSz5tTPuWPXCFFZV83egU7YrfwhWXl9YlzYR9z3a4AvPSSbES0feQF3BFdqLN40RUJpvhCu3kACoVvQJ6BldsK9rhjkflovO1K7iVyo1GMxqVvOcVrRs6n1Q2u+AKz7qASkefHfTbd8WHFqDy0YcaV3yT3g/XIjPgOtC0BrXJfbhOfIJeYNcmW+E60reterdp9fNai9rFrfSTUbtcRNgJfYGqZfTXQWFHrqGW0fMQdqTvp8Buo8/LTwM78D/t02j8A5eq+1w+pl4sAAAAAElFTkSuQmCC"></div>
                <div @click="toggleFilter(1)" v-bind:class="{ 'filter-item--active' : filter1 }" class="filter-item"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAMmSURBVGhD7dlJyI1RHMfxF5nHsFAyi4UxEaJYUBQlKxbIRuYFWdhYWMjGwhSykCEJKVMohY2EMpWdKVNmkSnj93e9/5xO5+XtPude59T91Sfec9/u8z/3ee6Z3rpaavn/aVf/b9bpjJuYW/op07TAOfzEBwxGltkMdcLcRhtklWn4AbcjshXZpCOewu+EfMdYZJGNCHXCXEITJJ3++IpQB1wzkHS2I1S47zySTRd8RKjwkIFIMvPgF/sEz702sxJJ5gj8Yg/ggddmTiDJvIZf7GJoIvTb5RqSi2bsULGjcNFrM4+QXAYgVKwGgINem3mG5DIMoWKVDQi9dhXJpQdCxSoLEHrtEJKLlhxv4RfbCuO8NrMIf0tbdEc/9IUe06pkF/xidae0Q/zmtIlWxj3hpiVmYj/uwP19own3OrSKng11NHomwr/wZCiX4bafhEV3cz4ewv2dxtJ3bSm0G42WM3AvYrP3Orjt46F0giZG97VyfcZeRFn69Ib7XTkOZSSsTY+Oon2LPk1rj0WP8R70QqFMgPboetN3aA7lLh6jK5riFPwiYlINq6Gzg7KjR8d2iVPUQFZg9O//lkYs/8KVcgODUHa6QbO6brOb1niB0EXvYQtmYQTaw6JRrQ/0wayBdpqhc4GQT9DqvFC0a3SzDO5FNKRuwlD40WOpDmlY1si0Ftuwo94FuO/1L1HPC9zV8FH484mK16d3GhqJ3EKKsEEmSjQ06k1V4HK4hxDqwBLch19EUTrt7IBoWYiXGFP66U+06NT+JFREUdqh+ne9cDRB+hOW2r4gVERRrzAc0eM/SjsRKiCGN9BAUdFoktJ6K1RADJp8h6CiUSeOIVRADDoz0+qhotGjtQ+hAorSfKSJ0pZEFY0uZBe+BY1gbjHl0pyjDVhVMh22pNCSQcsNLTvUvhsNbaYaorlIZ2lapFYtWlJrKLQitNQIRdvZqVgFnerrgE97nLPQX78OYz20ZIk6wTUm+l6oEOuEzrOy+8uVotNG64Rods8ueqTewzqh8b0qo0rsaPnh3o05yDKTYCPVFTRDttHwqP2FDhtqqaWWrFJX9wt5bWk0DNqDpwAAAABJRU5ErkJggg=="></div>
                <div @click="toggleFilter(2)" v-bind:class="{ 'filter-item--active' : filter2 }" class="filter-item"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAALsSURBVGhD1dpLqE1RHMfxI+9Hkbe8H0kYGMiAAZlLKFNKjDySyEBMDckrJInEyIBIRgYGSCKSvFISeUTyzuP7u9paZ9//3mvt016ndX71qXtu+5z1X2fvu/de/30bJRmAcxjZ9aqDcxx/cBU99YtOzDJoEplt6LgMx2u4E/mKmeionIE7icx1dMwhthTWJDJbkXz64jGsCWQ+IvmzmL5tq/i8w0g2A/EGVuF5PzERSWYjrKKL7EM7swA9/v1YHG3wDFbBRb5gMNqRufiMXV2vSjIfVrE+qxA7g/AEGu83FqIwe5AvMsQFxM5+uGPqrKrJmbkGd+NQbxEzi6G9kB9XkzPzCvmNQw1BjOhbfwprTE1uEbpF91HWG0KMRYzshjVe5gF6oSkPYW3s8wO9UXcmI+TLXY+mHIS1oc8VxMhpWOPl6QLe9Ic/B79gbVxmBerOVOjOwRrPshlNyZ/mfC7De6VtIYdgjVfkBfrgf/RC1wVr47xbiHFV7wfdXVtjllmCpmjRtBOfYL1Bu1x7Tk2JGMkvr0OdhBktddfiGM7jBDZhAmLmKKxCfd4jqahbYxUaYgSSSdGVPMQ8JJO7sIoMMR21Zwa0/q+aU7CK9PmAplNwHdGx+hzqUlaNr4NTpPCs1Wp0gbyIbIDVqBK9/ybcIn2+YxpqzRq4g+i0OA5VoqLewf2cMrpM1Jrx0LGaH0h7qGpmw9df+wZ9cbVGh4TuvawBpZUB+2M77sP9LK1Kj2ASas9KuIPlafChaDXDMAtaxEXrPetGL6SVpAZH0glts2o1OQVJRnvjJazCLVprJJl1sAouou7kGCSXG7AKLrMFSUXHu1WojyafVKp2712jkUwOwCoyRGkjut3REtgqMkTVm8moOQuryBDLkUx2wCoyRJTVXKvRPw9YLX+fO0guRf9YUEa9q+SiZe0jWAVbkn6srabdbViFu/ai2/OM1KIOxgbcg1u81tOXkNR1IzSjoMfJWggVPrSsP43GX8sGsP2zpWHuAAAAAElFTkSuQmCC"></div>
                <div @click="toggleFilter(3)" v-bind:class="{ 'filter-item--active' : filter3 }" class="filter-item"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGsSURBVGhD7dq/K0VxGMfxm19FoSQpm4lB2FHKRBJlMtiUxWJAFpuN7Fb/gQmLVVlMFoVsiuRHIT/eT91vPenp3HM7v255PvVa7nPP934/0b3nnnNLKWUGJ3jBTwyfOMcKGlAT2YK12biO0IhCM4pvWBusxhoKzT70hr5wh6sI13iHPu4SheYCekNjiJMOPEAf245M0oZJzEe4h97MAqznWeSvo49dhvU8MYseVJ1W/H2hor1iGLHSjSXswFqsaIeQ/Q0hMiOwFqg164iMF8lZxSKdsN41ak0f/memcVwDNpAo8iFl/Y/m7QCJ4kVS5kVCKhV5gpzFisfyY8EHwky8Qc+foefyFUDPtcyLDCBETsP1TM6LdORDTM+noHMDPde8SIgXgRcxeJEQLwIvYvAiIV4EXsTgRUK8CLyIwYuEeBF4EYMXCalUZBXhCvli+bFAfhCgr6DLZvR8G3r+936klnmRvHiRkDlYC+dtF4kid7Dk0qe1eJ7kfn/i7MFaPC9nqEPiNOMU1otk7Ra9SC1N2ETUW2Sa5Mq9/GCnC5mkHv0Yx0RGBtGCKlIq/QI+C+St9GvhtAAAAABJRU5ErkJggg=="></div>
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
            filter0: false,
            filter1: false,
            filter2: false,
            filter3: false,
        }
    },
    methods: {
        toggleFilter(filterNumber){
            if (filterNumber == 0){
                this.filter0 ? this.filter0 = false: this.filter0 = true;
                this.search(this.searchContent);
            }
            if (filterNumber == 1){
                this.filter1 ? this.filter1 = false: this.filter1 = true;
                this.search(this.searchContent);
            }
            if (filterNumber == 2){
                this.filter2 ? this.filter2 = false: this.filter2 = true;
                this.search(this.searchContent);
            }
            if (filterNumber == 3){
                this.filter3 ? this.filter3 = false: this.filter3 = true;
                this.search(this.searchContent);
            }
        },
        goToHelp(){
            this.$router.push({ path: 'help' });
        },
        search(val){
            if (this.filter0 || this.filter1 || this.filter2 || this.filter3){
                console.log("A filter is now active");
                var gen_string = "http://172.16.6.162:8000/api/search/?q=";
                gen_string += val;
                if (this.filter0){
                    gen_string += "&badge=local";
                }
                if (this.filter1){
                    gen_string += "&badge=veg";
                }
                if (this.filter2){
                    gen_string += "&badge=water";
                }
                if (this.filter3){
                    gen_string += "&badge=waste";
                }
                this.$http.get(gen_string).then((response) => {
			        this.$store.commit('updateData', response.data);
		        })

            }else{
                if (this.userLocation.lng == null){
                    console.log("Is null");
                    this.$http.get('http://172.16.6.162:8000/api/search/?q=' + val).then((response) => {
                        this.$store.commit('updateData', response.data);
                    })
                }else{ 
                    console.log("Is not null");
                    this.$http.get('http://172.16.6.162:8000/api/search/?q=' + val + '&lat=' + this.userLocation.lat + '&lon' + this.userLocation.lng).then((response) => {
                        this.$store.commit('updateData', response.data);
                    })
                }   
            }
        }
    },
    watch : {
        searchContent: function (val){
            this.search(val);
        }
    },
    computed: {
        userLocation (){
			return this.$store.getters.userLocation;
		}
    }
}
</script>
<style scoped>
    .help{
        padding: 8px;
        opacity: 0.3;
    }

    .logo{
        padding-bottom: 10px;
        padding-top: 10px;
        height: 100px;
    }

    .nav{
        background-color: #ffffff;
        display: flex;
        justify-content: space-between;
        padding-left: 20px;
        padding-right: 20px;
        align-items: center;
    }
    .search-bar{
        background-color: rgb(239, 255, 239);
        margin: 0px solid;
        border-radius: 10px;
        padding: 10px;
        font-size: 14px;
        min-width: 200px;
        border: 1px solid black;;
    }
    .search-bar:focus{
        background-color: rgb(215, 255, 217);
    }

    .filter-container{
        display: flex;
    }
    .filter-item{
        display: flex;
        padding: 10px;
        margin-right: 5px;
        /* background-color: blue; */
    }
    .filter-item:hover{
        border-radius: 10px;
        background-color: rgb(239, 255, 239);
    }


    .filter-item img{
        width: 20px;
        height: 20px;
    }
    .filter-item--active{
        border-radius: 10px;
        padding: 10px;
        margin-right: 5px;
        background-color: rgb(64, 207, 71);
    }
    .filter-item--active:hover{
        background-color: rgb(64, 207, 71);  
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
