<script setup lang="ts">
import { useLogin } from '@/api/generated/auth/auth'
import { parseApiError } from '@/lib/error-handler'
import { VALIDATION_MESSAGES } from '@/lib/validation'
import { ROUTES } from '@/router/routes'
import { toTypedSchema } from '@vee-validate/zod'
import { useForm } from 'vee-validate'
import { useRouter } from 'vue-router'
import { toast } from 'vue-sonner'
import * as z from 'zod'

import FormTextField from '@/components/form/FormTextField.vue'
import Button from '@/components/ui/button/Button.vue'
import Card from '@/components/ui/card/Card.vue'
import CardContent from '@/components/ui/card/CardContent.vue'

const loginSchema = toTypedSchema(
  z.object({
    email: z.string().min(1, VALIDATION_MESSAGES.REQUIRED),
    password: z.string().min(1, VALIDATION_MESSAGES.REQUIRED),
  }),
)

const { handleSubmit, setErrors } = useForm({
  validationSchema: loginSchema,
  initialValues: {
    email: '',
    password: '',
  },
})

const router = useRouter()
const { mutate: loginMutate } = useLogin()

const onSubmit = handleSubmit((values) => {
  loginMutate(
    { data: values },
    {
      onSuccess: () => {
        toast.success('Logged in successfully!')
        router.push(ROUTES.DASHBOARD)
      },
      onError: (error) => {
        const parsed = parseApiError(error)
        toast.error(parsed.message)
        if (parsed.validationErrors) {
          setErrors(parsed.validationErrors)
        }
      },
    },
  )
})
</script>

<template>
  <Card class="bg-card border-border min-w-96">
    <CardContent>
      <form @submit="onSubmit">
        <div class="flex flex-col space-y-4">
          <FormTextField name="email" label="Email" type="email" placeholder="johndoe@example.pl" />
          <FormTextField
            name="password"
            label="Password"
            type="password"
            placeholder="Enter your password"
          />
          <Button size="xl" class="mt-3">Sign in</Button>
        </div>
      </form>
    </CardContent>
  </Card>
</template>
