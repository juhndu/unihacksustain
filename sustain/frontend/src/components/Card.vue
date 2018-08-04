<template>
	<div class="card" @click="openModal()">
        <div class="image">
            <img v-if="data.image_url" class="image-not-found" :src="data.image_url">
            <img v-else src="http://res.cloudinary.com/dkhgru81l/image/upload/v1533408566/Image_Not_Found_1x_qjofp8_kvzmmv.webp">
        </div>
        <div class="bottom-content">
                <div class="bottom-content-title align-top">
                    <h2>{{ data.name }}</h2>
                    <h3>{{ data.location }}</h3>


                    <div class="badges">
                        <div v-for="badge in data.badges" class="badge">
                            <div v-if="badge.name == 'local'"><img class="badge-item" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAKkSURBVGhD7dpL6A1hHMbx41oiUQhFNooiLBQbKyXZyE5IJEkWYkUsiPoXC5fcQlm6hBWllKQohY2dsEFy2bjf+T6LU2/Tc86ZOed958yUpz47M+/v9Z55LzP/RoKMwDLsxEmcwynsw0qMQ6WzFFfwGX/b+IXb2IihqEzm4xZc0Z08wQr0PVvwE67IIs5gOErPIByHK6pbdzAGpUYPriumVzcxBKVEM88fuEJiOILk0dC/hysgFv0nLUTSDMA1Hpuel2QZiy9wDWe9wW5oap6CWdiEx3D/3lmMJFkN12DWdYyGy2Dsh7suS7uCJLkE12DoHvKsB4fgrg+9hDoePe/gGgzNRZ6MxGu4e4RmImq00XMNhR6gSA7D3Se0HFEzHa6h0FkUyTq4+4TWI2rydKTow6mF1d0nFL0jmoVcQ6EbKBJNz+4+oSWIHm25XWNN35D30KRN5yO4+zT9htau6DkN12DoBPJkFdz1obtIEg2zazBrG9plETqdImUDkmQYXsE1mnUV8xBmKg7iB9w1oY8YhWTZC9dwK1r0HuI5imz99TNOmkn4Ctd4LOrwbCTPMbgCYrmMUqJt+Xe4Inql0ZiD0qIXbq6QXmmSKDXTEHtUNBrZma6UHIUrqFvn0ZdMwAe4oorSSz5tTPuWPXCFFZV83egU7YrfwhWXl9YlzYR9z3a4AvPSSbES0feQF3BFdqLN40RUJpvhCu3kACoVvQJ6BldsK9rhjkflovO1K7iVyo1GMxqVvOcVrRs6n1Q2u+AKz7qASkefHfTbd8WHFqDy0YcaV3yT3g/XIjPgOtC0BrXJfbhOfIJeYNcmW+E60reterdp9fNai9rFrfSTUbtcRNgJfYGqZfTXQWFHrqGW0fMQdqTvp8Buo8/LTwM78D/t02j8A5eq+1w+pl4sAAAAAElFTkSuQmCC"></div>
                            <div v-if="badge.name == 'veg'"><img class="badge-item" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAMmSURBVGhD7dlJyI1RHMfxF5nHsFAyi4UxEaJYUBQlKxbIRuYFWdhYWMjGwhSykCEJKVMohY2EMpWdKVNmkSnj93e9/5xO5+XtPude59T91Sfec9/u8z/3ee6Z3rpaavn/aVf/b9bpjJuYW/op07TAOfzEBwxGltkMdcLcRhtklWn4AbcjshXZpCOewu+EfMdYZJGNCHXCXEITJJ3++IpQB1wzkHS2I1S47zySTRd8RKjwkIFIMvPgF/sEz702sxJJ5gj8Yg/ggddmTiDJvIZf7GJoIvTb5RqSi2bsULGjcNFrM4+QXAYgVKwGgINem3mG5DIMoWKVDQi9dhXJpQdCxSoLEHrtEJKLlhxv4RfbCuO8NrMIf0tbdEc/9IUe06pkF/xidae0Q/zmtIlWxj3hpiVmYj/uwP19own3OrSKng11NHomwr/wZCiX4bafhEV3cz4ewv2dxtJ3bSm0G42WM3AvYrP3Orjt46F0giZG97VyfcZeRFn69Ib7XTkOZSSsTY+Oon2LPk1rj0WP8R70QqFMgPboetN3aA7lLh6jK5riFPwiYlINq6Gzg7KjR8d2iVPUQFZg9O//lkYs/8KVcgODUHa6QbO6brOb1niB0EXvYQtmYQTaw6JRrQ/0wayBdpqhc4GQT9DqvFC0a3SzDO5FNKRuwlD40WOpDmlY1si0Ftuwo94FuO/1L1HPC9zV8FH484mK16d3GhqJ3EKKsEEmSjQ06k1V4HK4hxDqwBLch19EUTrt7IBoWYiXGFP66U+06NT+JFREUdqh+ne9cDRB+hOW2r4gVERRrzAc0eM/SjsRKiCGN9BAUdFoktJ6K1RADJp8h6CiUSeOIVRADDoz0+qhotGjtQ+hAorSfKSJ0pZEFY0uZBe+BY1gbjHl0pyjDVhVMh22pNCSQcsNLTvUvhsNbaYaorlIZ2lapFYtWlJrKLQitNQIRdvZqVgFnerrgE97nLPQX78OYz20ZIk6wTUm+l6oEOuEzrOy+8uVotNG64Rods8ueqTewzqh8b0qo0rsaPnh3o05yDKTYCPVFTRDttHwqP2FDhtqqaWWrFJX9wt5bWk0DNqDpwAAAABJRU5ErkJggg=="></div>
                            <div v-if="badge.name == 'water'"><img class="badge-item" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAALsSURBVGhD1dpLqE1RHMfxI+9Hkbe8H0kYGMiAAZlLKFNKjDySyEBMDckrJInEyIBIRgYGSCKSvFISeUTyzuP7u9paZ9//3mvt016ndX71qXtu+5z1X2fvu/de/30bJRmAcxjZ9aqDcxx/cBU99YtOzDJoEplt6LgMx2u4E/mKmeionIE7icx1dMwhthTWJDJbkXz64jGsCWQ+IvmzmL5tq/i8w0g2A/EGVuF5PzERSWYjrKKL7EM7swA9/v1YHG3wDFbBRb5gMNqRufiMXV2vSjIfVrE+qxA7g/AEGu83FqIwe5AvMsQFxM5+uGPqrKrJmbkGd+NQbxEzi6G9kB9XkzPzCvmNQw1BjOhbfwprTE1uEbpF91HWG0KMRYzshjVe5gF6oSkPYW3s8wO9UXcmI+TLXY+mHIS1oc8VxMhpWOPl6QLe9Ic/B79gbVxmBerOVOjOwRrPshlNyZ/mfC7De6VtIYdgjVfkBfrgf/RC1wVr47xbiHFV7wfdXVtjllmCpmjRtBOfYL1Bu1x7Tk2JGMkvr0OdhBktddfiGM7jBDZhAmLmKKxCfd4jqahbYxUaYgSSSdGVPMQ8JJO7sIoMMR21Zwa0/q+aU7CK9PmAplNwHdGx+hzqUlaNr4NTpPCs1Wp0gbyIbIDVqBK9/ybcIn2+YxpqzRq4g+i0OA5VoqLewf2cMrpM1Jrx0LGaH0h7qGpmw9df+wZ9cbVGh4TuvawBpZUB+2M77sP9LK1Kj2ASas9KuIPlafChaDXDMAtaxEXrPetGL6SVpAZH0glts2o1OQVJRnvjJazCLVprJJl1sAouou7kGCSXG7AKLrMFSUXHu1WojyafVKp2712jkUwOwCoyRGkjut3REtgqMkTVm8moOQuryBDLkUx2wCoyRJTVXKvRPw9YLX+fO0guRf9YUEa9q+SiZe0jWAVbkn6srabdbViFu/ai2/OM1KIOxgbcg1u81tOXkNR1IzSjoMfJWggVPrSsP43GX8sGsP2zpWHuAAAAAElFTkSuQmCC"></div>
                            <div v-if="badge.name == 'waste'"><img class="badge-item" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGsSURBVGhD7dq/K0VxGMfxm19FoSQpm4lB2FHKRBJlMtiUxWJAFpuN7Fb/gQmLVVlMFoVsiuRHIT/eT91vPenp3HM7v255PvVa7nPP934/0b3nnnNLKWUGJ3jBTwyfOMcKGlAT2YK12biO0IhCM4pvWBusxhoKzT70hr5wh6sI13iHPu4SheYCekNjiJMOPEAf245M0oZJzEe4h97MAqznWeSvo49dhvU8MYseVJ1W/H2hor1iGLHSjSXswFqsaIeQ/Q0hMiOwFqg164iMF8lZxSKdsN41ak0f/memcVwDNpAo8iFl/Y/m7QCJ4kVS5kVCKhV5gpzFisfyY8EHwky8Qc+foefyFUDPtcyLDCBETsP1TM6LdORDTM+noHMDPde8SIgXgRcxeJEQLwIvYvAiIV4EXsTgRUK8CLyIwYuEeBF4EYMXCalUZBXhCvli+bFAfhCgr6DLZvR8G3r+936klnmRvHiRkDlYC+dtF4kid7Dk0qe1eJ7kfn/i7MFaPC9nqEPiNOMU1otk7Ra9SC1N2ETUW2Sa5Mq9/GCnC5mkHv0Yx0RGBtGCKlIq/QI+C+St9GvhtAAAAABJRU5ErkJggg=="></div>
                        </div>


                    </div>

                </div>
                <div class="align-bottom">
                    <small>Sustainability: </small>
                    <star-rating 
                        v-model="data.sustain_rating"
                        v-bind:star-size="20"
                        v-bind:increment="0.1"
                        :border-width="0"
                        :read-only="true"
                        active-color="rgb(64, 207, 71)">
                    </star-rating>
                    <small>Zomato: </small>
                    <star-rating 
                        v-model="zomatoRating"
                        v-bind:star-size="15"
                        v-bind:increment="0.1"
                        :read-only="true"
                        :border-width="0"
                        active-color="rgb(64, 207, 71)" >
                    </star-rating>
                </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src
