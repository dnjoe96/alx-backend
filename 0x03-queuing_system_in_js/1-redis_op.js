import { createClient, print } from 'redis';

const client = createClient('26379');

client.on('connect', (err) => {
  console.log('Redis client connected to the server');
  if (err) {
    console.log('Redis client not connected to the server: ', err)
  }
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, value) => {
    if (err) { throw err }
    console.log(value)
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
