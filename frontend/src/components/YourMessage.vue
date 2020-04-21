<template>
  <q-page class="q-mx-xl q-mb-md q-mt-md">
    <div class="q-pa-md row justify-center">
      <div style="width: 100%; max-width: 400px">
        <q-chat-message
          name="me"
          avatar="https://cdn.quasar.dev/img/avatar1.jpg"
          :text="['hey, how are you?']"
          sent
        />
        <q-chat-message
          name="Jane"
          avatar="https://cdn.quasar.dev/img/avatar2.jpg"
          :text="['doing fine, how r you?']"
        />
      </div>
    </div>
  </q-page>
</template>