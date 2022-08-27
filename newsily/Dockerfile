FROM node:14.19.3-alpine3.16

WORKDIR /newsily-client

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 4000

CMD ["npm", "start"]