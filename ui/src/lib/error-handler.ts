import type { AxiosError } from 'axios'

interface ValidationErrorDetail {
  loc: (string | number)[]
  msg: string
  type: string
}

interface FastAPIError {
  detail?: string | ValidationErrorDetail[]
}

export interface ParsedError {
  message: string
  statusCode?: number
  validationErrors?: Record<string, string>
}

export function parseApiError(error: unknown): ParsedError {
  if (isAxiosError(error)) {
    const axiosError = error as AxiosError<FastAPIError>

    if (!axiosError.response) {
      if (axiosError.code === 'ERR_NETWORK') {
        return {
          message: 'Unable to connect to the server. Please check your internet connection.',
        }
      }
      if (axiosError.code === 'ECONNABORTED') {
        return {
          message: 'Request timeout. Please try again.',
        }
      }
      return {
        message: 'Network error. Please check your connection and try again.',
      }
    }

    const { status, data } = axiosError.response
    const detail = data?.detail

    if (status === 422 && Array.isArray(detail)) {
      const validationErrors: Record<string, string> = {}
      const messages: string[] = []

      detail.forEach((err: ValidationErrorDetail) => {
        const field = err.loc[err.loc.length - 1]
        const message = err.msg
        validationErrors[String(field)] = message
        messages.push(`${field}: ${message}`)
      })

      return {
        message: messages.length > 0 ? messages.join(', ') : 'Validation failed',
        statusCode: status,
        validationErrors,
      }
    }

    return {
      message: getStatusMessage(status, detail),
      statusCode: status,
    }
  }

  if (error instanceof Error) {
    return {
      message: error.message || 'An unexpected error occurred',
    }
  }

  return {
    message: 'An unexpected error occurred. Please try again.',
  }
}

function getStatusMessage(status: number, detail?: string | ValidationErrorDetail[]): string {
  if (typeof detail === 'string') {
    return detail
  }

  switch (status) {
    case 400:
      return 'Invalid request. Please check your input and try again.'
    case 401:
      return 'You are not authenticated. Please log in.'
    case 403:
      return 'You do not have permission to perform this action.'
    case 404:
      return 'The requested resource was not found.'
    case 405:
      return 'This operation is not allowed.'
    case 408:
      return 'Request timeout. Please try again.'
    case 409:
      return 'This resource already exists or conflicts with existing data.'
    case 410:
      return 'This resource is no longer available.'
    case 413:
      return 'Request is too large. Please reduce the size and try again.'
    case 415:
      return 'Unsupported file type or content format.'
    case 422:
      return 'Validation failed. Please check your input.'
    case 429:
      return 'Too many requests. Please try again later.'
    case 500:
      return 'Server error. Please try again later.'
    case 501:
      return 'This feature is not implemented yet.'
    case 502:
      return 'Bad gateway. The server is temporarily unavailable.'
    case 503:
      return 'Service unavailable. Please try again later.'
    case 504:
      return 'Gateway timeout. The server took too long to respond.'
    default:
      // Catch ALL other status codes
      if (status >= 500) {
        return `Server error (${status}). Please try again later.`
      }
      if (status >= 400) {
        return `Request error (${status}). Please check your input and try again.`
      }
      return `An unexpected error occurred (${status}). Please try again.`
  }
}

function isAxiosError(error: unknown): error is AxiosError {
  return (
    typeof error === 'object' &&
    error !== null &&
    'isAxiosError' in error &&
    (error as AxiosError).isAxiosError === true
  )
}
