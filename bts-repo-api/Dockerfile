#FROM hub.c.163.com/library/node
#FROM bts-repo-api
#FROM registry.gitlab.com/tw8774529/bank-nosql-api
FROM node:12

# Create app directory
WORKDIR /bts-repo-api

# Install app dependencies
COPY package*.json ./

RUN npm install
# Copy app source code

COPY . .

#Expose port and start application
EXPOSE 3030

CMD [ "npm", "start" ]