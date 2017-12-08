arg frontend

from vue-cli
run npm install -g vue-websocket
run git clone https://github.com/cristijora/vue-paper-dashboard && cd vue-paper-dashboard && npm install -g

expose 8080
workdir /app
copy ./frontend /app
cmd npm install && npm run dev
