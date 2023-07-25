<script setup>
import useApps from '../stores/app';
import { onMounted } from 'vue';

const { quests, getQuests } = useApps();

onMounted(() => getQuests());
</script>
<template>
    <div class="mt-12">
        <div class="relative overflow-x-auto">
            <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50">
                    <tr>
                        <th scope="col" class="px-6 py-3">
                            Question
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Answer
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="quest in quests" class="bg-white border-b">
                        <td class="px-6 py-4">
                            {{ quest.question }}
                        </td>
                        <td class="px-6 py-4">
                            {{ quest.answer }}
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
</div></template>