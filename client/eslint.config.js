// import tseslint from 'typescript-eslint';
// import prettierPlugin from 'eslint-plugin-prettier';
// import reactPlugin from 'eslint-plugin-react';
// import reactHooksPlugin from 'eslint-plugin-react-hooks';

// export default [
//     {
//         ignores: ['node_modules', 'dist', 'build', '.husky', '.circleci'],
//     },
//     {
//         files: ['**/*.{js,jsx}'],
//         languageOptions: {
//             parser: tseslint.parser,
//             parserOptions: {
//                 ecmaVersion: 'latest',
//                 sourceType: 'module',
//                 ecmaFeatures: { jsx: true },
//             },
//         },
//         plugins: {
//             '@typescript-eslint': tseslint.plugin,
//             prettier: prettierPlugin,
//             react: reactPlugin,
//             'react-hooks': reactHooksPlugin,
//         },
//         settings: {
//             react: { version: 'detect' },
//         },
//         rules: {
//             'react/react-in-jsx-scope': 'off',
//             'react/prop-types': 'off',

//             'react-hooks/rules-of-hooks': 'error',
//             'react-hooks/exhaution-deps': 'warn',
//         },
//     }
// ]