import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  resolve: {
    alias: {
      '@pages': '/src/pages',
    }
  },
  plugins: [
    tailwindcss(),
  ],
})