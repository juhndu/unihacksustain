<template>
	<div class="modal">
        <!-- <div class="inner-modal" v-click-outside="hideModal">
            
            
            
            
            
            <h1>This is the modal</h1>
        </div> -->
    </div>
</template>

<script>
import ClickOutside from 'vue-click-outside'

// @ is an alias to /src
export default {
    name: 'Modal',
    methods: {
        hideModal(){
            this.$store.commit('toggleModal');
        }
    },
	components: {

    },
    data: function(){
        return {

        }
    },
    directives: {
        ClickOutside
    }
}
</script>
<style scoped> 
    .modal{
        position: absolute;
        top: 0;
        bottom: 0;
        width: 100%;
        background-color: gray;
    }
    .inner-modal{
        background-color: white;
        min-height: 80vh;
    }

</style>
