export default function getListStudentIds(objArray) {
  const emptyArray = [];
  if (!Array.isArray(objArray)) {
    return emptyArray;
  }
  return objArray.map((obj) => obj.id);
}
