<script setup lang="ts">
import { ref } from "vue";

const repositoryPath = ref("");
const question = ref("Where is authentication handled?");
const result = ref("");
const loading = ref(false);

async function analyzeRepository() {
  loading.value = true;

  // need to implement this in API, may need refactoring later
  try {
    const response = await fetch("http://localhost:3000/api/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        repository_path: repositoryPath.value,
        question: question.value,
      }),
    });

    const data = await response.json();

    result.value = data.answer;
  } catch (error) {
    console.error(error);
  } finally {
    loading.value = false;
  }
}
</script>

<template>
  <v-app>
    <v-app-bar>
      <v-toolbar-title>AI Codebase Explorer</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <v-container class="d-flex justify-center" max-width="1000">
        <v-card class="pa-6 mt-8" width="700">
          <v-card-title class="text-center"> Analyze a Codebase </v-card-title>

          <v-card-text>
            <v-text-field
              v-model="repositoryPath"
              label="Repository path"
              placeholder="C:\dev\my-project"
              variant="outlined"
            />

            <v-textarea
              v-model="question"
              label="What do you want to know?"
              variant="outlined"
              rows="3"
            />

            <div class="d-flex justify-center">
              <v-btn
                color="primary"
                :loading="loading"
                @click="analyzeRepository"
              >
                Analyze Repository
              </v-btn>
            </div>
          </v-card-text>
        </v-card>
      </v-container>
    </v-main>
  </v-app>
</template>
