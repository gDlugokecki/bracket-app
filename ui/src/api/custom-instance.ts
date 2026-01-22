/* eslint-disable @typescript-eslint/no-explicit-any */
import { useAuth } from '@/composables/useAuth'
import { ROUTES } from '@/router/routes'
import Axios, { type AxiosRequestConfig } from 'axios'

const API_BASE_URL = 'http://localhost:8080'

// Separate instance for auth endpoints without interceptors
const authAxios = Axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true,
})

export const axiosInstance = Axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true,
})

let isRefreshing = false
let failedQueue: any[] = []

const processQueue = (error: any, token: string | null = null) => {
  failedQueue.forEach((prom) => {
    if (error) {
      prom.reject(error)
    } else {
      prom.resolve(token)
    }
  })

  failedQueue = []
}

axiosInstance.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config

    if (error.response?.status === 401 && !originalRequest._retry) {
      if (isRefreshing) {
        return new Promise((resolve, reject) => {
          failedQueue.push({ resolve, reject })
        })
          .then(() => {
            return axiosInstance(originalRequest)
          })
          .catch((err) => {
            return Promise.reject(err)
          })
      }

      originalRequest._retry = true
      isRefreshing = true

      try {
        await authAxios.post('/auth/refresh')

        isRefreshing = false
        processQueue(null)

        return axiosInstance(originalRequest)
      } catch (refreshError) {
        isRefreshing = false
        processQueue(refreshError, null)

        await authAxios.post('/auth/logout')

        const { logout } = useAuth()
        logout()

        window.location.href = ROUTES.LOGIN
        return Promise.reject(refreshError)
      }
    }

    return Promise.reject(error)
  },
)

export const customInstance = <T>(config: AxiosRequestConfig): Promise<T> => {
  return axiosInstance(config).then(({ data }) => data)
}

export default customInstance
