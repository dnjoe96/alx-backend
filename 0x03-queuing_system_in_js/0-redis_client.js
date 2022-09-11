import { createClient } from 'redis';

const client = createClient('26379');

client.on('connect', (err) => {
  console.log('Redis client connected to the server');
  if (err) {
    console.log('Redis client not connected to the server: ', err)
  }
});


// client.on('error', (err) => {
//   console.log('Redis client not connected to the server: ', err)
// });

// client.set('key', 'value');
// const value = client.get('key');
// console.log(value);
