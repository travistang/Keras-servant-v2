arg frontend

from vue-cli
run npm install -g vue-websocket vuex

run git clone https://github.com/cristijora/vue-paper-dashboard && cd vue-paper-dashboard && npm install -g

expose 8080
workdir /app
copy ./frontend /app
run npm install --save vuex
cmd npm install && npm run dev
