<script setup lang="ts">
import { useRegister } from '@/api/generated/auth/auth'
import { useMutationWithToast } from '@/composables/useMutationWithToast'
import { VALIDATION_MESSAGES } from '@/lib/validation'
import { ROUTES } from '@/router/routes'
import { toTypedSchema } from '@vee-validate/zod'
import { useForm } from 'vee-validate'
import { useRouter } from 'vue-router'
import * as z from 'zod'

import FormTextField from '@/components/form/FormTextField.vue'
import Button from '@/components/ui/button/Button.vue'
import Card from '@/components/ui/card/Card.vue'
import CardContent from '@/components/ui/card/CardContent.vue'

const createUserSchema = toTypedSchema(
  z
    .object({
      firstName: z.string().min(1, VALIDATION_MESSAGES.REQUIRED),
      lastName: z.string().min(1, VALIDATION_MESSAGES.REQUIRED),
      email: z.string().min(1, VALIDATION_MESSAGES.REQUIRED).email(VALIDATION_MESSAGES.EMAIL),
      password: z.string().min(8, VALIDATION_MESSAGES.MIN_LENGTH(8)),
      passwordConfirmation: z.string().min(1, VALIDATION_MESSAGES.REQUIRED),
    })
    .superRefine((val, ctx) => {
      if (val.password !== val.passwordConfirmation) {
        ctx.addIssue({
          code: z.ZodIssueCode.custom,
          message: VALIDATION_MESSAGES.PASSWORD_MATCH,
          path: ['passwordConfirmation'],
        })
      }
    }),
)

const { handleSubmit, setErrors } = useForm({
  validationSchema: createUserSchema,
  initialValues: {
    firstName: '',
    lastName: '',
    email: '',
    password: '',
    passwordConfirmation: '',
  },
})

const router = useRouter()

const createPlayer = useMutationWithToast(useRegister(), {
  successMessage: 'Account created successfully!',
  onSuccessCallback: () => router.push(ROUTES.LOGIN),
  onErrorCallback: (error, parsed) => {
    if (parsed.validationErrors) {
      setErrors(parsed.validationErrors)
    }
  },
})

const onSubmit = handleSubmit((values) => {
  const { passwordConfirmation: _, ...restData } = values

  createPlayer.mutate({
    data: restData,
  })
})
</script>

<template>
  <Card class="bg-card border-border">
    <CardContent>
      <form @submit="onSubmit">
        <div class="flex flex-col space-y-4">
          <div class="flex space-x-3">
            <FormTextField name="firstName" label="First name" />
            <FormTextField name="lastName" label="Last name" />
          </div>
          <FormTextField name="email" label="Email" type="email" />
          <FormTextField
            name="password"
            label="Password"
            type="password"
            description="Must be at least 8 characters"
          />
          <FormTextField name="passwordConfirmation" label="Confirm password" type="password" />
          <Button size="xl" class="mt-3">Create account</Button>
        </div>
      </form>
    </CardContent>
  </Card>
</template>
