import { uploadPhoto, createUser } from './utils';

async function asyncUploadUser() {
  try {
    const user = await createUser();
    const photo = await uploadPhoto();
    return {
      photo,
      user,
    };
  } catch (err) {
    return {
      photo: null,
      user: null,
    };
  }
}

export { asyncUploadUser as default };
