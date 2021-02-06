<template>
    <div>
        <div
            class="warning"
        >
        <h3 class="warningCode">{{ this.code }}</h3>
        <div class="warningMessage">{{ this.message }}</div>
        <!-- <b-img src="src/assets/sorry.jpg"></b-img> -->
        <!-- <img style="width:360px; margin:14px;" src="../assets/sorry.jpg"/> -->
        <b-img 
            fluid
            class="image" 
            src="https://media.giphy.com/media/ViHbdDMcIOeLeblrbq/giphy.gif"/>
        </div>
  </div>
</template>

<script scoped>
export default {
  name: 'Warning',
  props: {
    code: { type: Number, required: true},
    message: { type: String, required: true }
  }
}
</script>

<style scoped>
  .warningCode{
    font-size: 70px;
    font-weight: 850;
    font-family: Roboto;

    padding: 0px 520px;
    margin: 20px 70px;
    box-sizing: border-box;
  }

  .warningMessage{
    font-size: 20px;
    font-weight: 500;
    font-family: Roboto;

    margin: 5px 0px 0px 465px;
    box-sizing: border-box;
  }

  .image {
      max-width:200px;
      margin: 10px 0px 0px 560px;
      /* text-align: center; */
  }
</style>