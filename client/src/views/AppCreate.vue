<script>
import useApps from '../stores/app';
const { storeFile } = useApps();
export default {
    data() {
        return {
            file: ''
        }
    },

    methods: {
        handleFileUpload(event) {
            this.file = event.target.files[0];
        },

        submitFile() {
            let formData = new FormData();

            formData.append('file', this.file);

            storeFile(formData);
        }
    }
}
</script>
<template>
    <div class="grid grid-cols-12 gap-2">
        <div class="col-span-1 p-8">
        </div>
        <div class="col-span-10 p-8">
            <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white" for="file_input">Upload file</label>
            <input
                class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400"
                aria-describedby="file_input_help" id="file_input" type="file" @change="handleFileUpload($event)">
            <p class="mt-1 text-sm text-gray-500 dark:text-gray-300" id="file_input_help">.txt, .pdf
            </p>
            <button
                class="hover:shadow-form w-full rounded-md bg-[#6A64F1] py-3 px-8 text-center text-base font-semibold text-white outline-none"
                v-on:click="submitFile()">
                Send File
            </button>
        </div>
        <div class="col-span-1 p-8">
        </div>
    </div>
</template>