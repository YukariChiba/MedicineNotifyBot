FROM node:latest
RUN mkdir /code
COPY . /code
WORKDIR /code
RUN yarn
CMD ["node", "index.js"]
