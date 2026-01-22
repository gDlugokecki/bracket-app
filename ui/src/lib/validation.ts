export const VALIDATION_MESSAGES = {
  REQUIRED: 'This field is required',
  MIN_LENGTH: (min: number) => `Must be at least ${min} characters`,
  EMAIL: 'Please enter a valid email address',
  PASSWORD_MATCH: "Passwords don't match",
} as const
