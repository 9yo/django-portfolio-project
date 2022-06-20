FROM node:16-alpine

RUN mkdir -p /frontend-app
COPY ./frontend /frontend-app

WORKDIR /frontend-app

RUN npm install -g npm

COPY ./frontend/package.json /frontend-app
COPY ./frontend/package-lock.json /frontend-app

RUN npm install

CMD ["npm", "run", "serve"]
