<template>
	<div class="nav">
        <a href="#">Sustain</a>
        <input type="text" placeholder="Search">
	</div>
</template>

<script>
// @ is an alias to /src

export default {
	name: 'navigation',
	components: {

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

    input{
        padding: 15px;
    }


</style>
