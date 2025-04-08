import { fileURLToPath, URL } from 'url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: { //if we do not do this, we will get CORS error when we try to access the API from the frontend
    proxy: {
      '^/api*': {
        target: 'http://localhost:8080', // replace with your backend server URL
        changeOrigin: true,
      }
    }
  }
})
