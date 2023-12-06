FROM front:base 

WORKDIR /app
WORKDIR /app/frontend
COPY frontend ./
RUN cnpm run build 
