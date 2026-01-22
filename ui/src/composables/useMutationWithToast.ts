import type { ParsedError } from '@/lib/error-handler'
import { parseApiError } from '@/lib/error-handler'
import type { MutateFunction } from '@tanstack/query-core'
import type { UseMutationReturnType } from '@tanstack/vue-query'
import { toast } from 'vue-sonner'

type MutateOptions<TData, TError, TVariables, TContext> = Parameters<
  MutateFunction<TData, TError, TVariables, TContext>
>[1]

export interface MutationToastOptions<TData = unknown> {
  successMessage?: string | ((_data: TData) => string)

  showErrorToast?: boolean

  showSuccessToast?: boolean

  onErrorCallback?: (_error: unknown, _parsed: ParsedError) => void

  onSuccessCallback?: (_data: TData) => void
}

export function useMutationWithToast<
  TData = unknown,
  TError = unknown,
  TVariables = void,
  TContext = unknown,
>(
  mutation: UseMutationReturnType<TData, TError, TVariables, TContext>,
  options?: MutationToastOptions<TData>,
): UseMutationReturnType<TData, TError, TVariables, TContext> {
  const {
    successMessage,
    showErrorToast = true,
    showSuccessToast = true,
    onErrorCallback,
    onSuccessCallback,
  } = options || {}

  const originalMutate = mutation.mutate
  const originalMutateAsync = mutation.mutateAsync

  mutation.mutate = (
    variables: TVariables,
    mutationOptions?: MutateOptions<TData, TError, TVariables, TContext>,
  ) => {
    return originalMutate(variables, {
      ...mutationOptions,
      onSuccess: (...args) => {
        const [data] = args
        if (showSuccessToast) {
          const message =
            typeof successMessage === 'function' ? successMessage(data) : successMessage
          toast.success(message || 'Operation completed successfully')
        }

        mutationOptions?.onSuccess?.(...args)

        onSuccessCallback?.(data)
      },
      onError: (...args) => {
        const [error] = args
        const parsed = parseApiError(error)

        if (showErrorToast) {
          toast.error(parsed.message)
        }

        mutationOptions?.onError?.(...args)

        onErrorCallback?.(error, parsed)
      },
    })
  }

  mutation.mutateAsync = async (
    variables: TVariables,
    mutationOptions?: MutateOptions<TData, TError, TVariables, TContext>,
  ) => {
    try {
      const data = await originalMutateAsync(variables, {
        ...mutationOptions,
        onSuccess: (...args) => {
          const [data] = args
          if (showSuccessToast) {
            const message =
              typeof successMessage === 'function' ? successMessage(data) : successMessage
            toast.success(message || 'Operation completed successfully')
          }

          mutationOptions?.onSuccess?.(...args)
          onSuccessCallback?.(data)
        },
      })
      return data
    } catch (error) {
      const parsed = parseApiError(error)

      if (showErrorToast) {
        toast.error(parsed.message)
      }

      onErrorCallback?.(error, parsed)

      throw error
    }
  }

  return mutation
}
