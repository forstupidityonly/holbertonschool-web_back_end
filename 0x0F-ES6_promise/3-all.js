#!/usr/bin/node
import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()]).then((elements) => {
    console.log(`${elements[0].body} ${elements[1].firstName} ${elements[1].lastName}`);
  }).catch(() => console.log('Signup system offline'));
}
export { handleProfileSignup as default };
