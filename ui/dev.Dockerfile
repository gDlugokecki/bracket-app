FROM node:22-bullseye

# Install pnpm
RUN corepack enable && corepack prepare pnpm@latest --activate

WORKDIR /app

# Configure pnpm to use local store
RUN pnpm config set store-dir /app/.pnpm-store

# Copy package files
COPY package.json pnpm-lock.yaml ./

# Install dependencies
RUN pnpm install

# Copy the rest of the application
COPY . .

# Expose port for dev server (default Vue port)
EXPOSE 5173

# Run development server with host set to 0.0.0.0 to allow external access
CMD ["pnpm", "run", "dev"]
