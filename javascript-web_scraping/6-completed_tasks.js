#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasks = JSON.parse(body);
  const taskCount = {};

  // Parcourir les tâches et compter celles qui sont complétées par utilisateur
  tasks.forEach(task => {
    if (task.completed) {
      if (taskCount[task.userId]) {
        taskCount[task.userId] += 1;
      } else {
        taskCount[task.userId] = 1;
      }
    }
  });

  // Afficher les résultats
  console.log(taskCount);
});
