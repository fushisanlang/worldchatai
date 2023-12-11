FROM node:18-alpine AS FrontendBuilder
RUN npm config set registry http://registry.npmmirror.com
WORKDIR /app
RUN npm install pnpm -g
COPY frontend/package*.json ./frontend/

WORKDIR /app/frontend
RUN pnpm install
COPY frontend ./
RUN pnpm build
