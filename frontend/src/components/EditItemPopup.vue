<template>
    <q-dialog ref="dialog" @hide="onDialogHide">
        <q-card class="item-edit">
            <q-card-section class="row items-center">
                <div class="text-h6">Edit item</div>
                <q-space />
                <q-btn icon="close" flat round dense v-close-popup />
            </q-card-section>
            <q-card-section>
                <q-form class="q-gutter-sm" @submit="addItem">

                    <q-input filled v-model="title" label="Title" />
                    <q-input filled v-model="artist" label="Artist" />
                    <q-input filled v-model="genre" label="Genre" />
                    <q-input filled v-model="description" label="Description" />
                    <q-input filled v-model="mediatype" label="Media Type" />
                    <q-input filled stack-label v-model="release_year" type="date" label="Release Date" />
                    <q-input filled v-model="price" type="number" max-decimals="2" prefix="$" label="Price" />
                    <q-input filled v-model="inventory_count" type="number" label="Inventory" />
                    <q-input filled stack-label v-model="photo" type="file" @change="onFileChanged" label="Cover Art" />

                    <q-btn class="q-ma-sm" color="primary" type="submit" label="Add Item" />
                </q-form>
            </q-card-section>
        </q-card>
    </q-dialog>
</template>

<script>
export default {

    props: ["id", "description", "price", "photo", "title", "artist", "mediatype", "genre", "inventory_count", "release_year"],

    name: "EditItemPopup",

    data: function() {
        return {
        };
    },

    methods: {    
        // following method is REQUIRED
        show () {
            this.$refs.dialog.show()
        },

        // following method is REQUIRED
        hide () {
            this.$refs.dialog.hide()
        },

        addItem: function() {
            console.log('test')
        },

        test() {
            console.log('here 2222222')
        },

        onDialogHide () {
            this.$emit('hide')
        },

        onOKClick () {
            this.$emit('ok')
            // or with payload: this.$emit('ok', { ... })

            // then hiding dialog
            this.hide()
        },

        onCancelClick () {
            this.hide()
        },

        onFileChanged: function(event) {
             //   console.log(event.target.files[0].type);
            this.newPic = event.target.files[0];
            this.oldPic = URL.createObjectURL(event.target.files[0]);
        }
    }
};

</script>
<style lang='scss' scoped>
.item-edit {
    min-width: 500px;
}
</style>