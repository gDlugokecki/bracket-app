import pluginJs from '@eslint/js'
import pluginVue from 'eslint-plugin-vue'
import globals from 'globals'
import tseslint from 'typescript-eslint'

/** @type {import('eslint').Linter.Config[]} */
export default [
  { files: ['**/*.{js,mjs,cjs,ts,vue}'] },
  { languageOptions: { globals: globals.browser } },
  pluginJs.configs.recommended,
  ...tseslint.configs.recommended,
  ...pluginVue.configs['flat/essential'],
  { files: ['**/*.vue'], languageOptions: { parserOptions: { parser: tseslint.parser } } },
  {
    rules: {
      'no-unused-vars': [
        'error',
        {
          varsIgnorePattern: '^_', // For variables that start with underscore
          argsIgnorePattern: '^_', // For function arguments that start with underscore
        },
      ],
      '@typescript-eslint/no-unused-vars': [
        'error',
        {
          varsIgnorePattern: '^_',
          argsIgnorePattern: '^_',
        },
      ],
      'vue/multi-word-component-names': [
        'error',
        {
          ignores: ['Field', 'Input', 'Label', 'Button', 'Textarea', 'Typography'], // shadcn-vue components
        },
      ],
    },
  },
]
