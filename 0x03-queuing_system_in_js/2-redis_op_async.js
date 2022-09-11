import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient('26379');

client.on('connect', (err) => {
  console.log('Redis client connected to the server');
  if (err) {
    console.log('Redis client not connected to the server: ', err)
  }
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value);
  print('value added');
}

async function displaySchoolValue(schoolName) {
  const getAsync = promisify(client.get).bind(client);
  
  await getAsync(schoolName)
    .then((value) => console.log(value))
    .catch((err) => console.log(err));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
