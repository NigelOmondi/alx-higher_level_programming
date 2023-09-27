#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const completedTasksByUser = {};

    for (const task of tasks) {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    }

    console.log(completedTasksByUser);
  } else {
    console.error(`Error: Unable to fetch task data. Status code: ${response.statusCode}`);
  }
});
