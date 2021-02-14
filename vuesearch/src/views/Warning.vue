<template>
    <div>
        <div
            class="warning"
        >
          <h3 class="warningCode">{{ this.code }}</h3>
          <div class="warningMessage">{{ this.message }}</div>
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
  .warning{
    margin-top: 12px;
  }

  .warningCode{
    font-size: 70px;
    font-weight: 850;
    font-family: Roboto;

    text-align: center;
    /* min-height: 100vh;
    display: flex;
    flex-direction: row; */
    align-items: center;
  }

  .warningMessage{
    font-size: 20px;
    font-weight: 500;
    font-family: Roboto;

    text-align: center;
    align-items: center;
  }

  .image {
      max-width:200px;
      display: block;
      margin-left: auto;
      margin-right: auto;
      /* width: 15%; */
  }
</style>