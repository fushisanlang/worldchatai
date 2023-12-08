FROM harborplus.avepoint.net/edutech/lhub/front:base as FrontendBuilder
WORKDIR /app
WORKDIR /app/frontend
COPY frontend ./
RUN cnpm run build 

#FROM python:3.10-alpine
#
#RUN apk add --update caddy gcc musl-dev libffi-dev
#
#WORKDIR /app
#COPY backend/requirements.txt /tmp/requirements.txt
#RUN pip install --no-cache-dir -r /tmp/requirements.txt
#
#COPY Caddyfile ./Caddyfile
#COPY backend ./backend
#COPY --from=FrontendBuilder /app/frontend/dist ./dist
#
#EXPOSE 80
#
#COPY startup.sh ./startup.sh
#RUN chmod +x ./startup.sh; mkdir /data
#CMD ["/app/startup.sh"]