import StarRating from 'vue-star-rating'

export default {
    name: 'card',
    props: ['data'],
	components: {
        StarRating
    },
	methods: {
		openModal(){
            this.$store.commit('toggleModal', this.data.id);
		}
	},
    data: function(){
        return {
            rating: parseInt(this.data.rating)
        }
    },
    computed: {
        zomatoRating(){
            return parseFloat(this.data.rating);
        },

    }
}
</script>
<style scoped>

    .image-not-found{
        
    }

    .badge{
        display: flex;
        flex-direction: row;
        margin-right: 5px;
    }
    .badges{
        margin-top: 10px;
        display: flex;
    }

    .badge-item{
        display: flex;
        width:20px;
        padding: 10px;
        
        border-radius: 5px;
        background-color: rgb(64, 207, 71);
        /* background-color: blue; */
    }

    .bottom-content{
        /* height: 250px; */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }


    .bottom-content-title{
        display: flex;
        flex-direction: column;
    }
    h2{
        color: #4f4f4f;
        margin: 0px;
    }
    h3{
        margin: 0px;
        color: rgb(131, 131, 131);
    }
    .image{
        height: 150px;
        overflow: hidden;
    }
    img{
        border-radius: 5px;
        width: 100%;
    }
    .bottom-content{

        padding: 15px;
    }
    .card{
        border-radius: 5px;
        background-color: rgb(232, 242, 232);
        box-shadow: 0 0 12px 0 hsla(0, 0%, 0%, 0.2);
        display: flex;
        flex-direction: column;
        text-align: left;
    }
    .card:hover{
        box-shadow: 0 0 12px 0 hsla(0, 0%, 0%, 0.5);
    }
    .button{
        min-width: 100px;
        background-color: rgb(255, 136, 0);
        display: flex;
        justify-content: center;
        padding: 10px;
    }
    .bottom-modal{
        display: flex;
        justify-content: flex-end;
    }

</style>
