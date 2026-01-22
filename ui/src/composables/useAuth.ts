import { getMe } from '@/api/generated/auth/auth'
import type { UserResponse } from '@/api/generated/bracketAppAPI.schemas'
import { ref } from 'vue'

const currentUser = ref<null | UserResponse>(null)
const isAuthenticated = ref(false)
const isLoading = ref(false)

export function useAuth() {
  async function checkAuth() {
    if (isAuthenticated.value && currentUser.value) {
      return true
    }

    isLoading.value = true
    try {
      const data = await getMe()
      currentUser.value = data
      isAuthenticated.value = true
      return true
    } catch {
      currentUser.value = null
      isAuthenticated.value = false
      return false
    } finally {
      isLoading.value = false
    }
  }

  function logout() {
    currentUser.value = null
    isAuthenticated.value = false
  }

  return {
    currentUser,
    isAuthenticated,
    isLoading,
    checkAuth,
    logout,
  }
}
