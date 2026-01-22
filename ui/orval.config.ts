import { defineConfig } from 'orval'

export default defineConfig({
  bracketApi: {
    input: {
      target: 'http://localhost:8080/openapi.json',
    },
    output: {
      mode: 'tags-split',
      target: './src/api/generated',
      client: 'vue-query',
      clean: true,
      override: {
        mutator: {
          path: './src/api/custom-instance.ts',
          name: 'customInstance',
        },
      },
    },
  },
})
