FROM harborplus.avepoint.net/edutech/lhub/front:base
WORKDIR /app
WORKDIR /app/frontend
COPY frontend ./
RUN cnpm run build 