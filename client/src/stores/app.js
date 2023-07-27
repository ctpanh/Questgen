import { ref } from "vue";
import axios from "axios";
import router from "../router";
axios.defaults.baseURL = "http://localhost:8000/api";
export default function useApps() {

    const quests = ref([]);
    const errors = ref({});
    const getQuests = async () => {
        const response = await axios.get("/both");
        quests.value = response.data;
    };

    const genQuestFromFile = async (data) => {
        try {
            await axios.post("/getQuestFromFile", data, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            router.push({ name: "AppView" });
        } catch (error) {
            console.log(error);
        }
    };

    const genQuestFromText = async (data) => {
        try {
            await axios.post("/getQuestFromText", data);
            router.push({ name: "AppView" });
        } catch (error) {
            console.log(error);
        }
    };

    

    return {
        quests,
        genQuestFromFile,
        genQuestFromText,
        getQuests,
        errors
    };
}