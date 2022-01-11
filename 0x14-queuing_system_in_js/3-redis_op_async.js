import { createClient } from 'redis';
const { promisify } = require('util');
// This is a simple connection to a reddis client
const client = createClient();
const getSchoolVal = promisify(client.get).bind(client);
// Handles if connection is errored out
client.on('error', (err) => console.log('Redis client not connected to the server: ', err));
// Handles if connection works between server and client
client.on('ready', () => console.log('Redis client connected to the server'));
function setNewSchool(schoolName, value) {
  const setkey = client.set(schoolName, value, (reply) => reply);
  console.log('Reply: ', setkey);
}
async function displaySchoolValue(schoolName) {
  const value = getSchoolVal(schoolName);
  console.log(value);
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
